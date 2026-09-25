# -*- coding: utf-8 -*-
"""
Builds an exhaustive KJV Bible Lexicon & Concordance Table in bible.db.
Indexes every single unique word (13,000+ words) across all 31,100 verses in the KJV,
tracking total occurrences, OT/NT distribution, first biblical occurrence,
and integrating curated theological definitions in English and Telugu.
"""
import sqlite3
import os
import re
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "bible.db")
DICT_JSON = os.path.join(DATA_DIR, "dictionary.json")

def build_lexicon():
    start_time = time.time()
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = NORMAL")
    cur = conn.cursor()

    print("Fetching all verses from bible.db...")
    cur.execute("""
        SELECT v.id, b.name_en, b.name_te, b.testament, v.chapter, v.verse, v.text_en, v.text_te
        FROM verses v
        JOIN books b ON v.book_id = b.id
        ORDER BY v.id ASC
    """)
    verses = cur.fetchall()
    print(f"Loaded {len(verses)} verses in {time.time() - start_time:.2f}s")

    # Word stats mapping
    word_stats = {}
    # regex for word tokens (at least 2 letters)
    word_pattern = re.compile(r'\b[a-zA-Z]+\b')

    for vid, b_en, b_te, test, chap, ver, t_en, t_te in verses:
        tokens = word_pattern.findall(t_en)
        seen_in_verse = set()
        for token in tokens:
            w_lower = token.lower()
            if len(w_lower) < 2:
                continue
            if w_lower not in word_stats:
                word_stats[w_lower] = {
                    "word": w_lower,
                    "display_word": token if token.istitle() or token.isupper() else w_lower,
                    "count_total": 0,
                    "count_ot": 0,
                    "count_nt": 0,
                    "first_book_en": b_en,
                    "first_book_te": b_te,
                    "first_chap": chap,
                    "first_ver": ver,
                    "first_text_en": t_en,
                    "first_text_te": t_te
                }
            entry = word_stats[w_lower]
            entry["count_total"] += 1
            if test == "OT":
                entry["count_ot"] += 1
            else:
                entry["count_nt"] += 1

    print(f"Extracted {len(word_stats)} unique vocabulary words across KJV Bible.")

    # Load curated dictionary definitions if available
    curated_defs = {}
    if os.path.exists(DICT_JSON):
        try:
            with open(DICT_JSON, "r", encoding="utf-8") as f:
                d_data = json.load(f)
                for item in d_data.get("words", []):
                    w_key = item["word"].lower().strip()
                    curated_defs[w_key] = item
            print(f"Loaded {len(curated_defs)} curated theological definitions.")
        except Exception as e:
            print("Notice loading dict.json:", e)

    # Recreate table
    cur.execute("DROP TABLE IF EXISTS kjv_lexicon")
    cur.execute("""
        CREATE TABLE kjv_lexicon (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT UNIQUE NOT NULL,
            display_word TEXT NOT NULL,
            category TEXT,
            occurrences_total INTEGER NOT NULL,
            occurrences_ot INTEGER NOT NULL,
            occurrences_nt INTEGER NOT NULL,
            first_reference TEXT,
            first_reference_te TEXT,
            first_text_en TEXT,
            first_text_te TEXT,
            definition_en TEXT,
            definition_te TEXT,
            context_note TEXT
        )
    """)
    cur.execute("CREATE INDEX idx_kjv_lexicon_word ON kjv_lexicon(word)")
    cur.execute("CREATE INDEX idx_kjv_lexicon_occurrences ON kjv_lexicon(occurrences_total DESC)")

    # Prepare insert rows
    insert_rows = []
    for w_lower, s in word_stats.items():
        curated = curated_defs.get(w_lower)
        first_ref = f"{s['first_book_en']} {s['first_chap']}:{s['first_ver']}"
        first_ref_te = f"{s['first_book_te']} {s['first_chap']}:{s['first_ver']}"

        if curated:
            def_en = curated.get("definition_en", "")
            def_te = curated.get("definition_te", "")
            cat = curated.get("category", "Theological Doctrines")
            note = curated.get("context_note", "")
        else:
            cat = "Biblical Vocabulary"
            def_en = f"Appears {s['count_total']} times in the King James Version ({s['count_ot']} in OT, {s['count_nt']} in NT). First mentioned in {first_ref}."
            def_te = f"ఈ పదము పరిశుద్ధ గ్రంథములో మొత్తం {s['count_total']} సార్లు ప్రస్తావించబడినది (పాత నిబంధనలో {s['count_ot']} సార్లు, నూతన నిబంధనలో {s['count_nt']} సార్లు). మొదటి ప్రస్తావన: {first_ref_te}."
            note = f"First occurrence in Scripture: {first_ref}"

        insert_rows.append((
            w_lower,
            s["display_word"],
            cat,
            s["count_total"],
            s["count_ot"],
            s["count_nt"],
            first_ref,
            first_ref_te,
            s["first_text_en"],
            s["first_text_te"],
            def_en,
            def_te,
            note
        ))

    cur.executemany("""
        INSERT INTO kjv_lexicon (
            word, display_word, category, occurrences_total, occurrences_ot, occurrences_nt,
            first_reference, first_reference_te, first_text_en, first_text_te,
            definition_en, definition_te, context_note
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, insert_rows)

    conn.commit()
    conn.close()
    print(f"Successfully populated kjv_lexicon with {len(insert_rows)} words in {time.time() - start_time:.2f}s!")

if __name__ == "__main__":
    import json
    build_lexicon()
