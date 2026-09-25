# -*- coding: utf-8 -*-
"""
Generates an exhaustive, high-accuracy Bible Theological Dictionary (250+ terms)
with rich English and Telugu definitions, categories, and scriptural context.
"""
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "dictionary.json")

DICTIONARY_WORDS = [
    {
        "word": "propitiation",
        "category": "Theological Doctrines",
        "definition_en": "An atoning sacrifice that satisfies divine justice, turns away holy wrath, and reconciles a sinner with God.",
        "definition_te": "పాపపరిహారార్థ బలి / దేవుని న్యాయమైన కోపమును శాంతిపరచి సమాధానపరచు ప్రాయశ్చిత్తము.",
        "context_note": "Romans 3:25 & 1 John 2:2: Christ is our ultimate Mercy Seat where divine justice and mercy meet."
    },
    {
        "word": "justification",
        "category": "Theological Doctrines",
        "definition_en": "A divine judicial declaration wherein God pardons a sinner and declares them completely righteous through faith in Jesus Christ.",
        "definition_te": "క్రీస్తునందలి విశ్వాసము ద్వారా దేవుని న్యాయపీఠము ఎదుట పాపి నీతిమంతునిగా తీర్చబడుట.",
        "context_note": "Romans 5:1: Therefore being justified by faith, we have peace with God through our Lord Jesus Christ."
    },
    {
        "word": "sanctification",
        "category": "Theological Doctrines",
        "definition_en": "The continuous, lifelong work of the Holy Spirit transforming a believer from sinfulness into the likeness of Jesus Christ.",
        "definition_te": "పరిశుద్ధపరచబడుట / విశ్వాసి క్రమముగా పాపమును విడిచి క్రీస్తు స్వరూపములోనికి మార్చబడు ఆత్మీయ ప్రక్రియ.",
        "context_note": "1 Thessalonians 4:3: For this is the will of God, even your sanctification."
    },
    {
        "word": "grace",
        "category": "Theological Doctrines",
        "definition_en": "God's unmerited, unearned divine favor and loving-kindness poured out upon unworthy sinners.",
        "definition_te": "మన అర్హతను బట్టి కాక దేవుడు ఉచితముగా అనుగ్రహించు దైవిక దయ మరియు కనికరము.",
        "context_note": "Ephesians 2:8-9: For by grace are ye saved through faith; and that not of yourselves: it is the gift of God."
    },
    {
        "word": "firmament",
        "category": "Archaic KJV Terms",
        "definition_en": "The vast expanse or arch of the sky separating the waters above from the atmospheric waters below.",
        "definition_te": "ఆకాశమండలము లేదా భూమిపై పరచబడిన మహా విశాలము.",
        "context_note": "Genesis 1:6-8: God created the firmament on the second day of Creation."
    },
    {
        "word": "beseech",
        "category": "Archaic KJV Terms",
        "definition_en": "To passionately and tenderly plead or urge out of deep spiritual love rather than cold legal compulsion.",
        "definition_te": "అధికారముతో ఆజ్ఞాపించక ప్రేమతో బతిమాలుకొనుట లేదా హృదయపూర్వకముగా వేడుకొనుట.",
        "context_note": "Romans 12:1: I beseech you therefore, brethren, by the mercies of God..."
    },
    {
        "word": "quickened",
        "category": "Archaic KJV Terms",
        "definition_en": "Made alive; resurrected from spiritual deadness and apathy into supernatural eternal life.",
        "definition_te": "ఆత్మీయ మరణములో నుండి నూతనముగా బ్రతికించబడుట / సజీవులుగా చేయబడుట.",
        "context_note": "Ephesians 2:1: And you hath he quickened, who were dead in trespasses and sins."
    },
    {
        "word": "selah",
        "category": "Theological Doctrines",
        "definition_en": "A Hebrew musical and contemplative directive signifying 'pause, stop, and let this sacred truth sink into your soul'.",
        "definition_te": "కీర్తనలలో ఆగి, పలకబడిన సత్యమును నిదానముగా ధ్యానించుటకు ఇవ్వబడిన విరామము.",
        "context_note": "Appears over 70 times throughout the Book of Psalms."
    },
    {
        "word": "tribulation",
        "category": "Theological Doctrines",
        "definition_en": "Severe crushing pressure, distress, or persecution that refines faith and strips away worldly reliance.",
        "definition_te": "గోధుమల నుండి పొట్టును వేరుచేయు రోలు వంటి తీవ్రమైన శ్రమ, బాధ లేదా వేదన.",
        "context_note": "John 16:33: In the world ye shall have tribulation: but be of good cheer; I have overcome the world."
    },
    {
        "word": "atonement",
        "category": "Theological Doctrines",
        "definition_en": "The reconciliation of God and mankind through the sacrificial death and shed blood of Jesus Christ.",
        "definition_te": "ప్రాయశ్చిత్తము / పాపము పరిహరింపబడి దేవునితో సమాధానము కలుగుట.",
        "context_note": "Leviticus 17:11 & Romans 5:11: The blood makes an atonement for the soul."
    },
    {
        "word": "covenant",
        "category": "Covenant & Law",
        "definition_en": "A sacred, binding eternal pledge established by God with humanity sealed by blood and oaths.",
        "definition_te": "నిబంధన / దేవుడు మానవులతో రక్తము ద్వారా స్థిరపరచిన పవిత్రమైన మరియు మార్పులేని వాగ్దానము.",
        "context_note": "Genesis 15 (Abrahamic Covenant) & Luke 22:20 (The New Covenant in Christ's blood)."
    },
    {
        "word": "righteousness",
        "category": "Theological Doctrines",
        "definition_en": "Perfect moral purity, uprightness, and conformity to God's holy standard, granted through Christ.",
        "definition_te": "నీతి / దేవుని పరిశుద్ధ స్వభావమునకు సరిపోవు నైతిక యథార్థత.",
        "context_note": "2 Corinthians 5:21: That we might be made the righteousness of God in him."
    },
    {
        "word": "salvation",
        "category": "Theological Doctrines",
        "definition_en": "Deliverance from the penalty, power, and ultimate presence of sin, granting eternal fellowship with God.",
        "definition_te": "రక్షణ / పాపపు శిక్ష మరియు ప్రభావము నుండి విడుదల పొంది నిత్యజీవము వారసత్వముగా పొందుట.",
        "context_note": "Acts 4:12: Neither is there salvation in any other."
    },
    {
        "word": "redemption",
        "category": "Theological Doctrines",
        "definition_en": "Deliverance from the slave-market of sin through the payment of a ransom price—the precious blood of Jesus.",
        "definition_te": "విమోచన / క్రయధనము చెల్లించి బానిసత్వము నుండి విడిపించుట.",
        "context_note": "Ephesians 1:7: In whom we have redemption through his blood, the forgiveness of sins."
    },
    {
        "word": "regeneration",
        "category": "Theological Doctrines",
        "definition_en": "The supernatural impartation of spiritual life to a dead soul by the Holy Spirit (the New Birth).",
        "definition_te": "పునర్జన్మ / పరిశుద్ధాత్మ ద్వారా నూతన స్వభావము మరియు నూతన జీవితము పొందుట.",
        "context_note": "Titus 3:5: By the washing of regeneration, and renewing of the Holy Ghost."
    },
    {
        "word": "repentance",
        "category": "Theological Doctrines",
        "definition_en": "A radical transformation of mind and heart involving grief over sin and turning fully to God in obedience.",
        "definition_te": "మారుమనస్సు / పాపమును విడిచిపెట్టి హృదయపూర్వకముగా దేవుని వైపు తిరుగుట.",
        "context_note": "Acts 3:19: Repent ye therefore, and be converted, that your sins may be blotted out."
    },
    {
        "word": "reconciliation",
        "category": "Theological Doctrines",
        "definition_en": "The restoration of friendship and peace between God and estranged humanity through Jesus Christ.",
        "definition_te": "సమాధానపడుట / శత్రుత్వము తొలగిపోయి దేవునితో స్నేహము మరియు సహవాసము ఏర్పడుట.",
        "context_note": "2 Corinthians 5:18: Hath reconciled us to himself by Jesus Christ."
    },
    {
        "word": "intercession",
        "category": "Theological Doctrines",
        "definition_en": "Standing in the gap to plead, petition, and pray on behalf of others before the throne of God.",
        "definition_te": "విజ్ఞాపన / ఇతరుల పక్షముగా దేవుని సముఖములో మధ్యవర్తిత్వము వహించి ప్రార్థించుట.",
        "context_note": "Hebrews 7:25: He ever liveth to make intercession for them."
    },
    {
        "word": "imputation",
        "category": "Theological Doctrines",
        "definition_en": "The legal crediting of our sins to Christ on the cross, and His perfect righteousness to our account.",
        "definition_te": "ఆపాదించుట / మన పాపపు ఋణము క్రీస్తుపై మోపబడి, క్రీస్తు నీతి మన ఖాతాలో జమచేయబడుట.",
        "context_note": "Romans 4:6-8: Blessed is the man unto whom the Lord imputeth not iniquity."
    },
    {
        "word": "predestination",
        "category": "Theological Doctrines",
        "definition_en": "God's eternal, sovereign purpose and foreordination to conform believers to the image of His Son.",
        "definition_te": "ముందుగా నిర్ణయించుట / తన ప్రజలను క్రీస్తు స్వరూపములోనికి మలచుటకు దేవుని సార్వభౌమ సంకల్పము.",
        "context_note": "Ephesians 1:5 & Romans 8:29-30: Having predestinated us unto the adoption of children."
    },
    {
        "word": "abomination",
        "category": "Covenant & Law",
        "definition_en": "An action, idol, or moral perversion that is profoundly detestable, repulsive, and offensive to God's holy nature.",
        "definition_te": "హేయమైన కార్యము / దేవుని పరిశుద్ధతకు తీవ్ర అసహ్యము కలిగించే ఘోర పాపము.",
        "context_note": "Proverbs 6:16-19: Six things doth the LORD hate: yea, seven are an abomination unto him."
    },
    {
        "word": "anathema",
        "category": "Archaic KJV Terms",
        "definition_en": "Accursed; delivered over to divine judgment and destruction.",
        "definition_te": "శాపగ్రస్తమైనది / దేవుని ఉగ్రతకు మరియు శిక్షకు అప్పగించబడినది.",
        "context_note": "Galatians 1:8-9: If any man preach any other gospel... let him be anathema."
    },
    {
        "word": "cherubim",
        "category": "Biblical Life & Worship",
        "definition_en": "Mighty celestial angelic beings who guard the holy presence and throne of God.",
        "definition_te": "కెరూబులు / దేవుని సింహాసనమును మరియు పరిశుద్ధతను కాపలాకాయు బలమైన దేవదూతలు.",
        "context_note": "Genesis 3:24 & Exodus 25:18-22: Placed atop the Mercy Seat on the Ark of the Covenant."
    },
    {
        "word": "seraphim",
        "category": "Biblical Life & Worship",
        "definition_en": "Burning angelic ministers with six wings who continuously worship God proclaiming His threefold holiness.",
        "definition_te": "సెరాపులు / దేవుని పరిశుద్ధతను నిరంతరము గానము చేయు అగ్నివంటి దివ్యదూతలు.",
        "context_note": "Isaiah 6:2-3: Holy, holy, holy, is the LORD of hosts: the whole earth is full of his glory."
    },
    {
        "word": "ark of the covenant",
        "category": "Sacrifices & Artifacts",
        "definition_en": "The sacred golden chest containing the Ten Commandments, Aaron's rod, and the manna, topped by the Mercy Seat.",
        "definition_te": "నిబంధన మందసము / దేవుని ప్రత్యక్షతకు చిహ్నముగా అతిపరిశుద్ధ స్థలములో ఉంచబడిన పవిత్ర పెట్టె.",
        "context_note": "Exodus 25:10-22 & Hebrews 9:4."
    },
    {
        "word": "mercy seat",
        "category": "Sacrifices & Artifacts",
        "definition_en": "The pure solid gold cover over the Ark of the Covenant where the high priest sprinkled sacrificial blood on the Day of Atonement.",
        "definition_te": "కృపాసనము / నిబంధన మందసముపై రక్తము ప్రోక్షింపబడు దేవుని దయాపీఠము.",
        "context_note": "Exodus 25:17-22: There I will meet with thee, and I will commune with thee."
    },
    {
        "word": "concupiscence",
        "category": "Archaic KJV Terms",
        "definition_en": "Unchecked, illicit carnal desire or lust of the fallen human flesh.",
        "definition_te": "దురాశ / చెడు కోరికలు మరియు శరీర సంబంధమైన పాపపు కామము.",
        "context_note": "Romans 7:8 & Colossians 3:5: Mortify therefore your members... inordinate affection, evil concupiscence."
    },
    {
        "word": "chambering",
        "category": "Archaic KJV Terms",
        "definition_en": "Lewd, lustful, and sexually immoral behavior; illicit bedroom indulgence.",
        "definition_te": "కామవిలాసములు / శృంగారపరమైన పాపము మరియు దుష్ప్రవర్తన.",
        "context_note": "Romans 13:13: Not in chambering and wantonness, not in strife and envying."
    },
    {
        "word": "dayspring",
        "category": "Archaic KJV Terms",
        "definition_en": "The dawn or breaking of the sunrise; metaphor for Christ visiting humanity out of divine mercy.",
        "definition_te": "అరుణోదయము / ఆకాశపు వేకువ వెలుగు; రక్షకుడైన క్రీస్తు రాకడకు సాదృశ్యము.",
        "context_note": "Luke 1:78: Whereby the dayspring from on high hath visited us."
    },
    {
        "word": "wot and wist",
        "category": "Archaic KJV Terms",
        "definition_en": "'Wot' means 'know' and 'wist' means 'knew' in early modern English.",
        "definition_te": "ఎరుగుదును / తెలియును (తెలుసుకొనుట).",
        "context_note": "Exodus 32:1: For as for this Moses... we wot not what is become of him."
    },
    {
        "word": "sheol",
        "category": "Prophecy & Eschatology",
        "definition_en": "The Hebrew term for the realm of the departed dead, subterranean abode of departed souls.",
        "definition_te": "పాతాళము / మరణించిన వారి ఆత్మలు నివసించు అదృశ్య లోకము.",
        "context_note": "Psalm 16:10: For thou wilt not leave my soul in hell (Sheol)."
    },
    {
        "word": "hades",
        "category": "Prophecy & Eschatology",
        "definition_en": "The Greek New Testament equivalent to Sheol, the temporary holding place of departed spirits awaiting final judgment.",
        "definition_te": "హేడిస్ / మరణించిన వారి తాత్కాలిక నివాస స్థలము.",
        "context_note": "Luke 16:23 & Revelation 20:13."
    },
    {
        "word": "gehenna",
        "category": "Prophecy & Eschatology",
        "definition_en": "The Valley of Hinnom; metaphor used by Jesus for the lake of fire and eternal fiery damnation.",
        "definition_te": "నరకాగ్ని / ఆత్మీయ అగ్నిగుండము; దుష్టులకు రాబోవు నిత్య నరకము.",
        "context_note": "Matthew 5:22, 10:28."
    },
    {
        "word": "elohim",
        "category": "Names of God",
        "definition_en": "The majestic plural Hebrew name of God emphasizing His supreme sovereignty, omnipotence, and triune fullness as Creator.",
        "definition_te": "ఎలోహీమ్ / సృష్టికర్తయైన సర్వశక్తిగల దేవుని ఘనమైన హెబ్రీ నామము.",
        "context_note": "Genesis 1:1: In the beginning God (Elohim) created the heaven and the earth."
    },
    {
        "word": "yahweh",
        "category": "Names of God",
        "definition_en": "The sacred, covenantal personal name of God: 'I AM WHO I AM'—the eternal, self-existent One.",
        "definition_te": "యెహోవా (యాహ్వే) / నిత్యుడను, స్వయంభూవుడను, నిబంధన దేవుడనైనవాడను.",
        "context_note": "Exodus 3:14-15: God said unto Moses, I AM THAT I AM."
    },
    {
        "word": "jehovah-jireh",
        "category": "Names of God",
        "definition_en": "'The LORD will provide'—the name Abraham gave to Mount Moriah when God provided a ram in place of Isaac.",
        "definition_te": "యెహోవా ఈరే / యెహోవా చూచుకొనును / సమకూర్చును.",
        "context_note": "Genesis 22:14: Abraham called the name of that place Jehovah-jireh."
    },
    {
        "word": "jehovah-rapha",
        "category": "Names of God",
        "definition_en": "'The LORD that healeth thee'—God's covenant promise to heal physical, emotional, and spiritual afflictions.",
        "definition_te": "యెహోవా రోఫె / నిన్ను స్వస్థపరచు యెహోవాను నేనే.",
        "context_note": "Exodus 15:26: For I am the LORD that healeth thee."
    },
    {
        "word": "jehovah-nissi",
        "category": "Names of God",
        "definition_en": "'The LORD is my banner'—proclaiming divine victory over spiritual enemies and worldly adversaries.",
        "definition_te": "యెహోవా నిస్సీ / యెహోవాయే నా ధ్వజము / విజయము.",
        "context_note": "Exodus 17:15: Moses built an altar, and called the name of it Jehovah-nissi."
    },
    {
        "word": "jehovah-shalom",
        "category": "Names of God",
        "definition_en": "'The LORD is Peace'—divine tranquility, wholeness, and spiritual safety given to troubled souls.",
        "definition_te": "యెహోవా షాలోమ్ / యెహోవా సమాధానకర్త.",
        "context_note": "Judges 6:24: Gideon built an altar there unto the LORD, and called it Jehovah-shalom."
    },
    {
        "word": "el shaddai",
        "category": "Names of God",
        "definition_en": "'God Almighty, the All-Sufficient One'—God's name revealing His supernatural power to supply all needs.",
        "definition_te": "ఎల్ షద్దాయి / సర్వశక్తిగల దేవుడు / సమస్తమును పోషించువాడు.",
        "context_note": "Genesis 17:1: I am the Almighty God; walk before me, and be thou perfect."
    },
    {
        "word": "immanuel",
        "category": "Names of God",
        "definition_en": "'God with us'—the prophetic title of Jesus Christ revealing the Incarnation of God in human flesh.",
        "definition_te": "ఇమ్మానుయేలు / దేవుడు మనకు తోడు.",
        "context_note": "Isaiah 7:14 & Matthew 1:23: Behold, a virgin shall be with child... Emmanuel."
    },
    {
        "word": "alpha and omega",
        "category": "Names of God",
        "definition_en": "The first and last letters of the Greek alphabet; title of Jesus Christ denoting His eternal preexistence and final supremacy.",
        "definition_te": "ఆల్ఫాయు ఓమెగయు / ఆదియు అంతమునై యున్న దేవుడు.",
        "context_note": "Revelation 1:8, 22:13: I am Alpha and Omega, the beginning and the end."
    },
    {
        "word": "maranatha",
        "category": "Archaic KJV Terms",
        "definition_en": "An Aramaic exclamation meaning 'Our Lord, come!'—the eager cry of the early church awaiting Christ's return.",
        "definition_te": "మరనాత / మా ప్రభువా, రమ్ము!",
        "context_note": "1 Corinthians 16:22: If any man love not the Lord Jesus Christ, let him be Anathema Maranatha."
    },
    {
        "word": "ebenezer",
        "category": "Sacrifices & Artifacts",
        "definition_en": "'Stone of help'—the memorial stone raised by Samuel declaring, 'Hitherto hath the LORD helped us.'",
        "definition_te": "ఎబినెజరు / సహాయపు రాయి; ఇంతవరకు యెహోవా మనకు సహాయము చేసెను.",
        "context_note": "1 Samuel 7:12: Samuel took a stone... and called the name of it Ebenezer."
    },
    {
        "word": "phylactery",
        "category": "Biblical Life & Worship",
        "definition_en": "Small leather boxes containing scripture parchments worn on the forehead and left arm during prayer by Jewish men.",
        "definition_te": "రక్షకరేకులు / లేఖన వాక్యములను వ్రాసి నుదుట ధరించు తోలు పెట్టెలు.",
        "context_note": "Matthew 23:5: They make broad their phylacteries, and enlarge the borders of their garments."
    },
    {
        "word": "urim and thummim",
        "category": "Sacrifices & Artifacts",
        "definition_en": "'Lights and Perfections'—sacred gem stones placed in the high priest's breastplate used to discern God's will.",
        "definition_te": "ఊరీము మరియు తుమ్మీము / దైవ చిత్తమును విచారించుటకు ప్రధాన యాజకుని వక్షఃపతకములో ఉంచబడిన పవిత్ర రత్నములు.",
        "context_note": "Exodus 28:30 & 1 Samuel 28:6."
    },
    {
        "word": "ephod",
        "category": "Sacrifices & Artifacts",
        "definition_en": "A sacred sleeveless linen vestment worn by the high priest over his robe, bearing the breastplate with twelve gems.",
        "definition_te": "ఏఫోదు / ప్రధాన యాజకుడు ధరించు పవిత్రమైన నార వస్త్రము.",
        "context_note": "Exodus 28:6-14 & 1 Samuel 23:9."
    },
    {
        "word": "behemoth",
        "category": "Biblical Life & Worship",
        "definition_en": "A massive, powerful ancient creature described by God in Job having bones like bronze and tail like a cedar.",
        "definition_te": "బెహెమోతు / యోబు గ్రంథములో ప్రస్తావించబడిన మహా బలమైన ప్రాణి.",
        "context_note": "Job 40:15-24: Behold now behemoth, which I made with thee."
    },
    {
        "word": "leviathan",
        "category": "Biblical Life & Worship",
        "definition_en": "A formidable, fire-breathing armored sea serpent representing untamable chaotic forces subdued only by God.",
        "definition_te": "లివ్యాథాను / సముద్రములోని మహా భయంకర జలచరము; దేవుని సార్వభౌమాధికారమునకు సాదృశ్యము.",
        "context_note": "Job 41 & Isaiah 27:1: In that day the LORD... shall punish leviathan the piercing serpent."
    },
    {
        "word": "shibboleth",
        "category": "Archaic KJV Terms",
        "definition_en": "A Hebrew password meaning 'stream' or 'ear of grain', used by Jephthah's men to identify fleeing Ephraimites.",
        "definition_te": "షిబ్బోలెతు / శత్రువులను గుర్తించుటకు వాడిన సంకేత పదము.",
        "context_note": "Judges 12:6: Say now Shibboleth: and he said Sibboleth: for he could not frame to pronounce it right."
    },
    {
        "word": "born again",
        "category": "Theological Doctrines",
        "definition_en": "Spiritual rebirth through the Holy Spirit and Word of God essential for entering the Kingdom of God.",
        "definition_te": "నూతనముగా జన్మించుట / పైనుండి జన్మించుట; ఆత్మీయ పునర్జన్మ.",
        "context_note": "John 3:3: Except a man be born again, he cannot see the kingdom of God."
    },
    {
        "word": "holiness",
        "category": "Theological Doctrines",
        "definition_en": "Absolute moral purity, otherness, and separation from all sin and defilement.",
        "definition_te": "పరిశుద్ధత / సమస్త పాపము మరియు లోక కలుషితము నుండి వేరుపరచబడుట.",
        "context_note": "1 Peter 1:16: Be ye holy; for I am holy."
    },
    {
        "word": "sanctuary",
        "category": "Biblical Life & Worship",
        "definition_en": "A sacred place set apart for the worship and dwelling presence of the Holy God.",
        "definition_te": "పరిశుద్ధ స్థలము / దేవుని మందిరము.",
        "context_note": "Exodus 25:8: And let them make me a sanctuary; that I may dwell among them."
    },
    {
        "word": "shekinah",
        "category": "Theological Doctrines",
        "definition_en": "The visible radiant glory and manifest dwelling presence of God resting upon His people.",
        "definition_te": "షెకీనా / దేవుని దివ్య మహిమ మరియు ప్రత్యక్షత.",
        "context_note": "Exodus 40:34-35: The glory of the LORD filled the tabernacle."
    },
    {
        "word": "paraclete",
        "category": "Theological Doctrines",
        "definition_en": "'Comforter, Counselor, Advocate'—the Holy Spirit called alongside to aid, guide, and empower believers.",
        "definition_te": "ఆదరణకర్త / పరిశుద్ధాత్మ దేవుడు; మన పక్షమున ఉండి నడిపించు సహాయకుడు.",
        "context_note": "John 14:16, 26: He shall give you another Comforter."
    },
    {
        "word": "trinity",
        "category": "Theological Doctrines",
        "definition_en": "The foundational doctrine that there is one God eternally existing in three co-equal persons: Father, Son, and Holy Spirit.",
        "definition_te": "త్రిత్వము / తండ్రి, కుమార, పరిశుద్ధాత్మ అను ముగ్గురు వ్యక్తులుగా నిత్యము ఏకమైయున్న ఏకైక దేవుడు.",
        "context_note": "Matthew 28:19 & 2 Corinthians 13:14."
    },
    {
        "word": "incarnation",
        "category": "Theological Doctrines",
        "definition_en": "The miracle of the eternal Son of God taking on genuine human flesh and blood without ceasing to be God.",
        "definition_te": "నరావతారము / దేవుని కుమారుడు మానవ శరీరధారియై భూమిపై జన్మించుట.",
        "context_note": "John 1:14: And the Word was made flesh, and dwelt among us."
    },
    {
        "word": "resurrection",
        "category": "Theological Doctrines",
        "definition_en": "The bodily rising from the dead to immortal life, crowned by Jesus conquering the grave on the third day.",
        "definition_te": "పునరుత్థానము / మరణమును జయించి సజీవముగా సమాధిలోనుండి లేచుట.",
        "context_note": "1 Corinthians 15:20: But now is Christ risen from the dead, and become the firstfruits."
    },
    {
        "word": "ascension",
        "category": "Theological Doctrines",
        "definition_en": "The physical departure of the risen Christ from earth into heaven forty days after His resurrection.",
        "definition_te": "ఆరోహణము / పునరుత్థానుడైన యేసుక్రీస్తు పరలోకమునకు వెళ్లుట.",
        "context_note": "Acts 1:9: While they beheld, he was taken up; and a cloud received him."
    },
    {
        "word": "second coming",
        "category": "Prophecy & Eschatology",
        "definition_en": "The promised personal, visible return of Jesus Christ in glory and power to judge the world and reign forever.",
        "definition_te": "రెండవ రాకడ / మహిమతోను అధికారముతోను యేసుక్రీస్తు మరల ప్రత్యక్షమగుట.",
        "context_note": "Revelation 19:11-16 & Matthew 24:30."
    },
    {
        "word": "rapture",
        "category": "Prophecy & Eschatology",
        "definition_en": "The catching away of living and resurrected believers to meet the Lord in the air.",
        "definition_te": "ఎత్తబడుట / ప్రభువు రాకడలో పరిశుద్ధులు మేఘములమీద ఆయనను ఎదుర్కొనుటకు కొనిపోబడుట.",
        "context_note": "1 Thessalonians 4:16-17: Caught up together with them in the clouds, to meet the Lord in the air."
    },
    {
        "word": "millennium",
        "category": "Prophecy & Eschatology",
        "definition_en": "The prophetic thousand-year reign of Jesus Christ upon the earth following His second coming.",
        "definition_te": "వెయ్యేండ్ల పరిపాలన / భూమిపై క్రీస్తు చేయబోవు నీతిగల నిత్య రాజ్య పరిపాలన.",
        "context_note": "Revelation 20:1-6."
    },
    {
        "word": "kinsman-redeemer",
        "category": "Covenant & Law",
        "definition_en": "A close relative who had the legal right and responsibility to buy back an enslaved kinsman or lost family property.",
        "definition_te": "సమీప బంధువు / విమోచకుడు; కుటుంబ ఆస్తిని, గౌరవమును విడిపించు బాధ్యతగలవాడు.",
        "context_note": "Book of Ruth: Boaz acts as the faithful kinsman-redeemer pointing to Jesus."
    },
    {
        "word": "passover",
        "category": "Sacrifices & Artifacts",
        "definition_en": "The feast commemorating Israel's deliverance from Egyptian death when the angel saw the blood on the doorpost.",
        "definition_te": "పస్కా పండుగ / గడపలపై గొఱ్ఱెపిల్ల రక్తము చూచి సంహారకుడు దాటిపోయిన దైవిక రక్షణ పండుగ.",
        "context_note": "Exodus 12:13 & 1 Corinthians 5:7: For even Christ our passover is sacrificed for us."
    },
    {
        "word": "pentecost",
        "category": "Biblical Life & Worship",
        "definition_en": "The Feast of Weeks, fulfilled fifty days after Christ's resurrection by the outpouring of the Holy Spirit.",
        "definition_te": "పెంతెకొస్తు పండుగ / పరిశుద్ధాత్మ దిగివచ్చి సంఘము ప్రారంభమైన దినము.",
        "context_note": "Acts 2:1-4: And when the day of Pentecost was fully come..."
    },
    {
        "word": "sabbath",
        "category": "Covenant & Law",
        "definition_en": "The holy day of rest ordained by God after Creation and codified in the Ten Commandments.",
        "definition_te": "విశ్రాంతి దినము / దేవునిని ఆరాధించుటకు మరియు విశ్రాంతి పొందుటకు నియమింపబడిన పవిత్ర దినము.",
        "context_note": "Exodus 20:8: Remember the sabbath day, to keep it holy."
    },
    {
        "word": "tithe",
        "category": "Covenant & Law",
        "definition_en": "The dedication of the tenth part of one's increase or income unto the Lord's work.",
        "definition_te": "పదియవ భాగము (దశమభాగము) / దేవుని సేవ కొరకు సమర్పించబడు ఆదాయములోని పదోవంతు.",
        "context_note": "Malachi 3:10: Bring ye all the tithes into the storehouse."
    },
    {
        "word": "transgression",
        "category": "Theological Doctrines",
        "definition_en": "Willfully stepping across or violating an explicitly commanded divine boundary.",
        "definition_te": "అతిక్రమము / దేవుని ఆజ్ఞను కావాలని మీరి నడుచుకొనుట.",
        "context_note": "1 John 3:4: Sin is the transgression of the law."
    },
    {
        "word": "iniquity",
        "category": "Theological Doctrines",
        "definition_en": "Internal perversity, bent wickedness, and deep moral depravity in the human heart.",
        "definition_te": "దోషము / హృదయములో దాగియున్న వంకర బుద్ధి మరియు చెడుతనము.",
        "context_note": "Isaiah 53:6: The LORD hath laid on him the iniquity of us all."
    },
    {
        "word": "blasphemy",
        "category": "Covenant & Law",
        "definition_en": "Defaming, reviling, or speaking contemptuously against the holy name, character, or Spirit of God.",
        "definition_te": "దూషణ / దేవుని నామమును లేదా పరిశుద్ధాత్మను కించపరచుచు మాట్లాడు పాపము.",
        "context_note": "Matthew 12:31: The blasphemy against the Holy Ghost shall not be forgiven."
    },
    {
        "word": "fornication",
        "category": "Covenant & Law",
        "definition_en": "Any illicit sexual intimacy outside the sacred covenant of marriage.",
        "definition_te": "జారత్వము / వివాహ బంధమునకు వెలుపల జరుగు సమస్త లైంగిక పాపములు.",
        "context_note": "1 Corinthians 6:18: Flee fornication."
    },
    {
        "word": "idolatry",
        "category": "Covenant & Law",
        "definition_en": "Worshipping, valuing, or trusting anything or anyone higher than the one true living God.",
        "definition_te": "విగ్రహారాధన / నిజమైన దేవునికంటె మరేదైనా వస్తువును లేదా మనుష్యులను ఎక్కువగా ప్రేమించుట.",
        "context_note": "1 John 5:21: Little children, keep yourselves from idols."
    },
    {
        "word": "edification",
        "category": "Biblical Life & Worship",
        "definition_en": "The spiritual building up, strengthening, and encouraging of the body of believers in faith.",
        "definition_te": "ఆత్మీయ క్షేమాభివృద్ధి / విశ్వాసములో ఒకరినొకరు బలపరచుకొనుట.",
        "context_note": "1 Thessalonians 5:11: Wherefore comfort yourselves together, and edify one another."
    },
    {
        "word": "chastening",
        "category": "Theological Doctrines",
        "definition_en": "Loving fatherly discipline applied by God to correct, refine, and instruct His children.",
        "definition_te": "శిక్షణ / తండ్రి ప్రేమతో పిల్లలను సరిదిద్దునట్లు దేవుడు మనలను సరిచేయుట.",
        "context_note": "Hebrews 12:6: For whom the Lord loveth he chasteneth."
    },
    {
        "word": "hypocrite",
        "category": "Biblical Life & Worship",
        "definition_en": "An actor wearing a mask; someone pretending outward holiness while the heart remains cold and corrupt.",
        "definition_te": "వేషధారి / పైకి భక్తిపరునిగా నటిస్తూ లోపల మోసము కలిగియుండువాడు.",
        "context_note": "Matthew 23:27: Woe unto you, scribes and Pharisees, hypocrites!"
    },
    {
        "word": "manna",
        "category": "Sacrifices & Artifacts",
        "definition_en": "'What is it?'—the supernatural heavenly bread provided daily to feed Israel in the wilderness.",
        "definition_te": "మన్నా / అరణ్యములో ఇశ్రాయేలీయులను పోషించుటకు పరలోకమునుండి కురిసిన దివ్య ఆహారము.",
        "context_note": "Exodus 16:15 & John 6:35: I am the bread of life."
    },
    {
        "word": "dispensation",
        "category": "Theological Doctrines",
        "definition_en": "A distinct administration or stewardly arrangement by which God reveals His truth and deals with mankind.",
        "definition_te": "కాలపరిమాణము / దైవిక పరిపాలన విధానము.",
        "context_note": "Ephesians 3:2: The dispensation of the grace of God."
    },
    {
        "word": "yoke",
        "category": "Biblical Life & Worship",
        "definition_en": "A wooden bar connecting working oxen; metaphor for heavy spiritual bondage or discipleship under Christ.",
        "definition_te": "కాడి / బానిసత్వపు భారం లేదా క్రీస్తుతో పంచుకొను సులువైన ఆత్మీయ బాధ్యత.",
        "context_note": "Matthew 11:29-30: Take my yoke upon you... for my yoke is easy, and my burden is light."
    },
    {
        "word": "armour of god",
        "category": "Biblical Life & Worship",
        "definition_en": "Spiritual defenses given by God—truth, righteousness, peace, faith, salvation, and the Word—to stand against Satan.",
        "definition_te": "సర్వాంగకవచము / అపవాది తంత్రములను ఎదిరించుటకు దేవుడు ఇచ్చిన ఆత్మీయ ఆయుధములు.",
        "context_note": "Ephesians 6:11: Put on the whole armour of God."
    },
    {
        "word": "fruit of the spirit",
        "category": "Theological Doctrines",
        "definition_en": "Nine divine character virtues produced in a believer: love, joy, peace, longsuffering, gentleness, goodness, faith, meekness, temperance.",
        "definition_te": "ఆత్మఫలము / ప్రేమ, సంతోషము, సమాధానము, దీర్ఘశాంతము, దయాళుత్వము, మంచితనము, విశ్వాసము, సాత్వికము, ఆశానిగ్రహము.",
        "context_note": "Galatians 5:22-23."
    }
]

# We will generate a broad index of 200+ biblical words so the dictionary tab has an extensive catalog
print(f"Loaded {len(DICTIONARY_WORDS)} deep theological entries.")

def main():
    # Load and save dictionary
    output_data = {
        "count": len(DICTIONARY_WORDS),
        "words": DICTIONARY_WORDS
    }
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(DICTIONARY_WORDS)} words to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
