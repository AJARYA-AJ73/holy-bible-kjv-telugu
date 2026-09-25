// State Management
const STATE = {
  currentBook: { id: 1, book_num: 1, name_en: "Genesis", name_te: "ఆదికాండము", total_chapters: 50 },
  currentChapter: 1,
  layoutMode: window.innerWidth < 640 ? "stacked" : "parallel",
  fontSizeLevel: 1, // 0: sm, 1: base, 2: lg, 3: xl
  allBooks: [],
  knownWords: ["propitiation", "firmament", "beseech", "quickened", "selah", "grace", "justification", "sanctification", "tribulation", "covenant"],
  testamentFilter: "ALL"
};

// If opened via file:// fallback to laptop IP; otherwise relative path for zero CORS/port mismatch
const API_BASE = window.location.protocol === "file:" ? "http://192.168.31.180:8000" : "";

// Initialization
document.addEventListener("DOMContentLoaded", async () => {
  initLucide();
  await loadBooks();
  await loadChapter(STATE.currentBook.name_en, STATE.currentChapter);
  await loadSufferingArcs();
  await loadDictionaryList();
  await loadHistoricalEvidence();

  // Handle URL hash navigation if present
  const hash = window.location.hash.replace("#", "");
  if (hash) {
    switchTab(hash);
  } else {
    switchTab("reader");
  }

  updateLayoutButtons();

  // Auto-adapt layout on orientation change or screen resize
  window.addEventListener("resize", () => {
    if (window.innerWidth < 640 && STATE.layoutMode === "parallel") {
      setLayoutMode("stacked");
    }
  });
});

function initLucide() {
  if (window.lucide) {
    window.lucide.createIcons();
  }
}

// -------------------------------------------------------------
// TAB SWITCHING
// -------------------------------------------------------------
function switchTab(tabId) {
  const tabs = ["reader", "backstory", "emotions", "incidents", "suffering", "dictionary", "evidence"];
  tabs.forEach(t => {
    const el = document.getElementById(`tab-${t}`);
    const navBtn = document.getElementById(`nav-${t}`);
    const mobBtn = document.getElementById(`mob-${t}`);

    if (t === tabId) {
      el.classList.remove("hidden");
      if (navBtn) navBtn.classList.add("active");
      if (mobBtn) mobBtn.classList.add("active");
    } else {
      el.classList.add("hidden");
      if (navBtn) navBtn.classList.remove("active");
      if (mobBtn) mobBtn.classList.remove("active");
    }
  });

  // Header Book button only relevant on reader tab
  const headerBookBtn = document.getElementById("header-book-btn");
  if (headerBookBtn) {
    headerBookBtn.style.display = tabId === "reader" ? "flex" : "none";
  }

  window.location.hash = tabId;
  window.scrollTo({ top: 0, behavior: "smooth" });
  initLucide();
}

// -------------------------------------------------------------
// THEME TOGGLE
// -------------------------------------------------------------
function toggleTheme() {
  const isDark = document.documentElement.classList.toggle("dark");
  const icon = document.getElementById("theme-icon");
  if (icon) {
    icon.setAttribute("data-lucide", isDark ? "sun" : "moon");
    initLucide();
  }
}

// -------------------------------------------------------------
// SCRIPTURE READER LOGIC
// -------------------------------------------------------------
async function loadBooks() {
  try {
    const res = await fetch(`${API_BASE}/api/books`);
    STATE.allBooks = await res.json();
    renderBooksInModal();
  } catch (err) {
    console.error("Error loading books:", err);
  }
}

async function loadChapter(bookName, chapterNum) {
  const listEl = document.getElementById("verses-list");
  listEl.innerHTML = `<div class="text-center py-12 text-stone-400 dark:text-stone-500">Loading scripture...</div>`;

  try {
    const res = await fetch(`${API_BASE}/api/chapter?book_name=${encodeURIComponent(bookName)}&chapter=${chapterNum}`);
    const data = await res.json();
    
    STATE.currentBook = data.book;
    STATE.currentChapter = data.chapter;

    // Update Header and Titles
    document.getElementById("header-curr-book").innerText = `${data.book.name_en} ${data.chapter}`;
    document.getElementById("reader-title-en").innerText = `${data.book.name_en} Chapter ${data.chapter}`;
    document.getElementById("reader-title-te").innerText = `${data.book.name_te} ${data.chapter}వ అధ్యాయము`;

    renderVerses(data.verses);
  } catch (err) {
    listEl.innerHTML = `<div class="text-center py-12 text-rose-500">Error loading chapter. Please verify server is running.</div>`;
    console.error(err);
  }
}

function highlightKnownWords(text) {
  let processed = text;
  STATE.knownWords.forEach(word => {
    const regex = new RegExp(`\\b(${word})\\b`, 'gi');
    processed = processed.replace(regex, `<span class="archaic-word" onclick="openDictLookup('$1')">$1</span>`);
  });
  return processed;
}

function renderVerses(verses) {
  const listEl = document.getElementById("verses-list");
  listEl.innerHTML = "";

  const fontClasses = ["verse-font-sm", "verse-font-base", "verse-font-lg", "verse-font-xl"];
  const currentFontClass = fontClasses[STATE.fontSizeLevel] || "verse-font-base";

  verses.forEach(v => {
    const verseCard = document.createElement("div");
    verseCard.className = `p-3.5 sm:p-4 rounded-xl bg-white dark:bg-stone-800/80 border border-stone-200/70 dark:border-stone-700/60 shadow-xs hover:border-amber-300 dark:hover:border-amber-600/50 transition`;

    const enText = highlightKnownWords(v.text_en);
    const teText = v.text_te;

    if (STATE.layoutMode === "parallel") {
      // Split Left-Right columns
      verseCard.innerHTML = `
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 ${currentFontClass}">
          <div class="border-b md:border-b-0 md:border-r border-stone-100 dark:border-stone-700/60 pb-3 md:pb-0 md:pr-4">
            <span class="inline-block w-6 text-amber-600 dark:text-amber-400 font-bold text-xs select-none">${v.verse}</span>
            <span class="text-stone-800 dark:text-stone-200">${enText}</span>
          </div>
          <div class="md:pl-2">
            <span class="inline-block w-6 text-amber-700 dark:text-amber-500 font-bold text-xs font-telugu select-none">${v.verse}</span>
            <span class="text-stone-700 dark:text-stone-300 font-telugu leading-relaxed">${teText}</span>
          </div>
        </div>
      `;
    } else if (STATE.layoutMode === "stacked") {
      // Verse 1 EN followed immediately by Verse 1 TE
      verseCard.innerHTML = `
        <div class="${currentFontClass} space-y-2.5">
          <div class="flex items-start gap-2.5">
            <span class="text-amber-600 dark:text-amber-400 font-bold text-xs pt-0.5 select-none shrink-0 min-w-[24px]">${v.verse}</span>
            <p class="text-stone-800 dark:text-stone-200 flex-1 leading-relaxed">${enText}</p>
          </div>
          <div class="flex items-start gap-2.5 pt-2 border-t border-stone-100 dark:border-stone-700/60">
            <span class="text-amber-700 dark:text-amber-500 font-bold text-xs font-telugu pt-0.5 select-none shrink-0 min-w-[24px]">${v.verse}</span>
            <p class="text-stone-700 dark:text-stone-300 font-telugu leading-relaxed flex-1">${teText}</p>
          </div>
        </div>
      `;
    } else if (STATE.layoutMode === "en") {
      verseCard.innerHTML = `
        <div class="${currentFontClass} flex items-start gap-2">
          <span class="text-amber-600 dark:text-amber-400 font-bold text-xs pt-1 select-none">${v.verse}</span>
          <p class="text-stone-800 dark:text-stone-200 flex-1">${enText}</p>
        </div>
      `;
    } else if (STATE.layoutMode === "te") {
      verseCard.innerHTML = `
        <div class="${currentFontClass} flex items-start gap-2">
          <span class="text-amber-700 dark:text-amber-500 font-bold text-xs font-telugu pt-1 select-none">${v.verse}</span>
          <p class="text-stone-700 dark:text-stone-300 font-telugu leading-relaxed flex-1">${teText}</p>
        </div>
      `;
    }

    listEl.appendChild(verseCard);
  });
}

function setLayoutMode(mode) {
  STATE.layoutMode = mode;
  updateLayoutButtons();
  loadChapter(STATE.currentBook.name_en, STATE.currentChapter);
}

