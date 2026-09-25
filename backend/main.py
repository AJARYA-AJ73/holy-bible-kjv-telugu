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
    raw_query = req.query.strip()
    if not raw_query:
        return {"query": "", "results": []}

    query = raw_query.lower()
    query_words = [w for w in re.findall(r'\w+', query) if len(w) > 1]
    curated_matches = []

    # 1. Search curated incidents with rich keyword & title scoring
    inc_list = load_json("incidents.json").get("incidents", INCIDENTS_DATA)
    for inc in inc_list:
        score = 0
        inc_title = inc["title_en"].lower() + " " + inc["title_te"].lower()
        inc_summary = inc["summary_en"].lower() + " " + inc["summary_te"].lower()
        keywords = [k.lower() for k in inc.get("keywords", [])]

        for kw in keywords:
            if kw == query:
                score += 35
            elif kw in query or query in kw:
                score += 15
            elif any(w in kw for w in query_words if len(w) > 2):
                score += 5

        for w in query_words:
            if len(w) > 2:
                if w in inc_title:
                    score += 10
                if w in inc_summary:
                    score += 3

        if score > 0:
            curated_matches.append({"incident": inc, "score": score})

    curated_matches.sort(key=lambda x: x["score"], reverse=True)
    results = [r["incident"] for r in curated_matches[:8]]

    # 2. Dual-Layer Full-Bible Fallback: Query 31,100 verses in FTS5
    # This guarantees that ANY query (e.g. 'jacob', 'witchcraft', 'leper', 'tax collector') returns scripture accounts!
    conn = get_db()
    cur = conn.cursor()

    stop_words = {"story", "incident", "what", "where", "bible", "in", "the", "and", "about", "did", "how", "why"}
    fts_words = [w for w in query_words if w not in stop_words and len(w) > 2]
    
    if fts_words:
        fts_query = " OR ".join(fts_words[:3])
        try:
            cur.execute(
                """SELECT book_name_en, book_name_te, chapter, verse, text_en, text_te
                   FROM verses 
                   WHERE verses MATCH ? 
                   ORDER BY rank 
                   LIMIT 30""",
                (fts_query,)
            )
            raw_verse_hits = [dict(r) for r in cur.fetchall()]
            
            # Group verses by (book_name_en, chapter)
            grouped = {}
            for v in raw_verse_hits:
                key = (v["book_name_en"], v["book_name_te"], v["chapter"])
                if key not in grouped:
                    grouped[key] = []
                grouped[key].append(v)

            # Build dynamic incident cards from scripture groups
            for (b_en, b_te, ch), v_list in grouped.items():
                if any(r.get("book") == b_en and r.get("chapter_start") == ch for r in results):
                    continue

                snippet_en = " ".join([f"({v['verse']}) {v['text_en']}" for v in v_list[:2]])
                snippet_te = " ".join([f"({v['verse']}) {v['text_te']}" for v in v_list[:2]])

                dynamic_card = {
                    "id": f"dyn_{b_en}_{ch}",
                    "title_en": f"{b_en} Chapter {ch}: Biblical Account on '{raw_query}'",
                    "title_te": f"{b_te} {ch}వ అధ్యాయము: '{raw_query}' లేఖన వృత్తాంతము",
                    "book": b_en,
                    "chapter_start": ch,
                    "chapter_end": ch,
                    "reference": f"{b_en} {ch}",
                    "summary_en": snippet_en[:260] + "...",
                    "summary_te": snippet_te[:260] + "...",
                    "is_dynamic": True
                }
                results.append(dynamic_card)
                if len(results) >= 12:
                    break
        except Exception:
            pass

    conn.close()
    return {"query": raw_query, "results": results[:12]}

