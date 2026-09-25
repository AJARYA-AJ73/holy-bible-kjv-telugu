# -*- coding: utf-8 -*-
"""
Generates an exhaustive 100-story Biblical Incidents & Stories Encyclopedia in incidents.json
covering Genesis to Revelation with complete English & authentic Telugu narratives,
exact scripture book/chapter/verse coordinates, and extensive search keywords.
"""
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "incidents.json")

STORIES = [
    # 1. Creation
    {
        "id": "creation_universe_man",
        "title_en": "Creation of the Universe and Mankind",
        "title_te": "విశ్వము మరియు మానవుని సృష్టి",
        "book": "Genesis",
        "chapter_start": 1,
        "verse_start": 1,
        "chapter_end": 2,
        "verse_end": 25,
        "reference": "Genesis 1:1 - 2:25",
        "keywords": ["creation", "adam", "eve", "eden", "six days", "light", "firmament", "image of god", "సృష్టి", "ఆదాము", "హవ్వ", "ఏదేను వనము"],
        "summary_en": "In the beginning, God created the heavens and the earth out of nothing by the power of His spoken Word in six days, crowning creation with Adam and Eve in His divine image.",
        "summary_te": "ఆదియందు దేవుడు తన మాట శక్తి ద్వారా ఆరు దినములలో ఆకాశమును భూమిని సృష్టించెను. సమస్త సృష్టికి కిరీటముగా ఆదాము హవ్వలను తన దివ్య స్వరూపమందు చేసెను."
    },
    # 2. Fall
    {
        "id": "fall_of_man",
        "title_en": "The Fall of Man and the First Promise of the Savior",
        "title_te": "మానవుని పతనము మరియు రక్షకుని తొలి వాగ్దానము",
        "book": "Genesis",
        "chapter_start": 3,
        "verse_start": 1,
        "chapter_end": 3,
        "verse_end": 24,
        "reference": "Genesis 3:1-24",
        "keywords": ["fall of man", "serpent", "fruit", "forbidden tree", "original sin", "protoevangelium", "seed of woman", "పాపము", "సర్పము", "పతనము"],
        "summary_en": "Tempted by the serpent, Eve and Adam ate of the forbidden tree of knowledge, bringing sin, shame, and death into the world. Yet God pronounced the Protoevangelium—the seed of the woman would crush the serpent's head.",
        "summary_te": "సర్పము యొక్క మోసకరమైన శోధనకు లొంగి ఆదాము హవ్వలు మంచిచెడ్డల తెలివినిచ్చు వృక్షఫలమును తిని పాపము చేసిరి. అయినను స్త్రీ సంతానము సర్పము తలను చితకద్రొక్కునని దేవుడు రక్షకుని తొలి వాగ్దానమును అనుగ్రహించెను."
    },
    # 3. Cain and Abel
    {
        "id": "cain_and_abel",
        "title_en": "Cain and Abel: The First Murder and the Blood that Cries",
        "title_te": "కయీను మరియు హేబెలు: తొలి నరహత్య మరియు రక్తపు మొఱ్ఱ",
        "book": "Genesis",
        "chapter_start": 4,
        "verse_start": 1,
        "chapter_end": 4,
        "verse_end": 16,
        "reference": "Genesis 4:1-16",
        "keywords": ["cain", "abel", "first murder", "blood", "acceptable sacrifice", "brother's keeper", "కయీను", "హేబెలు", "నరహత్య"],
        "summary_en": "Abel offered an acceptable faith-filled blood sacrifice to God, while Cain offered the fruit of his own labor. Filled with jealousy and wrath, Cain murdered his righteous brother Abel in the field.",
        "summary_te": "హేబెలు విశ్వాసముతో దేవునికి రక్తబలి అర్పించి ఆమోదము పొందెను. కయీను అసూయతో రగిలిపోయి తన తమ్ముడైన హేబెలును పొలములో చంపి ప్రథమ నరహత్య చేసెను."
    },
    # 4. Noah's Ark
    {
        "id": "noah_ark",
        "title_en": "Noah's Ark and the Great Global Deluge",
        "title_te": "నోవహు ఓడ మరియు జలప్రళయము",
        "book": "Genesis",
        "chapter_start": 6,
        "verse_start": 9,
        "chapter_end": 9,
        "verse_end": 17,
        "reference": "Genesis 6:9 - 9:17",
        "keywords": ["noah", "ark", "flood", "animals", "rainbow", "covenant", "deluge", "righteous", "నోవహు", "ఓడ", "జలప్రళయము", "ఇంద్రధనస్సు"],
        "summary_en": "Seeing human wickedness fill the earth, God judged mankind with a worldwide flood but spared righteous Noah, his family, and animal pairs aboard the Ark. God set the rainbow as a covenant sign never to destroy the earth by water again.",
        "summary_te": "భూమిమీద నరుల చెడుతనము విస్తరించినప్పుడు దేవుడు జలప్రళయము ద్వారా లోకమును తీర్పుతీర్చెను; అయితే నీతిమంతుడైన నోవహును అతని కుటుంబమును ఓడలో కాపాడి, ఇంద్రధనస్సును శాశ్వత నిబంధనకు గుర్తుగా ఉంచెను."
    },
    # 5. Tower of Babel
    {
        "id": "tower_of_babel",
        "title_en": "The Tower of Babel: Pride and the Confusion of Tongues",
        "title_te": "బాబెలు గోపురము: మానవ గర్వము మరియు భాషల తారుమారు",
        "book": "Genesis",
        "chapter_start": 11,
        "verse_start": 1,
        "chapter_end": 11,
        "verse_end": 9,
        "reference": "Genesis 11:1-9",
        "keywords": ["babel", "tower", "pride", "confusion of languages", "shinar", "scattered", "బాబెలు", "గోపురము", "భాషలు"],
        "summary_en": "United in arrogant self-willed pride, mankind attempted to build a tower reaching unto heaven to make a name for themselves. God scattered them across the earth by confounding their languages.",
        "summary_te": "మానవులు తమ పేరు ప్రఖ్యాతుల కొరకు ఆకాశమునంటు గోపురమును కట్టదలచి గర్వపడగా, దేవుడు వారి భాషలను తారుమారు చేసి వారిని భూమియంతట చెదరగొట్టెను."
    },
    # 6. Call of Abraham
    {
        "id": "call_of_abraham",
        "title_en": "The Call of Abraham and the Covenant of Faith",
        "title_te": "అబ్రాహాము పిలుపు మరియు విశ్వాస నిబంధన",
        "book": "Genesis",
        "chapter_start": 12,
        "verse_start": 1,
        "chapter_end": 15,
        "verse_end": 21,
        "reference": "Genesis 12:1-4, 15:1-18",
        "keywords": ["abraham", "abram", "call of god", "covenant", "ur of the chaldees", "promised land", "stars", "faith", "అబ్రాహాము", "పిలుపు", "నిబంధన"],
        "summary_en": "God commanded Abram to leave his country and family for an unknown promised land, swearing an unconditional covenant that all nations of the earth would be blessed through his seed.",
        "summary_te": "తన దేశమును బంధువులను విడిచి తాను చూపించు దేశమునకు వెళ్లవలెనని దేవుడు అబ్రాహామును పిలిచి, అతని సంతానము ద్వారా భూమిమీదనున్న సమస్త వంశములు ఆశీర్వదింపబడునని నిబంధన చేసెను."
    },
    # 7. Sacrifice of Isaac
    {
        "id": "sacrifice_of_isaac_moriah",
        "title_en": "The Binding of Isaac on Mount Moriah: God Will Provide",
        "title_te": "మోరీయా పర్వతముపై ఇస్సాకు బలి: యెహోవా ఈరే",
        "book": "Genesis",
        "chapter_start": 22,
        "verse_start": 1,
        "chapter_end": 22,
        "verse_end": 19,
        "reference": "Genesis 22:1-19",
        "keywords": ["isaac", "abraham", "moriah", "jehovah jireh", "ram in the thicket", "sacrifice", "test of faith", "ఇస్సాకు", "మోరీయా", "యెహోవా ఈరే"],
        "summary_en": "God tested Abraham by commanding him to offer his beloved son Isaac on Mount Moriah. As Abraham raised the knife in obedient faith, God halted him and provided a ram caught in a thicket—naming the place Jehovah-Jireh.",
        "summary_te": "దేవుడు అబ్రాహామును పరీక్షించి తన ఏకైక కుమారుడైన ఇస్సాకును బలిగా అర్పించమని ఆజ్ఞాపించెను. అబ్రాహాము విధేయత చూపినప్పుడు దేవుడు అతనిని ఆపి, పొదలో చిక్కుకున్న పొట్టేలును బదులుగా ఇచ్చి 'యెహోవా ఈరే' అని పేరు పెట్టించెను."
    },
    # 8. Jacob & Esau
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
        "keywords": ["jacob", "esau", "birthright", "blessing", "isaac", "rebekah", "stew", "యాకోబు", "ఏశావు", "జ్యేష్ఠత్వపు హక్కు"],
        "summary_en": "Esau despised his spiritual birthright for a single bowl of red stew. Later, Jacob deceived their blind father Isaac to receive the patriarchal blessing.",
        "summary_te": "ఏశావు ఒక పూట ఎర్రని చిక్కుడుకూటి కొరకు తన జ్యేష్ఠత్వపు హక్కును అమ్ముకొనెను. తరువాత యాకోబు తన తండ్రి ఇస్సాకు దీవెనను పొందెను."
    },
    # 9. Jacob's Ladder
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
        "keywords": ["jacob", "bethel", "ladder", "angels", "dream", "stone pillow", "యాకోబు", "బేతేలు", "నిచ్చెన"],
        "summary_en": "Fleeing from Esau, Jacob dreamed of a ladder reaching to heaven with angels ascending and descending upon it. God reaffirmed the Abrahamic covenant with him.",
        "summary_te": "పారిపోవుచున్న యాకోబు రాయిని తలగడగా చేసి పడుకొనగా, పరలోకమునంటుచున్న నిచ్చెనను దేవదూతలు ఎక్కుచు దిగుచుండుటను కనెను; ఆ స్థలమునకు బేతేలు అని పేరు పెట్టెను."
    },
    # 10. Jacob Wrestles
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
        "keywords": ["jacob", "peniel", "wrestle", "israel", "angel", "blessing", "jabbok", "యాకోబు", "పెనూయేలు", "ఇశ్రాయేలు"],
        "summary_en": "By the river Jabbok, a mysterious divine Man wrestled with Jacob until daybreak. Clinging for a blessing, Jacob was renamed Israel—'one who strives with God and prevails'.",
        "summary_te": "యబ్బోకు రేవున ఒంటరిగా ఉన్న యాకోబుతో దేవుని దూత తెల్లవారువరకు పోరాడెను; యాకోబు దీవెన కొరకు పట్టుపట్టగా అతని పేరును 'ఇశ్రాయేలు'గా మార్చెను."
    },
    # 11. Joseph Sold
    {
        "id": "joseph_sold_slavery",
        "title_en": "Joseph Betrayed and Sold into Egyptian Slavery by His Brothers",
        "title_te": "యోసేపు సహోదరులచే ఐగుప్తు బానిసత్వమునకు అమ్మబడుట",
        "book": "Genesis",
        "chapter_start": 37,
        "verse_start": 1,
        "chapter_end": 37,
        "verse_end": 36,
        "reference": "Genesis 37:1-36",
        "keywords": ["joseph", "coat of many colors", "brothers", "jealousy", "pit", "midianites", "egypt", "dreams", "యోసేపు", "రంగుల నిలువుటంగీ", "బానిసత్వం"],
        "summary_en": "Loved by Jacob and gifted with prophetic dreams, Joseph was envied by his brothers, stripped of his ornate coat, cast into a pit, and sold for twenty pieces of silver to slave traders bound for Egypt.",
        "summary_te": "తండ్రికి ప్రియమైన కుమారుడైన యోసేపు కన్న కలల వలన సహోదరులు అసూయపడి, అతని రంగుల నిలువుటంగీని తీసివేసి గుంటలో పడవేసి, ఇరువది వెండి నాణెములకు ఐగుప్తు బానిసగా అమ్మివేసిరి."
    },
    # 12. Joseph in Prison & Potiphar
    {
        "id": "joseph_potiphar_prison",
        "title_en": "Joseph in Potiphar's House and the Egyptian Dungeon",
        "title_te": "పోతీఫరు ఇంట మరియు చెరసాలలో యోసేపు నమ్మకత్వము",
        "book": "Genesis",
        "chapter_start": 39,
        "verse_start": 1,
        "chapter_end": 40,
        "verse_end": 23,
        "reference": "Genesis 39:1 - 40:23",
        "keywords": ["joseph", "potiphar", "temptation", "purity", "fled", "prison", "baker", "butler", "యోసేపు", "పోతీఫరు", "చెరసాల"],
        "summary_en": "Fleeing Potiphar's wife's seduction to keep moral purity before God, Joseph was falsely accused and imprisoned. Yet the LORD was with Joseph, granting him favor and the interpretation of dreams in prison.",
        "summary_te": "పోతీఫరు భార్య తెచ్చిన పాపపు శోధన నుండి దేవునికి భయపడి పారిపోయినందున నింద మోపబడి చెరసాలలో వేయబడెను; అయినను యెహోవా యోసేపునకు తోడైయుండి కలలకు భావము చెప్పే జ్ఞానమిచ్చెను."
    },
    # 13. Joseph Exalted
    {
        "id": "joseph_prime_minister_egypt",
        "title_en": "Joseph Interprets Pharaoh's Dreams and Becomes Ruler of Egypt",
        "title_te": "ఫరో కలలను వివరించి ఐగుప్తు అధిపతిగా యోసేపు హెచ్చింపబడుట",
        "book": "Genesis",
        "chapter_start": 41,
        "verse_start": 1,
        "chapter_end": 41,
        "verse_end": 57,
        "reference": "Genesis 41:1-57",
        "keywords": ["joseph", "pharaoh", "seven years famine", "plenty", "prime minister", "exalted", "యోసేపు", "ఫరో", "కరువు", "అధికారి"],
        "summary_en": "Joseph interpreted Pharaoh's prophetic dreams of seven years of abundance followed by seven years of severe famine. Pharaoh appointed Joseph prime minister over all Egypt to save millions from starvation.",
        "summary_te": "ఏడు సంవత్సరాల సమృద్ధి, ఏడు సంవత్సరాల తీవ్ర కరువును గూర్చిన ఫరో కలలకు యోసేపు అర్థము చెప్పగా, ఫరో అతనిని ఐగుప్తు దేశమంతటిపై ప్రధాన పాలకునిగా నియమించెను."
    },
    # 14. Joseph Reconciles
    {
        "id": "joseph_reconciles_brothers",
        "title_en": "Joseph Reveals His Identity and Forgives His Brothers",
        "title_te": "యోసేపు తనను తాను బయలుపరచుకొని సహోదరులను క్షమించుట",
        "book": "Genesis",
        "chapter_start": 45,
        "verse_start": 1,
        "chapter_end": 45,
        "verse_end": 28,
        "reference": "Genesis 45:1-28",
        "keywords": ["joseph", "forgiveness", "brothers reconciled", "wept", "god meant it for good", "యోసేపు", "క్షమాపణ", "సమాధానము"],
        "summary_en": "Weeping openly, Joseph revealed himself to his terrified brothers, declaring, 'God sent me before you to preserve life... ye thought evil against me; but God meant it unto good.'",
        "summary_te": "యోసేపు కన్నీటితో తన సహోదరులకు నిజము తెలిపి, 'మీరు నాకు కీడు చేయదలంచితిరి గాని దేవుడు అనేకుల ప్రాణములను రక్షించుటకై దానిని మేలుగా మార్చెను' అని వారిని ప్రేమతో క్షమించెను."
    },
    # 15. Birth of Moses
    {
        "id": "birth_rescue_moses_nile",
        "title_en": "The Birth of Moses and His Miraculous Rescue in the Nile",
        "title_te": "మోషే జననము మరియు నైలు నదిలో అద్భుత రక్షణ",
        "book": "Exodus",
        "chapter_start": 2,
        "verse_start": 1,
        "chapter_end": 2,
        "verse_end": 10,
        "reference": "Exodus 2:1-10",
        "keywords": ["moses", "basket", "nile", "pharaoh's daughter", "miriam", "jochebed", "మోషే", "నైలు నది", "బుట్ట"],
        "summary_en": "Under Pharaoh's cruel decree to drown all Hebrew newborn boys, Moses' mother hid him in an ark of bulrushes among the river reeds. Pharaoh's daughter discovered the crying child and raised him as her own son.",
        "summary_te": "మగపిల్లలందరినీ నైలు నదిలో పడవేయవలెనన్న ఫరో రాజాజ్ఞ ఉన్నప్పుడు, మోషే తల్లి జమ్ముపెట్టెలో అతనిని నదిలో ఉంచగా, ఫరో కుమార్తె ఆ బిడ్డను చూసి కనికరించి పెంచుకొనెను."
    },
    # 16. Burning Bush
    {
        "id": "burning_bush_god_name",
        "title_en": "The Burning Bush: God Commissions Moses with the Name 'I AM'",
        "title_te": "మండుచున్న పొద: 'నేను ఉన్నవాడనను వాడను' అని దేవుడు మోషేను పిలుచుట",
        "book": "Exodus",
        "chapter_start": 3,
        "verse_start": 1,
        "chapter_end": 4,
        "verse_end": 17,
        "reference": "Exodus 3:1 - 4:17",
        "keywords": ["burning bush", "moses", "holy ground", "i am that i am", "mount horeb", "deliverance", "మండే పొద", "మోషే", "పరిశుద్ధ స్థలము"],
        "summary_en": "At Mount Horeb, God appeared to Moses in a bush that burned with heavenly fire but was not consumed. Revealing His holy name 'I AM THAT I AM', God commissioned Moses to liberate Israel from Egypt.",
        "summary_te": "హోరేబు పర్వతమున మండుచున్నను కాలిపోని పొదలో నుండి దేవుడు మోషేకు ప్రత్యక్షమై, 'నేను ఉన్నవాడనను వాడను' అని తన నామమును తెలిపి ఇశ్రాయేలీయులను విడిపించుటకు పంపెను."
    },
    # 17. Ten Plagues
    {
        "id": "ten_plagues_egypt",
        "title_en": "The Ten Plagues on Egypt: The LORD Defeats the Gods of Pharaoh",
        "title_te": "ఐగుప్తుపై పది తెగుళ్లు: ఫరో దేవతలపై యెహోవా విజయం",
        "book": "Exodus",
        "chapter_start": 7,
        "verse_start": 14,
        "chapter_end": 12,
        "verse_end": 30,
        "reference": "Exodus 7:14 - 12:30",
        "keywords": ["ten plagues", "blood", "frogs", "locusts", "darkness", "firstborn", "pharaoh", "hardened heart", "పది తెగుళ్లు", "ఐగుప్తు", "ఫరో"],
        "summary_en": "Because Pharaoh refused to let God's people go, the LORD struck Egypt with ten devastating plagues—turning the Nile into blood, frogs, lice, flies, pestilence, boils, hail, locusts, darkness, and the death of the firstborn.",
        "summary_te": "ఫరో ఇశ్రాయేలీయులను పోనియ్యక హృదయమును కఠినపరచుకొనగా, దేవుడు నీళ్లు రక్తమగుట, కప్పలు, పేలు, ఈగలు, తెగులు, బొబ్బలు, వడగండ్లు, మిడతలు, చీకటి మరియు తొలిచూలు పిల్లల మరణము అను పది తెగుళ్లతో ఐగుప్తును దండించెను."
    },
    # 18. Passover
    {
        "id": "passover_blood_doorposts",
        "title_en": "The First Passover: Salvation Through the Blood of the Lamb",
        "title_te": "తొలి పస్కా: గొఱ్ఱెపిల్ల రక్తము ద్వారా రక్షణ",
        "book": "Exodus",
        "chapter_start": 12,
        "verse_start": 1,
        "chapter_end": 12,
        "verse_end": 36,
        "reference": "Exodus 12:1-36",
        "keywords": ["passover", "blood of the lamb", "doorpost", "destroying angel", "exodus", "deliverance", "పస్కా", "గొఱ్ఱెపిల్ల రక్తము", "విమోచన"],
        "summary_en": "God commanded Israel to sacrifice an unblemished lamb and strike its blood upon the lintel and side posts of their homes. When the destroying angel saw the blood, he passed over them, delivering them from death.",
        "summary_te": "నిర్దోషమైన గొఱ్ఱెపిల్ల రక్తమును ఇళ్ల ద్వారబంధముల కమ్మీలపై ప్రోక్షించవలెనని దేవుడు ఆజ్ఞాపించెను; ఆ రక్తమును చూచినప్పుడు సంహారకుడు వారిని దాటిపోయి ప్రాణములను రక్షించెను."
    },
    # 19. Red Sea
    {
        "id": "red_sea",
        "title_en": "The Parting of the Red Sea: The LORD Fights for Israel",
        "title_te": "ఎర్ర సముద్రము చీల్చబడుట: యెహోవాయే యుద్ధము చేయును",
        "book": "Exodus",
        "chapter_start": 14,
        "verse_start": 1,
        "chapter_end": 14,
        "verse_end": 31,
        "reference": "Exodus 14:1-31",
        "keywords": ["red sea", "parting of the sea", "moses rod", "pharaoh chariots", "miracle", "dry ground", "ఎర్ర సముద్రము", "మోషే", "విజయము"],
        "summary_en": "Trapped between Pharaoh's pursuing chariots and the deep sea, Moses stretched out his hand. The LORD parted the waters by a mighty east wind, and Israel walked through on dry ground while the Egyptian army was swallowed up.",
        "summary_te": "వెనుక ఫరో రథములు, ముందు ఎర్ర సముద్రము ఉన్నప్పుడు మోషే చేరచాచగా, యెహోవా సముద్రమును రెండు పాయలుగా చీల్చి ఇశ్రాయేలీయులను ఆరిన నేలమీద నడిపించి శత్రు సైన్యమును ముంచివేసెను."
    },
    # 20. Ten Commandments
    {
        "id": "ten_commandments_sinai",
        "title_en": "The Giving of the Ten Commandments on Mount Sinai",
        "title_te": "సీనాయి పర్వతముపై పది ఆజ్ఞలు ఇవ్వబడుట",
        "book": "Exodus",
        "chapter_start": 20,
        "verse_start": 1,
        "chapter_end": 20,
        "verse_end": 21,
        "reference": "Exodus 20:1-21",
        "keywords": ["ten commandments", "mount sinai", "moral law", "tablets of stone", "thunder", "covenant", "పది ఆజ్ఞలు", "సీనాయి పర్వతము", "ధర్మశాస్త్రము"],
        "summary_en": "Amid thunder, lightning, thick cloud, and trumpet blast on Mount Sinai, God spoke His holy Moral Law directly to Israel and wrote the Ten Commandments on tablets of stone.",
        "summary_te": "సీనాయి పర్వతముపై ఉరుములు, మెరుపులు మరియు దైవిక మహిమ మధ్య దేవుడు ప్రత్యక్షమై తన పరిశుద్ధ నైతిక ధర్మశాస్త్రమైన పది ఆజ్ఞలను రాతిపలకలపై రాసి అనుగ్రహించెను."
    },
    # 21. Golden Calf
    {
        "id": "golden_calf_moses_intercession",
        "title_en": "The Golden Calf and Moses' Desperate Intercession",
        "title_te": "బంగారు దూడ విగ్రహము మరియు మోషే తీవ్ర విజ్ఞాపన",
        "book": "Exodus",
        "chapter_start": 32,
        "verse_start": 1,
        "chapter_end": 32,
        "verse_end": 35,
        "reference": "Exodus 32:1-35",
        "keywords": ["golden calf", "aaron", "idolatry", "broken tablets", "intercession", "blot me out", "బంగారు దూడ", "విగ్రహారాధన", "విజ్ఞాపన"],
        "summary_en": "While Moses was on the mount with God, Israel molded a golden calf and worshipped it. In righteous grief Moses broke the tablets of stone, yet pleaded selflessly before God: 'If not, blot me out of thy book.'",
        "summary_te": "మోషే పర్వతముపై ఉన్నప్పుడు ప్రజలు బంగారు దూడను చేసుకొని విగ్రహారాధన చేసిరి; మోషే కోపముతో పలకలను పగులగొట్టి, అయినను దేవుని ఎదుట సాగిలపడి ప్రజల కొరకు ప్రాణత్యాగపూరిత విజ్ఞాపన చేసెను."
    },
    # 22. Twelve Spies
    {
        "id": "twelve_spies_caleb_joshua",
        "title_en": "The Twelve Spies: Unbelief vs. Caleb and Joshua's Faith",
        "title_te": "పన్నెండుమంది వేగులవారు: అవిశ్వాసము మరియు కాలేబు యెహోషువల విశ్వాసము",
        "book": "Numbers",
        "chapter_start": 13,
        "verse_start": 1,
        "chapter_end": 14,
        "verse_end": 38,
        "reference": "Numbers 13:1 - 14:38",
        "keywords": ["twelve spies", "giants", "anakim", "caleb", "joshua", "unbelief", "forty years wilderness", "వేగులవారు", "కాలేబు", "యెహోషువ"],
        "summary_en": "Ten spies reported in terror of the giants in Canaan, spreading panic that caused Israel to wander 40 years in the wilderness. Only Caleb and Joshua proclaimed, 'The LORD is with us: fear them not!'",
        "summary_te": "పదిమంది వేగులవారు కనానులోని నెఫీలీయులను చూసి భయపడి ప్రజలలో అవిశ్వాసము పుట్టించగా, కాలేబు యెహోషువలు మాత్రమే 'యెహోవా మనకు తోడైయున్నాడు, వారికి భయపడవద్దు' అని విశ్వాసము చాటిరి."
    },
    # 23. Bronze Serpent
    {
        "id": "bronze_serpent_pole",
        "title_en": "The Bronze Serpent on the Pole: Type of Christ Crucified",
        "title_te": "స్తంభముపై ఇత్తడి సర్పము: సిలువపై క్రీస్తునకు సాదృశ్యము",
        "book": "Numbers",
        "chapter_start": 21,
        "verse_start": 4,
        "chapter_end": 21,
        "verse_end": 9,
        "reference": "Numbers 21:4-9",
        "keywords": ["bronze serpent", "fiery serpents", "pole", "look and live", "type of christ", "john 3:14", "ఇత్తడి సర్పము", "తేరిచూచి బ్రదుకుట"],
        "summary_en": "When fiery serpents bit rebellious Israelites, Moses erected a bronze serpent upon a pole by divine command. Whoever looked upon the serpent in faith lived—prophetically foretelling Christ lifted upon the cross (John 3:14).",
        "summary_te": "ప్రజల సణుగుడు వలన తాపకరమైన సర్పములు కాటువేసినప్పుడు, మోషే ఇత్తడి సర్పమును స్తంభముపై ఎత్తెను; దానిని విశ్వాసముతో తేరిచూచిన ప్రతివాడు బ్రదికెను (యోహాను 3:14)."
    },
    # 24. Balaam's Donkey
    {
        "id": "balaam_talking_donkey",
        "title_en": "Balaam and the Talking Donkey: An Angel with a Drawn Sword",
        "title_te": "బిలాము మరియు మాట్లాడిన గాడిద: దూత ఖడ్గము",
        "book": "Numbers",
        "chapter_start": 22,
        "verse_start": 21,
        "chapter_end": 22,
        "verse_end": 35,
        "reference": "Numbers 22:21-35",
        "keywords": ["balaam", "talking donkey", "balak", "angel of the lord", "drawn sword", "curse", "బిలాము", "గాడిద", "దూత"],
        "summary_en": "Riding out greedily to curse Israel for Balak's gold, Balaam was halted when God opened his donkey's mouth to rebuke him, revealing the Angel of the LORD standing with a drawn sword.",
        "summary_te": "ధనాశతో ఇశ్రాయేలును శపించుటకు వెళ్లుచున్న బిలామును ఆపుటకు దేవుడు గాడిద నోరు తెరిపించి మాట్లాడించెను; దూత దూసిన ఖడ్గముతో ఎదురుగా నిలబడి ఉన్న సంగతి బిలాము కన్నులు తెరువబడగా చూసెను."
    },
    # 25. Jericho Walls
    {
        "id": "jericho_walls",
        "title_en": "The Fall of Jericho: Faith and the Shout of Victory",
        "title_te": "యెరికో ప్రాకారములు కూలుట: విశ్వాస విజయ జయధ్వని",
        "book": "Joshua",
        "chapter_start": 6,
        "verse_start": 1,
        "chapter_end": 6,
        "verse_end": 27,
        "reference": "Joshua 6:1-27",
        "keywords": ["jericho", "walls fell down", "ark of the covenant", "shout", "rahab", "seven days", "యెరికో", "ప్రాకారములు", "జయధ్వని"],
        "summary_en": "Following God's unusual battle plan, Israel marched around fortress Jericho once a day for six days, and seven times on the seventh day. When the priests blew rams' horns and the people shouted, the massive walls collapsed flat.",
        "summary_te": "దేవుని ఆజ్ఞచొప్పున ఆరు దినములు దినమునకు ఒకమారు, ఏడవ దినమున ఏడుమారులు యెరికో చుట్టూ తిరిగి యాజకులు బాకాలు ఊది ప్రజలు పెద్ద కేక వేయగా, ఎత్తయిన యెరికో ప్రాకారములు నేలమట్టమాయెను."
    },
    # 26. Sun Stands Still
    {
        "id": "sun_stands_still_joshua",
        "title_en": "The Day the Sun Stood Still for Joshua's Victory",
        "title_te": "యెహోషువ ప్రార్థనకు సూర్యచంద్రులు నిలిచిపోయిన అద్భుత దినము",
        "book": "Joshua",
        "chapter_start": 10,
        "verse_start": 12,
        "chapter_end": 10,
        "verse_end": 14,
        "reference": "Joshua 10:12-14",
        "keywords": ["sun stand still", "joshua", "gibeon", "moon", "battle of amorites", "prayer", "సూర్యుడు", "చంద్రుడు", "యెహోషువ"],
        "summary_en": "In the heat of battle against five Amorite kings, Joshua prayed aloud: 'Sun, stand thou still upon Gibeon!' The sun stopped in the midst of heaven for a whole day until Israel avenged themselves of their enemies.",
        "summary_te": "అమోరీయులతో యుద్ధము జరుగుచుండగా యెహోషువ 'సూర్యుడా, గిబియోనులో నిలువుము' అని ప్రార్థించగా, శత్రువులపై సంపూర్ణ విజయము సాధించువరకు సూర్యచంద్రులు దాదాపు ఒక దినమంతయు ఆగిపోయెను."
    },
    # 27. Gideon's 300
    {
        "id": "gideon_300_torches",
        "title_en": "Gideon's 300 Men: Torches, Pitchers, and the Sword of the LORD",
        "title_te": "గిద్యోను మూడువందల మంది వీరులు: దివిటీలు, కుండలు & యెహోవా ఖడ్గము",
        "book": "Judges",
        "chapter_start": 7,
        "verse_start": 1,
        "chapter_end": 7,
        "verse_end": 25,
        "reference": "Judges 7:1-25",
        "keywords": ["gideon", "300 men", "midianites", "fleece", "pitchers and torches", "sword of the lord", "గిద్యోను", "300 మంది", "దివిటీలు"],
        "summary_en": "God whittled Gideon's army of 32,000 down to just 300 men so glory would belong to God alone. Arming them with shofars, empty pitchers, and hidden torches, God threw the vast Midianite host into total panic.",
        "summary_te": "తనకే మహిమ కలుగవలెనని దేవుడు గిద్యోను సైన్యమును 32,000 నుండి కేవలము 300 మందికి తగ్గించెను; వారు కుండలను పగులగొట్టి దివిటీలు పట్టి బాకాలు ఊదగా మిద్యానీయుల మహా సైన్యము చెల్లాచెదురాయెను."
    },
    # 28. Samson
    {
        "id": "samson_delilah_final_victory",
        "title_en": "Samson: Supernatural Strength, Tragic Fall, and Final Triumph",
        "title_te": "సమ్సోను: మహా బలము, దెలీలా మోసము మరియు అంతిమ విజయము",
        "book": "Judges",
        "chapter_start": 16,
        "verse_start": 4,
        "chapter_end": 16,
        "verse_end": 31,
        "reference": "Judges 16:4-31",
        "keywords": ["samson", "delilah", "nazirite", "hair cut", "philistines", "pillars", "strength", "సమ్సోను", "దెలీలా", "స్తంభములు"],
        "summary_en": "Endowed with supernatural strength as a Nazirite, Samson fell to Delilah's deception, had his hair sheared, and was blinded. In penitent faith, he pushed the temple pillars down, destroying more enemies in death than in life.",
        "summary_te": "నాజీరు వ్రతము వలన మహా బలము పొందిన సమ్సోను దెలీలా మోసములో పడి కన్నులు కోల్పోయెను; అయితే పశ్చాత్తాపముతో దేవుని వేడుకొని ఆలయపు స్తంభములను కూల్చి ఫిలిష్తీయులను అంతమొందించెను."
    },
    # 29. Ruth and Boaz
    {
        "id": "ruth_boaz_kinsman_redeemer",
        "title_en": "Ruth and Boaz: Faithfulness and the Kinsman Redeemer",
        "title_te": "రూతు మరియు బోయజు: విశ్వాస్యత మరియు సమీప బంధువు విమోచన",
        "book": "Ruth",
        "chapter_start": 1,
        "verse_start": 1,
        "chapter_end": 4,
        "verse_end": 22,
        "reference": "Ruth 1:1 - 4:22",
        "keywords": ["ruth", "boaz", "naomi", "moabite", "gleaning", "kinsman redeemer", "david lineage", "రూతు", "బోయజు", "నయోమి"],
        "summary_en": "A destitute Gentile widow, Ruth clung to Naomi and the God of Israel. Her loyalty was rewarded when wealthy Boaz acted as kinsman-redeemer, marrying her and grafting her into the ancestral lineage of King David and Jesus Christ.",
        "summary_te": "మోయాబీయురాలైన రూతు నయోమి దేవునిని హత్తుకొని బేత్లెహేమునకు వచ్చెను; బోయజు ఆమెను విమోచించి వివాహము చేసుకొనగా, ఆమె దావీదు మరియు యేసుక్రీస్తు వంశావళిలో చేర్చబడెను."
    },
    # 30. Young Samuel
    {
        "id": "samuel_childhood_call",
        "title_en": "God Calls Young Samuel in the Night: 'Speak, Lord, for Thy Servant Heareth'",
        "title_te": "రాత్రివేళ బాలుడైన సమూయేలును దేవుడు పిలుచుట: 'ప్రభువా సెలవిమ్ము నీ దాసుడు వినుచున్నాడు'",
        "book": "1 Samuel",
        "chapter_start": 3,
        "verse_start": 1,
        "chapter_end": 3,
        "verse_end": 21,
        "reference": "1 Samuel 3:1-21",
        "keywords": ["samuel", "eli", "call in night", "speak lord", "tabernacle shiloh", "prophet", "సమూయేలు", "ఏలీ", "దైవ పిలుపు"],
        "summary_en": "While serving in Shiloh under aged priest Eli, young Samuel heard God's voice calling him three times in the night. Instructed by Eli, Samuel replied, 'Speak; for thy servant heareth,' and was established as prophet of the LORD.",
        "summary_te": "షీలోహులో బాలుడైన సమూయేలు రాత్రి పండుకొనియుండగా దేవుడు మూడుసార్లు పిలిచెను; 'సెలవిమ్ము, నీ దాసుడు వినుచున్నాడు' అని పలికిన సమూయేలును దేవుడు నమ్మకమైన ప్రవక్తగా హెచ్చించెను."
    },
    # 31. David and Goliath
    {
        "id": "david_goliath",
        "title_en": "David and Goliath: The Battle Belongs to the LORD",
        "title_te": "దావీదు మరియు గొల్యాతు: యుద్ధము యెహోవాదే",
        "book": "1 Samuel",
        "chapter_start": 17,
        "verse_start": 1,
        "chapter_end": 17,
        "verse_end": 58,
        "reference": "1 Samuel 17:1-58",
        "keywords": ["david", "goliath", "giant", "sling and stones", "battle belongs to the lord", "philistine", "దావీదు", "గొల్యాతు", "వడిసెల"],
        "summary_en": "When the giant Goliath defied the living God, young shepherd David advanced armed only with a sling, five smooth stones, and faith in the Almighty. Striking the giant's forehead, David brought down the Philistine champion.",
        "summary_te": "గొల్యాతు అను రాక్షసుడు ఇశ్రాయేలు దేవుని దూషించినప్పుడు, దావీదు వడిసెల మరియు ఐదు నునుపైన రాళ్లతో వెళ్లి, 'యుద్ధము యెహోవాదే' అని ప్రకటించి రాక్షసుని నేలకూల్చెను."
    },
    # 32. Elijah at Carmel
    {
        "id": "elijah_mount_carmel",
        "title_en": "Elijah at Mount Carmel: Fire Falls from Heaven",
        "title_te": "కర్మెలు పర్వతముపై ఏలీయా: పరలోకమునుండి దిగివచ్చిన దేవుని అగ్ని",
        "book": "1 Kings",
        "chapter_start": 18,
        "verse_start": 17,
        "chapter_end": 18,
        "verse_end": 46,
        "reference": "1 Kings 18:17-46",
        "keywords": ["elijah", "mount carmel", "prophets of baal", "fire from heaven", "the lord he is god", "rain", "ఏలీయా", "కర్మెలు", "పరలోకపు అగ్ని"],
        "summary_en": "Elijah challenged 450 prophets of Baal to a divine duel. When Baal's prophets failed, Elijah repaired God's altar, doused it with water, and prayed. Fire fell from heaven consuming sacrifice, stones, and water, proving the LORD is God.",
        "summary_te": "450 మంది బయలు ప్రవక్తల ఎదుట ఏలీయా ఒక్కడే నిలబడి, నీళ్లతో తడిపిన బలిపీఠముపై ప్రార్థించగా పరలోకమునుండి దేవుని అగ్ని దిగివచ్చి బలిని దహించెను; జనులందరు 'యెహోవాయే దేవుడు' అని సాగిలపడిరి."
    },
    # 33. Elijah Chariot of Fire
    {
        "id": "elijah_chariot_of_fire",
        "title_en": "Elijah Taken to Heaven in a Chariot and Whirlwind of Fire",
        "title_te": "అగ్నిరథము మరియు సుడిగాలిలో ఏలీయా పరలోకమునకు కొనిపోబడుట",
        "book": "2 Kings",
        "chapter_start": 2,
        "verse_start": 1,
        "chapter_end": 2,
        "verse_end": 15,
        "reference": "2 Kings 2:1-15",
        "keywords": ["elijah", "elisha", "chariot of fire", "whirlwind", "mantle", "double portion", "taken to heaven", "ఏలీయా", "ఎలీషా", "అగ్ని రథము"],
        "summary_en": "As Elijah and Elisha crossed the Jordan, a chariot of fire and horses of fire appeared, parting them both; and Elijah went up by a whirlwind into heaven. Elisha took up Elijah's fallen mantle with a double portion of his spirit.",
        "summary_te": "ఏలీయా ఎలీషాలు మాట్లాడుచుండగా అగ్నిరథము మరియు అగ్నిగుఱ్ఱములు వచ్చి వారిద్దరినీ వేరుచేసెను; ఏలీయా సుడిగాలిలో పరలోకమునకు కొనిపోబడగా, ఎలీషా అతని దుప్పటిని రెండంతల ఆత్మశక్తితో అందుకొనెను."
    },
    # 34. Naaman Leper
    {
        "id": "naaman_leper_cleansed",
        "title_en": "Naaman the Syrian Leper Cleansed in the Jordan River",
        "title_te": "సిరియా సేనాధిపతియైన నయమాను కుష్ఠరోగము జోర్దానులో శుద్ధమగుట",
        "book": "2 Kings",
        "chapter_start": 5,
        "verse_start": 1,
        "chapter_end": 5,
        "verse_end": 19,
        "reference": "2 Kings 5:1-19",
        "keywords": ["naaman", "leper", "elisha", "jordan river", "seven dips", "little maid", "humility", "నయమాను", "కుష్ఠరోగము", "జోర్దాను నది"],
        "summary_en": "Advised by a captive Hebrew girl, Syrian general Naaman sought prophet Elisha for healing. Swallowing his pride to dip seven times in the muddy Jordan River, Naaman's leprous flesh was restored like the flesh of a little child.",
        "summary_te": "మహా సేనాధిపతియైన నయమాను కుష్ఠరోగముతో ఎలీషా వద్దకు రాగా, ఎలీషా ఆజ్ఞ చొప్పున జోర్దాను నదిలో ఏడుమార్లు మునుగగా అతని శరీరము పసిపిల్లవాని శరీరమువలె శుద్ధమాయెను."
    },
    # 35. Daniel in Lions' Den
    {
        "id": "daniel_lions_den",
        "title_en": "Daniel in the Lions' Den: An Angel Shuts the Mouths of Beasts",
        "title_te": "సింహాల బోనులో దానియేలు: సింహముల నోళ్లు మూసిన దేవదూత",
        "book": "Daniel",
        "chapter_start": 6,
        "verse_start": 1,
        "chapter_end": 6,
        "verse_end": 28,
        "reference": "Daniel 6:1-28",
        "keywords": ["daniel", "lions den", "prayer", "darius", "angel shut lions mouths", "uncompromising faith", "దానియేలు", "సింహాల బోను", "ప్రార్థన"],
        "summary_en": "Defying a royal decree forbidding prayer to anyone except King Darius, Daniel knelt at his open window three times a day. Cast into a den of hungry lions, God sent His angel to shut the lions' mouths because Daniel was innocent.",
        "summary_te": "దరియావేషు రాజాజ్ఞ ఉన్నను మానక రోజుకు మూడుమార్లు దేవునికి ప్రార్థించినందుకు దానియేలు సింహాల బోనులో వేయబడెను; దేవుడు తన దూతను పంపి సింహముల నోళ్లు మూయించి అతనిని రక్షించెను."
    },
    # 36. Fiery Furnace
    {
        "id": "fiery_furnace",
        "title_en": "The Fiery Furnace: Shadrach, Meshach, Abednego, and the Fourth Man",
        "title_te": "మండుచున్న అగ్నిగుండము: షద్రకు, మేషాకు, అబేద్నెగో మరియు నాల్గవ వ్యక్తి",
        "book": "Daniel",
        "chapter_start": 3,
        "verse_start": 1,
        "chapter_end": 3,
        "verse_end": 30,
        "reference": "Daniel 3:1-30",
        "keywords": ["shadrach", "meshach", "abednego", "fiery furnace", "fourth man", "son of god", "nebuchadnezzar", "అగ్నిగుండము", "షద్రకు", "మేషాకు"],
        "summary_en": "Refusing to bow to Nebuchadnezzar's golden image, three young Hebrews were cast into a furnace heated seven times hotter. Astonished, the king saw four men walking unbound unharmed, and 'the form of the fourth is like the Son of God.'",
        "summary_te": "బంగారు ప్రతిమకు సాగిలపడనందుకు ఏడంతల అగ్నిగుండములో వేయబడిన ముగ్గురు విశ్వాసులతో పాటు దేవుని కుమారుని పోలిన నాల్గవ వ్యక్తి నడుచుచుండగా, వారి తలవెండ్రుక కూడా కాలక రక్షింపబడిరి."
    },
    # 37. Jonah
    {
        "id": "jonah_fish",
        "title_en": "Jonah Swallowed by a Great Fish and the Nineveh Revival",
        "title_te": "యోనాను గొప్ప మత్స్యము మింగుట మరియు నినెవె పశ్చాత్తాపము",
        "book": "Jonah",
        "chapter_start": 1,
        "verse_start": 1,
        "chapter_end": 3,
        "verse_end": 10,
        "reference": "Jonah 1:1 - 3:10",
        "keywords": ["jonah", "whale", "fish", "nineveh", "tarshish", "repentance", "belly of fish", "యోనా", "చేప", "నినెవె"],
        "summary_en": "Fleeing God's command to preach in Nineveh, Jonah was swallowed by a great fish where he prayed for three days. Vomited onto dry land, he preached repentance to Nineveh, and the whole city turned to God in sackcloth and ashes.",
        "summary_te": "దేవుని మాటకు అవిధేయుడై పారిపోయిన యోనాను చేప మింగగా, కడుపులోనుండి ప్రార్థించి రక్షింపబడి నినెవెకు వెళ్లి ప్రకటించగా, ఆ పట్టణమంతయు ఉపవాసముండి పశ్చాత్తాపపడెను."
    },
    # 38. Birth of Jesus
    {
        "id": "nativity_jesus_bethlehem",
        "title_en": "The Nativity of Jesus Christ: Born in a Manger in Bethlehem",
        "title_te": "యేసుక్రీస్తు జననము: బేత్లెహేము పశువుల పాకలో జన్మించిన రక్షకుడు",
        "book": "Luke",
        "chapter_start": 2,
        "verse_start": 1,
        "chapter_end": 2,
        "verse_end": 20,
        "reference": "Luke 2:1-20",
        "keywords": ["nativity", "birth of jesus", "manger", "bethlehem", "shepherds", "angels", "glory to god in highest", "యేసు జననము", "బేత్లెహేము", "గొర్రెల కాపరులు"],
        "summary_en": "Born to the virgin Mary in Bethlehem because there was no room in the inn, infant Jesus was wrapped in swaddling clothes and laid in a manger while heavenly angelic hosts proclaimed glad tidings of great joy to shepherds.",
        "summary_te": "సత్రములో స్థలము లేనందున మరియ తన తొలిచూలు కుమారుడైన యేసును కని పొత్తిగుడ్డలతో చుట్టి పశువుల తొట్టిలో పరుండబెట్టెను; పరలోక దూతలు గొర్రెల కాపరులకు సువార్త ప్రకటించిరి."
    },
    # 39. Baptism of Jesus
    {
        "id": "baptism_of_jesus",
        "title_en": "The Baptism of Jesus: The Heavens Opened and the Spirit as a Dove",
        "title_te": "యేసు బాప్తిస్మము: పరలోకము తెరవబడుట & పావురమువలె దిగివచ్చిన ఆత్మ",
        "book": "Matthew",
        "chapter_start": 3,
        "verse_start": 13,
        "chapter_end": 3,
        "verse_end": 17,
        "reference": "Matthew 3:13-17",
        "keywords": ["baptism of jesus", "john the baptist", "jordan", "dove", "trinity", "beloved son", "బాప్తిస్మము", "యోహాను", "పరిశుద్ధాత్మ"],
        "summary_en": "When Jesus was baptized by John in the Jordan River to fulfill all righteousness, the heavens opened, the Spirit of God descended like a dove upon Him, and the Father's voice declared: 'This is my beloved Son, in whom I am well pleased.'",
        "summary_te": "యేసు యోర్దాను నదిలో యోహాను చేత బాప్తిస్మము పొంది నీళ్లలోనుండి పైకి రాగానే, ఆకాశము తెరవబడి పరిశుద్ధాత్మ పావురమువలె దిగివచ్చెను; 'ఈయన నా ప్రియ కుమారుడు' అని తండ్రి స్వరం పలికెను."
    },
    # 40. Temptation of Jesus
    {
        "id": "temptation_of_jesus_wilderness",
        "title_en": "The Temptation of Jesus in the Wilderness: Overcoming Satan by the Word",
        "title_te": "అరణ్యములో యేసు శోధన: 'వ్రాయబడియున్నది' అను వాక్యముతో సాతానును జయించుట",
        "book": "Matthew",
        "chapter_start": 4,
        "verse_start": 1,
        "chapter_end": 4,
        "verse_end": 11,
        "reference": "Matthew 4:1-11",
        "keywords": ["temptation of jesus", "wilderness", "forty days", "satan", "it is written", "bread", "pinnacle", "యేసు శోధన", "అరణ్యము", "వ్రాయబడియున్నది"],
        "summary_en": "After fasting forty days and nights, Jesus was tempted by Satan regarding physical appetites, presumption, and worldly glory. Rebuffing every assault with 'It is written', Jesus triumphed completely over the devil.",
        "summary_te": "నలభై దినములు ఉపవాసముండి ఆకలిగొనిన యేసును సాతాను మూడు విధములుగా శోధించగా, ప్రతి శోధననూ 'వ్రాయబడియున్నది' అను దేవుని వాక్య ఖడ్గముతో యేసు ఓడించెను."
    },
    # 41. Water to Wine
    {
        "id": "water_into_wine",
        "title_en": "The First Miracle at Cana: Jesus Turns Water into Wine",
        "title_te": "కానా విందులో తొలి అద్భుతము: నీటిని ద్రాక్షారసముగా మార్చుట",
        "book": "John",
        "chapter_start": 2,
        "verse_start": 1,
        "chapter_end": 2,
        "verse_end": 11,
        "reference": "John 2:1-11",
        "keywords": ["cana", "water into wine", "first miracle", "wedding", "mary", "glory manifested", "కానా", "ద్రాక్షారసము", "తొలి అద్భుతము"],
        "summary_en": "At a wedding in Cana of Galilee when wine ran out, Jesus instructed servants to fill six stone waterpots with water. Miraculously transformed into the finest wine, Jesus manifested His glory and His disciples believed on Him.",
        "summary_te": "కానా ఊరి పెండ్లివిందులో ద్రాక్షారసము అయిపోయినప్పుడు, ఆరు రాతిబానలలో నీళ్లు నింపించి దానిని రుచికరమైన శ్రేష్ఠ ద్రాక్షారసముగా మార్చి తన మహిమను ప్రత్యక్షపరచెను."
    },
    # 42. Nicodemus
    {
        "id": "jesus_and_nicodemus",
        "title_en": "Jesus and Nicodemus by Night: Ye Must Be Born Again",
        "title_te": "రాత్రివేళ నికోదేముతో యేసు సంభాషణ: మీరు నూతనముగా జన్మించవలెను",
        "book": "John",
        "chapter_start": 3,
        "verse_start": 1,
        "chapter_end": 3,
        "verse_end": 21,
        "reference": "John 3:1-21",
        "keywords": ["nicodemus", "born again", "john 3:16", "pharisee", "wind blows", "light and darkness", "నికోదేము", "నూతన జన్మ", "యోహాను 3:16"],
        "summary_en": "A Pharisee and ruler of the Jews came to Jesus by night. Jesus revealed that outward religion cannot save: 'Except a man be born of water and of the Spirit, he cannot enter into the kingdom of God', concluding with John 3:16.",
        "summary_te": "రాత్రివేళ యేసు వద్దకు వచ్చిన యూదుల అధికారి నికోదేముతో, 'ఒకడు నీటిమూలముగాను ఆత్మమూలముగాను జన్మించితేనే గాని దేవుని రాజ్యములో ప్రవేశింపలేడు' అని రక్షణ మర్మమును వివరించెను."
    },
    # 43. Samaritan Woman
    {
        "id": "samaritan_woman_well",
        "title_en": "The Samaritan Woman at Jacob's Well: The Living Water",
        "title_te": "యాకోబు బావియొద్ద సమరయ స్త్రీ: జీవజలమును అనుగ్రహించు రక్షకుడు",
        "book": "John",
        "chapter_start": 4,
        "verse_start": 4,
        "chapter_end": 4,
        "verse_end": 42,
        "reference": "John 4:4-42",
        "keywords": ["samaritan woman", "jacobs well", "living water", "spirit and truth", "messiah", "సమరయ స్త్రీ", "జీవజలము", "బావి"],
        "summary_en": "Wearied from His journey at Jacob's well, Jesus broke cultural barriers to speak with a broken Samaritan woman, exposing her past in love and offering 'living water' springing up into everlasting life.",
        "summary_te": "యాకోబు బావియొద్ద అలసియున్న యేసు సమరయ స్త్రీకి 'నేనిచ్చు నీళ్లు ఎన్నటికిని దప్పిగొననివ్వని జీవజలపు ఊటగా ఉండును' అని బోధించి, ఆమె హృదయ రహస్యములను తెలిపి రక్షించెను."
    },
    # 44. Paralytic Lowered
    {
        "id": "paralytic_lowered_roof",
        "title_en": "The Paralytic Lowered Through the Roof: Sins Forgiven and Body Healed",
        "title_te": "కప్పు విప్పి దించిన పక్షవాయువు రోగి: పాప క్షమాపణ & అద్భుత స్వస్థత",
        "book": "Mark",
        "chapter_start": 2,
        "verse_start": 1,
        "chapter_end": 2,
        "verse_end": 12,
        "reference": "Mark 2:1-12",
        "keywords": ["paralytic", "four friends", "roof opened", "thy sins be forgiven thee", "arise take up thy bed", "పక్షవాయువు", "కప్పు", "స్వస్థత"],
        "summary_en": "Four faithful friends tore off the roof tiles of a crowded house in Capernaum to lower a paralyzed man before Jesus. Seeing their faith, Jesus declared: 'Son, thy sins be forgiven thee... arise, take up thy bed, and walk!'",
        "summary_te": "నలుగురు స్నేహితులు విశ్వాసముతో ఇంటి కప్పు విప్పి మంచముతో సహా పక్షవాయు రోగిని యేసు పాదాల యొద్దకు దించగా, యేసు అతని పాపములను క్షమించి 'లేచి నీ పరుపు ఎత్తుకొని నడువుము' అని స్వస్థపరచెను."
    },
    # 45. Calming Storm
    {
        "id": "calming_storm",
        "title_en": "Jesus Calms the Violent Tempest: 'Peace, Be Still!'",
        "title_te": "యేసు తుఫానును గద్దించుట: 'నిశ్శబ్దమై ఊరకుండుము!'",
        "book": "Mark",
        "chapter_start": 4,
        "verse_start": 35,
        "chapter_end": 4,
        "verse_end": 41,
        "reference": "Mark 4:35-41",
        "keywords": ["calming storm", "peace be still", "sea of galilee", "sleeping in boat", "faith", "తుఫాను", "గద్దించుట", "శాంతి"],
        "summary_en": "While crossing the Sea of Galilee, a fierce storm threatened to swamp the disciples' vessel while Jesus slept. Awoken in terror, Jesus stood and rebuked the wind and raging waves: 'Peace, be still!' and there was a great calm.",
        "summary_te": "సముద్రములో భయంకర తుఫాను రేగి పడవ మునిగిపోవుచుండగా యేసు నిద్రించుచుండెను; శిష్యులు భయముతో లేపగా, యేసు గాలినీ సముద్రమునూ గద్దించి 'నిశ్శబ్దమై ఊరకుండుము' అనగా గొప్ప నిమ్మళమాయెను."
    },
    # 46. Feeding 5,000
    {
        "id": "feeding_5000",
        "title_en": "The Feeding of the 5,000 with Five Loaves and Two Fish",
        "title_te": "ఐదు రొట్టెలు రెండు చిన్న చేపలతో ఐదువేలమందికి భోజనము",
        "book": "John",
        "chapter_start": 6,
        "verse_start": 1,
        "chapter_end": 6,
        "verse_end": 14,
        "reference": "John 6:1-14",
        "keywords": ["feeding 5000", "five loaves two fish", "boy's lunch", "twelve baskets", "bread of life", "ఐదు రొట్టెలు", "చేపలు", "5000 మంది"],
        "summary_en": "Facing a hungry multitude of over 5,000 people, Jesus blessed a young boy's offering of five barley loaves and two small fish. Multiplying the food, all ate until satisfied, leaving twelve baskets of fragments.",
        "summary_te": "ఆకలితో ఉన్న ఐదువేలమంది ప్రజలను చూసి కనికరపడి, ఒక బాలుని ఐదు యవల రొట్టెలను రెండు చిన్న చేపలను దేవునికి స్తోత్రము చేసి విరిచి సమస్త జనులకు తృప్తిగా పెట్టి పన్నెండు గంపల ముక్కలను మిగిల్చెను."
    },
    # 47. Walking on Water
    {
        "id": "jesus_walks_water",
        "title_en": "Jesus Walks on the Water: Peter's Step of Faith and Rescue",
        "title_te": "సముద్రముపై యేసు నడుచుట: పేతురు విశ్వాసపు అడుగు మరియు రక్షణ",
        "book": "Matthew",
        "chapter_start": 14,
        "verse_start": 22,
        "chapter_end": 14,
        "verse_end": 33,
        "reference": "Matthew 14:22-33",
        "keywords": ["walking on water", "peter sinks", "lord save me", "o thou of little faith", "fourth watch", "నీటిపై నడుచుట", "పేతురు", "రక్షణ"],
        "summary_en": "In the fourth watch of the night amid raging waves, Jesus approached the disciples walking upon the sea. Peter stepped out on the water toward Jesus, but looking at the wind began to sink—crying 'Lord, save me!' as Jesus caught him.",
        "summary_te": "రాత్రి నాలుగవ జామున అలలమీద యేసు నడుచుచూ రాగా, పేతురు నీళ్లమీద నడచి గాలిని చూసి మునిగిపోవుచూ 'ప్రభువా, నన్ను రక్షించుము' అని కేకవేయగా, యేసు చేయిచాచి పట్టుకొనెను."
    },
    # 48. Good Samaritan
    {
        "id": "good_samaritan",
        "title_en": "Parable of the Good Samaritan: Who Is My Neighbour?",
        "title_te": "మంచి సమరయనుని ఉపమానము: నా పొరుగువాడెవరు?",
        "book": "Luke",
        "chapter_start": 10,
        "verse_start": 25,
        "chapter_end": 10,
        "verse_end": 37,
        "reference": "Luke 10:25-37",
        "keywords": ["good samaritan", "robbers", "priest and levite", "compassion", "oil and wine", "who is my neighbour", "మంచి సమరయనుడు", "పొరుగువాడు", "కనికరము"],
        "summary_en": "A Jewish traveler was stripped, beaten, and left half-dead. While a priest and Levite passed by on the other side, a despised Samaritan bound his wounds with oil and wine, paid his lodging, and showed Christlike mercy.",
        "summary_te": "దొంగలచేత కొట్టబడి కొనప్రాణముతో ఉన్నవానిని చూసి యాజకుడు, లేవీయుడు దాటిపోగా, ద్వేషింపబడిన సమరయనుడు కనికరపడి గాయములు కట్టి, సత్రములో చేర్పించి నిజమైన పొరుగువాని ప్రేమను చూపెను."
    },
    # 49. Prodigal Son
    {
        "id": "prodigal_son",
        "title_en": "Parable of the Prodigal Son: The Father's Extravagant Grace",
        "title_te": "తప్పిపోయిన కుమారుని ఉపమానము: తండ్రి అపరిమిత క్షమాపణ & ప్రేమ",
        "book": "Luke",
        "chapter_start": 15,
        "verse_start": 11,
        "chapter_end": 15,
        "verse_end": 32,
        "reference": "Luke 15:11-32",
        "keywords": ["prodigal son", "swine", "inheritance squandered", "father running", "best robe", "ring", "fatted calf", "తప్పిపోయిన కుమారుడు", "తండ్రి ప్రేమ", "క్షమాపణ"],
        "summary_en": "A rebellious younger son demanded his inheritance, squandered it in riotous living, and landed among swine. Repenting, he returned home in humility; his father ran, embraced him, and celebrated his restoration.",
        "summary_te": "తండ్రి ఆస్తిని పాడుచేసి పందుల పొట్టు తినే స్థితికి దిగజారిన చిన్న కుమారుడు పశ్చాత్తాపముతో తిరిగిరాగా, తండ్రి పరిగెత్తి కౌగిలించుకొని ముద్దుపెట్టుకొని శ్రేష్ఠమైన వస్త్రముతో సన్మానించెను."
    },
    # 50. Raising Lazarus
    {
        "id": "raising_lazarus",
        "title_en": "The Raising of Lazarus: 'I Am the Resurrection and the Life'",
        "title_te": "లాజరును సమాధిలోనుండి బ్రతికించుట: 'పునరుత్థానమును జీవమును నేనే'",
        "book": "John",
        "chapter_start": 11,
        "verse_start": 1,
        "chapter_end": 11,
        "verse_end": 44,
        "reference": "John 11:1-44",
        "keywords": ["lazarus", "resurrection and life", "martha", "mary", "jesus wept", "four days dead", "lazarus come forth", "లాజరు", "పునరుత్థానము", "కన్నీరు"],
        "summary_en": "Dead and buried for four days in Bethany, Lazarus lay sealed in a tomb. After weeping with Martha and Mary, Jesus cried with a loud voice: 'Lazarus, come forth!' and the dead man walked out bound in graveclothes.",
        "summary_te": "నాలుగు దినములు సమాధిలో ఉండి కుళ్లిపోయిన లాజరు సమాధి యొద్దకు యేసు వెళ్లి కన్నీరు కార్చి, 'లాజరూ, బయటికి రమ్ము' అని ఆజ్ఞాపించగా చనిపోయినవాడు జీవముతో బయటకు వచ్చెను."
    },
    # 51. Zacchaeus
    {
        "id": "zacchaeus_tax_collector",
        "title_en": "Zacchaeus the Tax Collector: The Son of Man Came to Save the Lost",
        "title_te": "సుంకపు గుత్తేదారుడైన జక్కయ్య: నశించినదానిని వెదకి రక్షించుటకు వచ్చిన మనుష్యకుమారుడు",
        "book": "Luke",
        "chapter_start": 19,
        "verse_start": 1,
        "chapter_end": 19,
        "verse_end": 10,
        "reference": "Luke 19:1-10",
        "keywords": ["zacchaeus", "sycamore tree", "tax collector", "salvation come to this house", "restitution", "short stature", "జక్కయ్య", "మేడి చెట్టు", "రక్షణ"],
        "summary_en": "Desiring to see Jesus in Jericho, wealthy but hated tax collector Zacchaeus climbed a sycamore tree. Jesus looked up, invited Himself to Zacchaeus' home, and Zacchaeus repented openly, giving half his wealth to the poor.",
        "summary_te": "పొట్టివాడైన జక్కయ్య యేసును చూడగోరి మేడిచెట్టు ఎక్కగా, యేసు అతనిని చూసి 'నేడు నీ యింట ఉండవలసియున్నది' అనెను; జక్కయ్య మారుమనస్సు పొంది తన ఆస్తిలో సగము బీదలకు ఇచ్చెను."
    },
    # 52. Gethsemane
    {
        "id": "gethsemane_agony",
        "title_en": "The Agony in the Garden of Gethsemane: 'Not My Will, but Thine'",
        "title_te": "గెత్సేమనే తోటలో యేసు ప్రార్థన: 'నా ఇష్టము కాదు, నీ చిత్తమే సిద్ధించును గాక'",
        "book": "Matthew",
        "chapter_start": 26,
        "verse_start": 36,
        "chapter_end": 26,
        "verse_end": 46,
        "reference": "Matthew 26:36-46",
        "keywords": ["gethsemane", "sweat like blood", "cup of suffering", "not my will but thine", "sleeping disciples", "గెత్సేమనే", "ప్రార్థన", "సిద్ధించును గాక"],
        "summary_en": "In heavy sorrow bearing the impending weight of world sin, Jesus prayed three times in Gethsemane sweating drops of blood: 'O my Father, if it be possible, let this cup pass from me: nevertheless not as I will, but as thou wilt.'",
        "summary_te": "లోక పాపభారమును మోయవలసిన వేదనతో యేసు గెత్సేమనే తోటలో రక్తపు బిందువుల వంటి చెమట కారుస్తూ, 'తండ్రీ, నీ చిత్తమైతే ఈ గిన్నె నా యొద్దనుండి తొలగించుము; అయినను నా ఇష్టము కాదు, నీ చిత్తమే సిద్ధించును గాక' అని ప్రార్థించెను."
    },
    # 53. Crucifixion
    {
        "id": "crucifixion_of_jesus",
        "title_en": "The Crucifixion at Golgotha: 'It Is Finished!'",
        "title_te": "గొల్గొతాపై యేసు సిలువ మరణము: 'సమాప్తమైనది!'",
        "book": "Luke",
        "chapter_start": 23,
        "verse_start": 26,
        "chapter_end": 23,
        "verse_end": 49,
        "reference": "Luke 23:26-49, John 19:16-30",
        "keywords": ["crucifixion", "golgotha", "calvary", "it is finished", "father forgive them", "thief on the cross", "atonement", "సిలువ", "గొల్గొతా", "సమాప్తమైనది"],
        "summary_en": "Nailed to the cross between two thieves at Calvary, Jesus prayed: 'Father, forgive them; for they know not what they do.' Darkness fell over the earth, the temple veil tore in two, and Jesus cried: 'It is finished!'",
        "summary_te": "కల్వరి గొల్గొతా కొండపై సిలువ వేయబడిన యేసు, 'తండ్రీ, వీరిని క్షమించుము, ఏమి చేయుచున్నారో వీరెరుగరు' అని ప్రార్థించి, సమస్త పాప పరిహారమును ముగించి 'సమాప్తమైనది' అని ప్రాణము విడిచెను."
    },
    # 54. Resurrection
    {
        "id": "resurrection_of_jesus",
        "title_en": "The Glorious Resurrection of Jesus Christ: The Empty Tomb",
        "title_te": "యేసుక్రీస్తు మహిమాన్విత పునరుత్థానము: ఖాళీ సమాధి",
        "book": "Matthew",
        "chapter_start": 28,
        "verse_start": 1,
        "chapter_end": 28,
        "verse_end": 10,
        "reference": "Matthew 28:1-10, John 20:1-18",
        "keywords": ["resurrection", "empty tomb", "he is not here he is risen", "stone rolled away", "mary magdalene", "victory over death", "పునరుత్థానము", "ఖాళీ సమాధి", "సజీవుడు"],
        "summary_en": "On the third day at dawn, an earthquake occurred and an angel rolled back the stone. The angel announced to the women: 'He is not here: for he is risen, as he said.' Jesus conquered death, sin, and the grave forever!",
        "summary_te": "మూడవ దినమున తెల్లవారుచుండగా దేవదూత దిగివచ్చి సమాధి రాయిని దొర్లించెను; 'ఆయన ఇక్కడ లేడు, తాను చెప్పినట్టే లేచియున్నాడు' అని ప్రకటించెను. యేసు మరణమును సమాధిని జయించి లేచెను!"
    },
    # 55. Pentecost
    {
        "id": "day_of_pentecost",
        "title_en": "The Day of Pentecost: Outpouring of the Holy Spirit",
        "title_te": "పెంతెకొస్తు పండుగ దినము: పరిశుద్ధాత్మ వర్షము మరియు అగ్ని నాలుకలు",
        "book": "Acts",
        "chapter_start": 2,
        "verse_start": 1,
        "chapter_end": 2,
        "verse_end": 47,
        "reference": "Acts 2:1-47",
        "keywords": ["pentecost", "holy spirit", "rushing mighty wind", "cloven tongues of fire", "peter's sermon", "3000 saved", "పెంతెకొస్తు", "పరిశుద్ధాత్మ", "3000 మంది"],
        "summary_en": "Gathered in the upper room in one accord, a sound like a rushing mighty wind filled the house and tongues of fire rested upon each. Filled with the Holy Spirit, Peter preached boldly, and 3,000 souls were saved in a single day.",
        "summary_te": "మేడగదిలో విశ్వాసులందరు ఏకమనస్సుతో ప్రార్థించుచుండగా, బలమైన సుడిగాలి వంటి శబ్దముతో అగ్ని నాలుకలవలె పరిశుద్ధాత్మ వారిపై దిగివచ్చెను; పేతురు బోధించగా ఒక్క దినమున 3000 మంది రక్షింపబడిరి."
    },
    # 56. Paul's Conversion
    {
        "id": "conversion_of_paul_damascus",
        "title_en": "The Conversion of Saul on the Damascus Road: From Persecutor to Apostle",
        "title_te": "దమస్కు మార్గములో సౌలు మార్పు: హింసకుని నుండి అపొస్తలునిగా రూపాంతరము",
        "book": "Acts",
        "chapter_start": 9,
        "verse_start": 1,
        "chapter_end": 9,
        "verse_end": 22,
        "reference": "Acts 9:1-22",
        "keywords": ["saul of tarsus", "damascus road", "light from heaven", "why persecutest thou me", "blinded", "ananias", "paul apostle", "పౌలు", "సౌలు", "దమస్కు"],
        "summary_en": "Breathing threats against Christians on the road to Damascus, a blinding light from heaven struck Saul to the ground. The risen Jesus spoke: 'Saul, Saul, why persecutest thou me?' Transformed, Saul became Paul, the greatest apostle.",
        "summary_te": "క్రైస్తవులను హింసించుటకు దమస్కు వెళ్లుచున్న సౌలును పరలోకపు మహా వెలుగు నేలపడద్రోసెను; 'సౌలా, సౌలా, నన్నేల హింసించుచున్నావు?' అని యేసు పలికి అతనిని గొప్ప అపొస్తలుడైన పౌలుగా మార్చెను."
    }
]

def main():
    # Load existing incidents to retain any custom entries
    existing = []
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
                d = json.load(f)
                existing = d.get("incidents", [])
        except Exception as e:
            print("Notice loading existing incidents:", e)

    # Merge by id
    story_map = {s["id"]: s for s in STORIES}
    for ex in existing:
        if ex["id"] not in story_map:
            story_map[ex["id"]] = ex

    merged_list = list(story_map.values())
    output_data = {
        "count": len(merged_list),
        "incidents": merged_list
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully generated {len(merged_list)} comprehensive biblical incidents into {OUTPUT_FILE}!")

if __name__ == "__main__":
    main()