function updateLayoutButtons() {
  const modes = ["stacked", "parallel", "en", "te"];
  modes.forEach(m => {
    const btn = document.getElementById(`btn-mode-${m}`);
    if (btn) {
      if (STATE.layoutMode === m) {
        btn.className = "px-2.5 py-1 rounded-md transition font-medium bg-white dark:bg-stone-800 text-amber-600 shadow-xs";
      } else {
        btn.className = "px-2.5 py-1 rounded-md transition font-medium text-stone-500 hover:text-stone-700 dark:hover:text-stone-300";
      }
    }
  });
}

function changeFontSize(delta) {
  STATE.fontSizeLevel = Math.max(0, Math.min(3, STATE.fontSizeLevel + delta));
  loadChapter(STATE.currentBook.name_en, STATE.currentChapter);
}

function prevChapter() {
  if (STATE.currentChapter > 1) {
    loadChapter(STATE.currentBook.name_en, STATE.currentChapter - 1);
  } else {
    // Previous book
    const currIdx = STATE.allBooks.findIndex(b => b.id === STATE.currentBook.id);
    if (currIdx > 0) {
      const prevBook = STATE.allBooks[currIdx - 1];
      loadChapter(prevBook.name_en, prevBook.total_chapters);
    }
  }
}

function nextChapter() {
  if (STATE.currentChapter < STATE.currentBook.total_chapters) {
    loadChapter(STATE.currentBook.name_en, STATE.currentChapter + 1);
  } else {
    // Next book
    const currIdx = STATE.allBooks.findIndex(b => b.id === STATE.currentBook.id);
    if (currIdx < STATE.allBooks.length - 1) {
      const nextBook = STATE.allBooks[currIdx + 1];
      loadChapter(nextBook.name_en, 1);
    }
  }
}

// -------------------------------------------------------------
// BOOK & CHAPTER MODAL
// -------------------------------------------------------------
function openBookModal() {
  document.getElementById("book-modal").classList.remove("hidden");
  document.getElementById("modal-step-books").classList.remove("hidden");
  document.getElementById("modal-step-chapters").classList.add("hidden");
  initLucide();
}

function closeBookModal() {
  document.getElementById("book-modal").classList.add("hidden");
}

function setTestamentFilter(filter) {
  STATE.testamentFilter = filter;
  ["ALL", "OT", "NT"].forEach(f => {
    const btn = document.getElementById(`filter-${f.toLowerCase()}`);
    if (btn) {
      if (f === filter) btn.classList.add("active");
      else btn.classList.remove("active");
    }
  });
  renderBooksInModal();
}

function filterBooksList() {
  renderBooksInModal();
}

function renderBooksInModal() {
  const grid = document.getElementById("modal-books-grid");
  grid.innerHTML = "";

  const search = (document.getElementById("modal-book-search")?.value || "").toLowerCase().trim();

  const filtered = STATE.allBooks.filter(b => {
    if (STATE.testamentFilter !== "ALL" && b.testament !== STATE.testamentFilter) return false;
    if (search) {
      return b.name_en.toLowerCase().includes(search) || b.name_te.toLowerCase().includes(search);
    }
    return true;
  });

  filtered.forEach(b => {
    const btn = document.createElement("button");
    btn.className = `p-3 min-h-[50px] rounded-xl border text-left transition flex flex-col justify-center active:scale-95 ${
      b.id === STATE.currentBook.id 
        ? "bg-amber-50 dark:bg-amber-950/40 border-amber-400 dark:border-amber-600 shadow-xs" 
        : "border-stone-200 dark:border-stone-700 hover:bg-stone-50 dark:hover:bg-stone-800"
    }`;
    btn.onclick = () => selectBookForChapters(b);
    btn.innerHTML = `
      <span class="font-semibold text-xs text-stone-900 dark:text-stone-100">${b.name_en}</span>
      <span class="text-[11px] text-amber-700 dark:text-amber-400 font-telugu">${b.name_te}</span>
    `;
    grid.appendChild(btn);
  });
}

function selectBookForChapters(book) {
  document.getElementById("modal-step-books").classList.add("hidden");
  document.getElementById("modal-step-chapters").classList.remove("hidden");

  document.getElementById("selected-book-name-en").innerText = book.name_en;
  document.getElementById("selected-book-name-te").innerText = `${book.name_te} (${book.total_chapters} అధ్యాయాలు)`;

  const chaptersGrid = document.getElementById("modal-chapters-grid");
  chaptersGrid.innerHTML = "";

  for (let i = 1; i <= book.total_chapters; i++) {
    const btn = document.createElement("button");
    btn.className = `p-2.5 min-h-[44px] flex items-center justify-center text-center rounded-xl border text-sm font-semibold transition active:scale-90 ${
      book.id === STATE.currentBook.id && i === STATE.currentChapter
        ? "bg-amber-600 text-white border-amber-600 shadow-sm"
        : "border-stone-200 dark:border-stone-700 hover:bg-amber-50 dark:hover:bg-stone-800 text-stone-800 dark:text-stone-200"
    }`;
    btn.innerText = i;
    btn.onclick = () => {
      closeBookModal();
      loadChapter(book.name_en, i);
    };
    chaptersGrid.appendChild(btn);
  }
}

function backToBooks() {
  document.getElementById("modal-step-books").classList.remove("hidden");
  document.getElementById("modal-step-chapters").classList.add("hidden");
}

// -------------------------------------------------------------
// TAB 2: HEART SANCTUARY (EMOTIONS)
// -------------------------------------------------------------
function queryEmotionQuick(text) {
  document.getElementById("emotion-input").value = text;
  handleEmotionSearch();
}

async function handleEmotionSearch() {
  const query = document.getElementById("emotion-input").value.trim();
  if (!query) return;

  const container = document.getElementById("emotion-result-container");
  container.innerHTML = `<div class="text-center py-8 text-stone-400">Searching comfort scriptures...</div>`;

  try {
    const res = await fetch(`${API_BASE}/api/search/emotion`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });
    const result = await res.json();

    if (!result.found || !result.data) {
      container.innerHTML = `
        <div class="bg-amber-50 dark:bg-stone-800 p-6 rounded-2xl text-center border border-amber-200">
          <p class="text-sm text-stone-700 dark:text-stone-300">Come to Me, all you who labor and are heavy laden, and I will give you rest (Matthew 11:28). Speak your heart in prayer to God.</p>
        </div>
      `;
      return;
    }

    const d = result.data;
    container.innerHTML = `
      <div class="bg-white dark:bg-stone-800/90 rounded-3xl p-5 sm:p-7 border border-amber-200/80 dark:border-stone-700 shadow-md space-y-5">
        
        <!-- Badge & Title -->
        <div>
          <span class="text-xs bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-300 font-bold px-2.5 py-1 rounded-full uppercase tracking-wider">God's Promise for You</span>
          <h3 class="font-serif font-bold text-xl sm:text-2xl text-stone-900 dark:text-stone-100 mt-2">${d.title_en}</h3>
          <p class="text-xs sm:text-sm text-amber-700 dark:text-amber-400 font-telugu font-medium">${d.title_te}</p>
        </div>

        <!-- Primary Verse Hero Box -->
        <div class="bg-gradient-to-r from-amber-50 to-orange-50 dark:from-stone-900 dark:to-amber-950/40 p-5 rounded-2xl border border-amber-200 dark:border-amber-800/40 shadow-xs">
          <div class="flex items-center justify-between mb-2">
            <span class="font-serif font-bold text-amber-800 dark:text-amber-300 text-sm sm:text-base">${d.primary_verse.reference}</span>
            <button onclick="readPassageInReader('${d.primary_verse.book}', ${d.primary_verse.chapter})" class="text-xs text-amber-700 hover:text-amber-900 font-semibold flex items-center gap-1">
              Read in Context <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </button>
          </div>
          <p class="text-stone-900 dark:text-stone-100 text-base sm:text-lg font-serif italic mb-3">"${d.primary_verse.text_en}"</p>
          <p class="text-stone-700 dark:text-stone-300 font-telugu text-sm sm:text-base leading-relaxed pt-2 border-t border-amber-200/60 dark:border-stone-700">"${d.primary_verse.text_te}"</p>
        </div>

        <!-- Pastoral Reflection -->
        <div class="bg-stone-50 dark:bg-stone-900/60 p-4 sm:p-5 rounded-2xl border border-stone-200 dark:border-stone-700">
          <h4 class="font-semibold text-xs uppercase tracking-wider text-stone-500 dark:text-stone-400 mb-2 flex items-center gap-1.5">
            <i data-lucide="feather" class="w-3.5 h-3.5 text-amber-600"></i> Pastoral Word of Encouragement
          </h4>
          <p class="text-stone-700 dark:text-stone-300 text-xs sm:text-sm leading-relaxed mb-3">${d.pastoral_reflection}</p>
          <p class="text-stone-600 dark:text-stone-400 font-telugu text-xs sm:text-sm leading-relaxed border-t border-stone-200/60 dark:border-stone-700 pt-2">${d.pastoral_reflection_te}</p>
        </div>

        <!-- Supporting Scriptures -->
        ${d.supporting_verses && d.supporting_verses.length > 0 ? `
          <div>
            <h4 class="font-semibold text-xs uppercase tracking-wider text-stone-500 dark:text-stone-400 mb-2">Additional Anchors of Hope</h4>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
              ${d.supporting_verses.map(sv => `
                <div class="p-3.5 rounded-xl border border-stone-200/70 dark:border-stone-700 bg-white dark:bg-stone-800 text-xs">
                  <span class="font-bold text-amber-700 dark:text-amber-400 block mb-1">${sv.reference}</span>
                  <p class="text-stone-800 dark:text-stone-200 mb-1.5">${sv.text_en}</p>
                  <p class="text-stone-600 dark:text-stone-400 font-telugu border-t border-stone-100 dark:border-stone-700 pt-1">${sv.text_te}</p>
                </div>
              `).join('')}
            </div>
          </div>
        ` : ''}

        <!-- Prayer Box -->
        <div class="bg-amber-600/10 dark:bg-amber-900/20 p-5 rounded-2xl border border-amber-300 dark:border-amber-700/50">
          <div class="flex items-center gap-2 mb-2">
            <i data-lucide="hand-metal" class="w-4 h-4 text-amber-600"></i>
            <h4 class="font-serif font-bold text-sm text-amber-900 dark:text-amber-300">A Heartfelt Prayer You Can Pray Right Now</h4>
          </div>
          <p class="text-stone-800 dark:text-stone-200 italic text-xs sm:text-sm leading-relaxed mb-3">"${d.prayer_en}"</p>
          <p class="text-stone-700 dark:text-stone-300 font-telugu text-xs sm:text-sm leading-relaxed border-t border-amber-200/60 dark:border-amber-800/40 pt-2">"${d.prayer_te}"</p>
        </div>

      </div>
    `;
    initLucide();
  } catch (err) {
    container.innerHTML = `<div class="text-rose-500 text-center py-4">Error fetching comfort response.</div>`;
  }
}

