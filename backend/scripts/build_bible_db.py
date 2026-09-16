import os
import sys
import json
import sqlite3
import time
import urllib.request
import urllib.parse

# Ensure UTF-8 output encoding for console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
RAW_TE_DIR = os.path.join(RAW_DIR, "telugu")
DB_PATH = os.path.join(DATA_DIR, "bible.db")

os.makedirs(RAW_TE_DIR, exist_ok=True)

KJV_URL = "https://raw.githubusercontent.com/thiagobodruk/bible/master/json/en_kjv.json"
TE_BASE_URL = "https://raw.githubusercontent.com/aruljohn/Bible-telugu/master"
TE_BOOKS_URL = f"{TE_BASE_URL}/Books.json"

NAME_MAP = {
    "Song of Solomon": "Song of Songs",
    "Song of Songs": "Song of Songs"
}

def fetch_url(url, retries=3):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=20) as resp:
                return resp.read()
        except Exception as e:
            print(f"Retry {i+1}/{retries} for {url}: {e}")
            time.sleep(1)
    raise RuntimeError(f"Failed to fetch {url}")

def download_raw_data():
    # 1. Download KJV
    kjv_file = os.path.join(RAW_DIR, "en_kjv.json")
    if not os.path.exists(kjv_file) or os.path.getsize(kjv_file) < 1000000:
        print("Downloading complete KJV English Bible...")
        data = fetch_url(KJV_URL)
        with open(kjv_file, "wb") as f:
            f.write(data)
        print("Downloaded KJV English Bible.")
    else:
        print("KJV English Bible already cached.")

    # 2. Download Telugu Books metadata
    books_meta_file = os.path.join(RAW_DIR, "telugu_books.json")
    if not os.path.exists(books_meta_file):
        print("Downloading Telugu books metadata...")
        data = fetch_url(TE_BOOKS_URL)
        with open(books_meta_file, "wb") as f:
            f.write(data)
    
    with open(books_meta_file, "r", encoding="utf-8") as f:
        te_books_list = json.load(f)

    # 3. Download Telugu chapters
    print("Downloading 66 Telugu Bible books...")
    for idx, item in enumerate(te_books_list):
        book_en = item["book"]["english"]
        safe_filename = f"{book_en}.json"
        dest_path = os.path.join(RAW_TE_DIR, safe_filename)
        if not os.path.exists(dest_path) or os.path.getsize(dest_path) < 100:
            encoded_name = urllib.parse.quote(safe_filename)
            book_url = f"{TE_BASE_URL}/{encoded_name}"
            try:
                content = fetch_url(book_url)
                with open(dest_path, "wb") as f:
                    f.write(content)
                print(f"[{idx+1}/66] Downloaded Telugu {book_en}")
            except Exception as e:
                print(f"Error downloading {book_en}: {e}")
        else:
            # already exists
            pass

    print("All Bible source data acquired.")

