import os
import sys
import json
import sqlite3
import re
from typing import Optional, List
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "bible.db")

app = FastAPI(title="Holy Bible Bilingual API (KJV & Telugu)", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Knowledge Bases into memory
def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

EMOTIONS_DATA = load_json("emotions.json").get("emotions", [])
INCIDENTS_DATA = load_json("incidents.json").get("incidents", [])
SUFFERING_DATA = load_json("suffering_arcs.json").get("arcs", [])
DICTIONARY_DATA = load_json("dictionary.json").get("words", [])
HISTORICAL_EVIDENCE = load_json("historical_evidence.json")
CHAPTER_CONTEXTS = load_json("chapter_contexts.json").get("contexts", [])

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Models
class SearchQuery(BaseModel):
    query: str

@app.get("/api/health")
def health():
    return {"status": "ok", "db": os.path.exists(DB_PATH)}

@app.get("/api/books")
def get_books():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, book_num, name_en, name_te, abbrev, testament, total_chapters FROM books ORDER BY book_num ASC")
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

@app.get("/api/chapter")
def get_chapter(book_name: Optional[str] = None, book_id: Optional[int] = None, chapter: int = 1):
    conn = get_db()
    cur = conn.cursor()

    if book_id:
        cur.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    elif book_name:
        cur.execute("SELECT * FROM books WHERE name_en LIKE ? OR name_te LIKE ?", (f"%{book_name}%", f"%{book_name}%"))
    else:
        book_id = 1
        cur.execute("SELECT * FROM books WHERE id = 1")
    
    book_row = cur.fetchone()
    if not book_row:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")
    
    book = dict(book_row)
    cur.execute(
        """SELECT verse, text_en, text_te FROM verses 
           WHERE book_id = ? AND chapter = ? 
           ORDER BY verse ASC""",
        (book["id"], chapter)
    )
    verses = [dict(r) for r in cur.fetchall()]
    conn.close()

    return {
        "book": book,
        "chapter": chapter,
        "verses_count": len(verses),
        "verses": verses
    }

@app.post("/api/search/incident")
def search_incident(req: SearchQuery):
    query = req.query.lower().strip()
    if not query:
        return {"results": []}

    query_words = set(re.findall(r'\w+', query))
    results = []

    for inc in INCIDENTS_DATA:
        score = 0
        inc_title = inc["title_en"].lower() + " " + inc["title_te"].lower()
        inc_summary = inc["summary_en"].lower() + " " + inc["summary_te"].lower()
        keywords = [k.lower() for k in inc.get("keywords", [])]

        # Exact phrase or keyword matching
        for kw in keywords:
            if kw in query:
                score += 8
            elif any(w in kw for w in query_words if len(w) > 2):
                score += 3

        for w in query_words:
            if len(w) > 2:
                if w in inc_title:
                    score += 5
                if w in inc_summary:
                    score += 2

        if score > 0:
            results.append({"incident": inc, "score": score})

    results.sort(key=lambda x: x["score"], reverse=True)
    return {"query": req.query, "results": [r["incident"] for r in results[:10]]}

@app.post("/api/search/emotion")
def search_emotion(req: SearchQuery):
    query = req.query.lower().strip()
    if not query:
        return {"match": None}

    # Direct keyword matching against curated emotions
    best_match = None
    best_score = 0

    for emo in EMOTIONS_DATA:
        score = 0
        for kw in emo["keywords"]:
            if kw in query:
                score += 10
            elif any(word in kw for word in query.split() if len(word) > 2):
                score += 3
        if score > best_score:
            best_score = score
            best_match = emo

    if best_match and best_score >= 3:
        return {
            "query": req.query,
            "found": True,
            "data": best_match
        }

    # Fallback to default depression/comfort if keywords indicate downcast feeling
    if any(term in query for term in ["sad", "cry", "pain", "hurt", "die", "give up", "tired"]):
        dep = next((e for e in EMOTIONS_DATA if e["id"] == "depressed"), None)
        return {"query": req.query, "found": True, "data": dep}

    return {"query": req.query, "found": False, "data": None}

@app.get("/api/suffering/arcs")
def get_suffering_arcs(q: Optional[str] = None):
    if not q:
        return {"arcs": SUFFERING_DATA}
    
    query = q.lower().strip()
    results = []
    for arc in SUFFERING_DATA:
        text_corpus = (
            arc["person"].lower() + " " +
            arc.get("person_te", "").lower() + " " +
            arc["title_en"].lower() + " " +
            arc["the_trial"]["summary_en"].lower() + " " +
            arc["gods_purpose"]["summary_en"].lower() + " " +
            arc["the_aftermath"]["summary_en"].lower() + " " +
            " ".join(arc.get("keywords", []))
        )
        score = 0
        for word in query.split():
            if word in text_corpus:
                score += 1
        if score > 0 or any(k in query for k in arc.get("keywords", [])):
            results.append(arc)

    return {"arcs": results if results else SUFFERING_DATA}

@app.get("/api/dictionary/lookup")
def lookup_word(word: str, book: Optional[str] = None, chapter: Optional[int] = None):
    clean_word = word.lower().strip()
    found_entry = None
    for entry in DICTIONARY_DATA:
        if entry["word"].lower() == clean_word:
            found_entry = entry
            break

    if not found_entry:
        # Partial match
        for entry in DICTIONARY_DATA:
            if clean_word in entry["word"].lower() or entry["word"].lower() in clean_word:
                found_entry = entry
                break

    if not found_entry:
        return {
            "word": word,
            "found": False,
            "message": f"Meaning for '{word}' is being added to the theological concordance."
        }

    # Contextual note
    context_note = None
    if book and "chapters" in found_entry:
        for ref_key, text in found_entry["chapters"].items():
            if book.lower() in ref_key.lower():
                context_note = text
                break

    return {
        "word": found_entry["word"],
        "found": True,
        "definition_en": found_entry["definition_en"],
        "definition_te": found_entry["definition_te"],
        "context_note": context_note,
        "all_chapter_contexts": found_entry.get("chapters", {})
    }

@app.get("/api/search/verses")
def search_verses(q: str, limit: int = 20):
    query = q.strip()
    if not query:
        return {"results": []}

    conn = get_db()
    cur = conn.cursor()
    
    # Try exact phrase or term search in FTS5
    safe_query = '"' + query.replace('"', '""') + '"'
    try:
        cur.execute(
            """SELECT book_name_en, book_name_te, chapter, verse, text_en, text_te
               FROM verses_fts 
               WHERE verses_fts MATCH ? 
               LIMIT ?""",
            (safe_query, limit)
        )
        rows = cur.fetchall()
    except Exception:
        # Fallback to standard LIKE
        cur.execute(
            """SELECT book_name_en, book_name_te, chapter, verse, text_en, text_te
               FROM verses 
               WHERE text_en LIKE ? OR text_te LIKE ?
               LIMIT ?""",
            (f"%{query}%", f"%{query}%", limit)
        )
        rows = cur.fetchall()

    conn.close()
    return {"query": q, "results": [dict(r) for r in rows]}

@app.get("/api/evidence/historical")
def get_historical_evidence(category: Optional[str] = None):
    categories = HISTORICAL_EVIDENCE.get("categories", [])
    evidences = HISTORICAL_EVIDENCE.get("evidences", [])
    if category and category != "all":
        evidences = [e for e in evidences if e.get("category") == category]
    return {
        "categories": categories,
        "evidences": evidences,
        "total": len(evidences)
    }

@app.get("/api/context/chapter")
def get_chapter_context(book: str, chapter: int = 1):
    clean_book = book.strip().lower()
    
    # 1. Check pre-computed specific chapter context
    for entry in CHAPTER_CONTEXTS:
        if entry["book"].lower() == clean_book and entry["chapter"] == chapter:
            return {"found": True, "context": entry}
            
    # 2. Check book name in DB to get Telugu title & testament
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE LOWER(name_en) = ? OR LOWER(name_te) = ? LIMIT 1", (clean_book, clean_book))
    book_row = cur.fetchone()
    conn.close()
    
    book_en = book_row["name_en"] if book_row else book
    book_te = book_row["name_te"] if book_row else book
    testament = book_row["testament"] if book_row else "OT"
    
    # 3. Dynamic contextual synthesis for any chapter
    dynamic_entry = {
        "book": book_en,
        "chapter": chapter,
        "title_en": f"{book_en} Chapter {chapter}: Context & Divine Purpose",
        "title_te": f"{book_te} {chapter}వ అధ్యాయము: నేపథ్యం & దైవిక సంకల్పం",
        "backstory": {
            "summary_en": f"In {book_en} Chapter {chapter}, we witness a pivotal stage in {'Old Testament covenant history' if testament == 'OT' else 'New Testament apostolic revelation'}. The preceding events established the historical setting and the spiritual state of God's people in this era.",
            "summary_te": f"{book_te} {chapter}వ అధ్యాయము {'పాత నిబంధన దైవిక చరిత్రలో' if testament == 'OT' else 'నూతన నిబంధన సువార్త మరియు అపొస్తలుల బోధలలో'} ఒక ముఖ్యమైన ఘట్టము. దీనికి పూర్వము జరిగిన సంఘటనలు ప్రజల ఆత్మీయ స్థితిని మరియు దేవుని నడిపింపును తెలియజేస్తాయి."
        },
        "why_it_happened": {
            "summary_en": f"This chapter unfolds as a direct consequence of human choices, trials of faith, and God's sovereign intervention to teach, correct, or protect His people according to His holy character.",
            "summary_te": "మానవుల నిర్ణయాలు, విశ్వాస పోరాటాలు మరియు తన ప్రజలను సరిచేసి రక్షించుటకు దేవుడు స్వయంగా చేసిన కార్యం వలన ఈ సంఘటనలు జరిగినవి."
        },
        "gods_future_plan": {
            "summary_en": f"God allowed these specific events in {book_en} {chapter} not in isolation, but as a stepping stone toward His ultimate redemptive purpose: preparing character, fulfilling prophecy, and pointing toward eternal salvation in Christ.",
            "summary_te": f"దేవుడు {book_te} {chapter}వ అధ్యాయములోని సంగతులను కేవలం ఆ సమయము కొరకే కాక, భవిష్యత్తులో తన రక్షణ ప్రణాళికను, క్రీస్తు నందలి నిత్య వాగ్దానములను నెరవేర్చుట కొరకై ఒక సోపానముగా మలచుకొనెను."
        }
    }
    return {"found": True, "context": dynamic_entry}

@app.post("/api/context/lookup")
def lookup_context(req: SearchQuery):
    raw_q = req.query.strip()
    if not raw_q:
        return {"found": False, "message": "Please provide a verse or chapter"}

    # Try parsing book, chapter, verse
    m = re.search(r'([\d\s]*[^\d\s:]+)\s*(\d+)?(?::(\d+)(?:-(\d+))?)?', raw_q, re.UNICODE)
    book_candidate = m.group(1).strip() if m else raw_q
    chapter_num = int(m.group(2)) if (m and m.group(2)) else 1
    verse_num = int(m.group(3)) if (m and m.group(3)) else None

    conn = get_db()
    cur = conn.cursor()

    # 1. Search books by candidate
    cur.execute(
        """SELECT * FROM books 
           WHERE LOWER(name_en) = ? OR LOWER(name_te) = ? 
              OR LOWER(name_en) LIKE ? OR LOWER(name_te) LIKE ?
           ORDER BY CASE WHEN LOWER(name_en) = ? THEN 1 ELSE 2 END
           LIMIT 1""",
        (book_candidate.lower(), book_candidate.lower(), f"%{book_candidate.lower()}%", f"%{book_candidate.lower()}%", book_candidate.lower())
    )
    book_row = cur.fetchone()

    # 2. If not found, check incidents to see if query is a story name
    if not book_row:
        for inc in INCIDENTS_DATA:
            if any(kw in raw_q.lower() for kw in inc.get("keywords", [])):
                cur.execute("SELECT * FROM books WHERE name_en = ? LIMIT 1", (inc["book"],))
                book_row = cur.fetchone()
                chapter_num = inc["chapter_start"]
                break

    if not book_row:
        conn.close()
        return {"found": False, "message": f"Could not locate book or passage matching '{raw_q}'. Try e.g. 'John 11', 'Genesis 37:20', 'Exodus 14'."}

    book_dict = dict(book_row)

    # Fetch verse(s)
    if verse_num:
        cur.execute(
            """SELECT verse, text_en, text_te FROM verses
               WHERE book_id = ? AND chapter = ? AND verse = ?""",
            (book_dict["id"], chapter_num, verse_num)
        )
    else:
        cur.execute(
            """SELECT verse, text_en, text_te FROM verses
               WHERE book_id = ? AND chapter = ?
               ORDER BY verse ASC LIMIT 10""",
            (book_dict["id"], chapter_num)
        )
    verses = [dict(r) for r in cur.fetchall()]
    conn.close()

    # Get context (backstory, why it happened, god's future plan)
    ctx_result = get_chapter_context(book_dict["name_en"], chapter_num)

    ref_display = f"{book_dict['name_en']} {chapter_num}"
    ref_display_te = f"{book_dict['name_te']} {chapter_num}"
    if verse_num:
        ref_display += f":{verse_num}"
        ref_display_te += f":{verse_num}"

    return {
        "found": True,
        "query": raw_q,
        "reference": ref_display,
        "reference_te": ref_display_te,
        "book": book_dict,
        "chapter": chapter_num,
        "verse": verse_num,
        "verses": verses,
        "context": ctx_result.get("context")
    }

# Mount frontend static directory at root
FRONTEND_DIR = os.path.join(os.path.dirname(BASE_DIR), "frontend")
if os.path.exists(FRONTEND_DIR):
    app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