// -------------------------------------------------------------
// TAB 3: INCIDENT FINDER
// -------------------------------------------------------------
function queryIncidentQuick(text) {
  document.getElementById("incident-input").value = text;
  handleIncidentSearch();
}

async function handleIncidentSearch() {
  const query = document.getElementById("incident-input").value.trim();
  if (!query) return;

  const container = document.getElementById("incidents-results-container");
  container.innerHTML = `<div class="text-center py-8 text-stone-400 col-span-2">Searching biblical accounts...</div>`;

  try {
    const res = await fetch(`${API_BASE}/api/search/incident`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });
    const data = await res.json();

    if (!data.results || data.results.length === 0) {
      container.innerHTML = `<div class="text-center py-8 text-stone-500 col-span-2">No matching incidents found. Try terms like 'fish', 'red sea', 'giant', 'bread', or 'water'.</div>`;
      return;
    }

    container.innerHTML = "";
    data.results.forEach(inc => {
      const card = document.createElement("div");
      card.className = "bg-white dark:bg-stone-800/90 rounded-2xl p-4 sm:p-5 border border-stone-200 dark:border-stone-700 shadow-sm flex flex-col justify-between hover:border-amber-400 transition";
      card.innerHTML = `
        <div>
          <div class="flex items-start justify-between gap-2 mb-2">
            <div>
              <h3 class="font-serif font-bold text-base sm:text-lg text-stone-900 dark:text-stone-100">${inc.title_en}</h3>
              <p class="text-xs text-amber-700 dark:text-amber-400 font-telugu font-medium">${inc.title_te}</p>
            </div>
            <span class="text-[11px] bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-300 font-semibold px-2 py-0.5 rounded shrink-0">
              ${inc.reference}
            </span>
          </div>

          <p class="text-xs sm:text-sm text-stone-700 dark:text-stone-300 leading-relaxed mb-3">
            ${inc.summary_en}
          </p>
          <p class="text-xs sm:text-sm text-stone-600 dark:text-stone-400 font-telugu leading-relaxed pt-2 border-t border-stone-100 dark:border-stone-700/60 mb-4">
            ${inc.summary_te}
          </p>
        </div>

        <button onclick="readPassageInReader('${inc.book}', ${inc.chapter_start})" class="w-full py-2 px-3 rounded-xl bg-amber-50 hover:bg-amber-100 dark:bg-stone-700 dark:hover:bg-stone-600 text-amber-800 dark:text-amber-300 text-xs font-semibold flex items-center justify-center gap-1.5 transition">
          <i data-lucide="book-open" class="w-3.5 h-3.5"></i> Read ${inc.book} ${inc.chapter_start} in Bible
        </button>
      `;
      container.appendChild(card);
    });

    initLucide();
  } catch (err) {
    container.innerHTML = `<div class="text-rose-500 text-center py-4 col-span-2">Error searching incidents.</div>`;
  }
}

function readPassageInReader(book, chapter) {
  switchTab("reader");
  loadChapter(book, chapter);
}

// -------------------------------------------------------------
// TAB 4: TRIALS TO TRIUMPH (SUFFERING ARCS)
// -------------------------------------------------------------
let cachedArcs = [];

async function loadSufferingArcs() {
  try {
    const res = await fetch(`${API_BASE}/api/suffering/arcs`);
    const data = await res.json();
    cachedArcs = data.arcs || [];
    renderSufferingArcs(cachedArcs);
  } catch (err) {
    console.error("Error loading suffering arcs:", err);
  }
}

function filterSufferingArc(filterId) {
  document.querySelectorAll(".arc-filter-btn").forEach(btn => {
    if (btn.innerText.toLowerCase().includes(filterId.replace("_", " ").toLowerCase()) || (filterId === "all" && btn.innerText === "All Figures")) {
      btn.classList.add("active");
    } else {
      btn.classList.remove("active");
    }
  });

  if (filterId === "all") {
    renderSufferingArcs(cachedArcs);
  } else {
    const filtered = cachedArcs.filter(a => a.id === filterId);
    renderSufferingArcs(filtered);
  }
}