@app.post("/api/search/emotion")
def search_emotion(req: SearchQuery):
    raw_query = req.query.strip()
    if not raw_query:
        return {"query": "", "found": False, "data": None}

    query = raw_query.lower()
    query_words = set(re.findall(r'\w+', query))

    # Detect specific emotional & life crisis intents
    has_friend = any(w in query for w in ["friend", "friends", "friendship", "companion", "pal"])
    has_anger = any(w in query for w in ["angry", "mad", "furious", "wrath", "rage", "fight", "quarrel", "hate", "bitter", "betray", "hurt", "temper"])
    has_money = any(w in query for w in ["money", "broke", "debt", "financial", "jobless", "unemployed", "rent", "bills", "bankrupt", "poverty", "డబ్బులు", "అప్పు"])
    has_sickness = any(w in query for w in ["sick", "ill", "disease", "healing", "heal", "cancer", "pain", "hospital", "doctor", "fever", "stroke", "రోగము", "అనారోగ్యం", "స్వస్థత"])
    has_rejection = any(w in query for w in ["rejected", "rejection", "betrayed", "betrayal", "abandoned", "cheated", "nobody loves", "unwanted", "left alone", "తిరస్కారము", "మోసము"])
    has_hopeless = any(w in query for w in ["give up", "hopeless", "want to die", "end my life", "suicide", "no point in living", "tired of life", "meaningless", "నిరాశ", "విరక్తి"])
    has_waiting = any(w in query for w in ["waiting", "impatient", "how long", "delay", "silent", "tired of waiting", "ఎదురుచూచుట", "నిరీక్షణ", "ఆలస్యము"])
    has_guidance = any(w in query for w in ["confused", "confusion", "guidance", "decision", "direction", "crossroads", "what to do", "which path", "wisdom", "గందరగోళం", "నడిపింపు"])
    has_peace = any(w in query for w in ["peace", "sleep", "insomnia", "rest", "calm", "can't sleep", "cant sleep", "night terror", "శాంతి", "నిద్ర", "ప్రశాంతత"])
    has_gratitude = any(w in query for w in ["grateful", "thankful", "praise", "blessed", "joy", "rejoice", "thanksgiving", "కృతజ్ఞత", "స్తుతి", "ఆనందం"])
    has_addiction = any(w in query for w in ["addicted", "addiction", "alcohol", "drugs", "smoking", "pornography", "lust", "habits", "bondage", "chains", "వ్యసనము", "బానిసత్వం", "విడుదల"])

    best_match = None
    best_score = 0

    emo_list = load_json("emotions.json").get("emotions", EMOTIONS_DATA)
    for emo in emo_list:
        score = 0
        emo_id = emo.get("id", "")

        # Intent-based priority boosting
        if has_friend and has_anger and emo_id == "anger_at_friend_conflict":
            score += 45
        elif has_anger and emo_id == "anger_and_wrath" and not has_friend:
            score += 35
        elif has_money and emo_id == "financial_distress":
            score += 40
        elif has_sickness and emo_id == "sickness_and_healing":
            score += 40
        elif has_rejection and emo_id == "rejection_and_betrayal":
            score += 40
        elif has_hopeless and emo_id == "hopelessness_and_giving_up":
            score += 45
        elif has_waiting and emo_id == "waiting_on_god_impatience":
            score += 40
        elif has_guidance and emo_id == "confusion_and_guidance":
            score += 40
        elif has_peace and emo_id == "peace_and_rest":
            score += 40
        elif has_gratitude and emo_id == "gratitude_and_praise":
            score += 40
        elif has_addiction and emo_id == "addiction_and_bondage":
            score += 40

        for kw in emo.get("keywords", []):
            if kw == query:
                score += 30
            elif kw in query:
                score += 15
            elif any(w in kw for w in query_words if len(w) > 2):
                score += 4

        if score > best_score:
            best_score = score
            best_match = emo

    if best_match and best_score >= 5:
        return {
            "query": raw_query,
            "found": True,
            "data": best_match
        }

    # Fallback to downcast comfort ONLY if words explicitly indicate sadness/depression
    if any(term in query for term in ["depressed", "depression", "sad", "crying", "brokenhearted"]):
        dep = next((e for e in emo_list if e["id"] == "depressed"), None)
        return {"query": raw_query, "found": True, "data": dep}

    # Dynamic FTS5 scripture comfort fallback across 31,100 verses:
    conn = get_db()
    cur = conn.cursor()
    search_terms = [w for w in query_words if len(w) > 2 and w not in ["feel", "feeling", "today", "very", "much", "want"]]
    found_verses = []
    if search_terms:
        try:
            cur.execute(
                """SELECT book_name_en, book_name_te, chapter, verse, text_en, text_te
                   FROM verses 
                   WHERE verses MATCH ? 
                   LIMIT 4""",
                (" OR ".join(search_terms[:3]),)
            )
            found_verses = [dict(r) for r in cur.fetchall()]
        except Exception:
            pass
    conn.close()

    if found_verses:
        primary = found_verses[0]
        dynamic_emotion = {
            "id": "scripture_comfort",
            "title_en": f"Biblical Guidance & Promises for '{raw_query}'",
            "title_te": f"'{raw_query}' గురించి దేవుని వాక్య ఓదార్పు & వాగ్దానము",
            "primary_verse": {
                "reference": f"{primary['book_name_en']} {primary['chapter']}:{primary['verse']}",
                "book": primary["book_name_en"],
                "chapter": primary["chapter"],
                "verse": primary["verse"],
                "text_en": primary["text_en"],
                "text_te": primary["text_te"]
            },
            "supporting_verses": [
                {
                    "reference": f"{v['book_name_en']} {v['chapter']}:{v['verse']}",
                    "text_en": v["text_en"],
                    "text_te": v["text_te"]
                }
                for v in found_verses[1:]
            ],
            "pastoral_reflection": f"Whatever emotion or struggle you are facing regarding '{raw_query}', God's living Word has a divine answer. Casting all your care upon Him; for He careth for you (1 Peter 5:7). Surrender this circumstance in prayer and trust His sovereign grace.",
            "pastoral_reflection_te": f"'{raw_query}' విషయంలో మీరు ఎదుర్కొంటున్న మానసిక స్థితిని దేవుని పాదాల చెంత ఉంచండి. దేవుడు మీ గూర్చి చింతించుచున్నాడు గనుక మీ చింత యావత్తు ఆయనమీద వేయుడి (1 పేతురు 5:7).",
            "prayer_en": "Lord God, You know my heart, my thoughts, and the situation I am facing. Give me Your divine peace that surpasses all understanding. Anchor my soul in Your holy Word and lead me in Your righteous path. In Jesus' name, Amen.",
            "prayer_te": "ప్రభువైన దేవా, నా హృదయ తలంపులను మీరు ఎరిగియున్నారు. సమస్త జ్ఞానమునకు మించిన మీ సమాధానముతో నన్ను నింపండి. మీ జీవ వాక్యములో నన్ను స్థిరపరచి నడిపించండి. యేసు నామములో ప్రార్థిస్తున్నాను, ఆమేన్."
        }
        return {"query": raw_query, "found": True, "data": dynamic_emotion}

    return {"query": raw_query, "found": False, "data": None}

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

