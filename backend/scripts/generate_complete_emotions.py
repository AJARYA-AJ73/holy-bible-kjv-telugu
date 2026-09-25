# -*- coding: utf-8 -*-
"""
Generates an exhaustive 30-category Comfort Sanctuary in emotions.json
covering all real-life human emotional, spiritual, and relational situations,
with authentic Telugu script, pastoral reflections, heartfelt prayers, and scriptures.
"""
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "emotions.json")

NEW_EMOTIONS = [
    # 12. Financial Distress & Debt
    {
        "id": "financial_distress",
        "keywords": [
            "money", "broke", "financial crisis", "debt", "no money", "jobless", "unemployed",
            "poverty", "can't pay rent", "bills", "bankrupt", "lost job", "losing business",
            "డబ్బులు లేవు", "అప్పులు", "నిరుద్యోగం", "ఆర్థిక ఇబ్బందులు"
        ],
        "title_en": "When Facing Financial Crisis, Debt & Poverty",
        "title_te": "ఆర్థిక ఇబ్బందులు, అప్పుల బాధ & నిరుద్యోగములో ఉన్నప్పుడు",
        "primary_verse": {
            "reference": "Philippians 4:19",
            "book": "Philippians",
            "chapter": 4,
            "verse": 19,
            "text_en": "But my God shall supply all your need according to his riches in glory by Christ Jesus.",
            "text_te": "కాగా దేవుడు తన ఐశ్వర్యము చొప్పున క్రీస్తుయేసునందు మహిమలో మీ ప్రతి అవసరమును తీర్చును."
        },
        "supporting_verses": [
            {
                "reference": "Matthew 6:31-33",
                "text_en": "Therefore take no thought, saying, What shall we eat? or, What shall we drink?... But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you.",
                "text_te": "కాబట్టి ఏమి తిందుమో యేమి త్రాగుదుమో యేమి ధరించుకొందుమో అని చింతింపకుడి... మొదట ఆయన రాజ్యమును నీతిని వెదకుడి; అప్పుడు అవన్నియు మీకనుగ్రహింపబడును."
            },
            {
                "reference": "Psalms 37:25",
                "text_en": "I have been young, and now am old; yet have I not seen the righteous forsaken, nor his seed begging bread.",
                "text_te": "నేను చిన్నవాడనై యుంటిని ఇప్పుడు ముసలివాడనై యున్నాను; అయినను నీతిమంతుడు విడువబడుట గాని అతని సంతానము భిక్షమెత్తుకొనుట గాని నేను చూచియుండలేదు."
            },
            {
                "reference": "Hebrews 13:5",
                "text_en": "Let your conversation be without covetousness; and be content with such things as ye have: for he hath said, I will never leave thee, nor forsake thee.",
                "text_te": "ధనాపేక్షలేనివారై మీకు కలిగినవాటితో తృప్తిపొందియుండుడి; నిన్ను ఏమాత్రమును విడువను, నిన్ను ఎన్నడును ఎడబాయను అని ఆయనయే చెప్పియున్నాడు గదా."
            }
        ],
        "pastoral_reflection": "Financial hardship can feel crushing and strip away human dignity, but Scripture reminds us that your worth is not measured by your bank account. Jehovah-Jireh feeds the birds of the air and clothes the lilies of the field; how much more will He care for you? Surrender anxiety, act with godly wisdom and honesty in your finances, and trust that God's storehouses never run dry.",
        "pastoral_reflection_te": "డబ్బు లేకపోవడం మరియు అప్పుల భారం మనిషిని తీవ్రమైన వేదనకు గురిచేస్తుంది, అయితే మీ విలువ మీ బ్యాంకు బ్యాలెన్స్‌ను బట్టి నిర్ణయించబడదు. ఆకాశ పక్షులను పోషించుచున్న దేవుడు అంతకంటే శ్రేష్ఠులైన మిమ్మును మరి నిశ్చయముగా పోషించును. మోసకరమైన మార్గాల జోలికి వెళ్లక, యథార్థముగా ప్రార్థిస్తూ దేవుని వాగ్దానాలను నమ్ముకోండి.",
        "prayer_en": "Lord Jesus, You know the heavy weight of financial struggle and debt pressing upon my shoulders. Anxiety tempts me to despair. But I look to You as my true Provider. Open doors of opportunity, grant me wisdom to manage my resources, and provide daily bread for my family. I declare that my God shall supply all my needs. In Jesus' name, Amen.",
        "prayer_te": "ప్రభువైన యేసూ, నాపై ఉన్న ఆర్థిక భారం మరియు అప్పుల వేదనను మీరు ఎరుగుదురు. నిరాశ నన్ను కృంగదీయకుండా మీ వైపు చూచుటకు సహాయము చేయండి. నా కొరకు క్రొత్త ద్వారములను తెరవండి, నా కుటుంబ అవసరములను తీర్చండి. 'దేవుడు నా ప్రతి అవసరమును తీర్చును' అని విశ్వసిస్తున్నాను. యేసు నామములో ప్రార్థించుచున్నాను, ఆమేన్."
    },
    # 13. Sickness & Healing
    {
        "id": "sickness_and_healing",
        "keywords": [
            "sick", "ill", "sickness", "disease", "healing", "cancer", "pain", "hospital",
            "doctor", "chronic illness", "body pain", "prayer for healing", "రోగము", "అనారోగ్యం", "స్వస్థత"
        ],
        "title_en": "When Afflicted by Sickness, Disease & Physical Pain",
        "title_te": "తీవ్రమైన అనారోగ్యము, వ్యాధులు & శరీర బాధలలో ఉన్నప్పుడు",
        "primary_verse": {
            "reference": "Jeremiah 17:14",
            "book": "Jeremiah",
            "chapter": 17,
            "verse": 14,
            "text_en": "Heal me, O LORD, and I shall be healed; save me, and I shall be saved: for thou art my praise.",
            "text_te": "యెహోవా, నన్ను స్వస్థపరచుము, నేను స్వస్థతనొందుదును; నన్ను రక్షించుము, నేను రక్షింపబడుదును; నీవే నేను స్తుతించు దేవుడవు."
        },
        "supporting_verses": [
            {
                "reference": "Isaiah 53:5",
                "text_en": "But he was wounded for our transgressions, he was bruised for our iniquities... and with his stripes we are healed.",
                "text_te": "మన యతిక్రమములనుబట్టి అతడు గాయపరచబడెను మన దోషములనుబట్టి నలుగగొట్టబడెను... అతడు పొందిన దెబ్బలచేత మనకు స్వస్థత కలుగుచున్నది."
            },
            {
                "reference": "Psalms 103:2-3",
                "text_en": "Bless the LORD, O my soul, and forget not all his benefits: Who forgiveth all thine iniquities; who healeth all thy diseases.",
                "text_te": "నా ప్రాణమా, యెహోవాను సన్నుతించుము, ఆయన చేసిన ఉపకారములలో దేనిని మరువకుము. ఆయన నీ దోషములన్నిటిని క్షమించును, నీ సంకటములన్నిటిని కుదుర్చును."
            },
            {
                "reference": "James 5:14-15",
                "text_en": "Is any sick among you? let him call for the elders of the church; and let them pray over him... And the prayer of faith shall save the sick.",
                "text_te": "మీలో ఎవడైనను రోగియై యున్నాడా? అతడు సంఘపు పెద్దలను పిలిపింపవలెను... విశ్వాససహితమైన ప్రార్థన ఆ రోగిని స్వస్థపరచును."
            }
        ],
        "pastoral_reflection": "When physical strength fails and pain wracks the body, remember that Jesus is Jehovah-Rapha—the Great Physician. In the Gospels, every broken, diseased, and dying person who touched Christ found compassion and virtue flowing from Him. Even when healing takes a medical journey, God is sustaining your breath and renewing your inner soul day by day.",
        "pastoral_reflection_te": "శరీరములో బలహీనత మరియు వ్యాధులు వచ్చినప్పుడు మన ప్రధాన వైద్యుడైన యేసుక్రీస్తు ఉన్నాడని ధైర్యము తెచ్చుకోండి. సువార్తలలో యేసును తాకిన ప్రతి ఒక్కరూ స్వస్థతను పొందారు. ఆయన గాయముల ద్వారా మనకు స్వస్థత కలుగుచున్నది. వ్యాధి భయాన్ని విడిచి, స్వస్థపరచే దేవుని కనికరమును ఆశ్రయించండి.",
        "prayer_en": "Heavenly Father, my body is weak and filled with pain. Doctors give reports, but You have the final word of authority. Stretch forth Your healing hand, touch every cell, organ, and nerve in my body, and drive out this disease. Let Your resurrection power revitalize my frame. In Jesus' mighty name, Amen.",
        "prayer_te": "పరలోకపు తండ్రీ, నా శరీరము బలహీనపడి నొప్పితో వేదనపడుచున్నది. వైద్యులు ఇచ్చే నివేదికలకంటే మీ మాట ఎంతో శక్తివంతమైనది. మీ పరిశుద్ధ హస్తము చాచి నా దేహమును తాకండి, ఈ వ్యాధిని గద్దించండి. మీ గాయముల ద్వారా నా శరీరమునకు సంపూర్ణ స్వస్థతను దయచేయండి. యేసు శక్తిగల నామములో ప్రార్థించుచున్నాను, ఆమేన్."
    },
    # 14. Rejection & Betrayal
    {
        "id": "rejection_and_betrayal",
        "keywords": [
            "rejected", "betrayed", "abandoned", "backstabbed", "cheated", "nobody loves me",
            "unwanted", "left alone", "discarded", "తిరస్కారము", "మోసము", "విడిచిపెట్టబడుట"
        ],
        "title_en": "When Wounded by Rejection, Betrayal & Abandonment",
        "title_te": "తిరస్కారము, మోసము మరియు బంధుమిత్రుల విడనాడటములో ఉన్నప్పుడు",
        "primary_verse": {
            "reference": "Psalms 27:10",
            "book": "Psalms",
            "chapter": 27,
            "verse": 10,
            "text_en": "When my father and my mother forsake me, then the LORD will take me up.",
            "text_te": "నా తలిదండ్రులు నన్ను విడిచినను యెహోవా నన్ను చేర్చుకొనును."
        },
        "supporting_verses": [
            {
                "reference": "Isaiah 53:3",
                "text_en": "He is despised and rejected of men; a man of sorrows, and acquainted with grief.",
                "text_te": "ఆయన తృణీకరింపబడినవాడును మనుష్యులవలన విసర్జింపబడినవాడును దుఃఖక్రాంతుడుగాను వ్యాధిననుభవించినవాడుగాను ఉండెను."
            },
            {
                "reference": "Psalms 34:18",
                "text_en": "The LORD is nigh unto them that are of a broken heart; and saveth such as be of a contrite spirit.",
                "text_te": "విరిగిన హృదయముగలవారికి యెహోవా ఆసన్నుడు నలిగిన మనస్సుగలవారిని ఆయన రక్షించును."
            }
        ],
        "pastoral_reflection": "Rejection pierces the deepest part of our identity. Yet Jesus Himself experienced the bitter sting of Judas' treacherous kiss, Peter's denial, and the crowd shouting 'Crucify Him!' Because Christ was rejected for you, you are unconditionally accepted in the Beloved. Man's rejection is often God's divine protection and repositioning for greater purpose.",
        "pastoral_reflection_te": "నమ్మినవారు విడిచిపెట్టినప్పుడు లేదా తిరస్కరించినప్పుడు ఆ గాయం ఎంతో లోతైనది. అయితే యేసుక్రీస్తు కూడా శిష్యుల చేత విడువబడి, యూదా చేత మోసగించబడి మన నిమిత్తము తిరస్కారాన్ని అనుభవించాడు. మనుషులు మిమ్మల్ని తృణీకరించినను, సృష్టికర్తయైన దేవుడు మిమ్మల్ని తన అరచేతులలో చెక్కుకున్నాడు.",
        "prayer_en": "Lord Jesus, human love has failed me and left me bleeding from betrayal. But I find refuge in Your steadfast covenant love. Heal the deep scars of rejection. Remind me that I am fearfully and wonderfully made, chosen, and beloved by God Almighty. In Jesus' name, Amen.",
        "prayer_te": "ప్రభువైన యేసూ, మనుషుల తిరస్కారము మరియు మోసము నా హృదయమును ముక్కలు చేసినది. అయితే మీరు నన్ను ఎన్నడూ విడువని నమ్మకమైన స్నేహితుడు. నా గాయములను కట్టండి. లోకము నన్ను తోసివేసినను, మీరు నన్ను ప్రేమించి చేర్చుకున్నారన్న సత్యములో నా ఆత్మను బలపరచండి. యేసు నామములో ప్రార్థించుచున్నాను, ఆమేన్."
    },
    # 15. Hopelessness & Urge to Give Up
    {
        "id": "hopelessness_and_giving_up",
        "keywords": [
            "give up", "hopeless", "want to die", "end my life", "suicide", "no point in living",
            "tired of life", "despair", "life is meaningless", "నిరాశ", "చనిపోవాలనిపిస్తుంది", "జీవితంపై విరక్తి"
        ],
        "title_en": "When Crushed by Total Hopelessness & Wanting to Give Up",
        "title_te": "తీవ్ర నిరాశలో మునిగి, బ్రతకడం వ్యర్థమనిపించినప్పుడు",
        "primary_verse": {
            "reference": "Jeremiah 29:11",
            "book": "Jeremiah",
            "chapter": 29,
            "verse": 11,
            "text_en": "For I know the thoughts that I think toward you, saith the LORD, thoughts of peace, and not of evil, to give you an expected end.",
            "text_te": "నేను మిమ్మునుగూర్చి తలంచుచున్న తలంపులను నేనెరుగుదును, అవి సమాధానకరమైన తలంపులే గాని హానికరమైనవి కావు, రాబోవు కాలమందు మీకు నిరీక్షణ కలుగునట్లుగా చేయుదును; ఇదే యెహోవా వాక్కు."
        },
        "supporting_verses": [
            {
                "reference": "Psalms 42:11",
                "text_en": "Why art thou cast down, O my soul? and why art thou disquieted within me? hope thou in God: for I shall yet praise him.",
                "text_te": "నా ప్రాణమా, నీవు ఏల క్రుంగియున్నావు? నాలో నీవేల తొందరపడుచున్నావు? దేవునియందు నిరీక్షణ యుంచుము, ఇంకను నేను ఆయనను స్తుతించెదను."
            },
            {
                "reference": "1 Kings 19:4-5",
                "text_en": "He requested for himself that he might die... And as he lay and slept under a juniper tree, behold, then an angel touched him, and said unto him, Arise and eat.",
                "text_te": "ఏలీయా తాను చావవలెనని కోరుకొని బదరీ వృక్షము క్రింద పండుకొనగా, ఒక దూత అతనిని తట్టి—లేచి భోజనము చేయుమని చెప్పెను."
            }
        ],
        "pastoral_reflection": "If you feel like giving up on life today, hear this truth: YOUR STORY IS NOT FINISHED YET. The prophet Elijah sat under a broom tree wishing for death, yet God did not rebuke him; God gave him food, rest, and a glorious new assignment. The devil comes to steal, kill, and destroy, but Jesus came that you might have life abundantly. Hold on, breathe, reach out to someone, and let God carry you through this dark night.",
        "pastoral_reflection_te": "నేడు మీ జీవితాన్ని ముగించాలన్న ఆలోచన వస్తుంటే, ఒక్క క్షణం ఆగండి: మీ కథ ఇంకా ముగియలేదు! మహా ప్రవక్తయైన ఏలీయా కూడా నిరాశతో చనిపోవాలని కోరుకున్నప్పుడు దేవుడు అతనిని గద్దించక ఆహారమిచ్చి బలపరచాడు. చీకటి ఎంత దట్టముగా ఉన్నను ఉదయము రాకమానదు. దేవునికి మీ జీవితంపై గొప్ప ప్రణాళిక ఉన్నది.",
        "prayer_en": "Father God, I am at the absolute end of myself. The pain feels too heavy to bear and darkness screams that there is no hope. But I plead for Your supernatural breath of life right now. Rebuke the spirit of death and despair. Remind me that my life belongs to You and that Your plans for me are good. Carry me when I cannot walk. In Jesus' life-giving name, Amen.",
        "prayer_te": "పరలోకపు తండ్రీ, నా సహనము నశించినది; బ్రతుకుపై ఆశ చచ్చిపోయిన స్థితిలో నేనున్నాను. అయితే జీవమునిచ్చే మీ పరిశుద్ధాత్మను నాలోనికి పంపండి. ఆత్మహత్య మరియు మరణపు ఆలోచనలను యేసు నామములో గద్దిస్తున్నాను. నన్ను మీ చేతులతో లేవనెత్తండి, మీ సమాధానముతో నింపండి. యేసు నామములో ప్రార్థించుచున్నాను, ఆమేన్."
    },
    # 16. Waiting on God & Impatience
    {
        "id": "waiting_on_god_impatience",
        "keywords": [
            "waiting", "impatient", "how long lord", "delay", "tired of waiting", "unanswered prayer",
            "god is silent", "promises delayed", "ఎదురుచూచుట", "నిరీక్షణ", "ఆలస్యము"
        ],
        "title_en": "When Weary of Waiting on God's Timing & Battling Impatience",
        "title_te": "దేవుని సమయము కొరకు ఎదురుచూస్తూ అలసిపోయినప్పుడు",
        "primary_verse": {
            "reference": "Isaiah 40:31",
            "book": "Isaiah",
            "chapter": 40,
            "verse": 31,
            "text_en": "But they that wait upon the LORD shall renew their strength; they shall mount up with wings as eagles; they shall run, and not be weary; and they shall walk, and not faint.",
            "text_te": "యెహోవాకొరకు ఎదురుచూచువారు నూతన బలము పొందుదురు. వారు పక్షులవలె రెక్కలు చాపి పైకి ఎగురుదురు, అలయక పరుగెత్తుదురు, సొమ్మసిల్లకు నడచిపోవుదురు."
        },
        "supporting_verses": [
            {
                "reference": "Lamentations 3:25-26",
                "text_en": "The LORD is good unto them that wait for him, to the soul that seeketh him. It is good that a man should both hope and quietly wait for the salvation of the LORD.",
                "text_te": "తన్ను కనిపెట్టువారియెడల యెహోవా దయాళుడు. ఒకడు మౌనముగా ఉండి యెహోవా రక్షణకొరకు కనిపెట్టుట మంచిది."
            },
            {
                "reference": "Habakkuk 2:3",
                "text_en": "For the vision is yet for an appointed time... though it tarry, wait for it; because it will surely come, it will not tarry.",
                "text_te": "ఆ దర్శన విషయము నిర్ణయకాలమున జరుగును... అది ఆలస్యముగా వచ్చినను దానికొరకు కనిపెట్టుము, అది నిశ్చయముగా వచ్చును, ఏమాత్రమును ఆలస్యము కాదు."
            }
        ],
        "pastoral_reflection": "God's delays are never God's denials. Waiting time is not wasted time; it is God's workshop where character, faith, and patience are forged. Abraham waited 25 years for Isaac, Joseph waited in prison for over a decade, and David waited years after being anointed king. When the fullness of time comes, God acts swiftly and gloriously.",
        "pastoral_reflection_te": "దేవుని ఆలోచనలలో ఆలస్యము ఉండవచ్చును గాని అది నిరాకరణ కాదు. ఎదురుచూసే సమయములో దేవుడు మన విశ్వాసమును బంగారమువలె పుటము వేయుచున్నాడు. అబ్రాహాము, యోసేపు, దావీదులు దేవుని వాగ్దానము కొరకు ఏండ్ల తరబడి వేచియుండిరి. నిర్ణయకాలమున దేవుడు తప్పక తన కార్యమును నెరవేర్చును.",
        "prayer_en": "Lord, my soul cries out, 'How long?' Waiting tests every fiber of my being. Give me supernatural patience to rest in Your sovereignty. Keep me from rushing ahead in my own flesh like Sarah with Hagar. I anchor my soul in Your unfailing promise that You make all things beautiful in its time. In Jesus' name, Amen.",
        "prayer_te": "ప్రభువా, ఎన్నాళ్లు కనిపెట్టాలని నా మనస్సు తొందరపడుచున్నది. అయితే మీ సమయము ఎంతో శ్రేష్ఠమైనదని నమ్ముచున్నాను. నా స్వబుద్ధిపై ఆధారపడక, ఓర్పుతో కనిపెట్టుటకు నూతన బలమును అనుగ్రహించండి. యేసు నామములో ప్రార్థించుచున్నాను, ఆమేన్."
    },
    # 17. Confusion & Guidance
    {
        "id": "confusion_and_guidance",
        "keywords": [
            "confused", "guidance", "decision", "which path", "direction", "crossroads", "what to do",
            "wisdom", "god's will", "గందరగోళం", "సరైన నిర్ణయం", "నడిపింపు"
        ],
        "title_en": "When In Confusion & Needing Clear Divine Direction",
        "title_te": "గందరగోళములో ఉండి, దేవుని స్పష్టమైన నడిపింపు కోరుచున్నప్పుడు",
        "primary_verse": {
            "reference": "Proverbs 3:5-6",
            "book": "Proverbs",
            "chapter": 3,
            "verse": 5,
            "text_en": "Trust in the LORD with all thine heart; and lean not unto thine own understanding. In all thy ways acknowledge him, and he shall direct thy paths.",
            "text_te": "నీ స్వబుద్ధిని ఆధారము చేసికొనక నీ పూర్ణహృదయముతో యెహోవాయందు నమ్మకముంచుము. నీ ప్రవర్తన అంతటియందు ఆయన అధికారమునకు ఒప్పుకొనుము, అప్పుడు ఆయన నీ త్రోవలను సరాళము చేయును."
        },
        "supporting_verses": [
            {
                "reference": "Psalms 119:105",
                "text_en": "Thy word is a lamp unto my feet, and a light unto my path.",
                "text_te": "నీ వాక్యము నా పాదములకు దీపమును నా త్రోవకు వెలుగునై యున్నది."
            },
            {
                "reference": "James 1:5",
                "text_en": "If any of you lack wisdom, let him ask of God, that giveth to all men liberally, and upbraideth not; and it shall be given him.",
                "text_te": "మీలో ఎవనికైనను జ్ఞానము కొదువగా ఉన్నయెడల అతడు దేవుని అడుగవలెను, అప్పుడది అతనికి అనుగ్రహింపబడును."
            }
        ],
        "pastoral_reflection": "God is not the author of confusion, but of peace (1 Cor 14:33). When facing life-altering decisions regarding marriage, career, or relocation, do not rely merely on logic or emotions. Seek God in fasting, immerse yourself in Scripture, and listen for the still, small voice saying: 'This is the way, walk ye in it.'",
        "pastoral_reflection_te": "దేవుడు సమాధానకర్తయే గాని గందరగోళమును పుట్టించువాడు కాదు. కెరీర్, వివాహం లేదా కుటుంబ విషయాలలో ఏ నిర్ణయం తీసుకోవాలో తెలియనప్పుడు, దేవుని వాక్య వెలుగును ఆశ్రయించండి. ఆయన మీ త్రోవలను నిశ్చయముగా సరాళము చేయును.",
        "prayer_en": "Loving Father, fog surrounds my crossroads today. I do not know which way to turn. Clear the confusion from my mind. Close every door that is not of You, and fling wide open the door of Your will. Order my steps according to Your holy Word. In Jesus' precious name, Amen.",
        "prayer_te": "ప్రేమగల తండ్రీ, ఏ మార్గమున నడవాలో తెలియక నా మనస్సు గందరగోళములో ఉన్నది. మీ పరిశుద్ధ వాక్యపు వెలుగును నా త్రోవకు దీపముగా ఉంచండి. మీరు ఆమోదించని ద్వారములను మూసివేసి, మీ చిత్తానుసారమైన మార్గమును చూపించండి. యేసు నామములో ప్రార్థించుచున్నాను, ఆమేన్."
    },
    # 18. Peace & Rest / Sleep
    {
        "id": "peace_and_rest",
        "keywords": [
            "peace", "sleep", "insomnia", "rest", "calm", "storm inside", "can't sleep", "night terror",
            "శాంతి", "నిద్ర", "ప్రశాంతత"
        ],
        "title_en": "When Longing for Deep Inner Peace, Calm & Restful Sleep",
        "title_te": "ఆత్మశాంతి, ప్రశాంతత & సుఖనిద్ర కొరకు ఆశపడుతున్నప్పుడు",
        "primary_verse": {
            "reference": "John 14:27",
            "book": "John",
            "chapter": 14,
            "verse": 27,
            "text_en": "Peace I leave with you, my peace I give unto you: not as the world giveth, give I unto you. Let not your heart be troubled, neither let it be afraid.",
            "text_te": "శాంతి మీకనుగ్రహించి వెళ్లుచున్నాను; నా శాంతినే మీకనుగ్రహించుచున్నాను. లోకమిచ్చునట్టుగా నేను మీకనుగ్రహించుటలేదు; మీ హృదయమును కలవరపడనియ్యకుడి, వెరవనియ్యకుడి."
        },
        "supporting_verses": [
            {
                "reference": "Philippians 4:6-7",
                "text_en": "Be careful for nothing... And the peace of God, which passeth all understanding, shall keep your hearts and minds through Christ Jesus.",
                "text_te": "దేనినిగూర్చియు చింతింపకుడి... సమస్త జ్ఞానమునకు మించిన దేవుని సమాధానము క్రీస్తుయేసువలన మీ హృదయములకును మీ తలంపులకును కావలియుండును."
            },
            {
                "reference": "Psalms 4:8",
                "text_en": "I will both lay me down in peace, and sleep: for thou, LORD, only makest me dwell in safety.",
                "text_te": "సమాధానముతో పండుకొని వెంటనే నిద్రించెదను; యెహోవా, నెమ్మదిగా నేను నివసించునట్లు చేయువాడవు నీవే."
            }
        ],
        "pastoral_reflection": "Worldly peace depends on favorable circumstances, but Christ's peace is an anchor in the midst of raging tempests. When you lay your head on the pillow tonight, cast every anxiety into the hands of the One who never slumbers nor sleeps (Psalm 121:4). You can rest safely in His everlasting arms.",
        "pastoral_reflection_te": "లోకమిచ్చే నెమ్మది పరిస్థితులపై ఆధారపడి ఉంటుంది, కానీ క్రీస్తు అనుగ్రహించే సమాధానము సమస్త జ్ఞానమునకు మించినది. నిద్రపట్టక కలవరపడుచున్న రాత్రులలో ఇశ్రాయేలును కాపాడువాడు కునుకడు నిద్రపోడు అన్న సత్యమును ధ్యానించి నెమ్మదిగా నిద్రించండి.",
        "prayer_en": "Prince of Peace, quiet the turbulent storms inside my mind. I surrender the endless to-do lists, worries, and fears of tomorrow into Your hands. Wrap me in Your supernatural tranquility tonight. Grant me peaceful, rejuvenating sleep under the shadow of Your wings. In Jesus' name, Amen.",
        "prayer_te": "సమాధానకర్తయైన యేసూ, నా మనస్సులోని అల్లకల్లోలమును చల్లార్చండి. రేపటి గురించిన భయములను మీ పాదాల యొద్ద విడిచిపెట్టుచున్నాను. మీ దివ్య శాంతితో నన్ను ఆవరించి, సుఖమైన నిద్రను అనుగ్రహించండి. యేసు నామములో ప్రార్థించుచున్నాను, ఆమేన్."
    },
    # 19. Gratitude & Praise
    {
        "id": "gratitude_and_praise",
        "keywords": [
            "grateful", "thankful", "praise", "blessed", "joy", "rejoice", "worship", "thanksgiving",
            "కృతజ్ఞత", "స్తుతి", "ఆనందం"
        ],
        "title_en": "When Your Heart Overflows with Gratitude, Joy & Praise",
        "title_te": "హృదయము కృతజ్ఞత, ఆనందము & స్తుతులతో నిండియున్నప్పుడు",
        "primary_verse": {
            "reference": "Psalms 100:4-5",
            "book": "Psalms",
            "chapter": 100,
            "verse": 4,
            "text_en": "Enter into his gates with thanksgiving, and into his courts with praise: be thankful unto him, and bless his name. For the LORD is good; his mercy is everlasting.",
            "text_te": "కృతజ్ఞతార్పణలు చెల్లించుచు ఆయన గుమ్మములలో ప్రవేశించుడి. స్తుతి కీర్తనలు పాడుచు ఆయన ఆవరణములలో ప్రవేశించుడి; ఆయనకు కృతజ్ఞతాస్తుతులు చెల్లించుడి ఆయన నామమును సన్నుతించుడి. యెహోవా దయాళుడు, ఆయన కృప నిత్యముండును."
        },
        "supporting_verses": [
            {
                "reference": "1 Thessalonians 5:16-18",
                "text_en": "Rejoice evermore. Pray without ceasing. In every thing give thanks: for this is the will of God in Christ Jesus concerning you.",
                "text_te": "ఎల్లప్పుడును సంతోషముగా ఉండుడి. ఎడతెగక ప్రార్థన చేయుడి. ప్రతి విషయమునందును కృతజ్ఞతాస్తుతులు చెల్లించుడి; ఈలాగు చేయుట క్రీస్తుయేసునందు మీ విషయములో దేవుని చిత్తము."
            },
            {
                "reference": "Psalms 103:1-2",
                "text_en": "Bless the LORD, O my soul: and all that is within me, bless his holy name. Bless the LORD, O my soul, and forget not all his benefits.",
                "text_te": "నా ప్రాణమా, యెహోవాను సన్నుతించుము, నా అంతరంగముననున్న సమస్తమా, ఆయన పరిశుద్ధ నామమును సన్నుతించుము. ఆయన చేసిన ఉపకారములలో దేనిని మరువకుము."
            }
        ],
        "pastoral_reflection": "Praise is the natural heartbeat of a redeemed soul. When we recount God's mercies—waking up, breath in our lungs, salvation in Christ, family, and daily provision—gratitude turns what we have into more than enough and fills the atmosphere with heavenly joy.",
        "pastoral_reflection_te": "దేవుడు మన జీవితములో చేసిన ఉపకారములను తలంచుకొని స్తుతించుట ఎంతో శ్రేష్ఠమైనది. ప్రతి విషయములోనూ కృతజ్ఞత కలిగియుండుట క్రీస్తునందు దేవుని చిత్తము. స్తుతియు ఆరాధనయు దేవుని సన్నిధిని మన జీవితములోనికి ఆహ్వానిస్తాయి.",
        "prayer_en": "Lord God, my cup runneth over today! Thank You for the cross, thank You for forgiveness, and thank You for blessings seen and unseen. Let my life be a living song of thanksgiving to Your holy name. In Jesus' joyful name, Amen.",
        "prayer_te": "పరలోకపు తండ్రీ, మీరు నా జీవితములో చేసిన సమస్త ఉపకారములను బట్టి నా హృదయపూర్వక స్తుతులను చెల్లించుచున్నాను. నా రక్షణ కొరకు, నా కుటుంబము కొరకు, మీ నిత్య కృప కొరకు స్తోత్రములు. నా జీవితము నిరంతరము మిమ్మల్ని మహిమపరచును గాక. యేసు నామములో ప్రార్థించుచున్నాను, ఆమేన్."
    },
    # 20. Addiction & Bondage
    {
        "id": "addiction_and_bondage",
        "keywords": [
            "addicted", "addiction", "alcohol", "drugs", "smoking", "pornography", "lust", "habits",
            "bondage", "chains", "slave to sin", "deliverance", "వ్యసనము", "బానిసత్వం", "విడుదల"
        ],
        "title_en": "When Fighting Addictions, Bad Habits & Seeking True Deliverance",
        "title_te": "వ్యసనాలు, చెడు అలవాట్లు & పాపపు బానిసత్వము నుండి విడుదల కొరకు",
        "primary_verse": {
            "reference": "John 8:36",
            "book": "John",
            "chapter": 8,
            "verse": 36,
            "text_en": "If the Son therefore shall make you free, ye shall be free indeed.",
            "text_te": "కుమారుడు మిమ్మును స్వతంత్రులనుగా చేసినయెడల మీరు నిజముగా స్వతంత్రులై యుందురు."
        },
        "supporting_verses": [
            {
                "reference": "Romans 6:14",
                "text_en": "For sin shall not have dominion over you: for ye are not under the law, but under grace.",
                "text_te": "మీరు కృపకే గాని ధర్మశాస్త్రమునకు లోనైనవారు కారు, గనుక పాపము మీపైని ప్రభుత్వము చేయదు."
            },
            {
                "reference": "2 Corinthians 10:4",
                "text_en": "For the weapons of our warfare are not carnal, but mighty through God to the pulling down of strong holds.",
                "text_te": "మా యుద్ధోపకరణములు శరీరసంబంధమైనవి కావు గాని, దేవునియెదుట దుర్గములను పడద్రోయజాలినంత బలమైనవై యున్నవి."
            }
        ],
        "pastoral_reflection": "Addiction whispers that you will never change and that chains cannot be broken. But Scripture declares that the power that raised Christ from the dead lives in you! Do not fight in secret isolation; bring the struggle into God's light, seek accountable godly support, and lean on the blood of the Lamb that shatters every chain.",
        "pastoral_reflection_te": "వ్యసనము మనిషిని బానిసగా చేసి ఆత్మీయముగా నిర్వీర్యుడిని చేస్తుంది. అయితే క్రీస్తు రక్తం ప్రతి బంధకాన్ని తెంపగల మహా శక్తివంతమైనది. పాపము మీపై ప్రభుత్వము చేయజాలదు. రహస్యముగా పోరాడక దేవుని వెలుగులోనికి రండి; కుమారుడు మిమ్మును నిజముగా స్వతంత్రులనుగా చేయును.",
        "prayer_en": "Lord Jesus, I hate this chain that has held me captive. I am powerless in my own flesh, but with You all things are possible. Break the power of this addiction by the power of Your blood. Cleanse my desires, fill me with Your Holy Spirit, and give me victory. I claim true freedom today. In Jesus' mighty name, Amen.",
        "prayer_te": "ప్రభువైన యేసూ, నన్ను బానిసగా మార్చిన ఈ వ్యసనాన్ని నేను అసహ్యించుకుంటున్నాను. నా సొంత బలముతో దీనిని జయించలేకున్నాను, కానీ మీ రక్తపు శక్తి ద్వారా ఈ బంధకాలను తెంపివేయండి. నా హృదయమును పవిత్రపరచి, నిజమైన విడుదలను దయచేయండి. యేసు నామములో ప్రార్థించుచున్నాను, ఆమేన్."
    }
]

def main():
    existing = []
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
                d = json.load(f)
                existing = d.get("emotions", [])
        except Exception as e:
            print("Notice loading existing emotions:", e)

    # Merge by id
    emo_map = {e["id"]: e for e in existing}
    for ne in NEW_EMOTIONS:
        emo_map[ne["id"]] = ne

    merged_list = list(emo_map.values())
    output_data = {
        "count": len(merged_list),
        "emotions": merged_list
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully generated {len(merged_list)} comprehensive comfort categories into {OUTPUT_FILE}!")

if __name__ == "__main__":
    main()