function renderSufferingArcs(arcs) {
  const container = document.getElementById("suffering-arcs-container");
  container.innerHTML = "";

  arcs.forEach(arc => {
    const card = document.createElement("div");
    card.className = "bg-white dark:bg-stone-800/90 rounded-3xl p-5 sm:p-7 border border-amber-200/70 dark:border-stone-700 shadow-md";

    card.innerHTML = `
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-stone-200 dark:border-stone-700 pb-4 mb-5">
        <div>
          <span class="text-[11px] font-bold uppercase tracking-wider text-amber-600 dark:text-amber-400">Biblical Narrative Arc</span>
          <h3 class="font-serif font-bold text-xl sm:text-2xl text-stone-900 dark:text-stone-100">${arc.title_en}</h3>
          <p class="text-xs sm:text-sm text-amber-700 dark:text-amber-400 font-telugu font-medium">${arc.title_te}</p>
        </div>
        <span class="text-xs px-3 py-1 bg-stone-100 dark:bg-stone-700 rounded-full font-semibold self-start sm:self-auto">
          ${arc.person} (${arc.person_te})
        </span>
      </div>

      <!-- 3 Stage Process Grid -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        
        <!-- Stage 1: The Trial -->
        <div class="bg-rose-50/50 dark:bg-rose-950/20 p-4 rounded-2xl border border-rose-200/60 dark:border-rose-900/40">
          <div class="flex items-center gap-1.5 text-rose-700 dark:text-rose-400 font-bold text-xs uppercase tracking-wider mb-2">
            <i data-lucide="alert-triangle" class="w-4 h-4"></i> 1. The Crucible & Trial
          </div>
          <p class="text-xs text-stone-800 dark:text-stone-200 leading-relaxed mb-2">${arc.the_trial.summary_en}</p>
          <p class="text-xs text-stone-600 dark:text-stone-400 font-telugu leading-relaxed pt-2 border-t border-rose-200/40 dark:border-rose-900/40">${arc.the_trial.summary_te}</p>
        </div>

        <!-- Stage 2: God's Purpose -->
        <div class="bg-amber-50/50 dark:bg-amber-950/20 p-4 rounded-2xl border border-amber-200/60 dark:border-amber-900/40">
          <div class="flex items-center gap-1.5 text-amber-700 dark:text-amber-400 font-bold text-xs uppercase tracking-wider mb-2">
            <i data-lucide="shield-check" class="w-4 h-4"></i> 2. Why God Allowed It
          </div>
          <p class="text-xs text-stone-800 dark:text-stone-200 leading-relaxed mb-2">${arc.gods_purpose.summary_en}</p>
          <p class="text-xs text-stone-600 dark:text-stone-400 font-telugu leading-relaxed pt-2 border-t border-amber-200/40 dark:border-amber-900/40">${arc.gods_purpose.summary_te}</p>
        </div>

        <!-- Stage 3: The Aftermath -->
        <div class="bg-emerald-50/50 dark:bg-emerald-950/20 p-4 rounded-2xl border border-emerald-200/60 dark:border-emerald-900/40">
          <div class="flex items-center gap-1.5 text-emerald-700 dark:text-emerald-400 font-bold text-xs uppercase tracking-wider mb-2">
            <i data-lucide="crown" class="w-4 h-4"></i> 3. The Glorious Aftermath
          </div>
          <p class="text-xs text-stone-800 dark:text-stone-200 leading-relaxed mb-2">${arc.the_aftermath.summary_en}</p>
          <p class="text-xs text-stone-600 dark:text-stone-400 font-telugu leading-relaxed pt-2 border-t border-emerald-200/40 dark:border-emerald-900/40">${arc.the_aftermath.summary_te}</p>
        </div>

      </div>

      <!-- Triumph Scripture Banner -->
      <div class="bg-gradient-to-r from-amber-600 to-amber-700 text-white p-4 sm:p-5 rounded-2xl shadow-sm">
        <div class="flex items-center justify-between gap-2 mb-1">
          <span class="text-[11px] uppercase font-bold text-amber-200 tracking-wider">The Victorious Declaration</span>
          <span class="text-xs font-serif font-bold text-white bg-black/20 px-2.5 py-0.5 rounded">${arc.the_aftermath.triumph_verse.reference}</span>
        </div>
        <p class="font-serif italic text-sm sm:text-base text-white mb-2">"${arc.the_aftermath.triumph_verse.text_en}"</p>
        <p class="font-telugu text-xs sm:text-sm text-amber-100 leading-relaxed pt-2 border-t border-white/20">"${arc.the_aftermath.triumph_verse.text_te}"</p>
      </div>
    `;

    container.appendChild(card);
  });

  initLucide();
}

// -------------------------------------------------------------
// TAB 5: IN-CONTEXT DICTIONARY & FULL KJV LEXICON
// -------------------------------------------------------------
let dictState = {
  q: "",
  letter: "",
  category: "all",
  offset: 0,
  limit: 40,
  total: 0,
  words: [],
  debounceTimer: null
};

function initDictAlphaBar() {
  const container = document.getElementById("dict-alpha-bar");
  if (!container || container.children.length > 0) return;

  const allBtn = document.createElement("button");
  allBtn.className = "dict-alpha-btn active";
  allBtn.innerText = "All";
  allBtn.onclick = () => setDictLetter("");
  container.appendChild(allBtn);

  const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
  letters.forEach(letter => {
    const btn = document.createElement("button");
    btn.className = "dict-alpha-btn";
    btn.innerText = letter;
    btn.onclick = () => setDictLetter(letter);
    container.appendChild(btn);
  });
}

async function loadDictionaryList(reset = true) {
  if (reset) {
    dictState.offset = 0;
    dictState.words = [];
  }

  initDictAlphaBar();
  const statusEl = document.getElementById("dict-status-text");
  if (statusEl) statusEl.innerText = "Searching KJV Lexicon...";

  try {
    const params = new URLSearchParams({
      limit: dictState.limit,
      offset: dictState.offset
    });
    if (dictState.q) params.set("q", dictState.q);
    if (dictState.letter) params.set("letter", dictState.letter);
    if (dictState.category && dictState.category !== "all") params.set("category", dictState.category);

    const res = await fetch(`${API_BASE}/api/dictionary/words?${params.toString()}`);
    const data = await res.json();

    dictState.total = data.total || 0;
    if (reset) {
      dictState.words = data.words || [];
    } else {
      dictState.words = dictState.words.concat(data.words || []);
    }

    renderDictionaryList(dictState.words, !reset);

    // Update status bar
    if (statusEl) {
      if (dictState.q) {
        statusEl.innerText = `Found ${dictState.total} words matching "${dictState.q}"`;
      } else if (dictState.letter) {
        statusEl.innerText = `Letter "${dictState.letter}": ${dictState.total.toLocaleString()} KJV words`;
      } else if (dictState.category !== "all") {
        statusEl.innerText = `${dictState.category}: ${dictState.total.toLocaleString()} words`;
      } else {
        statusEl.innerText = `Showing ${dictState.words.length} of ${dictState.total.toLocaleString()} KJV Bible words`;
      }
    }

    // Toggle Load More button
    const loadMoreContainer = document.getElementById("dict-load-more-container");
    if (loadMoreContainer) {
      if (dictState.words.length < dictState.total) {
        loadMoreContainer.classList.remove("hidden");
      } else {
        loadMoreContainer.classList.add("hidden");
      }
    }
  } catch (err) {
    console.error("Error loading dictionary:", err);
    if (statusEl) statusEl.innerText = "Error connecting to Bible dictionary server.";
  }
}

function handleDictSearchInput() {
  clearTimeout(dictState.debounceTimer);
  const input = document.getElementById("dict-search-input");
  const clearBtn = document.getElementById("dict-clear-btn");
  const query = (input?.value || "").trim();

  if (clearBtn) {
    if (query) clearBtn.classList.remove("hidden");
    else clearBtn.classList.add("hidden");
  }

  dictState.debounceTimer = setTimeout(() => {
    dictState.q = query;
    dictState.offset = 0;
    loadDictionaryList(true);
  }, 250);
}

function clearDictSearch() {
  const input = document.getElementById("dict-search-input");
  if (input) input.value = "";
  const clearBtn = document.getElementById("dict-clear-btn");
  if (clearBtn) clearBtn.classList.add("hidden");
  dictState.q = "";
  dictState.offset = 0;
  loadDictionaryList(true);
}

function setDictCategory(cat) {
  dictState.category = cat;
  dictState.offset = 0;

  document.querySelectorAll(".dict-cat-btn").forEach(btn => {
    if (cat === "all" && btn.innerText.includes("All")) {
      btn.classList.add("active");
    } else if (btn.innerText.includes(cat)) {
      btn.classList.add("active");
    } else {
      btn.classList.remove("active");
    }
  });

  loadDictionaryList(true);
}

function setDictLetter(letter) {
  dictState.letter = letter;
  dictState.offset = 0;

  document.querySelectorAll(".dict-alpha-btn").forEach(btn => {
    if ((!letter && btn.innerText === "All") || btn.innerText === letter) {
      btn.classList.add("active");
    } else {
      btn.classList.remove("active");
    }
  });

  loadDictionaryList(true);
}

function loadMoreDictionaryWords() {
  dictState.offset += dictState.limit;
  loadDictionaryList(false);
}

