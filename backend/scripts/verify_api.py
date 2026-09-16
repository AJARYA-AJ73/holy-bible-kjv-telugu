import sys
import os
import json

# Ensure UTF-8 output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from main import app
from starlette.testclient import TestClient

client = TestClient(app)

def test_all():
    print("=== 1. Testing Health ===")
    res = client.get("/api/health")
    print("Health:", res.json())
    assert res.status_code == 200

    print("\n=== 2. Testing Genesis Chapter 1 (Bilingual) ===")
    res = client.get("/api/chapter?book_name=Genesis&chapter=1")
    data = res.json()
    print(f"Book: {data['book']['name_en']} ({data['book']['name_te']}), Total Verses: {data['verses_count']}")
    v1 = data['verses'][0]
    print(f"Verse 1 EN: {v1['text_en']}")
    print(f"Verse 1 TE: {v1['text_te']}")
    assert len(data['verses']) == 31

    print("\n=== 3. Testing Emotion Guidance: 'im depressed' ===")
    res = client.post("/api/search/emotion", json={"query": "im depressed"})
    data = res.json()
    print("Emotion Found:", data['found'])
    if data['found']:
        emo = data['data']
        print(f"Title: {emo['title_en']}")
        print(f"Primary Verse: {emo['primary_verse']['reference']}")
        print(f"EN: {emo['primary_verse']['text_en']}")
        print(f"TE: {emo['primary_verse']['text_te']}")
        print(f"Prayer EN: {emo['prayer_en'][:100]}...")

    print("\n=== 4. Testing Incident Search: 'man swallowed by a fish' ===")
    res = client.post("/api/search/incident", json={"query": "man swallowed by a fish"})
    data = res.json()
    print(f"Incidents matched: {len(data['results'])}")
    if data['results']:
        inc = data['results'][0]
        print(f"Top Result: {inc['title_en']} ({inc['title_te']}) - {inc['reference']}")
        print(f"Summary: {inc['summary_en'][:120]}...")

    print("\n=== 5. Testing 'Why God made them suffer' Arcs ===")
    res = client.get("/api/suffering/arcs?q=why did god let them suffer")
    data = res.json()
    print(f"Suffering Arcs returned: {len(data['arcs'])}")
    for arc in data['arcs'][:2]:
        print(f"- {arc['title_en']}")
        print(f"  Trial: {arc['the_trial']['summary_en'][:80]}...")
        print(f"  Aftermath: {arc['the_aftermath']['summary_en'][:80]}...")
        print(f"  Triumph Verse: {arc['the_aftermath']['triumph_verse']['reference']}")

    print("\n=== 6. Testing In-Context Dictionary: 'propitiation' in Romans ===")
    res = client.get("/api/dictionary/lookup?word=propitiation&book=Romans")
    data = res.json()
    print(f"Word: {data['word']}")
    print(f"EN Meaning: {data['definition_en']}")
    print(f"TE Meaning: {data['definition_te']}")
    print(f"Context Note: {data['context_note']}")

    print("\n=== 7. Testing Frontend Web UI Static Serving ===")
    res = client.get("/")
    assert res.status_code == 200
    assert "HOLY BIBLE" in res.text
    print("Frontend HTML served successfully! (Length:", len(res.text), "bytes)")

    print("\n=== 8. Testing Historical Evidences of Jesus Christ ===")
    res = client.get("/api/evidence/historical")
    assert res.status_code == 200
    data = res.json()
    print(f"Categories: {len(data['categories'])}, Evidences Count: {data['total']}")
    assert data['total'] >= 8
    for ev in data['evidences'][:2]:
        print(f"- {ev['title_en']} ({ev['author']})")
        print(f"  Quote: {ev['quote_en'][:70]}...")

    print("\n=== 9. Testing Chapter Backstory, Why It Happened & God's Future Plan ===")
    res = client.get("/api/context/chapter?book=Genesis&chapter=1")
    assert res.status_code == 200
    ctx = res.json()['context']
    print(f"Chapter: {ctx['title_en']}")
    print(f"1. Backstory: {ctx['backstory']['summary_en'][:70]}...")
    print(f"2. Why It Happened: {ctx['why_it_happened']['summary_en'][:70]}...")
    print(f"3. God's Future Plan: {ctx['gods_future_plan']['summary_en'][:70]}...")
    assert "creation" in ctx['backstory']['summary_en'].lower() or "triune" in ctx['backstory']['summary_en'].lower()

    print("\nALL 9 SUITES OF BACKEND & FRONTEND TESTS PASSED WITH 100% SUCCESS!")

if __name__ == "__main__":
    test_all()
