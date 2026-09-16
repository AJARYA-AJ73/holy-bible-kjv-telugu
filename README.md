# Holy Bible • పవిత్ర గ్రంథము (KJV & Telugu)

An intelligent, responsive bilingual Bible study web platform featuring the complete 66 books (31,100 verses) of the Holy Bible in both the **Authorized King James Version (KJV)** and **Telugu**, paired with semantic incident retrieval, emotional/pastoral counseling, an in-context dictionary, and a "Trials to Triumph" redemptive suffering guide.

---

## 🌟 Key Features

1. **Complete Bilingual Scripture Database:**
   - All 66 Books from Genesis to Revelation.
   - 31,100 verses aligned 1-to-1 in English and Telugu.
   - High-performance SQLite database with FTS5 Full-Text Search.
   - View modes: Parallel Split (side-by-side for laptops), Stacked (for smartphones), English-only, and Telugu-only.

2. **Heart & Soul Guidance ("I am depressed / anxious"):**
   - Natural language emotional matching (e.g. *"I'm depressed"*, *"anxious"*, *"lonely"*, *"afraid"*).
   - Serves targeted primary comfort scripture in English and Telugu.
   - Provides thoughtful pastoral reflection and heartfelt bilingual prayers.

3. **Semantic Incident & Story Finder ("Find a Story"):**
   - Search by natural recollection without knowing chapter or verse (e.g. *"man swallowed by a fish"*, *"parting of red sea"*, *"david defeats giant"*, *"water into wine"*).
   - Displays summaries and one-click navigation to open the exact chapter.

4. **"Trials to Triumph" (Suffering & God's Purpose):**
   - Explores the question: *"Why did God let them suffer?"*
   - Interactive narrative timeline for major biblical figures (Joseph, Job, Jesus, Daniel, Paul, Israelites):
     1. **The Crucible / Trial** (What happened)
     2. **God's Purpose** (Why it was permitted)
     3. **The Glorious Aftermath** (The restoration and eternal blessing!)
     4. **The Triumph Scripture** (e.g., Genesis 50:20, Job 42:10, 2 Timothy 4:7-8).

5. **In-Context Dictionary:**
   - Tap any archaic KJV word (*propitiation, firmament, beseech, quickened, selah, grace, justification, tribulation*) to see its modern English meaning, Telugu translation, and chapter-specific theological context.

---

## 🚀 How to Run the Web Application

### Option A: One-Click Launch (Windows)
Double-click the **`run.bat`** file located in this folder. It will launch the server and automatically open the application in your browser!

### Option B: From Command Line
1. Open PowerShell or Command Prompt in this folder.
2. Run:
   ```bash
   python backend/main.py
   ```
3. Open your browser to:
   ```
   http://localhost:8000
   ```

---

## 📱 How to Open on Mobile Phone (Same Wi-Fi)

To experience the mobile view on your phone with the exact same accuracy:
1. Make sure your phone and laptop are connected to the same Wi-Fi network.
2. Find your laptop's local IP address by opening Command Prompt and typing `ipconfig` (e.g., `192.168.1.15`).
3. Open Chrome or Safari on your phone and navigate to:
   ```
   http://<your-laptop-ip>:8000
   ```
*(e.g., `http://192.168.1.15:8000`)*

---

## 📂 Project Structure

```
BIBLE/
├── backend/
│   ├── data/
│   │   ├── bible.db              # SQLite DB containing 31,100 verses (KJV & Telugu) with FTS5
│   │   ├── incidents.json        # Curated major biblical incidents database
│   │   ├── emotions.json         # Pastoral guidance for emotional states & prayers
│   │   ├── suffering_arcs.json   # Trials to Triumph suffering aftermath arcs
│   │   └── dictionary.json       # In-context theological dictionary
│   ├── scripts/
│   │   ├── build_bible_db.py     # Script to download and compile Bible datasets
│   │   └── verify_api.py         # Automated test suite
│   └── main.py                   # FastAPI application server & static file host
├── frontend/
│   ├── index.html                # Responsive web app layout (Mobile & Desktop)
│   ├── style.css                 # Custom styling, fonts, and archaic word highlights
│   └── app.js                    # Client-side UI logic and API connectors
├── run.bat                       # One-click Windows launch script
└── README.md                     # Documentation
```