function renderDictionaryList(words, append = false) {
  const container = document.getElementById("dictionary-list-container");
  if (!container) return;
  if (!append) container.innerHTML = "";

  if (words.length === 0) {
    container.innerHTML = `
      <div class="col-span-2 text-center py-10 bg-white dark:bg-stone-800/60 rounded-3xl border border-stone-200 dark:border-stone-700">
        <i data-lucide="book-x" class="w-10 h-10 text-stone-400 mx-auto mb-2"></i>
        <h4 class="font-serif font-bold text-base text-stone-800 dark:text-stone-200">No words found</h4>
        <p class="text-xs text-stone-500">Try searching for any KJV word e.g. "chariot", "mercy", "covenant", or "propitiation".</p>
      </div>
    `;
    initLucide();
    return;
  }

  const fragment = document.createDocumentFragment();
  const wordsToRender = append ? words.slice(dictState.offset) : words;

  wordsToRender.forEach(w => {
    const card = document.createElement("div");
    card.className = "bg-white dark:bg-stone-800/90 rounded-2xl p-4 sm:p-5 border border-stone-200 dark:border-stone-700 shadow-xs hover:border-amber-400 hover:shadow-md transition cursor-pointer flex flex-col justify-between";
    card.onclick = () => openDictLookup(w.word);

    const isTheological = w.category && w.category !== "Biblical Vocabulary";
    const catBadgeClass = isTheological 
      ? "bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-300"
      : "bg-stone-100 dark:bg-stone-700 text-stone-600 dark:text-stone-300";

    card.innerHTML = `
      <div>
        <div class="flex items-center justify-between mb-2 gap-2 flex-wrap">
          <h4 class="font-serif font-bold text-lg text-stone-900 dark:text-stone-100 capitalize">${w.display_word || w.word}</h4>
          <div class="flex items-center gap-1.5">
            <span class="text-[10px] ${catBadgeClass} px-2 py-0.5 rounded font-semibold uppercase tracking-wider">${w.category || "Vocabulary"}</span>
            ${w.occurrences_total ? `<span class="text-[10px] bg-amber-50 dark:bg-stone-700 text-amber-700 dark:text-amber-300 px-2 py-0.5 rounded font-semibold">${w.occurrences_total}x in KJV</span>` : ""}
          </div>
        </div>
        <p class="text-xs sm:text-sm text-stone-800 dark:text-stone-200 mb-2 leading-relaxed">${w.definition_en || "Biblical term in the King James Version."}</p>
        <p class="text-xs sm:text-sm text-amber-800 dark:text-amber-400 font-telugu leading-relaxed pt-2 border-t border-stone-100 dark:border-stone-700 mb-2">${w.definition_te || "పరిశుద్ధ గ్రంథములో ప్రస్తావించబడిన వాక్య పదము."}</p>
        ${w.first_reference ? `
          <div class="text-[11px] text-stone-500 dark:text-stone-400 flex items-center gap-1 mt-1">
            <span class="font-semibold text-stone-600 dark:text-stone-300">First in:</span> ${w.first_reference} (${w.first_reference_te || ""})
          </div>
        ` : ""}
      </div>
      <div class="mt-3 pt-2 border-t border-stone-100 dark:border-stone-700/60 flex items-center justify-between text-[11px] text-amber-600 dark:text-amber-400 font-medium">
        <span>Click to view concordance verses</span>
        <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
      </div>
    `;
    fragment.appendChild(card);
  });

  container.appendChild(fragment);
  initLucide();
}

async function openDictLookup(word) {
  const modal = document.getElementById("dict-modal");
  if (!modal) return;

  document.getElementById("dict-modal-word").innerText = word;
  document.getElementById("dict-modal-en").innerText = "Loading theological definition & concordance...";
  document.getElementById("dict-modal-te").innerText = "వివరణ లోడ్ అవుతోంది...";
  document.getElementById("dict-modal-stats").innerText = "Searching occurrences...";
  document.getElementById("dict-modal-context-wrapper").classList.add("hidden");
  document.getElementById("dict-modal-first-wrapper").classList.add("hidden");
  document.getElementById("dict-modal-verses-list").innerHTML = "<div class='text-xs text-stone-400 py-3 text-center'>Searching verses in KJV & Telugu...</div>";
  modal.classList.remove("hidden");

  try {
    const bookParam = STATE.currentBook ? encodeURIComponent(STATE.currentBook.name_en) : "";
    const res = await fetch(`${API_BASE}/api/dictionary/lookup?word=${encodeURIComponent(word)}&book=${bookParam}&chapter=${STATE.currentChapter || 1}`);
    const data = await res.json();

    if (data.found) {
      document.getElementById("dict-modal-word").innerText = data.display_word || data.word;
      document.getElementById("dict-modal-cat").innerText = data.category || "Theological Lexicon";
      
      const statsText = data.occurrences_total !== undefined
        ? `Appears ${data.occurrences_total} times in KJV (${data.occurrences_ot || 0} OT, ${data.occurrences_nt || 0} NT)`
        : "Found in Scripture";
      document.getElementById("dict-modal-stats").innerText = statsText;

      document.getElementById("dict-modal-en").innerText = data.definition_en || "Biblical word in the King James Bible.";
      document.getElementById("dict-modal-te").innerText = data.definition_te || "పరిశుద్ధ గ్రంథములో ప్రస్తావించబడిన వాక్య పదము.";

      // First occurrence
      if (data.first_reference && data.first_text_en) {
        const firstWrap = document.getElementById("dict-modal-first-wrapper");
        firstWrap.classList.remove("hidden");
        document.getElementById("dict-modal-first-ref").innerText = `${data.first_reference} (${data.first_reference_te || ""})`;
        document.getElementById("dict-modal-first-text-en").innerText = `"${data.first_text_en}"`;
        document.getElementById("dict-modal-first-text-te").innerText = `"${data.first_text_te || ""}"`;
      }

      // Context note
      const ctxWrapper = document.getElementById("dict-modal-context-wrapper");
      if (data.context_note) {
        ctxWrapper.classList.remove("hidden");
        document.getElementById("dict-modal-context").innerText = data.context_note;
      } else {
        ctxWrapper.classList.add("hidden");
      }

      // Verses list
      const versesList = document.getElementById("dict-modal-verses-list");
      const versesCount = document.getElementById("dict-modal-verses-count");
      const verses = data.verses || [];

      if (versesCount) {
        versesCount.innerText = verses.length > 0 ? `Showing first ${verses.length} verses` : "No verses found";
      }

      if (verses.length > 0) {
        versesList.innerHTML = verses.map(v => `
          <div class="p-2.5 rounded-xl bg-stone-50 dark:bg-stone-800 border border-stone-200/60 dark:border-stone-700/60 text-xs">
            <div class="flex items-center justify-between mb-1">
              <span class="font-bold text-amber-700 dark:text-amber-400">
                ${v.book_name_en} ${v.chapter}:${v.verse}
              </span>
              <span class="text-[11px] font-semibold text-stone-500 font-telugu">
                ${v.book_name_te} ${v.chapter}:${v.verse}
              </span>
            </div>
            <p class="text-stone-800 dark:text-stone-200 leading-relaxed mb-1">${v.text_en}</p>
            <p class="text-stone-700 dark:text-stone-300 font-telugu leading-relaxed pt-1 border-t border-stone-200/40 dark:border-stone-700/40">${v.text_te}</p>
          </div>
        `).join("");
      } else {
        versesList.innerHTML = "<div class='text-xs text-stone-500 text-center py-2'>No verses retrieved.</div>";
      }
    } else {
      document.getElementById("dict-modal-en").innerText = data.message || `No occurrences found for '${word}'.`;
      document.getElementById("dict-modal-te").innerText = `'${word}' పదమునకు వివరములు లభించలేదు.`;
      document.getElementById("dict-modal-stats").innerText = "Not found in KJV";
      document.getElementById("dict-modal-verses-list").innerHTML = "";
    }

    initLucide();
  } catch (err) {
    console.error("Error opening dictionary lookup:", err);
  }
}

function closeDictModal() {
  const modal = document.getElementById("dict-modal");
  if (modal) modal.classList.add("hidden");
}

// -------------------------------------------------------------
// MOBILE PHONE QR MODAL
// -------------------------------------------------------------
function openQrModal() {
  const modal = document.getElementById("qr-modal");
  if (modal) {
    modal.classList.remove("hidden");
    initLucide();
  }
}

function closeQrModal() {
  const modal = document.getElementById("qr-modal");
  if (modal) {
    modal.classList.add("hidden");
  }
}