@app.get("/api/dictionary/words")
def get_dictionary_words(
    q: Optional[str] = None,
    letter: Optional[str] = None,
    category: Optional[str] = None,
    limit: int = 40,
    offset: int = 0
):
    conn = get_db()
    cur = conn.cursor()

    conditions = []
    params = []

    if q:
        clean_q = q.strip().lower()
        conditions.append("(word LIKE ? OR definition_en LIKE ? OR definition_te LIKE ?)")
        params.extend([f"%{clean_q}%", f"%{clean_q}%", f"%{clean_q}%"])

    if letter:
        clean_letter = letter.strip().lower()[:1]
        conditions.append("word LIKE ?")
        params.append(f"{clean_letter}%")

    if category and category.lower() != "all":
        conditions.append("category = ?")
        params.append(category)

    where_clause = ("WHERE " + " AND ".join(conditions)) if conditions else ""

    try:
        cur.execute(f"SELECT COUNT(*) FROM kjv_lexicon {where_clause}", params)
        total_count = cur.fetchone()[0]

        cur.execute(f"""
            SELECT id, word, display_word, category, occurrences_total, occurrences_ot, occurrences_nt,
                   first_reference, first_reference_te, definition_en, definition_te, context_note
            FROM kjv_lexicon
            {where_clause}
            ORDER BY 
                CASE WHEN category != 'Biblical Vocabulary' THEN 1 ELSE 2 END,
                occurrences_total DESC
            LIMIT ? OFFSET ?
        """, params + [limit, offset])
        rows = [dict(r) for r in cur.fetchall()]
    except Exception as e:
        total_count = 0
        rows = []
    finally:
        conn.close()

    return {
        "total": total_count,
        "limit": limit,
        "offset": offset,
        "words": rows
    }

