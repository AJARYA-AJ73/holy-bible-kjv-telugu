# -*- coding: utf-8 -*-
"""
Safely enriches emotions.json, incidents.json, and chapter_contexts.json
with high-accuracy Telugu script and deep apologetic content without ANY encoding corruption.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def enrich_chapter_contexts():
    filepath = os.path.join(DATA_DIR, "chapter_contexts.json")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Filter out any corrupted entries if present
    contexts = [c for c in data.get("contexts", []) if not (
        (c.get("book") == "Genesis" and c.get("chapter") == 19) or
        (c.get("book") == "1 Samuel" and c.get("chapter") == 28) or
        (c.get("book") == "2 Samuel" and c.get("chapter") == 11)
    )]

    new_contexts = [
        {
            "book": "Genesis",
            "chapter": 19,
            "title_en": "The Destruction of Sodom and the Moral Tragedy of Lot's Daughters",
            "title_te": "సొదొమ నాశనము మరియు లోతు కుమార్తెల పాపపు ఉదంతము",
            "moral_verdict": {
                "is_sin": True,
                "badge_en": "⚠️ SEVERE HUMAN SIN (EXPLICITLY FORBIDDEN & CONDEMNED BY GOD)",
                "badge_te": "⚠️ ఘోరమైన మానవ పాపము (లేఖనాల్లో దేవునిచే ఖండించబడిన అగమ్యాగమన పాపము)",
                "summary_en": "The Bible records this as an abhorrent human sin, NOT something God approved, commanded, or smiled upon. Leviticus 18:6-18 and Leviticus 20:11-21 categorically forbid incest as a detestable abomination worthy of capital punishment. The Bible is an honest historical mirror that truthfully exposes human moral depravity rather than hiding it.",
                "summary_te": "ఈ సంఘటనను లేఖనములు తీవ్రమైన మానవ పాపముగా నమోదు చేసినవి; దేవుడు దీనిని ఎన్నడూ ఆమోదించలేదు లేదా ఆజ్ఞాపించలేదు! లేవీయకాండము 18:6-18 మరియు 20:11-21 లలో ఇలాంటి కార్యములు దేవునికి హేయమైనవని, మరణశిక్షకు పాత్రమైన ఘోర పాపమని స్పష్టముగా నిషేధించబడెను. బైబిలు మానవుల పాపపు స్థితిని ఉన్నది ఉన్నట్లుగా బయటపెట్టే సత్యవాక్కు తప్ప కల్పిత కథ కాదు."
            },
            "backstory": {
                "summary_en": "Lot chose to pitch his tents toward decadent Sodom for material prosperity, eventually settling inside the city despite its pervasive sexual perversion. When God sent holy angels to destroy Sodom and Gomorrah with heavenly fire and brimstone, Lot hesitated until angels dragged him, his wife, and two daughters out. His wife looked back in longing and turned into a pillar of salt. Lot and his daughters fled into an isolated, desolate cave in the mountains of Zoar, stripped of all wealth, society, and home.",
                "summary_te": "లోతు మొదట సొదొమ వైపు తన గుడారములు వేసికొని, తరువాత ఆ పట్టణపు భోగలాలసత్వములో మునిగిపోయెను. దేవుడు గంధకముతో అగ్నితో సొదొమ గొమొఱ్ఱాలను నాశనము చేసినప్పుడు, దేవదూతలు లోతును అతని భార్యను ఇద్దరు కుమార్తెలను బలవంతముగా బయటకు తెచ్చిరి. లోతు భార్య వెనుకకు తిరిగి చూసి ఉప్పుస్తంభమాయెను. సర్వస్వమును కోల్పోయిన లోతు మరియు అతని కుమార్తెలు జోయరు పర్వతములోని ఒక నిర్జనమైన గుహలో ఆశ్రయము పొందిరి."
            },
            "why_it_happened": {
                "summary_en": "Why did Lot's daughters commit this sin? Having spent years inside decadent Sodom, the daughters had absorbed its worldly panic, moral compromise, and ungodly philosophy. Believing that all humanity had perished in the cosmic fire and that their family line was completely extinct, they took matters into their own hands rather than trusting God. Knowing their father would never consciously agree to such an abomination, they conspired to get him intoxicated with wine on two consecutive nights to secretly lay with him (Genesis 19:32-35).",
                "summary_te": "ఈ పాపం ఎందుకు జరిగింది? సొదొమలో నివసించిన సంవత్సరాల వలన ఆ కుమార్తెలు సొదొమ లోకరీతిని, భయాన్ని, నైతిక రాజీని అలవర్చుకున్నారు. లోకమంతా నాశనమైపోయిందని, తమ వంశం అంతరించిపోతుందని భావించి, దేవునిపై ఆధారపడకుండా తమ స్వబుద్ధిపై ఆధారపడ్డారు. తమ తండ్రి స్పృహలో ఉంటే ఈ పాపానికి ఒప్పుకోడని ఎరిగి, ఆయనకు ద్రాక్షారసము త్రాగించి మత్తులో ముంచి రెండు రాత్రులు ఈ దుష్కార్యము చేసిరి (ఆదికాండము 19:32-35)."
            },
            "consequences_of_sin": {
                "summary_en": "Sin in Scripture always bears bitter, poisoned fruit. Both daughters conceived: the firstborn bore Moab (father of the Moabites) and the younger bore Ben-Ammi (father of the Ammonites). Throughout the entire Old Testament, the Moabites and Ammonites were perennial, bitter pagan enemies of God's covenant people. They waged cruel wars against Israel, hired Balaam to curse them, and seduced Israel into the sexually perverse worship of Baal-Peor, bringing devastating plagues (Numbers 25). Furthermore, God commanded that no Moabite or Ammonite could enter the assembly of the LORD to the tenth generation (Deut 23:3). Lot's legacy ended in shame and darkness in an isolated cave.",
                "summary_te": "పాపము ఎల్లప్పుడూ చేదైన ఫలితములనే తెస్తుంది. ఇద్దరు కుమార్తెలు గర్భవతులైరి: పెద్ద కుమార్తె ద్వారా 'మోయాబు' (మోయాబీయుల తండ్రి), చిన్న కుమార్తె ద్వారా 'బెనమ్మీ' (అమ్మోనీయుల తండ్రి) జన్మించిరి. పాత నిబంధన అంతటా మోయాబీయులు మరియు అమ్మోనీయులు దేవుని ప్రజలైన ఇశ్రాయేలీయులకు నిరంతర శత్రువులుగా ఉండి యుద్ధములు చేసిరి, బయల్పెయోరు ద్వారా ఇశ్రాయేలీయులను వ్యభిచార పాపములోనికి దింపిరి. మోయాబీయులు, అమ్మోనీయులు పది తరముల వరకు యెహోవా సమాజములో చేరకూడదని దేవుడు ఆజ్ఞాపించెను (ద్వితీయోపదేశకాండము 23:3). లోతు జీవితం ఒక గుహలో అవమానంతో ముగిసింది."
            },
            "gods_future_plan": {
                "summary_en": "Genesis 19 demonstrates that human scheming outside God's will creates generational tragedy. Yet, in God's astounding grace and sovereign providence centuries later, a repentant Moabite woman named Ruth turned away from pagan idols to embrace the God of Israel ('Thy people shall be my people, and thy God my God'). God redeemed this broken lineage by placing Ruth in the royal ancestral line of King David and Jesus Christ the Savior! Where sin abounded, grace did much more abound (Romans 5:20).",
                "summary_te": "మానవ ఆలోచనలు ఎంతటి ఘోరమైన పర్యవసానాలను తెస్తాయో ఈ అధ్యాయము హెచ్చరిస్తుంది. అయినప్పటికీ దేవుని అద్భుతమైన కృప చొప్పున, శతాబ్దాల తరువాత అదే మోయాబు జాతికి చెందిన 'రూతు' అను స్త్రీ విగ్రహాలను విడిచి ఇశ్రాయేలు దేవుని ఆశ్రయించినప్పుడు, ఆమెను దావీదు రాజు మరియు రక్షకుడైన యేసుక్రీస్తు వంశావళిలో దేవుడు చేర్చెను! పాపము విస్తరించిన చోట కృప మరింతగా విస్తరించెను (రోమీయులకు 5:20)!"
            },
            "apologetics_for_critics": {
                "question_en": "Why is this horrific story in the Holy Bible? Does the Bible promote or condone incest?",
                "question_te": "బైబిలు గ్రంథములో ఈ ఘోరమైన సంఘటన ఎందుకు రాయబడింది? బైబిల్ దీనిని సమర్థిస్తుందా?",
                "defense_en": "ABSOLUTELY NOT. The Bible distinguishes between 'prescriptive' (what God commands) and 'descriptive' (what fallen humans actually did). The Bible is an honest historical document that tells the truth about human sin rather than painting fairytales. Notice: (1) God never commanded or commended this; (2) God's Law in Leviticus 18 and 20 explicitly condemns incest as an abomination punishable by death; (3) The immediate biblical consequence was the birth of Israel's bitter pagan enemies (Moabites & Ammonites); (4) The narrative warns every reader that worldly compromise in Sodom destroys families. Critics who cite Genesis 19 mistakenly confuse the Bible's historical reporting of a sin with an endorsement of it.",
                "defense_te": "ఖచ్చితముగా లేదు! బైబిలు 'దేవుని ఆజ్ఞలు' (ఆచరించవలసినవి) మరియు 'మానవ చరిత్ర' (మానవులు చేసిన తప్పులు) మధ్య స్పష్టమైన తేడాను చూపిస్తుంది. బైబిల్ కల్పిత కథలను రాయదు, పాపపు భయంకరత్వాన్ని ఉన్నదున్నట్లు చూపిస్తుంది. గమనించండి: 1. దేవుడు ఎన్నడూ ఈ పనిని ఆజ్ఞాపించలేదు లేదా మెచ్చుకోలేదు. 2. లేవీయకాండము 18, 20 అధ్యాయాలలో దీనిని మరణశిక్షకు పాత్రమైన పాపముగా దేవుడు ఖండించాడు. 3. దీని వలన ఇశ్రాయేలుకు శత్రు జాతులు పుట్టి తీవ్ర నష్టము జరిగింది. కాబట్టి బైబిలు చరిత్రను రికార్డు చేయడాన్ని బట్టి బైబిలు తప్పు అనడం అవివేకం; పాపం వల్ల వచ్చే నాశనాన్ని హెచ్చరించడానికే ఇది రాయబడింది."
            }
        },
        {
            "book": "1 Samuel",
            "chapter": 28,
            "title_en": "King Saul and the Witch of Endor: The Sin of Witchcraft & Necromancy",
            "title_te": "సౌలు రాజు మరియు ఏన్దోరు కర్ణపిశాచి: చేతబడి మరియు మాంత్రికత అను పాపము",
            "moral_verdict": {
                "is_sin": True,
                "badge_en": "⚠️ SEVERE SIN: FORBIDDEN WITCHCRAFT & REBELLION AGAINST GOD",
                "badge_te": "⚠️ ఘోర పాపము: దేవునిచే ఖండించబడిన మాంత్రికత, చేతబడి మరియు తిరుగుబాటు",
                "summary_en": "Witchcraft, consulting mediums, necromancy (speaking to the dead), and the occult are explicitly condemned in the Bible as spiritual treason against God (Deuteronomy 18:9-12, Leviticus 19:31). Saul's desperate act was his crowning sin of rebellion.",
                "summary_te": "మాంత్రికత, చేతబడి, కర్ణపిశాచములను అడుగుట, చనిపోయినవారితో మాట్లాడుట (భూతవైద్యము) దేవునికి తీవ్రమైన అసహ్యము మరియు ఆత్మీయ ద్రోహమని లేఖనములు ఖండిస్తున్నాయి (ద్వితీయోపదేశకాండము 18:9-12, లేవీయకాండము 19:31). దేవునికి వ్యతిరేకముగా సౌలు చేసిన తిరుగుబాటుకు ఇది పరాకాష్ట."
            },
            "backstory": {
                "summary_en": "King Saul had progressively hardened his heart against God, disobeying divine instructions at Gilgal and sparing King Agag of Amalek. The prophet Samuel had died, and the Holy Spirit had departed from Saul. When the massive Philistine army assembled at Shunem, Saul was consumed by mortal terror. He inquired of the LORD, but the LORD refused to answer him by dreams, by Urim, or by prophets.",
                "summary_te": "సౌలు రాజు దేవుని మాటను ధిక్కరించి గిల్గాలులోను, అమాలేకీయుల విషయంలోను దేవునికి అవిధేయత చూపెను. సమూయేలు ప్రవక్త మరణించెను, యెహోవా ఆత్మ సౌలును విడిచిపోయెను. ఫిలిష్తీయుల మహా సైన్యము దాడికి వచ్చినప్పుడు సౌలు భయముతో వణకెను. అతడు దేవుని యొద్ద విచారణ చేసెను గాని స్వప్నముల ద్వారానైనను, ఊరీము ద్వారానైనను, ప్రవక్తల ద్వారానైనను యెహోవా అతనికి ప్రత్యుత్తరమియ్యలేదు."
            },
            "why_it_happened": {
                "summary_en": "Instead of falling on his knees in true, broken repentance for his lifetime of rebellion, Saul turned to demonic channels. He commanded his servants to find a woman with a familiar spirit (a medium), despite having previously expelled them in accordance with God's law. In deep disguise under cover of darkness, Saul sought counsel from the occult at Endor to summon Samuel.",
                "summary_te": "సౌలు తన తప్పులను ఒప్పుకొని దేవుని పాదాల యొద్ద నిజమైన పశ్చాత్తాపముతో కన్నీరు కార్చడానికి బదులుగా, చీకటి శక్తుల వైపు తిరిగెను. దేవుని ధర్మశాస్త్రము ప్రకారం దేశము నుండి కర్ణపిశాచములను తానే వెళ్లగొట్టినప్పటికీ, వేషము మార్చుకొని రాత్రివేళ ఏన్దోరులోని ఒక కర్ణపిశాచముగల స్త్రీ యొద్దకు వెళ్లి సమూయేలును రప్పించుటకు ప్రయత్నించెను."
            },
            "consequences_of_sin": {
                "summary_en": "The consequences were catastrophic and immediate. 1 Chronicles 10:13-14 delivers the final divine epitaph: 'So Saul died for his unfaithfulness which he committed against the LORD, even against the word of the LORD, which he kept not, and also for asking counsel of one that had a familiar spirit, to enquire of it; And enquired not of the LORD: therefore he slew him, and turned the kingdom unto David.' The very next day on Mount Gilboa, Israel was routed, Saul's sons Jonathan, Abinadab, and Malchishua were killed, and the wounded Saul fell upon his own sword in suicide.",
                "summary_te": "ఈ పాపమునకు పర్యవసానము వెంటనే వచ్చింది. 1 దినవృత్తాంతములు 10:13-14 స్పష్టముగా చెబుతోంది: 'సౌలు యెహోవా ఆజ్ఞను గైకొనక ఆయన దృష్టికి ద్రోహము చేసెను; మరియు అతడు యెహోవాయొద్ద విచారణ చేయక కర్ణపిశాచముగల దానియొద్ద విచారణ చేసినందున ఆయన అతని చంపి దావీదునకు రాజ్యము అప్పగించెను.' మరుసటి రోజే గిల్బోవ పర్వతముపై జరిగిన యుద్ధములో సౌలు కుమారులైన యోనాతాను, అబీనాదాబు, మల్కీషూవ చనిపోయిరి, గాయపడిన సౌలు తన ఖడ్గముపై పడి ఆత్మహత్య చేసుకునెను."
            },
            "gods_future_plan": {
                "summary_en": "God brought an end to the self-willed, carnal dynasty of Saul to establish David, a man after God's own heart, through whose seed the eternal King Jesus Christ would be born. Furthermore, the incident serves as an eternal warning: seeking answers from horoscopes, astrology, mediums, or witchcraft always leads to spiritual destruction.",
                "summary_te": "స్వార్థముతో నిండిన సౌలు వంశమును అంతమొందించి, దేవుని హృదయానుసారుడైన దావీదును దేవుడు సింహాసనమెక్కించెను; ఆయన సంతతిలోనే రక్షకుడైన యేసుక్రీస్తు జన్మించెను. జ్యోతిష్యం, చేతబడి, మాంత్రికత మరియు జాతకాల వైపు చూడటం ఆత్మీయ నాశనానికి దారితీస్తుందని ఈ చరిత్ర హెచ్చరిస్తున్నది."
            },
            "apologetics_for_critics": {
                "question_en": "Does the Witch of Endor prove that the Bible endorses witchcraft or consulting the dead?",
                "question_te": "ఏన్దోరు సంఘటనను బట్టి బైబిల్ చేతబడిని లేదా చనిపోయినవారితో మాట్లాడటాన్ని సమర్థిస్తుందా?",
                "defense_en": "No! Scripture expressly points to Saul's consultation of the medium as the primary transgression that brought God's execution upon him (1 Chron 10:13). The Bible shows the tragedy of a man who refused to listen to God in life, and in his death was completely shattered by turning to the occult.",
                "defense_te": "ఎంతమాత్రము లేదు! సౌలు మరణానికి మరియు అతని పతనానికి ముఖ్య కారణం అతడు కర్ణపిశాచముగల స్త్రీ వద్దకు వెళ్లడమేనని బైబిల్ స్పష్టముగా చెబుతోంది (1 దినవృత్తాంతములు 10:13). బ్రతికియున్నప్పుడు దేవుని మాటకు లోబడని వ్యక్తి అంతిమముగా చీకటి శక్తుల చేతిలో ఎలా సర్వనాశనమయ్యాడో చూపడానికే ఈ సంఘటన రాయబడింది."
            }
        },
        {
            "book": "2 Samuel",
            "chapter": 11,
            "title_en": "David's Sin with Bathsheba and the Treacherous Murder of Uriah",
            "title_te": "దావీదు బత్షెబతో చేసిన వ్యభిచార పాపము మరియు ఊరియా హత్య",
            "moral_verdict": {
                "is_sin": True,
                "badge_en": "⚠️ GRAVE MORAL SIN: ADULTERY, DECEIT & MURDER (CONDEMNED BY GOD)",
                "badge_te": "⚠️ దేవుని దృష్టికి తీవ్రమైన పాపము: వ్యభిచారము, కపటము మరియు నరహత్య",
                "summary_en": "The Bible pulls no punches: 'The thing that David had done displeased the LORD' (2 Samuel 11:27). King David committed catastrophic sins of adultery, deception, and arranged murder. God did not overlook it because of David's status; rather, God dispatched Nathan the prophet to expose and severely judge his household.",
                "summary_te": "బైబిల్ స్పష్టముగా సెలవిచ్చుచున్నది: 'దావీదు చేసినది యెహోవా దృష్టికి బహు చెడ్డదిగా ఉండెను' (2 సమూయేలు 11:27). దావీదు రాజు వ్యభిచారము, కపటము మరియు హత్య అను ఘోర పాపములను చేసెను. దావీదు రాజు అయినందున దేవుడు దానిని ఉపేక్షించలేదు; నాతాను ప్రవక్తను పంపి అతని పాపమును బట్టబయలు చేసి శిక్షను ప్రకటించెను."
            },
            "backstory": {
                "summary_en": "In the springtime, when kings normally led their armies out to battle, David remained behind in Jerusalem in idle luxury. Walking upon the palace roof at twilight, he saw Bathsheba bathing and allowed lust to overpower his conscience.",
                "summary_te": "రాజులు యుద్ధములకు బయలుదేరు వసంతకాలములో దావీదు యుద్ధమునకు వెళ్లకుండా యెరూషలేములోనే ఉండిపోయెను. ఒక సాయంకాలమున రాజభవనపు మిద్దెపై తిరుగుచు స్నానము చేయుచున్న బత్షెబను చూసి, దురాశతో తన హృదయములో పాపమునకు చోటిచ్చెను."
            },
            "why_it_happened": {
                "summary_en": "Spiritual complacency and unchecked lust led to catastrophic moral collapse. When Bathsheba sent word that she was pregnant, David attempted an elaborate cover-up. When the faithful soldier Uriah refused to sleep at home while his comrades slept in the battlefield, David's panic led him to arrange Uriah's assassination on the frontline.",
                "summary_te": "ఆత్మీయ అజాగ్రత్త, వ్యర్థమైన విలాసము మరియు అనియంత్రిత కామము ఈ ఘోర పతనానికి దారితీసింది. బత్షెబ గర్భవతియైనప్పుడు ఆ పాపాన్ని కప్పిపుచ్చుటకు దావీదు ప్రయత్నించెను. నమ్మకస్తుడైన ఊరియా యుద్ధభూమిని తలంచుకుని ఇంటికి వెళ్లి నిద్రించకపోవడంతో, దావీదు యుద్ధము ముందరి వరుసలో ఊరియాను ఉంచి చంపించెను."
            },
            "consequences_of_sin": {
                "summary_en": "God's judgment was unrelenting: 'Now therefore the sword shall never depart from thine house; because thou hast despised me' (2 Samuel 12:10). The child died; Amnon violated Tamar; Absalom murdered Amnon; Absalom staged a bloody coup against his own father David; and civil war ravaged Israel. David wept bitter tears of grief for the rest of his reign.",
                "summary_te": "దేవుని తీర్పు తప్పలేదు: 'నీవు నన్ను తృణీకరించితివి గనుక నీ యింటినుండి ఖడ్గము ఎన్నటికిని తొలగిపోదు' (2 సమూయేలు 12:10). ఆ బిడ్డ మరణించెను; అమ్నోను తామారును చెరిచెను; అబ్షాలోము అమ్నోనును చంపెను; అబ్షాలోము తన తండ్రిపైనే తిరుగుబాటు చేసెను; ఇశ్రాయేలులో అంతర్యుద్ధం చెలరేగెను. దావీదు జీవితాంతం కన్నీటితో వేదనను అనుభవించెను."
            },
            "gods_future_plan": {
                "summary_en": "David penned Psalm 51 in shattered, broken repentance ('Create in me a clean heart, O God'). God forgave David's eternal soul, though the temporal scars of sin remained. From Bathsheba, Solomon was later born, demonstrating that God can take the deepest human ruins and, through repentance, birth a future king of peace.",
                "summary_te": "దావీదు పగిలిన హృదయముతో పశ్చాత్తాపపడి కీర్తన 51 రాసెను ('దేవా, నాయందు శుద్ధహృదయము కలుగజేయుము'). దేవుడు దావీదు ఆత్మను క్షమించినను, పాపపు భౌతిక చేదు అనుభవాలు మిగిలిపోయెను. తరువాత బత్షెబ ద్వారా సొలొమోను జన్మించెను. నిజమైన పశ్చాత్తాపము ద్వారా దేవుడు విరిగిన జీవితాలను బాగుచేయగలడని ఇది చూపిస్తుంది."
            },
            "apologetics_for_critics": {
                "question_en": "If David was a 'man after God's own heart', why did he commit adultery and murder? Does the Bible excuse leaders?",
                "question_te": "దావీదు 'దేవుని హృదయానుసారుడు' అయినప్పుడు అతడు ఇంత ఘోర పాపాలు ఎందుకు చేశాడు? బైబిల్ నాయకులను వెనకేసుకొస్తుందా?",
                "defense_en": "The Bible never whitewashes heroes. Unlike ancient pagan kings whose chronicles erased their flaws, the Bible fearlessly exposes David's crimes and records God's harsh, uncompromising judgment against him. David was 'after God's heart' not because he was sinless, but because when confronted with his sin, he did not make excuses—he tore his clothes and wept in genuine, broken repentance before God.",
                "defense_te": "బైబిల్ ఎన్నడూ మనుషుల తప్పులను దాచిపెట్టదు. అన్యరాజుల చరిత్రలలో వారి తప్పులను తుడిచివేసేవారు, కానీ బైబిల్ దావీదు చేసిన ఘోర పాపములను దాచకుండా చూపి, దేవుడు ఇచ్చిన కఠినమైన శిక్షను కూడా నమోదు చేసింది. దావీదు నిర్దోషి అయినందున దేవుని హృదయానుసారుడు కాలేదు; ప్రవక్త తన పాపాన్ని చూపిన వెంటనే సాకులు చెప్పకుండా విరిగి నలిగిన మనస్సుతో దేవుని ఎదుట పశ్చాత్తాపపడినందుకే అతనికి క్షమాపణ దొరికింది."
            }
        }
    ]

    contexts.extend(new_contexts)
    data["contexts"] = contexts

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Enriched chapter_contexts.json with {len(new_contexts)} new contexts. Total: {len(contexts)}")


def enrich_emotions():
    filepath = os.path.join(DATA_DIR, "emotions.json")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    emotions = [e for e in data.get("emotions", []) if e.get("id") not in [
        "anger_and_wrath", "anger_at_friend_conflict", "temptation_and_sin", "doubt_and_faith"
    ]]

    new_emotions = [
        {
            "id": "anger_and_wrath",
            "keywords": [
                "angry", "anger", "wrath", "rage", "furious", "mad", "temper",
                "irritated", "frustrated", "resentful", "bitterness", "hot-headed",
                "fight", "shouting", "blowing up", "i am angry", "im angry", "feel angry", "కోపం", "ఆగ్రహం"
            ],
            "title_en": "When You Struggle with Anger, Wrath & Frustration",
            "title_te": "మీరు కోపము, ఆవేశము మరియు అసహనముతో పోరాడుతున్నప్పుడు",
            "primary_verse": {
                "reference": "Ephesians 4:26, 31-32",
                "book": "Ephesians",
                "chapter": 4,
                "verse": 26,
                "text_en": "Be ye angry, and sin not: let not the sun go down upon your wrath... Let all bitterness, and wrath, and anger, and clamour, and evil speaking, be put away from you, with all malice: And be ye kind one to another, tenderhearted, forgiving one another, even as God for Christ's sake hath forgiven you.",
                "text_te": "కోపపడుడి గాని పాపము చేయకుడి; సూర్యుడస్తమించువరకు మీ కోపము నిలిచియుండకూడదు... సమస్తమైన చేదును, క్రోధమును, కోపమును, అల్లరియు, దూషణయు, సకలమైన దుష్టత్వమును మీలోనుండి తీసివేయుడి. ఒకరియెడల ఒకరు దయాళువులై, కరుణాహృదయులై, క్రీస్తునందు దేవుడు మిమ్మును క్షమించిన ప్రకారము మీరును ఒకరినొకరు క్షమించుడి."
            },
            "supporting_verses": [
                {
                    "reference": "James 1:19-20",
                    "text_en": "Wherefore, my beloved brethren, let every man be swift to hear, slow to speak, slow to wrath: For the wrath of man worketh not the righteousness of God.",
                    "text_te": "నా ప్రియ సహోదరులారా, మీరు ఈ సంగతి గ్రహించుడి; ప్రతి మనుష్యుడు వినుటకు వేగిరపడువాడును, మాటలాడుటకును కోపించుటకును నిదానించువాడునై యుండవలెను. ఏలయనగా నరుని కోపము దేవుని నీతిని నెరవేర్చదు."
                },
                {
                    "reference": "Proverbs 15:1",
                    "text_en": "A soft answer turneth away wrath: but grievous words stir up anger.",
                    "text_te": "మృదువైన మాట క్రోధమును చల్లార్చును. నొప్పించు మాట కోపమును రేపును."
                },
                {
                    "reference": "Proverbs 16:32",
                    "text_en": "He that is slow to anger is better than the mighty; and he that ruleth his spirit than he that taketh a city.",
                    "text_te": "దీర్ఘశాంతముగలవాడు శౌర్యముగలవానికంటె శ్రేష్ఠుడు, తన మనస్సును స్వాధీనపరచుకొనువాడు పట్టణము పట్టుకొనువానికంటె శ్రేష్ఠుడు."
                },
                {
                    "reference": "Ecclesiastes 7:9",
                    "text_en": "Be not hasty in thy spirit to be angry: for anger resteth in the bosom of fools.",
                    "text_te": "కోపపడుటకు నీ మనస్సులో త్వరపడకుము, బుద్ధిహీనుల రొమ్ముననే కోపము నివసించును."
                }
            ],
            "pastoral_reflection": "Anger itself is an emotional alarm, but letting it boil into wrath, bitterness, or vengeance is spiritual poison. The devil seeks an open door whenever anger lingers past sundown. True strength in God's kingdom is not blasting someone with fiery words, but ruling your own spirit with Christ's quiet power. Surrender the offense to God, breathe deeply in prayer, and remember that Christ absorbed the ultimate insult on the Cross so you could be forgiven.",
            "pastoral_reflection_te": "కోపం కలగడం సహజమే అయినప్పటికీ, అది ఆవేశముగాను, చేదుగాను, పగగాను మారినప్పుడు మన జీవితాన్ని నాశనం చేస్తుంది. సూర్యుడు అస్తమించకముందే కోపాన్ని విడిచిపెట్టకపోతే అపవాదికి చోటిచ్చినవారమవుతాము. కోపంతో ఎదుటివారిని దూషించడం గొప్పతనం కాదు, తన మనస్సును స్వాధీనపరచుకొనువాడే బలవంతుడైన యోధునికంటె శ్రేష్ఠుడు. మీ మనస్తాపమును ప్రభువు పాదాల వద్ద ఉంచి, క్రీస్తు మనలను క్షమించినట్లే శాంతముగా క్షమించండి.",
            "prayer_en": "Lord Jesus, my heart is burning with anger and frustration. You know how wounded and irritated I feel. But I refuse to give the devil a foothold in my soul. Quench the flames of wrath within me with the water of Your Holy Spirit. Give me a soft answer instead of cruel words, and grant me the supernatural patience to forgive. Fill me with Your peace that surpasses all understanding. In Jesus' name, Amen.",
            "prayer_te": "ప్రభువైన యేసూ, నా హృదయము కోపముతో, అసహనముతో మండుచున్నది. నేను ఎంతగా గాయపడ్డానో మీరు ఎరుగుదురు. అయితే నా ఆత్మలో అపవాదికి ఏమాత్రం చోటివ్వనని తీర్మానించుకుంటున్నాను. పరిశుద్ధాత్మ శాంతితో నాలోని కోపాగ్నిని చల్లార్చండి. నొప్పించు మాటలకు బదులుగా మృదువైన మాటలాడే జ్ఞానమును నాకు దయచేయండి. క్రీస్తు నన్ను క్షమించినట్లే నేనును క్షమించుటకు కృపనివ్వండి. యేసు నామములో ప్రార్థించుచున్నాను, ఆమేన్."
        },
        {
            "id": "anger_at_friend_conflict",
            "keywords": [
                "im angry on my friend", "i am angry on my friend", "angry on my friend", "angry on friend",
                "angry with friend", "angry with my friend", "mad at my friend", "mad at friend",
                "friend betrayed me", "friend hurt me", "friend fight", "argument with friend",
                "friendship broken", "conflict with friend", "best friend fight", "hate my friend",
                "disappointed with friend", "upset with friend", "స్నేహితునిపై కోపం", "స్నేహితుడు బాధపెట్టాడు"
            ],
            "title_en": "When You Are Angry with a Friend / Friendship Conflict",
            "title_te": "స్నేహితునిపై కోపం వచ్చినప్పుడు / స్నేహితుల మధ్య మనస్పర్ధలు ఏర్పడినప్పుడు",
            "primary_verse": {
                "reference": "Colossians 3:13",
                "book": "Colossians",
                "chapter": 3,
                "verse": 13,
                "text_en": "Forbearing one another, and forgiving one another, if any man have a quarrel against any: even as Christ forgave you, so also do ye.",
                "text_te": "ఎవడైనను తనకు మరియొకనిమీద ఫిర్యాదు పడవలసిన హేతువు కలిగినయెడల, ఒకనినొకడు సహించుచు ఒకనినొకడు క్షమించుడి; ప్రభువు మిమ్మును క్షమించినలాగున మీరును క్షమించుడి."
            },
            "supporting_verses": [
                {
                    "reference": "Proverbs 17:17",
                    "text_en": "A friend loveth at all times, and a brother is born for adversity.",
                    "text_te": "నిజమైన స్నేహితుడు విడువక ప్రేమింతును, ఆపత్కాలమునందు అతడు సహోదరుడుగా ఉండును."
                },
                {
                    "reference": "Ephesians 4:31-32",
                    "text_en": "Let all bitterness, and wrath, and anger, and clamour, and evil speaking, be put away from you, with all malice: And be ye kind one to another, tenderhearted, forgiving one another, even as God for Christ's sake hath forgiven you.",
                    "text_te": "సమస్తమైన చేదును, క్రోధమును, కోపమును, అల్లరియు, దూషణయు, సకలమైన దుష్టత్వమును మీలోనుండి తీసివేయుడి. ఒకరియెడల ఒకరు దయాళువులై, కరుణాహృదయులై, క్రీస్తునందు దేవుడు మిమ్మును క్షమించిన ప్రకారము మీరును ఒకరినొకరు క్షమించుడి."
                },
                {
                    "reference": "Matthew 5:23-24",
                    "text_en": "Therefore if thou bring thy gift to the altar, and there rememberest that thy brother hath ought against thee; Leave there thy gift before the altar, and go thy way; first be reconciled to thy brother, and then come and offer thy gift.",
                    "text_te": "కావున నీవు బలిపీఠమునొద్ద అర్పణము నర్పించుచుండగా, నీమీద నీ సహోదరునికి విరోధమేమైనను కలదని అక్కడ నీకు జ్ఞాపకము వచ్చినయెడల, అక్కడనే బలిపీఠము నెదుట నీ యర్పణమును విడిచిపెట్టి, మొదట వెళ్లి నీ సహోదరునితో సమాధానపడుము, అటు తరువాత వచ్చి నీ యర్పణము నర్పింపుము."
                },
                {
                    "reference": "Proverbs 27:6",
                    "text_en": "Faithful are the wounds of a friend; but the kisses of an enemy are deceitful.",
                    "text_te": "స్నేహితుడు రేపు గాయములు నమ్మకమైనవి; పగవాడు ముద్దులు పెట్టుకొనుట వంచనయే."
                },
                {
                    "reference": "Romans 12:18",
                    "text_en": "If it be possible, as much as lieth in you, live peaceably with all men.",
                    "text_te": "శక్యమైతే మీ చేతనైనంత మట్టుకు సమస్త మనుష్యులతో సమాధానముగా ఉండుడి."
                }
            ],
            "pastoral_reflection": "Few pains sting sharper than feeling betrayed, mocked, or let down by a trusted friend. You shared your heart, and now your soul feels bruised and boiling with indignation. God sees every tear and understands every wound. But hear this loving counsel: do not let this hurt freeze into lifelong bitterness. Talk directly to your friend in private humility (Matthew 18:15) rather than venting on social media or gossiping to others. Value the bond of friendship higher than the pride of winning an argument. Christ died for us while we were yet enemies; ask Him for the grace to reach out with forgiveness.",
            "pastoral_reflection_te": "మనం ఎంతో నమ్మిన స్నేహితుడు బాధపెట్టినప్పుడు లేదా మోసం చేసినప్పుడు ఆ గాయం గుండెల్లో తీవ్రమైన బాధను, కోపాన్ని కలిగిస్తుంది. మీరు వారిని నమ్మారు, కానీ ఇప్పుడు మీ మనస్సు రగిలిపోతోంది. మీ కన్నీటిని దేవుడు చూస్తున్నాడు. అయితే ఈ కోపము మీ హృదయంలో చేదుగా మారకుండా జాగ్రత్తపడండి. ఇతరుల వద్ద లేదా సోషల్ మీడియాలో స్నేహితునిపై నిందలు వేయకుండా, ఏకాంతముగా ప్రేమతో మాట్లాడి సమస్యను పరిష్కరించుకోండి (మత్తయి 18:15). వాదన గెలవడం కంటే స్నేహాన్ని కాపాడుకోవడం చాలా విలువైనది. క్రీస్తు మనలను ప్రేమించినట్లుగా క్షమాపణతో ముందుకు సాగండి.",
            "prayer_en": "Dear Lord, my friend has deeply hurt my feelings today, and I am struggling with fierce anger and sadness. Part of me wants to retaliate or walk away forever. But You command me to love, to bear with weaknesses, and to seek peace. Cleanse my heart of vengeance. Give me wisdom to speak the truth in love, humility to admit my own shortcomings, and the grace to forgive just as You forgave me completely. Restore our bond according to Your holy will. In Jesus' loving name, Amen.",
            "prayer_te": "ప్రియమైన ప్రభువా, నేడు నా స్నేహితుని ప్రవర్తన వలన నా మనస్సు ఎంతో నొచ్చుకున్నది, నాలో తీవ్రమైన కోపము రగులుచున్నది. వారిపై ప్రతీకారం తీర్చుకోవాలని లేదా సంబంధాన్ని తెంచుకోవాలని నా స్వభావం అనుకుంటోంది. కానీ మీరు నన్ను క్షమించి, ప్రేమతో సమాధానపడమని ఆజ్ఞాపిస్తున్నారు. నా హృదయములోని కోపమును, పగను కడిగివేయండి. నా స్నేహితునితో ప్రేమతో, వినయంతో మాట్లాడి సమాధానపడుటకు కృపనివ్వండి. మా మధ్య ఉన్న స్నేహబంధమును మీ చిత్తానుసారముగా సరిచేయండి. యేసుక్రీస్తు నామములో ప్రార్థించుచున్నాను, ఆమేన్."
        },
        {
            "id": "temptation_and_sin",
            "keywords": [
                "tempted", "temptation", "sin", "addiction", "lust", "weakness", "fall",
                "backslide", "flesh", "struggling with sin", "resist devil", "శోధన", "పాపం"
            ],
            "title_en": "When Battling Fierce Temptation & Overcoming Sin",
            "title_te": "తీవ్రమైన శోధనను ఎదుర్కొనుచున్నప్పుడు & పాపముపై జయము పొందుటకు",
            "primary_verse": {
                "reference": "1 Corinthians 10:13",
                "book": "1 Corinthians",
                "chapter": 10,
                "verse": 13,
                "text_en": "There hath no temptation taken you but such as is common to man: but God is faithful, who will not suffer you to be tempted above that ye are able; but will with the temptation also make a way to escape, that ye may be able to bear it.",
                "text_te": "మనుష్యులకు సాధారణముగా రాని ఏ శోధనయు మీకు రాలేదు; దేవుడు నమ్మదగినవాడు, మీరు సహింపగలకంటె ఎక్కువ శోధన మీకు రానియ్యడు; దానిని సహింపగలుగుటకు శోధనతోకూడ తప్పించుకొను మార్గమును కలుగజేయును."
            },
            "supporting_verses": [
                {
                    "reference": "James 4:7",
                    "text_en": "Submit yourselves therefore to God. Resist the devil, and he will flee from you.",
                    "text_te": "కాబట్టి దేవునికి లోబడియుండుడి; అపవాదిని ఎదిరించుడి, అప్పుడు వాడు మీయొద్దనుండి పారిపోవును."
                },
                {
                    "reference": "Psalms 119:11",
                    "text_en": "Thy word have I hid in mine heart, that I might not sin against thee.",
                    "text_te": "నీ యెదుట నేను పాపము చేయకుండునట్లు నా హృదయములో నీ వాక్యము ఉంచుకొనియున్నాను."
                }
            ],
            "pastoral_reflection": "Being tempted is not sin—even Jesus was tempted in the wilderness. Yielding to temptation is where sin conceives. Remember that in every single temptation, God always creates an exit door. Flee from compromising environments, hide God's Word in your heart, and call upon the name of the Lord who breaks every chain.",
            "pastoral_reflection_te": "శోధించబడటం పాపం కాదు; యేసుక్రీస్తు కూడా అరణ్యములో శోధించబడ్డాడు. శోధనకు లొంగిపోవడమే పాపము. ప్రతి శోధనలోనూ దేవుడు తప్పించుకునే మార్గమును సిద్ధపరచాడని మరువకండి. పాపపు పరిస్థితుల నుండి పారిపోండి, దేవుని వాక్యమును హృదయములో దాచుకోండి.",
            "prayer_en": "Father, the pull of sin is strong, but Your grace is greater. Provide the way of escape right now. Give me holy courage to say NO to ungodliness and YES to righteousness. In Jesus' mighty name, Amen.",
            "prayer_te": "పరలోకపు తండ్రీ, శోధన తీవ్రముగా ఉన్నది, కానీ మీ కృప అంతకంటే గొప్పది. ఇప్పుడే తప్పించుకొను మార్గమును నాకు చూపించండి. పాపమును తిరస్కరించి, పరిశుద్ధతలో నిలబడే ధైర్యమును నాకు దయచేయండి. యేసు శక్తిగల నామములో ప్రార్థించుచున్నాను, ఆమేన్."
        },
        {
            "id": "doubt_and_faith",
            "keywords": [
                "doubt", "doubting", "unbelief", "struggling faith", "is god real",
                "confusion", "skeptical", "questions", "faith weak", "lost faith", "సందేహం", "అపనమ్మకం"
            ],
            "title_en": "When Plagued by Doubts & Wrestling with Faith",
            "title_te": "సందేహాలు చుట్టుముట్టినప్పుడు & విశ్వాస పోరాటములో ఉన్నప్పుడు",
            "primary_verse": {
                "reference": "Mark 9:24",
                "book": "Mark",
                "chapter": 9,
                "verse": 24,
                "text_en": "And straightway the father of the child cried out, and said with tears, Lord, I believe; help thou mine unbelief.",
                "text_te": "వెంటనే ఆ చిన్నవాని తండ్రి కేకవేసి—నేను నమ్ముచున్నాను, నాకు అపనమ్మకము లేకుండా సహాయము చేయుమని కన్నీళ్లతో చెప్పెను."
            },
            "supporting_verses": [
                {
                    "reference": "James 1:5-6",
                    "text_en": "If any of you lack wisdom, let him ask of God, that giveth to all men liberally, and upbraideth not; and it shall be given him. But let him ask in faith, nothing wavering.",
                    "text_te": "మీలో ఎవనికైనను జ్ఞానము కొదువగా ఉన్నయెడల అతడు దేవుని అడుగవలెను, అప్పుడది అతనికి అనుగ్రహింపబడును. అయితే అతడు ఏమాత్రమును సందేహింపక విశ్వాసముతో అడుగవలెను."
                },
                {
                    "reference": "Hebrews 11:1",
                    "text_en": "Now faith is the substance of things hoped for, the evidence of things not seen.",
                    "text_te": "విశ్వాసమనునది నిరీక్షింపబడువాటియొక్క నిజస్వరూపమును, అదృశ్యమైన సంగతులు ఉన్నవనుటకు రుజువునై యున్నది."
                }
            ],
            "pastoral_reflection": "Doubt does not mean you have lost your faith; it means your faith is growing and wrestling for deeper roots. Thomas doubted Christ's resurrection, yet Jesus gently held out His nail-pierced hands. Bring your honest questions to Scripture, seek wise counsel, and watch God reveal Himself faithfully.",
            "pastoral_reflection_te": "సందేహం రావడం వల్ల మీ విశ్వాసం పోయిందని భావించవద్దు; మీ విశ్వాసము లోతైన వేళ్లు వేయడానికి ఇది ఒక ఆహ్వానము. తోమా కూడా సందేహించినప్పుడు యేసు అతనిని తోసివేయక తన గాయములను చూపి బలపరిచాడు. మీ సందేహాలతో దేవుని పాదాల యొద్దకు రండి.",
            "prayer_en": "Lord, help my unbelief. When doubts cloud my understanding, anchor my heart in the steadfast truth of Your Word. Let Your Holy Spirit shine light into my questions. In Jesus' name, Amen.",
            "prayer_te": "ప్రభువా, నా అపనమ్మకమును తీసివేసి సహాయము చేయండి. నా మనస్సులో సందేహాలు రేగినప్పుడు మీ వాక్య సత్యములో నన్ను నిలబెట్టండి. మీ పరిశుద్ధాత్మ వెలుగును నా హృదయములో ప్రకాశింపజేయండి. యేసు నామములో ప్రార్థించుచున్నాను, ఆమేన్."
        }
    ]

    emotions.extend(new_emotions)
    data["emotions"] = emotions

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Enriched emotions.json with {len(new_emotions)} new emotions. Total: {len(emotions)}")


def enrich_incidents():
    filepath = os.path.join(DATA_DIR, "incidents.json")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    incidents = [inc for inc in data.get("incidents", []) if inc.get("id") not in [
        "jacob_birthright_esau", "jacob_ladder_bethel", "jacob_wrestles_peniel",
        "witchcraft_saul_endor", "witchcraft_scripture_condemnation", "lot_daughters_sin_cave"
    ]]

    new_incidents = [
        {
            "id": "jacob_birthright_esau",
            "title_en": "Jacob and Esau: The Stolen Birthright and Blessing",
            "title_te": "యాకోబు మరియు ఏశావు: జ్యేష్ఠత్వపు హక్కు & ఆశీర్వాదము",
            "book": "Genesis",
            "chapter_start": 25,
            "verse_start": 29,
            "chapter_end": 27,
            "verse_end": 45,
            "reference": "Genesis 25:29-34, 27:1-45",
            "keywords": [
                "jacob", "esau", "birthright", "blessing", "isaac", "rebekah", "stew",
                "lentils", "deception", "goatskin", "inheritance", "stolen blessing",
                "యాకోబు", "ఏశావు", "జ్యేష్ఠత్వపు హక్కు", "ఆశీర్వాదము"
            ],
            "summary_en": "Esau despised his birthright for a single bowl of red stew. Later, Jacob disguised himself with goatskins to receive Isaac's patriarchal blessing. While Jacob used human cunning, God's sovereign covenant was fulfilled, teaching that spiritual blessings must never be traded for momentary earthly appetites.",
            "summary_te": "ఏశావు ఒక పూట ఎర్రని చిక్కుడుకూటి కొరకు తన జ్యేష్ఠత్వపు హక్కును తృణీకరించెను. తరువాత యాకోబు తన తల్లి రెబ్కా ఆలోచన చొప్పున మేకపిల్లల చర్మములతో వేషము వేసికొని ఇస్సాకు తండ్రి దీవెనను పొందెను. యాకోబు ఉపాయము వాడినప్పటికీ దేవుని సంకల్పము నెరవేరెను; క్షణికమైన శరీర భోగాల కొరకు ఆత్మీయ దీవెనలను తృణీకరించకూడదని ఇది మనకు నేర్పుతుంది."
        },
        {
            "id": "jacob_ladder_bethel",
            "title_en": "Jacob's Dream at Bethel: The Heavenly Ladder",
            "title_te": "బేతేలులో యాకోబు కల: పరలోకపు నిచ్చెన",
            "book": "Genesis",
            "chapter_start": 28,
            "verse_start": 10,
            "chapter_end": 28,
            "verse_end": 22,
            "reference": "Genesis 28:10-22",
            "keywords": [
                "jacob", "bethel", "ladder", "angels", "dream", "stone pillow",
                "gate of heaven", "vow", "covenant", "vision", "యాకోబు", "బేతేలు", "నిచ్చెన"
            ],
            "summary_en": "Fleeing from Esau, Jacob slept in the wilderness with a stone for a pillow. He dreamed of a ladder set on earth reaching to heaven, with angels ascending and descending upon it, and the LORD standing above it promising covenant protection. Jacob woke declaring, 'Surely the LORD is in this place!' and named it Bethel (House of God).",
            "summary_te": "ఏశావుకు భయపడి పారిపోవుచున్న యాకోబు అరణ్యములో ఒక రాయిని తలగడగా చేసుకొని నిద్రించెను. భూమిపై నిలువబడిన ఒక నిచ్చెన పైకొన ఆకాశమునంటుచుండగా, దానిపై దేవుని దూతలు ఎక్కుచు దిగుచుండుట అతడు కనెను; యెహోవా దానిపై నిలిచి అబ్రాహాము ఇస్సాకుల వాగ్దానమును అతనికి అనుగ్రహించెను. యాకోబు మేల్కొని 'నిశ్చయముగా యెహోవా ఈ స్థలమందున్నాడు' అని ఆ స్థలమునకు 'బేతేలు' (దేవుని మందిరము) అని పేరు పెట్టెను."
        },
        {
            "id": "jacob_wrestles_peniel",
            "title_en": "Jacob Wrestles with God at Peniel: Transformed to Israel",
            "title_te": "పెనూయేలులో యాకోబు దేవునితో పోరాడుట: ఇశ్రాయేలుగా రూపాంతరం",
            "book": "Genesis",
            "chapter_start": 32,
            "verse_start": 22,
            "chapter_end": 32,
            "verse_end": 32,
            "reference": "Genesis 32:22-32",
            "keywords": [
                "jacob", "peniel", "wrestle", "israel", "angel", "blessing", "hip",
                "face to face with god", "jabbok", "transformation", "యాకోబు", "పెనూయేలు", "ఇశ్రాయేలు"
            ],
            "summary_en": "Alone by the river Jabbok facing terrified reunion with Esau, a mysterious Man wrestled with Jacob until dawn. Even with a displaced hip, Jacob clung tightly, crying, 'I will not let thee go, except thou bless me!' God changed his name from Jacob ('deceiver') to Israel ('one who strives with God and prevails').",
            "summary_te": "యబ్బోకు రేవు దాటిన తర్వాత ఒంటరిగా ఉన్న యాకోబుతో ఒక పురుషుడు తెల్లవారువరకు పోరాడెను. ఆయన అతని తొడగూడును మణగగొట్టినను యాకోబు 'నీవు నన్ను ఆశీర్వదించితేనే గాని నిన్ను పోనియ్యను' అని పట్టుపట్టెను. దేవుడు అతని పేరును 'యాకోబు' నుండి 'ఇశ్రాయేలు'గా మార్చి ఆశీర్వదించెను. యాకోబు దేవుని ముఖాముఖిగా చూచి ప్రాణము దక్కించుకొనెను."
        },
        {
            "id": "witchcraft_saul_endor",
            "title_en": "King Saul and the Witch of Endor: The Forbidden Occult",
            "title_te": "సౌలు మరియు ఏన్దోరులోని కర్ణపిశాచముగల స్త్రీ: నిషేధించబడిన మాంత్రికత",
            "book": "1 Samuel",
            "chapter_start": 28,
            "verse_start": 3,
            "chapter_end": 28,
            "verse_end": 25,
            "reference": "1 Samuel 28:3-25",
            "keywords": [
                "witchcraft", "witch", "witch of endor", "saul", "medium", "familiar spirit",
                "necromancy", "occult", "samuel ghost", "sorcery", "philistines",
                "చేతబడి", "మాంత్రికత", "కర్ణపిశాచి", "సౌలు", "ఏన్దోరు"
            ],
            "summary_en": "Terrified by the Philistine armies and abandoned by God due to chronic disobedience, King Saul disguised himself and consulted a medium with a familiar spirit at Endor. Samuel was summoned to pronounce doom: Israel would fall, and Saul and his sons would die the next day. Saul's tragic death was divine judgment for inquiring of mediums (1 Chron 10:13).",
            "summary_te": "ఫిలిష్తీయుల సైన్యమునకు భయపడి, అవిధేయత వలన దేవుని సహాయము కోల్పోయిన సౌలు రాజు వేషము మార్చుకుని ఏన్దోరులోని కర్ణపిశాచముగల స్త్రీ యొద్దకు వెళ్లి సమూయేలును రప్పించెను. మరుసటి రోజే ఇశ్రాయేలు సైన్యం ఓడిపోవునని, సౌలు మరియు అతని కుమారులు చనిపోవుదురని తీర్పు వినబడెను. కర్ణపిశాచము యొద్ద విచారణ చేసినందుకే సౌలు చంపబడెనని లేఖనము సెలవిచ్చుచున్నది (1 దినవృత్తాంతములు 10:13)."
        },
        {
            "id": "witchcraft_scripture_condemnation",
            "title_en": "Scripture's Absolute Condemnation of Witchcraft, Sorcery, and the Occult",
            "title_te": "చేతబడి, మాంత్రికత, బాణామతి మరియు భూతవైద్యముపై దేవుని తీర్పు",
            "book": "Deuteronomy",
            "chapter_start": 18,
            "verse_start": 10,
            "chapter_end": 18,
            "verse_end": 14,
            "reference": "Deut 18:10-14, Galatians 5:19-21, Revelation 21:8",
            "keywords": [
                "witchcraft", "sorcery", "occult", "black magic", "astrology", "medium",
                "horoscope", "fortune telling", "soothsayer", "necromancer", "charmer",
                "works of the flesh", "lake of fire", "చేతబడి", "మాంత్రికత", "బాణామతి", "జ్యోతిష్యం"
            ],
            "summary_en": "God strictly forbids all forms of witchcraft, astrology, fortune-telling, necromancy, and charms as abominations. Galatians 5 lists sorcery as works of the flesh that exclude from the Kingdom of God, while Revelation 21:8 confirms sorcerers face the lake of fire unless they repent. Believers are called to trust in the living God alone.",
            "summary_te": "తన కుమారులనైనను కుమార్తెలనైనను అగ్నిగుండము దాటించువాడైనను, శకునము చెప్పువాడైనను, గారడీవాడైనను, మంత్రగాడైనను, కర్ణపిశాచముగలవాడైనను మీలో ఉండకూడదనియు; ఈ హేయమైన పనులు చేయువారిని యెహోవా అసహ్యించుకొనుననియు దేవుడు ఆజ్ఞాపించెను. గలతీ 5 లో మాంత్రికత శరీరకార్యమని, ప్రకటన 21:8 లో మాంత్రికులకు అగ్నిగుండములో పాలుండునని దేవుని వాక్యము తీవ్రముగా హెచ్చరిస్తోంది."
        },
        {
            "id": "lot_daughters_sin_cave",
            "title_en": "Lot and His Daughters in the Cave: Human Sin and Generational Bitter Fruit",
            "title_te": "లోతు మరియు అతని కుమార్తెలు గుహలో చేసిన పాపము",
            "book": "Genesis",
            "chapter_start": 19,
            "verse_start": 30,
            "chapter_end": 19,
            "verse_end": 38,
            "reference": "Genesis 19:30-38",
            "keywords": [
                "lot", "daughters", "cave", "sodom", "incest", "wine", "moab", "ammon",
                "moabites", "ammonites", "sin of lot", "zoar", "consequences of sin",
                "లోతు", "కుమార్తెలు", "గుహ", "పాపము", "మోయాబు", "అమ్మోను"
            ],
            "summary_en": "After Sodom's fiery destruction, Lot's daughters despaired in an isolated cave. Compromised by Sodom's godless worldview, they intoxicated their father with wine and committed incest. The children born—Moab and Ben-Ammi—fathered pagan nations that persecuted Israel for centuries. The Bible records this human sin to demonstrate the poisonous decay of Sodom and the devastating consequences of human rebellion.",
            "summary_te": "సొదొమ నాశనమైన తర్వాత లోతు కుమార్తెలు ఒక గుహలో నివసిస్తూ, సొదొమ నైతిక పతనం వలన దేవునిపై విశ్వాసం కోల్పోయి, తమ తండ్రికి ద్రాక్షారసము త్రాగించి ఆయనతో శయనించిరి. దీని ద్వారా మోయాబీయులు మరియు అమ్మోనీయులు అను అన్యజాతులు పుట్టి ఇశ్రాయేలీయులను తరతరాలుగా హింసించిరి. పాపం ఎంతటి ఘోరమైన పర్యవసానాలను తెస్తుందో హెచ్చరించడానికే బైబిల్ ఈ ఉదంతాన్ని దాచకుండా రాసింది."
        }
    ]

    incidents.extend(new_incidents)
    data["incidents"] = incidents

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Enriched incidents.json with {len(new_incidents)} new incidents. Total: {len(incidents)}")


if __name__ == "__main__":
    print("Starting clean UTF-8 enrichment...")
    enrich_chapter_contexts()
    enrich_emotions()
    enrich_incidents()
    print("Enrichment finished successfully!")