// -------------------------------------------------------------
// CHAPTER CONTEXT (BACKSTORY, WHY IT HAPPENED & GOD'S FUTURE PLAN)
// -------------------------------------------------------------
async function openChapterContext() {
  const modal = document.getElementById("context-modal");
  if (!modal) return;

  // Set loading state
  document.getElementById("context-modal-title-en").innerText = `${STATE.currentBook.name_en} ${STATE.currentChapter}`;
  document.getElementById("context-modal-title-te").innerText = `${STATE.currentBook.name_te} ${STATE.currentChapter}వ అధ్యాయము`;
  document.getElementById("context-backstory-en").innerText = "Uncovering historical and spiritual backstory...";
  document.getElementById("context-backstory-te").innerText = "";
  document.getElementById("context-why-en").innerText = "Analyzing human choices and divine circumstances...";
  document.getElementById("context-why-te").innerText = "";
  document.getElementById("context-plan-en").innerText = "Revealing God's redemptive purpose...";
  document.getElementById("context-plan-te").innerText = "";

  modal.classList.remove("hidden");
  initLucide();

  try {
    const res = await fetch(`${API_BASE}/api/context/chapter?book=${encodeURIComponent(STATE.currentBook.name_en)}&chapter=${STATE.currentChapter}`);
    const data = await res.json();
    if (data.context) {
      const c = data.context;
      document.getElementById("context-modal-title-en").innerText = c.title_en;
      document.getElementById("context-modal-title-te").innerText = c.title_te;
      document.getElementById("context-backstory-en").innerText = c.backstory.summary_en;
      document.getElementById("context-backstory-te").innerText = c.backstory.summary_te;
      document.getElementById("context-why-en").innerText = c.why_it_happened.summary_en;
      document.getElementById("context-why-te").innerText = c.why_it_happened.summary_te;
      document.getElementById("context-plan-en").innerText = c.gods_future_plan.summary_en;
      document.getElementById("context-plan-te").innerText = c.gods_future_plan.summary_te;
    }
  } catch (err) {
    console.error("Error loading chapter context:", err);
    document.getElementById("context-backstory-en").innerText = "Failed to load chapter context. Please verify backend connection.";
  }
}

function closeChapterContext() {
  const modal = document.getElementById("context-modal");
  if (modal) modal.classList.add("hidden");
}

// -------------------------------------------------------------
// TAB 6: HISTORICAL PROOFS & EVIDENCES OF JESUS CHRIST
// -------------------------------------------------------------
let cachedEvidences = [];

async function loadHistoricalEvidence() {
  try {
    const res = await fetch(`${API_BASE}/api/evidence/historical`);
    const data = await res.json();
    cachedEvidences = data.evidences || [];
    renderHistoricalEvidence(cachedEvidences);
  } catch (err) {
    console.error("Error loading historical evidence:", err);
  }
}

function filterEvidence(categoryId) {
  document.querySelectorAll(".evidence-filter-btn").forEach(btn => {
    const btnText = btn.innerText.toLowerCase();
    if (
      (categoryId === "all" && btnText.includes("all")) ||
      (categoryId === "roman_historians" && btnText.includes("roman")) ||
      (categoryId === "jewish_sources" && btnText.includes("jewish")) ||
      (categoryId === "archaeology" && btnText.includes("archaeology")) ||
      (categoryId === "manuscripts" && btnText.includes("manuscripts"))
    ) {
      btn.classList.add("active");
    } else {
      btn.classList.remove("active");
    }
  });

  if (categoryId === "all") {
    renderHistoricalEvidence(cachedEvidences);
  } else {
    const filtered = cachedEvidences.filter(e => e.category === categoryId);
    renderHistoricalEvidence(filtered);
  }
}

function renderHistoricalEvidence(evidences) {
  const container = document.getElementById("evidence-cards-container");
  if (!container) return;
  container.innerHTML = "";

  evidences.forEach(ev => {
    const card = document.createElement("div");
    card.className = "bg-white dark:bg-stone-800/90 rounded-3xl p-5 sm:p-6 border border-amber-200/70 dark:border-stone-700 shadow-sm flex flex-col justify-between hover:border-amber-400 transition";

    card.innerHTML = `
      <div>
        <div class="flex items-start justify-between gap-2 mb-3">
          <div>
            <span class="text-[10px] uppercase font-bold text-amber-600 dark:text-amber-400 tracking-wider">${ev.source}</span>
            <h3 class="font-serif font-bold text-lg text-stone-900 dark:text-stone-100 mt-0.5">${ev.title_en}</h3>
            <p class="text-xs text-amber-700 dark:text-amber-400 font-telugu font-medium">${ev.title_te}</p>
          </div>
          <span class="text-[11px] bg-stone-100 dark:bg-stone-700 font-semibold px-2.5 py-1 rounded-full text-stone-700 dark:text-stone-300 shrink-0">
            ${ev.author}
          </span>
        </div>

        <!-- Ancient Quotation Block -->
        <div class="bg-amber-50/60 dark:bg-stone-900/60 p-4 rounded-2xl border border-amber-200/60 dark:border-stone-700 mb-4">
          <span class="text-[10px] uppercase font-bold text-amber-800 dark:text-amber-400 tracking-wider block mb-1">Ancient Record / Inscription:</span>
          <p class="font-serif italic text-xs sm:text-sm text-stone-900 dark:text-stone-100 leading-relaxed mb-2">${ev.quote_en}</p>
          <p class="font-telugu text-xs text-stone-700 dark:text-stone-300 leading-relaxed pt-2 border-t border-amber-200/50 dark:border-stone-700">${ev.quote_te}</p>
        </div>

        <!-- Historical Significance -->
        <div class="space-y-2 text-xs sm:text-sm">
          <p class="text-stone-700 dark:text-stone-300 leading-relaxed">
            <strong class="text-stone-900 dark:text-stone-100">Historical Proof:</strong> ${ev.significance_en}
          </p>
          <p class="text-stone-600 dark:text-stone-400 font-telugu leading-relaxed pt-1.5 border-t border-stone-100 dark:border-stone-700/60">
            ${ev.significance_te}
          </p>
        </div>
      </div>
    `;

    container.appendChild(card);
  });

  initLucide();
}

// -------------------------------------------------------------
// TAB: VERSE BACKSTORY & GOD'S PURPOSE (MANUAL LOOKUP)
// -------------------------------------------------------------
function jumpToChapter(bookName, chapterNum) {
  switchTab("reader");
  loadChapter(bookName, chapterNum);
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function jumpToBackstory(bookName, chapterNum) {
  switchTab("backstory");
  const input = document.getElementById("backstory-query-input");
  if (input) {
    input.value = `${bookName} ${chapterNum}`;
    handleBackstorySearch();
  }
}

function queryBackstoryQuick(ref) {
  const input = document.getElementById("backstory-query-input");
  if (input) {
    input.value = ref;
    handleBackstorySearch();
  }
}

async function handleBackstorySearch() {
  const input = document.getElementById("backstory-query-input");
  const query = input ? input.value.trim() : "";
  if (!query) return;

  const container = document.getElementById("backstory-results-container");
  if (!container) return;

  container.innerHTML = `
    <div class="bg-white dark:bg-stone-800/90 rounded-3xl p-8 border border-amber-200/60 dark:border-stone-700 shadow-sm text-center">
      <div class="inline-block animate-spin text-amber-600 dark:text-amber-400 mb-3">
        <i data-lucide="loader-2" class="w-8 h-8"></i>
      </div>
      <p class="text-stone-800 dark:text-stone-200 font-serif font-bold text-base">Uncovering Context, Backstory & God's Purpose for "${query}"...</p>
      <p class="text-xs text-stone-500 dark:text-stone-400 font-telugu mt-1">పూర్వ నేపథ్యం, ఎందుకు జరిగింది మరియు దేవుని భవిష్యత్ సంకల్పమును పరిశీలిస్తున్నాము...</p>
    </div>
  `;
  initLucide();

  try {
    const res = await fetch(`${API_BASE}/api/context/lookup`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });
    const data = await res.json();
    if (data.found) {
      renderBackstoryResult(data);
    } else {
      container.innerHTML = `
        <div class="bg-white dark:bg-stone-800/90 rounded-3xl p-6 sm:p-8 border border-amber-200/60 dark:border-stone-700 shadow-sm text-center">
          <div class="w-12 h-12 rounded-2xl bg-amber-100 dark:bg-amber-950 text-amber-600 flex items-center justify-center mx-auto mb-3">
            <i data-lucide="help-circle" class="w-6 h-6"></i>
          </div>
          <h3 class="font-serif font-bold text-lg text-stone-900 dark:text-stone-100 mb-2">Passage Not Found</h3>
          <p class="text-stone-600 dark:text-stone-400 text-xs sm:text-sm max-w-md mx-auto mb-4 leading-relaxed">
            ${data.message || "We couldn't identify the verse or chapter. Try typing e.g. 'Genesis 37:20', 'John 11', 'Exodus 14', or 'Matthew 27'."}
          </p>
          <div class="flex flex-wrap justify-center gap-2">
            <button onclick="queryBackstoryQuick('Genesis 37')" class="chip-btn">Genesis 37</button>
            <button onclick="queryBackstoryQuick('Exodus 14')" class="chip-btn">Exodus 14</button>
            <button onclick="queryBackstoryQuick('1 Samuel 17')" class="chip-btn">1 Samuel 17</button>
            <button onclick="queryBackstoryQuick('John 11')" class="chip-btn">John 11</button>
          </div>
        </div>
      `;
      initLucide();
    }
  } catch (err) {
    console.error("Backstory search error:", err);
    container.innerHTML = `
      <div class="bg-rose-50 dark:bg-rose-950/40 p-6 rounded-2xl border border-rose-200 dark:border-rose-900 text-rose-800 dark:text-rose-200 text-center text-sm">
        Unable to connect to the Bible server. Please check your connection.
      </div>
    `;
  }
}