@app.get("/api/dictionary/lookup")
def lookup_word(word: str, book: Optional[str] = None, chapter: Optional[int] = None):
    clean_word = word.lower().strip()
    if not clean_word:
        return {"found": False, "message": "Please provide a word."}

    conn = get_db()
    cur = conn.cursor()

    # 1. Check kjv_lexicon in database
    word_entry = None
    try:
        cur.execute("SELECT * FROM kjv_lexicon WHERE word = ? LIMIT 1", (clean_word,))
        row = cur.fetchone()
        if not row:
            cur.execute("SELECT * FROM kjv_lexicon WHERE word LIKE ? ORDER BY occurrences_total DESC LIMIT 1", (f"{clean_word}%",))
            row = cur.fetchone()
        if row:
            word_entry = dict(row)
    except Exception:
        pass

    # 2. Fetch bilingual verses containing this word via FTS5
    verses = []
    try:
        cur.execute("""
            SELECT v.id, b.name_en AS book_name_en, b.name_te AS book_name_te, b.testament, v.chapter, v.verse, v.text_en, v.text_te
            FROM verses v
            JOIN books b ON v.book_id = b.id
            WHERE v.rowid IN (SELECT rowid FROM verses_fts WHERE verses_fts MATCH ?)
            ORDER BY v.id ASC
            LIMIT 25
        """, (f'"{clean_word}"',))
        verses = [dict(r) for r in cur.fetchall()]
    except Exception:
        pass

    conn.close()

    if word_entry:
        return {
            "found": True,
            "word": word_entry["word"],
            "display_word": word_entry["display_word"],
            "category": word_entry["category"],
            "occurrences_total": word_entry["occurrences_total"],
            "occurrences_ot": word_entry["occurrences_ot"],
            "occurrences_nt": word_entry["occurrences_nt"],
            "first_reference": word_entry["first_reference"],
            "first_reference_te": word_entry["first_reference_te"],
            "first_text_en": word_entry.get("first_text_en"),
            "first_text_te": word_entry.get("first_text_te"),
            "definition_en": word_entry["definition_en"],
            "definition_te": word_entry["definition_te"],
            "context_note": word_entry["context_note"],
            "verses_count": len(verses),
            "verses": verses
        }

    if verses:
        first_v = verses[0]
        return {
            "found": True,
            "word": clean_word,
            "display_word": clean_word.capitalize(),
            "category": "Biblical Vocabulary",
            "occurrences_total": len(verses),
            "occurrences_ot": sum(1 for v in verses if v.get("testament") == "OT"),
            "occurrences_nt": sum(1 for v in verses if v.get("testament") == "NT"),
            "first_reference": f"{first_v['book_name_en']} {first_v['chapter']}:{first_v['verse']}",
            "first_reference_te": f"{first_v['book_name_te']} {first_v['chapter']}:{first_v['verse']}",
            "first_text_en": first_v["text_en"],
            "first_text_te": first_v["text_te"],
            "definition_en": f"Scriptural term appearing across the King James Bible.",
            "definition_te": f"పరిశుద్ధ గ్రంథములో ప్రస్తావించబడిన వాక్య పదము.",
            "context_note": f"First found in {first_v['book_name_en']} {first_v['chapter']}:{first_v['verse']}.",
            "verses_count": len(verses),
            "verses": verses
        }

    return {
        "word": word,
        "found": False,
        "message": f"No biblical occurrences found for '{word}' in the King James Bible."
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
    
    # 1. Check fresh pre-computed specific chapter context
    all_contexts = load_json("chapter_contexts.json").get("contexts", [])
    for entry in all_contexts:
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
    
    # 3. Dynamic contextual synthesis with moral assessment & biblical consequence analysis
    dynamic_entry = {
        "book": book_en,
        "chapter": chapter,
        "title_en": f"{book_en} Chapter {chapter}: Context, Moral Verdict & Divine Purpose",
        "title_te": f"{book_te} {chapter}వ అధ్యాయము: నేపథ్యం, నైతిక తీర్పు & దైవిక సంకల్పం",
        "moral_verdict": {
            "is_sin": False,
            "badge_en": "📜 BIBLICAL RECORD & DIVINE REVELATION",
            "badge_te": "📜 దైవిక ప్రత్యక్షత & లేఖన సత్యము",
            "summary_en": f"This chapter forms part of inspired Scripture revealing God's holiness, human moral accountability, and the unfolding drama of redemption. The Bible distinguishes between what God commands and what fallen humanity does.",
            "summary_te": f"ఈ అధ్యాయము దేవుని పరిశుద్ధతను, మానవ నైతిక బాధ్యతను మరియు రక్షణ ప్రణాళికను తెలియజేసే దైవ వాక్యభాగము. దేవుడు ఆజ్ఞాపించిన దానికి మరియు పాపపు మానవులు చేసిన పనులకు మధ్య బైబిల్ స్పష్టమైన తేడాను చూపుతుంది."
        },
        "backstory": {
            "summary_en": f"In {book_en} Chapter {chapter}, we witness a pivotal stage in {'Old Testament covenant history' if testament == 'OT' else 'New Testament apostolic revelation'}. The preceding narratives established the historical setting and the spiritual state of God's people in this era.",
            "summary_te": f"{book_te} {chapter}వ అధ్యాయము {'పాత నిబంధన దైవిక చరిత్రలో' if testament == 'OT' else 'నూతన నిబంధన సువార్త మరియు అపొస్తలుల బోధలలో'} ఒక ముఖ్యమైన ఘట్టము. దీనికి పూర్వము జరిగిన సంఘటనలు ప్రజల ఆత్మీయ స్థితిని మరియు దేవుని నడిపింపును తెలియజేస్తాయి."
        },
        "why_it_happened": {
            "summary_en": f"This chapter unfolds as a direct consequence of human choices, trials of faith, and God's sovereign intervention to teach, correct, test, or protect His people according to His holy character.",
            "summary_te": "మానవుల నిర్ణయాలు, విశ్వాస పోరాటాలు మరియు తన ప్రజలను సరిచేసి రక్షించుటకు దేవుడు స్వయంగా చేసిన కార్యం వలన ఈ సంఘటనలు జరిగినవి."
        },
        "consequences_of_sin": {
            "summary_en": f"Scripture demonstrates that obedience to God brings righteousness, peace, and covenant blessings, whereas human sin and moral rebellion bring sorrow, division, judgment, and spiritual exile.",
            "summary_te": "దేవునికి విధేయత చూపుట ద్వారా దీవెనలు, సమాధానము కలుగుననియు; పాపము మరియు అవిధేయత వలన శ్రమలు, దైవిక తీర్పు మరియు నష్టము కలుగుననియు లేఖనములు సత్యమును చాటుచున్నవి."
        },
        "gods_future_plan": {
            "summary_en": f"God allowed these specific events in {book_en} {chapter} not in isolation, but as a stepping stone toward His ultimate redemptive purpose: refining human character, fulfilling prophecy, and pointing toward eternal salvation in Christ.",
            "summary_te": f"దేవుడు {book_te} {chapter}వ అధ్యాయములోని సంగతులను కేవలం ఆ సమయము కొరకే కాక, భవిష్యత్తులో తన రక్షణ ప్రణాళికను, క్రీస్తు నందలి నిత్య వాగ్దానములను నెరవేర్చుట కొరకై ఒక సోపానముగా మలచుకొనెను."
        },
        "apologetics_for_critics": {
            "question_en": f"How should readers answer skeptics or critics questioning events in {book_en} {chapter}?",
            "question_te": f"ఈ అధ్యాయములోని సంఘటనలపై విమర్శకులు ప్రశ్నలు వేసినప్పుడు ఎలా సమాధానం చెప్పాలి?",
            "defense_en": f"The Bible is a truthful historical record, not a collection of mythical heroes. When Scripture records human failures or tragic sins, it does so to expose the danger of sin and highlight the holiness of God. The reporting of a sin is never an endorsement of it.",
            "defense_te": "బైబిల్ మానవ బలహీనతలను దాచిపెట్టే కల్పిత కథల పుస్తకం కాదు. మానవుల పాపములను లేఖనములు రికార్డ్ చేసినప్పుడు, పాపపు భయంకరత్వాన్ని హెచ్చరించడానికే తప్ప వాటిని సమర్థించడానికి కాదు. బైబిల్ సత్యసంధమైన పరిశుద్ధ గ్రంథము."
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