def build_database():
    print(f"Building SQLite database at {DB_PATH}...")
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Tables
    cur.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        book_num INTEGER NOT NULL,
        name_en TEXT NOT NULL,
        name_te TEXT NOT NULL,
        abbrev TEXT NOT NULL,
        testament TEXT NOT NULL,
        total_chapters INTEGER NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE verses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        book_name_en TEXT NOT NULL,
        book_name_te TEXT NOT NULL,
        chapter INTEGER NOT NULL,
        verse INTEGER NOT NULL,
        text_en TEXT NOT NULL,
        text_te TEXT NOT NULL,
        FOREIGN KEY(book_id) REFERENCES books(id)
    );
    """)

    cur.execute("""
    CREATE INDEX idx_verses_lookup ON verses(book_id, chapter, verse);
    """)

    # FTS5 Full-Text Search Table
    cur.execute("""
    CREATE VIRTUAL TABLE verses_fts USING fts5(
        book_name_en,
        book_name_te,
        chapter UNINDEXED,
        verse UNINDEXED,
        text_en,
        text_te,
        tokenize = 'unicode61'
    );
    """)

    # Load KJV
    kjv_file = os.path.join(RAW_DIR, "en_kjv.json")
    with open(kjv_file, "r", encoding="utf-8-sig") as f:
        kjv_data = json.load(f)

    # Load Telugu Books Meta
    books_meta_file = os.path.join(RAW_DIR, "telugu_books.json")
    with open(books_meta_file, "r", encoding="utf-8") as f:
        te_meta = json.load(f)

    te_name_dict = {}
    for item in te_meta:
        b_en = item["book"]["english"]
        b_te = item["book"]["telugu"]
        te_name_dict[b_en] = b_te
        if b_en == "Song of Songs":
            te_name_dict["Song of Solomon"] = b_te

    # Cache all telugu books in memory
    te_book_data = {}
    for file in os.listdir(RAW_TE_DIR):
        if file.endswith(".json"):
            b_name = file[:-5]
            with open(os.path.join(RAW_TE_DIR, file), "r", encoding="utf-8") as f:
                try:
                    te_book_data[b_name] = json.load(f)
                except Exception as e:
                    print(f"Error parsing {file}: {e}")

    total_inserted_verses = 0

    for book_idx, book_obj in enumerate(kjv_data):
        book_num = book_idx + 1
        name_en = book_obj["name"]
        abbrev = book_obj.get("abbrev", "")
        testament = "OT" if book_num <= 39 else "NT"
        name_te = te_name_dict.get(name_en, name_en)
        chapters_kjv = book_obj["chapters"]
        total_chapters = len(chapters_kjv)

        cur.execute(
            "INSERT INTO books (book_num, name_en, name_te, abbrev, testament, total_chapters) VALUES (?, ?, ?, ?, ?, ?)",
            (book_num, name_en, name_te, abbrev, testament, total_chapters)
        )
        book_db_id = cur.lastrowid

        # Look up Telugu book data
        te_lookup_name = NAME_MAP.get(name_en, name_en)
        te_obj = te_book_data.get(te_lookup_name)
        te_chapters_dict = {}
        if te_obj and "chapters" in te_obj:
            for ch_entry in te_obj["chapters"]:
                ch_num = int(ch_entry.get("chapter", 0))
                verses_map = {}
                for v in ch_entry.get("verses", []):
                    try:
                        v_num = int(v.get("verse", 0))
                        verses_map[v_num] = v.get("text", "")
                    except Exception:
                        pass
                te_chapters_dict[ch_num] = verses_map

        verse_rows = []
        fts_rows = []

        for ch_idx, chap_verses in enumerate(chapters_kjv):
            ch_num = ch_idx + 1
            te_ch_verses = te_chapters_dict.get(ch_num, {})

            for v_idx, text_en in enumerate(chap_verses):
                v_num = v_idx + 1
                text_te = te_ch_verses.get(v_num, "")

                verse_rows.append((
                    book_db_id, name_en, name_te, ch_num, v_num, text_en, text_te
                ))
                fts_rows.append((
                    name_en, name_te, str(ch_num), str(v_num), text_en, text_te
                ))

        cur.executemany(
            """INSERT INTO verses (book_id, book_name_en, book_name_te, chapter, verse, text_en, text_te)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            verse_rows
        )

        cur.executemany(
            """INSERT INTO verses_fts (book_name_en, book_name_te, chapter, verse, text_en, text_te)
               VALUES (?, ?, ?, ?, ?, ?)""",
            fts_rows
        )

        total_inserted_verses += len(verse_rows)
        if book_num % 10 == 0 or book_num == 66:
            print(f"Indexed {book_num}/66 books ({name_en}). Total verses: {total_inserted_verses}")

    conn.commit()
    conn.close()
    print(f"\nSUCCESS! Database complete with {total_inserted_verses} verses in English and Telugu.")
    print(f"Database saved to {DB_PATH}")

if __name__ == "__main__":
    download_raw_data()
    build_database()