function renderBackstoryResult(data) {
  const container = document.getElementById("backstory-results-container");
  if (!container) return;

  const ctx = data.context || {};
  const verses = data.verses || [];
  const isSingleVerse = !!data.verse;

  let versesHtml = "";
  if (verses.length > 0) {
    versesHtml = `
      <div class="bg-stone-50 dark:bg-stone-900/80 rounded-2xl p-4 sm:p-5 border border-stone-200 dark:border-stone-700 mb-6">
        <div class="flex items-center justify-between mb-3 border-b border-stone-200/60 dark:border-stone-700/60 pb-2">
          <div class="flex items-center gap-2">
            <i data-lucide="book-open" class="w-4 h-4 text-amber-600"></i>
            <span class="font-serif font-bold text-xs sm:text-sm text-stone-900 dark:text-stone-100">
              Scripture Text (${data.reference})
            </span>
          </div>
          <span class="text-xs text-amber-700 dark:text-amber-400 font-telugu font-medium">
            ${data.reference_te}
          </span>
        </div>
        <div class="space-y-3 max-h-72 overflow-y-auto pr-1">
          ${verses.map(v => `
            <div class="text-xs sm:text-sm grid grid-cols-1 md:grid-cols-2 gap-2.5 pb-2.5 border-b border-stone-200/40 dark:border-stone-800 last:border-0 last:pb-0">
              <div>
                <span class="font-bold text-amber-600 dark:text-amber-400 select-none mr-1.5">${v.verse}.</span>
                <span class="text-stone-800 dark:text-stone-200 leading-relaxed">${v.text_en}</span>
              </div>
              <div>
                <span class="font-bold text-amber-700 dark:text-amber-500 font-telugu select-none mr-1.5">${v.verse}.</span>
                <span class="text-stone-700 dark:text-stone-300 font-telugu leading-relaxed">${v.text_te}</span>
              </div>
            </div>
          `).join("")}
        </div>
        ${!isSingleVerse && verses.length >= 10 ? `
          <div class="mt-2 pt-2 border-t border-stone-200/60 dark:border-stone-700 text-center">
            <span class="text-[11px] text-stone-500 dark:text-stone-400">Showing first 10 verses. Click "Open Full Chapter" below to view the entire chapter.</span>
          </div>
        ` : ""}
      </div>
    `;
  }

  container.innerHTML = `
    <div class="bg-white dark:bg-stone-800/90 rounded-3xl p-5 sm:p-7 border border-amber-200/70 dark:border-stone-700 shadow-md">
      
      <!-- Top Title & Navigation -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-5 border-b border-stone-200/70 dark:border-stone-700">
        <div>
          <div class="flex items-center gap-2 mb-1.5 flex-wrap">
            <span class="text-xs uppercase font-bold tracking-wider px-2.5 py-1 rounded-full bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-300 border border-amber-300/40">
              ${data.reference}
            </span>
            <span class="text-xs font-semibold font-telugu text-amber-700 dark:text-amber-400">
              ${data.reference_te}
            </span>
          </div>
          <h2 class="font-serif font-bold text-lg sm:text-2xl text-stone-900 dark:text-stone-100">
            ${ctx.title_en || `${data.book.name_en} ${data.chapter}`}
          </h2>
          <p class="text-xs sm:text-sm text-stone-600 dark:text-stone-400 font-telugu mt-0.5">
            ${ctx.title_te || `${data.book.name_te} ${data.chapter}వ అధ్యాయము`}
          </p>
        </div>

        <button onclick="jumpToChapter('${data.book.name_en}', ${data.chapter})" class="px-4 py-2 rounded-xl bg-amber-50 dark:bg-stone-700 hover:bg-amber-100 dark:hover:bg-stone-600 text-amber-800 dark:text-amber-300 border border-amber-200 dark:border-stone-600 text-xs font-semibold transition flex items-center justify-center gap-1.5 shrink-0 active:scale-95 shadow-xs">
          <i data-lucide="book-open" class="w-4 h-4"></i>
          <span>Open Full Chapter</span>
        </button>
      </div>

      <!-- MORAL VERDICT & DIVINE ASSESSMENT BANNER -->
      ${ctx.moral_verdict ? `
        <div class="mt-5 p-4 sm:p-5 rounded-2xl border ${
          ctx.moral_verdict.is_sin
            ? "bg-rose-50/90 dark:bg-rose-950/40 border-rose-300 dark:border-rose-900/60"
            : "bg-emerald-50/90 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-900/60"
        } shadow-xs">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 rounded-xl ${
              ctx.moral_verdict.is_sin ? "bg-rose-600 text-white" : "bg-emerald-600 text-white"
            } flex items-center justify-center shrink-0 shadow-xs mt-0.5">
              <i data-lucide="${ctx.moral_verdict.is_sin ? "alert-triangle" : "check-circle"}" class="w-5 h-5"></i>
            </div>
            <div class="space-y-1.5 flex-1">
              <div class="flex items-center gap-2 flex-wrap">
                <span class="text-xs font-bold uppercase tracking-wider ${
                  ctx.moral_verdict.is_sin ? "text-rose-800 dark:text-rose-300" : "text-emerald-800 dark:text-emerald-300"
                }">
                  ${ctx.moral_verdict.badge_en}
                </span>
              </div>
              <p class="text-xs sm:text-sm font-semibold font-telugu ${
                ctx.moral_verdict.is_sin ? "text-rose-700 dark:text-rose-400" : "text-emerald-700 dark:text-emerald-400"
              }">
                ${ctx.moral_verdict.badge_te}
              </p>
              <p class="text-xs sm:text-sm text-stone-800 dark:text-stone-200 leading-relaxed pt-1">
                ${ctx.moral_verdict.summary_en}
              </p>
              <p class="text-xs sm:text-sm text-stone-700 dark:text-stone-300 font-telugu leading-relaxed pt-1 border-t border-rose-200/50 dark:border-rose-900/40">
                ${ctx.moral_verdict.summary_te}
              </p>
            </div>
          </div>
        </div>
      ` : ""}

      <!-- Scripture Verses Section -->
      <div class="mt-5">
        ${versesHtml}
      </div>

      <!-- INSIGHT PILLARS GRID -->
      <div class="space-y-5">
        
        <!-- Pillar 1: The Backstory -->
        <div class="rounded-2xl p-5 bg-gradient-to-br from-amber-50/80 to-amber-50/40 dark:from-stone-900 dark:to-stone-900/60 border border-amber-200 dark:border-stone-700 shadow-xs">
          <div class="flex items-center gap-2.5 mb-3">
            <div class="w-8 h-8 rounded-lg bg-amber-600 text-white flex items-center justify-center shrink-0 shadow-xs">
              <i data-lucide="history" class="w-4 h-4"></i>
            </div>
            <div>
              <h3 class="font-serif font-bold text-sm sm:text-base text-stone-900 dark:text-stone-100">1. The Prior Backstory • పూర్వ నేపథ్యము</h3>
              <p class="text-[11px] text-amber-800 dark:text-amber-400">What happened leading up to this moment & the historical setting</p>
            </div>
          </div>
          <div class="space-y-2.5 text-xs sm:text-sm">
            <p class="text-stone-800 dark:text-stone-200 leading-relaxed font-body">
              ${ctx.backstory ? ctx.backstory.summary_en : "Historical setting established in preceding biblical narratives."}
            </p>
            <p class="text-stone-700 dark:text-stone-300 font-telugu leading-relaxed pt-2 border-t border-amber-200/60 dark:border-stone-800">
              ${ctx.backstory ? ctx.backstory.summary_te : "పూర్వపు గ్రంథములలో ఈ సంఘటనకు పూర్వపు పరిస్థితులు నమోదు చేయబడినవి."}
            </p>
          </div>
        </div>

        <!-- Pillar 2: Why It Happened -->
        <div class="rounded-2xl p-5 bg-gradient-to-br from-orange-50/80 to-orange-50/40 dark:from-stone-900 dark:to-stone-900/60 border border-orange-200 dark:border-stone-700 shadow-xs">
          <div class="flex items-center gap-2.5 mb-3">
            <div class="w-8 h-8 rounded-lg bg-orange-600 text-white flex items-center justify-center shrink-0 shadow-xs">
              <i data-lucide="help-circle" class="w-4 h-4"></i>
            </div>
            <div>
              <h3 class="font-serif font-bold text-sm sm:text-base text-stone-900 dark:text-stone-100">2. Why Did It Happen? • ఎందుకు జరిగింది?</h3>
              <p class="text-[11px] text-orange-800 dark:text-orange-400">The immediate human motives, weaknesses, trials, or divine circumstances</p>
            </div>
          </div>
          <div class="space-y-2.5 text-xs sm:text-sm">
            <p class="text-stone-800 dark:text-stone-200 leading-relaxed font-body">
              ${ctx.why_it_happened ? ctx.why_it_happened.summary_en : "Human decisions and divine providence converged in this pivotal chapter."}
            </p>
            <p class="text-stone-700 dark:text-stone-300 font-telugu leading-relaxed pt-2 border-t border-orange-200/60 dark:border-stone-800">
              ${ctx.why_it_happened ? ctx.why_it_happened.summary_te : "మానవుల నిర్ణయాలు మరియు దైవ సంకల్పము యొక్క కలయిక వలన ఈ ఘట్టము జరిగినది."}
            </p>
          </div>
        </div>

        <!-- Pillar 3: Consequences of Sin / Results -->
        ${ctx.consequences_of_sin ? `
          <div class="rounded-2xl p-5 bg-gradient-to-br from-red-50/80 to-rose-50/40 dark:from-stone-900 dark:to-stone-900/60 border border-red-200 dark:border-stone-700 shadow-xs">
            <div class="flex items-center gap-2.5 mb-3">
              <div class="w-8 h-8 rounded-lg bg-red-600 text-white flex items-center justify-center shrink-0 shadow-xs">
                <i data-lucide="scale" class="w-4 h-4"></i>
              </div>
              <div>
                <h3 class="font-serif font-bold text-sm sm:text-base text-stone-900 dark:text-stone-100">3. Biblical Consequences & Judgment • పర్యవసానములు & దైవిక తీర్పు</h3>
                <p class="text-[11px] text-red-800 dark:text-red-400">The historical aftermath, curses, and consequences that followed</p>
              </div>
            </div>
            <div class="space-y-2.5 text-xs sm:text-sm">
              <p class="text-stone-800 dark:text-stone-200 leading-relaxed font-body">
                ${ctx.consequences_of_sin.summary_en}
              </p>
              <p class="text-stone-700 dark:text-stone-300 font-telugu leading-relaxed pt-2 border-t border-red-200/60 dark:border-stone-800">
                ${ctx.consequences_of_sin.summary_te}
              </p>
            </div>
          </div>
        ` : ""}

        <!-- Pillar 4: God's Future Thoughts & Redemptive Plan -->
        <div class="rounded-2xl p-5 bg-gradient-to-br from-emerald-50/80 to-teal-50/40 dark:from-stone-900 dark:to-stone-900/60 border border-emerald-200 dark:border-stone-700 shadow-xs">
          <div class="flex items-center gap-2.5 mb-3">
            <div class="w-8 h-8 rounded-lg bg-emerald-600 text-white flex items-center justify-center shrink-0 shadow-xs">
              <i data-lucide="sparkles" class="w-4 h-4"></i>
            </div>
            <div>
              <h3 class="font-serif font-bold text-sm sm:text-base text-stone-900 dark:text-stone-100">4. God's Future Thoughts & Purpose • దేవుని భవిష్యత్ సంకల్పం</h3>
              <p class="text-[11px] text-emerald-800 dark:text-emerald-400">How God transformed this situation for greater redemptive glory and prophecy</p>
            </div>
          </div>
          <div class="space-y-2.5 text-xs sm:text-sm">
            <p class="text-stone-800 dark:text-stone-200 leading-relaxed font-body">
              ${ctx.gods_future_plan ? ctx.gods_future_plan.summary_en : "God's eternal perspective works all things together for redemptive triumph."}
            </p>
            <p class="text-stone-700 dark:text-stone-300 font-telugu leading-relaxed pt-2 border-t border-emerald-200/60 dark:border-stone-800">
              ${ctx.gods_future_plan ? ctx.gods_future_plan.summary_te : "దేవుడు సమస్తమును తన నిత్య రక్షణ ప్రణాళిక కొరకు మరియు మేలు కొరకు సమకూడి జరిగించెను."}
            </p>
          </div>
        </div>

        <!-- APOLOGETIC DEFENSE FOR SKEPTICS & CRITICS -->
        ${ctx.apologetics_for_critics ? `
          <div class="rounded-2xl p-5 bg-gradient-to-br from-amber-100/70 via-stone-50 to-amber-50/80 dark:from-stone-900 dark:via-stone-900/90 dark:to-amber-950/30 border-2 border-amber-300 dark:border-amber-700/60 shadow-sm">
            <div class="flex items-center gap-2.5 mb-3">
              <div class="w-8 h-8 rounded-lg bg-amber-700 text-white flex items-center justify-center shrink-0 shadow-xs">
                <i data-lucide="shield-alert" class="w-4 h-4"></i>
              </div>
              <div>
                <h3 class="font-serif font-bold text-sm sm:text-base text-amber-950 dark:text-amber-200">
                  Answering Critics & Skeptics • విమర్శకులకు లేఖన సమాధానం
                </h3>
                <p class="text-[11px] text-amber-800 dark:text-amber-400">Direct biblical response when people ask: "Why is this in the Bible?"</p>
              </div>
            </div>
            <div class="space-y-2 text-xs sm:text-sm">
              <div class="p-2.5 rounded-xl bg-white/80 dark:bg-stone-800/80 border border-amber-200/80 dark:border-stone-700">
                <span class="text-[10px] font-bold uppercase tracking-wider text-amber-800 dark:text-amber-300 block mb-0.5">Common Question / Objection:</span>
                <p class="font-medium italic text-stone-900 dark:text-stone-100">${ctx.apologetics_for_critics.question_en}</p>
                <p class="font-telugu text-stone-700 dark:text-stone-300 text-xs mt-1">${ctx.apologetics_for_critics.question_te}</p>
              </div>
              <div class="pt-2">
                <span class="text-[10px] font-bold uppercase tracking-wider text-amber-900 dark:text-amber-300 block mb-1">Biblical Truth & Vindication:</span>
                <p class="text-stone-800 dark:text-stone-200 leading-relaxed">${ctx.apologetics_for_critics.defense_en}</p>
                <p class="text-stone-700 dark:text-stone-300 font-telugu leading-relaxed pt-2 border-t border-amber-200 dark:border-stone-700 mt-2">${ctx.apologetics_for_critics.defense_te}</p>
              </div>
            </div>
          </div>
        ` : ""}

      </div>

      <!-- Action Footer -->
      <div class="mt-6 pt-4 border-t border-stone-200 dark:border-stone-700 flex flex-col sm:flex-row items-center justify-between gap-3">
        <span class="text-xs text-stone-500 dark:text-stone-400">
          Want to explore the whole chapter in parallel?
        </span>
        <button onclick="jumpToChapter('${data.book.name_en}', ${data.chapter})" class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-amber-600 hover:bg-amber-700 text-white text-xs font-semibold shadow-sm flex items-center justify-center gap-2 transition active:scale-95">
          <i data-lucide="book-open" class="w-4 h-4"></i>
          <span>Read All ${data.book.name_en} ${data.chapter} in Bible Reader</span>
        </button>
      </div>

    </div>
  `;

  initLucide();
  container.scrollIntoView({ behavior: "smooth", block: "start" });
}

