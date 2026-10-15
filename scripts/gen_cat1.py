# Category 1: Home & Daily Life (6), Family & Relatives (5), Travel & Transport (5) = 16 topics
import os
import sys
sys.path.append(os.path.dirname(__file__))
from helper import item, export_ts_module

w1 = {}
w2 = {}

# 1. breakfast-chat
w1["breakfast-chat"] = [
    item(
        "Warm toast", "گرم ٹوسٹ", "Garam toast", "गर्म टोस्ट", "Garm toast",
        "خبز دافئ", "Khubz dafi'", "Tostada caliente", "Tohs-TAH-dah kah-LYEHN-teh",
        "Pain chaud", "Pan sho", "Warmer Toast", "VAHR-mer toast",
        "Pane caldo", "PAH-neh KAHL-doh", "Torrada quente", "Toh-RAH-dah KEHN-chee",
        "Тёплый тост", "TYOHP-lyy tost", "Sıcak tost", "Suh-dzhak tost",
        "Roti hangat", "Roh-tee hahng-aht", "热 吐司", "Rè tǔsī",
        "温かい トースト", "Atatakai tōsuto", "따뜻한 토스트", "Ttatteut-han toseuteu"
    ),
    item(
        "Cold milk", "ٹھنڈا دودھ", "Thanda doodh", "ठंडा दूध", "Thanda doodh",
        "حليب بارد", "Halib barid", "Leche fría", "LEH-cheh FREE-ah",
        "Lait froid", "Leh fwah", "Kalte Milch", "KAHL-teh milkh",
        "Latte freddo", "LAHT-teh FREHD-doh", "Leite frio", "LAY-chee FREE-oo",
        "Холодное молоко", "Khah-LAHD-nah-yeh mah-lah-KOH", "Soğuk süt", "Soh-ook sewt",
        "Susu dingin", "Soo-soo deeng-een", "冷 牛奶", "Lěng niúnǎi",
        "冷たい ミルク", "Tsumetai miruku", "차가운 우유", "Chaga-un uyu"
    ),
    item(
        "Fresh juice", "تازہ جوس", "Taaza juice", "ताज़ा जूस", "Taaza juice",
        "عصير طازج", "'Asir tazij", "Jugo fresco", "HOO-goh FREHS-koh",
        "Jus frais", "Zhoo freh", "Frischer Saft", "FRISH-er zahft",
        "Succo fresco", "SOOK-koh FREHS-koh", "Suco fresco", "SOO-koo FREHS-koo",
        "Свежий сок", "SVYEH-zhyy sohk", "Taze meyvesuyu", "Tah-zeh mey-veh-soo-yoo",
        "Jus segar", "Joos seh-gahr", "鲜 果汁", "Xiān guǒzhī",
        "新鮮な ジュース", "Shinsen na jūsu", "신선한 주스", "Sinseon-han juseu"
    )
]

w2["breakfast-chat"] = [
    item(
        "Eat toast", "ٹوسٹ کھاؤ", "Toast khao", "टोस्ट खाओ", "Toast khao",
        "كل خبزاً", "Kul khubzan", "Come tostada", "KOH-meh tohs-TAH-dah",
        "Mange toast", "Manzh toast", "Iss Toast", "ISS toast",
        "Mangia pane", "MAHN-jah PAH-neh", "Come torrada", "KOH-mee toh-RAH-dah",
        "Ешь тост", "Yesh tost", "Tost ye", "Tost yeh",
        "Makan roti", "Mah-kahn roh-tee", "吃 吐司", "Chī tǔsī",
        "トースト 食べる", "Tōsuto taberu", "토스트 먹어", "Toseuteu meogeo"
    ),
    item(
        "Drink milk", "دودھ پیو", "Doodh peeyo", "दूध पियो", "Doodh piyo",
        "اشرب حليباً", "Ishrab haliban", "Toma leche", "TOH-mah LEH-cheh",
        "Bois lait", "Bwah leh", "Trink Milch", "TRINK milkh",
        "Bevi latte", "BEH-vee LAHT-teh", "Bebe leite", "BEH-bee LAY-chee",
        "Пей молоко", "Pey mah-lah-KOH", "Süt iç", "Sewt eech",
        "Minum susu", "Mee-noom soo-soo", "喝 牛奶", "Hē niúnǎi",
        "ミルク 飲む", "Miruku nomu", "우유 마셔", "Uyu masyeo"
    ),
    item(
        "Pour juice", "جوس ڈالو", "Juice daalo", "जूस डालो", "Juice daalo",
        "صب عصيراً", "Subb 'asiran", "Sirve jugo", "SEER-veh HOO-goh",
        "Verse jus", "Vehrz zhoo", "Gieß Saft", "GEESS zahft",
        "Versa succo", "VEHR-sah SOOK-koh", "Põe suco", "POY SOO-koo",
        "Налей сок", "Nah-LEY sohk", "Meyvesuyu doldur", "Mey-veh-soo-yoo dohl-dur",
        "Tuang jus", "Too-ahng joos", "倒 果汁", "Dào guǒzhī",
        "ジュース 注ぐ", "Jūsu sosogu", "주스 따라", "Juseu ttara"
    )
]

# 2. lunch-dinner
w1["lunch-dinner"] = [
    item(
        "Hot soup", "گرم سوپ", "Garam soup", "गर्म सूप", "Garm soup",
        "حساء ساخن", "Hisa' sakhin", "Sopa caliente", "SOH-pah kah-LYEHN-teh",
        "Soupe chaude", "Soop shod", "Heiße Suppe", "HY-seh ZUP-peh",
        "Zuppa calda", "DZOOP-pah KAHL-dah", "Sopa quente", "SOH-pah KEHN-chee",
        "Горячий суп", "Gah-RYAH-chiy soop", "Sıcak çorba", "Suh-dzhak chor-ba",
        "Sup hangat", "Soop hahng-aht", "热 汤", "Rè tāng",
        "温かい スープ", "Atatakai sūpu", "따뜻한 수프", "Ttatteut-han supeu"
    ),
    item(
        "Yummy rice", "مزیدار چاول", "Mazedar chawal", "स्वादिष्ट चावल", "Swaadisht chawal",
        "أرز لذيذ", "Aruz ladhidh", "Arroz rico", "ah-RROHS REE-koh",
        "Bon riz", "Bohn ree", "Leckerer Reis", "LEK-ker-er rye-ss",
        "Riso buono", "REE-zoh BWAW-noh", "Arroz gostoso", "ah-HOYZ gohs-TOH-zoo",
        "Вкусный рис", "VKOOS-nyy rees", "Lezzetli pilav", "Lez-zet-lee pee-lahv",
        "Nasi enak", "Nah-see eh-nahk", "香 米饭", "Xiāng mǐfàn",
        "美味しい ご飯", "Oishii gohan", "맛있는 밥", "Mas-inneun bap"
    ),
    item(
        "Sweet bread", "میٹھی روٹی", "Meethi roti", "मीठी रोटी", "Meethi roti",
        "خبز حلو", "Khubz hulw", "Pan dulce", "PAHN DOOL-seh",
        "Pain doux", "Pan doo", "Süßes Brot", "ZYOO-ses broht",
        "Pane dolce", "PAH-neh DOHL-cheh", "Pão doce", "POW DOH-see",
        "Сладкий хлеб", "SLAHT-kiy khlyeb", "Tatlı ekmek", "Taht-luh ek-mek",
        "Roti manis", "Roh-tee mah-nees", "甜 面包", "Tián miànbāo",
        "甘い パン", "Amai pan", "달콤한 빵", "Dalkom-han ppang"
    )
]

w2["lunch-dinner"] = [
    item(
        "Taste soup", "سوپ چکھو", "Soup chakho", "सूप चखो", "Soup chakho",
        "تذوق حساءً", "Tadhawwaq hisa'", "Prueba sopa", "PRAY-bah SOH-pah",
        "Goûte soupe", "Goot soop", "Koste Suppe", "KOS-teh ZUP-peh",
        "Assaggia zuppa", "Ahs-SAHD-jah DZOOP-pah", "Prova sopa", "PRAW-vah SOH-pah",
        "Попробуй суп", "Pah-PROH-buy soop", "Çorba tat", "Chor-bah taht",
        "Cicipi sup", "Chee-chee-pee soop", "尝 汤", "Cháng tāng",
        "スープ 味わう", "Sūpu ajiwau", "수프 맛봐", "Supeu matbwa"
    ),
    item(
        "Eat rice", "چاول کھاؤ", "Chawal khao", "चावल खाओ", "Chawal khao",
        "كل أرزاً", "Kul aruzan", "Come arroz", "KOH-meh ah-RROHS",
        "Mange riz", "Manzh ree", "Iss Reis", "ISS rye-ss",
        "Mangia riso", "MAHN-jah REE-zoh", "Come arroz", "KOH-mee ah-HOYZ",
        "Ешь рис", "Yesh rees", "Pilav ye", "Pee-lahv yeh",
        "Makan nasi", "Mah-kahn nah-see", "吃 米饭", "Chī mǐfàn",
        "ご飯 食べる", "Gohan taberu", "밥 먹어", "Bap meogeo"
    ),
    item(
        "Break bread", "روٹی توڑو", "Roti toro", "रोटी तोड़ो", "Roti todo",
        "اكسر خبزاً", "Iksir khubzan", "Parte pan", "PAR-teh pahn",
        "Romps pain", "Rohn pan", "Brich Brot", "BRISH broht",
        "Spezza pane", "SPEHD-tsah PAH-neh", "Parte pão", "PAR-chee pow",
        "Преломи хлеб", "Pryeh-lah-MEE khlyeb", "Ekmek böl", "Ek-mek berl",
        "Bagi roti", "Bah-gee roh-tee", "掰 面包", "Bāi miànbāo",
        "パン ちぎる", "Pan chigiru", "빵 떼어", "Ppang tteeo"
    )
]

# 3. kitchen-help
w1["kitchen-help"] = [
    item(
        "Clean plate", "صاف پلیٹ", "Saaf plate", "साफ़ प्लेट", "Saaf plate",
        "صحن نظيف", "Sahn nadhif", "Plato limpio", "PLAH-toh LEEM-pyoh",
        "Assiette propre", "Ah-syet proh-pruh", "Sauberer Teller", "ZOW-ber-er TEL-ler",
        "Piatto pulito", "PYAHT-toh poo-LEE-toh", "Prato limpo", "PRAH-too LEEM-poo",
        "Чистая тарелка", "CHEES-tah-yah tah-RYEL-kah", "Temiz tabak", "Teh-meez tah-bahk",
        "Piring bersih", "Pee-reeng behr-seeh", "净 盘子", "Jìng pánzi",
        "綺麗な お皿", "Kireina osara", "깨끗한 접시", "Kkaekkeut-han jeopsi"
    ),
    item(
        "Big spoon", "بڑا چمچ", "Bara chamach", "बड़ा चम्मच", "Bada chammach",
        "ملعقة كبيرة", "Mil'aqa kabira", "Cuchara grande", "Koo-CHAH-rah GRAHN-deh",
        "Grande cuillère", "Grahnd kwee-yehr", "Großer Löffel", "GROHS-ser LERF-fel",
        "Cucchiaio grande", "Kook-KYAH-yoh GRAHN-deh", "Colher grande", "Kohl-YEHR GRAHN-jee",
        "Большая ложка", "Bahl-SHAH-yah LOHZH-kah", "Büyük kaşık", "Bew-yewk kah-shuk",
        "Sendok besar", "Sehn-dohk beh-sahr", "大 勺子", "Dà sháozi",
        "大きな スプーン", "Ōkina supūn", "큰 숟가락", "Keun sutgarak"
    ),
    item(
        "Dry towel", "خشک تولیہ", "Khushk toliya", "सूखा तौलिया", "Sookha tauliya",
        "منشفة جافة", "Minshafa jaffa", "Toalla seca", "Toh-AH-yah SEH-kah",
        "Serviette sèche", "Sehr-vyet sesh", "Trockenes Tuch", "TROK-neh-nes tookh",
        "Asciugamano asciutto", "Ah-shoo-gah-MAH-noh ah-SHOOT-toh", "Toalha seca", "Toh-AHL-yah SEH-kah",
        "Сухое полотенце", "Soo-KHOY-eh pah-lah-TYEHN-tseh", "Kuru havlu", "Koo-roo hahv-loo",
        "Handuk kering", "Hahn-dook keh-reeng", "干 毛巾", "Gān máojīn",
        "乾いた タオル", "Kawaita taoru", "마른 수건", "Mareun sugeon"
    )
]

w2["kitchen-help"] = [
    item(
        "Wash plate", "پلیٹ دھوؤ", "Plate dhoo", "प्लेट धोओ", "Plate dhoo",
        "اغسل صحناً", "Ighsil sahna", "Lava plato", "LAH-vah PLAH-toh",
        "Lave assiette", "Lahv ah-syet", "Spül Teller", "SHPYOOL TEL-ler",
        "Lava piatto", "LAH-vah PYAHT-toh", "Lava prato", "LAH-vah PRAH-too",
        "Помой тарелку", "Pah-MOY tah-RYEL-koo", "Tabak yıka", "Tah-bahk yuh-kah",
        "Cuci piring", "Choo-chee pee-reeng", "洗 盘子", "Xǐ pánzi",
        "お皿 洗う", "Osara arau", "접시 닦아", "Jeopsi dakka"
    ),
    item(
        "Pass spoon", "چمچ پکڑاؤ", "Chamach pakrao", "चम्मच पकड़ो", "Chammach pakdo",
        "ناول ملعقة", "Nawil mil'aqa", "Pasa cuchara", "PAH-sah koo-CHAH-rah",
        "Passe cuillère", "Pahs kwee-yehr", "Reich Löffel", "RYE-kh LERF-fel",
        "Passa cucchiaio", "PAHS-sah kook-KYAH-yoh", "Passa colher", "PAHS-sah kohl-YEHR",
        "Передай ложку", "Pyeh-ryeh-DAY LOHZH-koo", "Kaşık ver", "Kah-shuk vehr",
        "Oper sendok", "Oh-pehr sehn-dohk", "递 勺子", "Dì sháozi",
        "スプーン 渡す", "Supūn watasu", "숟가락 줘", "Sutgarak jwo"
    ),
    item(
        "Wipe table", "میز پونچھو", "Mez pooncho", "मेज़ पोंछो", "Mez poncho",
        "امسح طاولة", "Imsah tawila", "Limpia mesa", "LEEM-pyah MEH-sah",
        "Essuie table", "Eh-swee tah-bluh", "Wisch Tisch", "VISH tish",
        "Pulisci tavolo", "Poo-LEE-shee TAH-voh-loh", "Limpa mesa", "LEEM-pah MEH-zah",
        "Вытри стол", "VY-tree stohl", "Masa sil", "Mah-sah seel",
        "Lap meja", "Lahp meh-jah", "擦 桌子", "Cā zhuōzi",
        "机 拭く", "Tsukue fuku", "식탁 닦아", "Siktak dakka"
    )
]

# 4. bedtime-stories
w1["bedtime-stories"] = [
    item(
        "Soft pillow", "نرم تکیہ", "Naram takiya", "नरम तकिया", "Naram takiya",
        "وسادة ناعمة", "Wisada na'ima", "Almohada suave", "Ahl-moh-AH-dah SWAH-veh",
        "Oreiller doux", "Oh-ray-yay doo", "Weiches Kissen", "VY-khes KIS-sen",
        "Cuscino morbido", "Koo-SHEE-noh MOHR-bee-doh", "Travesseiro macio", "Trah-veh-SAY-roo mah-SEE-oo",
        "Мягкая подушка", "MYAHK-kah-yah pah-DOOSH-kah", "Yumuşak yastık", "Yoo-moo-shahk yahs-tuk",
        "Bantal lembut", "Bahn-tahl lehm-boot", "软 枕头", "Ruǎn zhěntou",
        "柔らかい 枕", "Yawarakai makura", "부드러운 베개", "Budeureo-un begae"
    ),
    item(
        "Warm blanket", "گرم کمبل", "Garam kambal", "गर्म कंबल", "Garm kambal",
        "بطانية دافئة", "Bataniya dafi'a", "Manta cálida", "MAHN-tah KAH-lee-dah",
        "Couverture chaude", "Koo-vehr-toor shod", "Warme Decke", "VAHR-meh DEK-keh",
        "Coperta calda", "Koh-PEHR-tah KAHL-dah", "Cobertor quente", "Koh-behr-TOHR KEHN-chee",
        "Тёплое одеяло", "TYOHP-lah-yeh ah-dyeh-YAH-lah", "Sıcak battaniye", "Suh-dzhak baht-tah-nee-yeh",
        "Selimut hangat", "Seh-lee-moot hahng-aht", "暖 被子", "Nuǎn bèizi",
        "温かい 毛布", "Atatakai mōfu", "따뜻한 담요", "Ttatteut-han damyo"
    ),
    item(
        "Sweet dreams", "اچھے خواب", "Achhe khwaab", "मीठे सपने", "Meethe sapne",
        "أحلام جميلة", "Ahlam jamila", "Dulces sueños", "DOOL-sehs SWEH-nyohs",
        "Beaux rêves", "Boh rehv", "Süße Träume", "ZYOO-seh TROY-meh",
        "Sogni d'oro", "SOH-nyee DOH-roh", "Bons sonhos", "Bohns SOHN-yoos",
        "Сладкие сны", "SLAHT-kee-yeh sny", "Tatlı rüyalar", "Taht-luh rew-yah-lahr",
        "Mimpi indah", "Meem-pee een-dah", "美 梦", "Měi mèng",
        "良い 夢", "Yoi yume", "좋은 꿈", "Joeun kkum"
    )
]

w2["bedtime-stories"] = [
    item(
        "Read book", "کتاب پڑھو", "Kitab parho", "किताब पढ़ो", "Kitab padho",
        "اقرأ كتاباً", "Iqra' kitaba", "Lee libro", "LEH-eh LEE-broh",
        "Lis livre", "Lee leev-ruh", "Lies Buch", "LEES bookh",
        "Leggi libro", "LEHD-jee LEE-broh", "Lê livro", "LEH LEE-vroo",
        "Читай книгу", "Chee-TYE KNEE-goo", "Kitap oku", "Kee-tahp oh-koo",
        "Baca buku", "Bah-chah boo-koo", "读 故事", "Dú gùshi",
        "本 読む", "Hon yomu", "책 읽어", "Chaek ilgeo"
    ),
    item(
        "Close eyes", "آنکھیں بند", "Aankhein band", "आँखें बंद", "Aankhein band",
        "أغمض عينيك", "Aghmid 'aynayk", "Cierra ojos", "SYEH-rrah OH-hohs",
        "Ferme yeux", "Fehrm yuh", "Schließe Augen", "SHLEE-seh OW-gen",
        "Chiudi occhi", "KYOO-dee OHK-kee", "Fecha olhos", "FEH-shah OH-lyoos",
        "Закрой глаза", "Zah-KROY glah-ZAH", "Gözleri kapa", "Gerz-leh-ree kah-pah",
        "Tutup mata", "Too-toop mah-tah", "闭 眼睛", "Bì yǎnjīng",
        "目 閉じる", "Me tojiru", "눈 감아", "Nun gama"
    ),
    item(
        "Sleep now", "اب سوؤ", "Ab so-o", "अब सोओ", "Ab sooo",
        "نم الآن", "Nam al-an", "Duerme ya", "DWEHR-meh yah",
        "Dors maintenant", "Dohr man-teh-nahn", "Schlaf jetzt", "SHLAHF yetst",
        "Dormi ora", "DOHR-mee OH-rah", "Dorme agora", "DOHR-mee ah-GAW-rah",
        "Спи сейчас", "Spee see-CHAHS", "Şimdi uyu", "Sheem-dee oo-yoo",
        "Tidur sekarang", "Tee-door seh-kah-rahng", "快 睡", "Kuài shuì",
        "今 寝る", "Ima neru", "푹 자", "Puk ja"
    )
]

# 5. morning-talk
w1["morning-talk"] = [
    item(
        "Bright sun", "روشن سورج", "Roshan sooraj", "चमकीला सूरज", "Chamkeela sooraj",
        "شمس مشرقة", "Shams mushriqa", "Sol brillante", "SOHL bree-YAHN-teh",
        "Soleil brillant", "Soh-lay bree-yahn", "Helle Sonne", "HEL-leh ZON-neh",
        "Sole splendente", "SOH-leh splehn-DEHN-teh", "Sol brilhante", "SOHL breel-YAHN-chee",
        "Яркое солнце", "YAHR-kah-yeh SOHN-tseh", "Parlak güneş", "Pahr-lahk gew-nesh",
        "Matahari cerah", "Mah-tah-hah-ree cheh-rah", "亮 太阳", "Liàng tàiyáng",
        "明るい 太陽", "Akarui taiyō", "밝은 햇살", "Balgeun haetsal"
    ),
    item(
        "Fresh air", "تازہ ہوا", "Taaza hawa", "ताज़ा हवा", "Taaza hawa",
        "هواء نقي", "Hawa' naqi", "Aire fresco", "EYE-reh FREHS-koh",
        "Air frais", "Ehr freh", "Frische Luft", "FRISH-eh looft",
        "Aria fresca", "AH-ryah FREHS-kah", "Ar fresco", "AHR FREHS-koo",
        "Свежий воздух", "SVYEH-zhyy VOHZ-dookh", "Temiz hava", "Teh-meez hah-vah",
        "Udara segar", "Oo-dah-rah seh-gahr", "新 空气", "Xīn kōngqì",
        "新鮮な 空気", "Shinsen na kūki", "맑은 공기", "Malgeun gonggi"
    ),
    item(
        "Good morning", "صبح بخیر", "Subah bakhair", "शुभ प्रभात", "Shubh prabhat",
        "صباح الخير", "Sabah al-khayr", "Buen día", "BWEHN DEE-ah",
        "Bon matin", "Bohn mah-tan", "Guten Morgen", "GOO-ten MOR-gen",
        "Buongiorno", "Bwohn-JOHR-noh", "Bom dia", "BOHN JEE-ah",
        "Доброе утро", "DOHB-rah-yeh OO-trah", "Günaydın", "Gew-neye-dun",
        "Selamat pagi", "Seh-lah-maht pah-gee", "早 上好", "Zǎo shànghǎo",
        "おはよう ございます", "Ohayō gozaimasu", "좋은 아침", "Joeun achim"
    )
]

w2["morning-talk"] = [
    item(
        "Wake up", "جاگ جاؤ", "Jaag jaao", "जाग जाओ", "Jaag jaao",
        "استيقظ الآن", "Istayqidh al-an", "Despierta ya", "Dehs-PYEHR-tah yah",
        "Réveille-toi", "Ray-vay twah", "Wach auf", "VAHKH owf",
        "Svegliati subito", "SVEHL-yah-tee SOO-bee-toh", "Acorda logo", "Ah-KOHR-dah LOH-goo",
        "Просыпайся скорей", "Prah-sy-PAY-syah skah-RYEY", "Hemen uyan", "Heh-men oo-yahn",
        "Bangun sekarang", "Bahng-oon seh-kah-rahng", "快 起床", "Kuài qǐchuáng",
        "すぐ 起きる", "Sugu okiru", "일어나 어서", "Ireona eoseo"
    ),
    item(
        "Smile big", "کھلکھلا کر", "Khilkhila kar", "खुलकर मुस्कुराओ", "Khulkar muskuraao",
        "ابتسم بفرح", "Ibtasim bi-farah", "Sonríe feliz", "Sohn-REE-eh feh-LEES",
        "Souris fort", "Soo-ree fohr", "Lächle schön", "LEKH-leh shern",
        "Sorridi tanto", "Sohr-REE-dee TAHN-toh", "Sorri muito", "SOH-hee MOON-too",
        "Улыбайся шире", "Oo-ly-BAY-syah SHEE-ryeh", "Neşeyle gülümse", "Neh-shay-leh gew-lewm-seh",
        "Tersenyum lebar", "Tehr-sehn-yoom leh-bahr", "大声 笑", "Dàshēng xiào",
        "にっこり 笑う", "Nikkori warau", "활짝 웃어", "Hwaljjak useo"
    ),
    item(
        "Open window", "کھڑکی کھولو", "Khirki kholo", "खिड़की खोलो", "Khidki kholo",
        "افتح نافذة", "Iftah nafida", "Abre ventana", "AH-breh vehn-TAH-nah",
        "Ouvre fenêtre", "Oo-vruh feh-net-ruh", "Öffne Fenster", "ERF-neh FEN-ster",
        "Apri finestra", "AH-pree fee-NEHS-trah", "Abre janela", "AH-bree zhah-NEH-lah",
        "Открой окно", "Aht-KROY ahk-NOH", "Pencere aç", "Pen-djeh-reh ahch",
        "Buka jendela", "Boo-kah jehn-deh-lah", "开 窗户", "Kāi chuānghu",
        "窓 開ける", "Mado akeru", "창문 열어", "Changmun yeoreo"
    )
]

# 6. evening-tea
w1["evening-tea"] = [
    item(
        "Hot tea", "گرم چائے", "Garam chai", "गर्म चाय", "Garm chai",
        "شاي ساخن", "Shay sakhin", "Té caliente", "TEH kah-LYEHN-teh",
        "Thé chaud", "Tay sho", "Heißer Tee", "HY-ser tay",
        "Tè caldo", "TEH KAHL-doh", "Chá quente", "SHAH KEHN-chee",
        "Горячий чай", "Gah-RYAH-chiy chy", "Sıcak çay", "Suh-dzhak chy",
        "Teh hangat", "Teh hahng-aht", "热 茶", "Rè chá",
        "温かい お茶", "Atatakai ocha", "따뜻한 차", "Ttatteut-han cha"
    ),
    item(
        "Crisp biscuit", "کرکرا بسکٹ", "Kurkura biscuit", "कुरकुरा बिस्कुट", "Kurkura biscuit",
        "بسكويت مقرمش", "Baskawit muqarmash", "Galleta crujiente", "Gah-YEH-tah kroo-HYEHN-teh",
        "Biscuit croquant", "Bees-kwee kroh-kahn", "Knuspriger Keks", "KNOOS-pree-ger kayks",
        "Biscotto croccante", "Bees-KOHT-toh krohk-KAHN-teh", "Biscoito crocante", "Bees-KOY-too kroh-KAHN-chee",
        "Хрустящее печенье", "Khroo-STYAH-shyeh pyeh-CHEHN-yeh", "Kıtır bisküvi", "Kuh-tuhr bees-kew-vee",
        "Biskuit renyah", "Bees-koo-eet rehn-yah", "脆 饼干", "Cuì bǐnggān",
        "サクサク クッキー", "Sakusaku kukkī", "바삭한 과자", "Basak-han gwaja"
    ),
    item(
        "Quiet evening", "پرسکون شام", "Pursukoon shaam", "शांत शाम", "Shaant shaam",
        "مساء هادئ", "Masa' hadi'", "Tarde tranquila", "TAR-deh trahn-KEE-lah",
        "Soir calme", "Swahr kahlm", "Ruhiger Abend", "ROO-hee-ger AH-bent",
        "Sera tranquilla", "SEH-rah trahn-KWEEL-lah", "Tarde calma", "TAHR-jee KAHL-mah",
        "Тихий вечер", "TEE-khiy VYEH-cheer", "Sakin akşam", "Sah-keen ahk-shahm",
        "Sore tenang", "Soh-reh teh-nahng", "静 傍晚", "Jìng bàngwǎn",
        "静かな 夕暮れ", "Shizukana yūgure", "조용한 저녁", "Joyong-han jeonyeok"
    )
]

w2["evening-tea"] = [
    item(
        "Sip tea", "چائے پیو", "Chai peeyo", "चाय पियो", "Chai piyo",
        "ارتشف شاياً", "Irtashif shayan", "Toma té", "TOH-mah teh",
        "Bois thé", "Bwah tay", "Trink Tee", "TRINK tay",
        "Bevi tè", "BEH-vee teh", "Toma chá", "TOH-mah shah",
        "Пей чай", "Pey chy", "Çay iç", "Chy eech",
        "Minum teh", "Mee-noom teh", "品 茶", "Pǐn chá",
        "お茶 飲む", "Ocha nomu", "차 마셔", "Cha masyeo"
    ),
    item(
        "Dip biscuit", "بسکٹ ڈبوؤ", "Biscuit daboo", "बिस्कुट डुबोओ", "Biscuit dubooo",
        "اغمس بسكويتاً", "Ighmis baskawit", "Moja galleta", "MOH-hah gah-YEH-tah",
        "Trempe biscuit", "Trahmp bees-kwee", "Tunk Keks", "TOONK kayks",
        "Inzuppa biscotto", "Een-DZOOP-pah bees-KOHT-toh", "Molha biscoito", "MOHL-yah bees-KOY-too",
        "Макай печенье", "Mah-KYE pyeh-CHEHN-yeh", "Bisküvi batır", "Bees-kew-vee bah-tuhr",
        "Celup biskuit", "Cheh-loop bees-koo-eet", "蘸 饼干", "Zhàn bǐnggān",
        "ビスケット 浸す", "Bisuketto hitasu", "과자 적셔", "Gwaja jeoksyeo"
    ),
    item(
        "Share story", "بات سناؤ", "Baat sunao", "बात सुनाओ", "Baat sunaao",
        "احك قصة", "Ihk qissa", "Cuenta historia", "KWEHN-tah ees-TOH-ryah",
        "Raconte histoire", "Rah-kohnt ees-twahr", "Erzähl Geschichte", "Ehr-TSAYL geh-SHIKH-teh",
        "Racconta storia", "Rahk-KOHN-tah STOH-ryah", "Conta história", "KOHN-tah ees-TAW-ryah",
        "Расскажи историю", "Rahs-skah-ZHY ees-TOH-ryoo", "Hikaye anlat", "Hee-kah-yeh ahn-laht",
        "Bercerita santai", "Behr-cheh-ree-tah sahn-tye", "讲 故事", "Jiǎng gùshi",
        "お話 聞かせる", "Ohanashi kikaseru", "이야기 나눠", "Iyagi nanwo"
    )
]

# 7. mom-and-dad
w1["mom-and-dad"] = [
    item(
        "Loving mom", "پیاری امی", "Pyaari ammi", "प्यारी माँ", "Pyaari maa",
        "أم حنونة", "Umm hanuna", "Mamá cariñosa", "Mah-MAH kah-ree-NYOH-sah",
        "Maman douce", "Mah-mahn doos", "Liebe Mama", "LEE-beh MAH-mah",
        "Mamma affettuosa", "MAHM-mah ahf-feht-TWOH-zah", "Mãe amorosa", "MYE ah-moh-RAW-zah",
        "Любимая мама", "Lyoo-BEE-mah-yah MAH-mah", "Sevgi dolu anne", "Sehv-gee doh-loo ahn-neh",
        "Ibu penyayang", "Ee-boo pehn-yah-yahng", "慈 母亲", "Cí mǔqīn",
        "優しい お母さん", "Yasashii okāsan", "다정한 엄마", "Dajeong-han eomma"
    ),
    item(
        "Kind dad", "مہربان ابو", "Meherbaan abbu", "दयालु पापा", "Dayaalu papa",
        "أب لطيف", "Ab latif", "Papá bueno", "Pah-PAH BWEH-noh",
        "Papa gentil", "Pah-pah zhan-tee", "Lieber Papa", "LEE-ber PAH-pah",
        "Papà buono", "Pah-PAH BWAW-noh", "Pai bondoso", "PYE bohn-DOH-zoo",
        "Добродушный папа", "Dah-brah-DOOSH-nyy PAH-pah", "İyi baba", "Ee-yee bah-bah",
        "Ayah baik", "Ah-yah by-eek", "和 父亲", "Hé fùqīn",
        "親切な お父さん", "Shinsetsu na otōsan", "착한 아빠", "Chak-han appa"
    ),
    item(
        "Happy home", "خوشگوار گھر", "Khushgawar ghar", "खुशनुमा घर", "Khushnuma ghar",
        "بيت سعيد", "Bayt sa'id", "Hogar alegre", "Oh-GAHR ah-LEH-greh",
        "Foyer joyeux", "Fwah-yay zhwah-yuh", "Glückliches Zuhause", "GLOOK-likh-es tsoo-HOW-zeh",
        "Casa felice", "KAH-zah feh-LEE-cheh", "Lar feliz", "LAHR feh-LEES",
        "Счастливый дом", "Schas-TLEE-vyy dohm", "Mutlu ev", "Moot-loo ev",
        "Rumah damai", "Roo-mah dah-mye", "乐 家庭", "Lè jiātíng",
        "温かい 我が家", "Atatakai wagaya", "행복한 집", "Haengbok-han jip"
    )
]

w2["mom-and-dad"] = [
    item(
        "Hug mom", "امی کو گلے", "Ammi ko galay", "माँ को गले", "Maa ko gale",
        "عانق أمك", "'Aniq ummak", "Abraza mamá", "Ah-BRAH-zah mah-MAH",
        "Embrasse maman", "Ahn-brahs mah-mahn", "Umarme Mama", "Oom-AHR-meh MAH-mah",
        "Abbraccia mamma", "Ahb-BRAHT-chah MAHM-mah", "Abraça mãe", "Ah-BRAH-sah mye",
        "Обними маму", "Ahb-nee-MEE MAH-moo", "Anneye sarıl", "Ahn-neh-yeh sah-ruhl",
        "Peluk ibu", "Peh-look ee-boo", "抱 妈妈", "Bào māmā",
        "お母さん 抱きしめる", "Okāsan dakishimeru", "엄마 안아", "Eomma ana"
    ),
    item(
        "Help dad", "ابو کی مدد", "Abbu ki madad", "पापा की मदद", "Papa ki madad",
        "ساعد أباك", "Sa'id abak", "Ayuda papá", "Ah-YOO-dah pah-PAH",
        "Aide papa", "Ehd pah-pah", "Hilf Papa", "HILF PAH-pah",
        "Aiuta papà", "Ah-YOO-tah pah-PAH", "Ajuda pai", "Ah-ZHOO-dah pye",
        "Помоги папе", "Pah-mah-GEE PAH-pyeh", "Babana yardım", "Bah-bah-nah yahr-duhm",
        "Bantu ayah", "Bahn-too ah-yah", "帮 爸爸", "Bāng bàba",
        "お父さん 手伝う", "Otōsan tetsudau", "아빠 도와", "Appa dowa"
    ),
    item(
        "Say thanks", "شکریہ کہو", "Shukriya kaho", "धन्यवाद कहो", "Dhanyavaad kaho",
        "قل شكراً", "Qul shukran", "Da gracias", "DAH GRAH-syahs",
        "Dis merci", "Dee mehr-see", "Sag Danke", "ZAHK DAHN-keh",
        "Dì grazie", "DEE GRAHT-tsyeh", "Diga obrigado", "JEE-gah oh-bree-GAH-doo",
        "Скажи спасибо", "Skah-ZHY spah-SEE-bah", "Teşekkür et", "Teh-shehk-kewr et",
        "Ucap terimakasih", "Oo-chahp teh-ree-mah-kah-seeh", "说 谢谢", "Shuō xièxie",
        "感謝 伝える", "Kansha tsutaeru", "고마워 해", "Gomawo hae"
    )
]

# 8. grandparents-chat
w1["grandparents-chat"] = [
    item(
        "Wise grandpa", "عقلمند دادا", "Aqlmand daada", "बुद्धिमान दादा", "Buddhiman dada",
        "جد حكيم", "Jadd hakim", "Abuelo sabio", "Ah-BWEH-loh SAH-byoh",
        "Grand-père sage", "Grahn-pehr sahzh", "Weiser Opa", "VY-zer OH-pah",
        "Nonno saggio", "NOHN-noh SAHD-joh", "Avô sábio", "Ah-VOH SAH-byoo",
        "Мудрый дедушка", "MOOD-ryy DYEH-doosh-kah", "Bilge dede", "Beel-geh deh-deh",
        "Kakek bijak", "Kah-kehk bee-jahk", "睿 爷爷", "Ruì yéyé",
        "物知りな おじいさん", "Monoshirina ojiisan", "지혜로운 할아버지", "Jihyeroun harabeoji"
    ),
    item(
        "Sweet grandma", "پیاری دادی", "Pyaari daadi", "प्यारी दादी", "Pyaari daadi",
        "جدة طيبة", "Jadda tayyiba", "Abuela dulce", "Ah-BWEH-lah DOOL-seh",
        "Grand-mère douce", "Grahn-mehr doos", "Liebe Oma", "LEE-beh OH-mah",
        "Nonna cara", "NOHN-nah KAH-rah", "Avó doce", "Ah-VAW DOH-see",
        "Милая бабушка", "MEE-lah-yah BAH-boosh-kah", "Tatlı nine", "Taht-luh nee-neh",
        "Nenek manis", "Neh-nehk mah-nees", "慈 奶奶", "Cí nǎinai",
        "優しい おばあさん", "Yasashii obāsan", "다정한 할머니", "Dajeong-han halmeoni"
    ),
    item(
        "Old story", "پرانی کہانی", "Puraani kahani", "पुरानी कहानी", "Puraani kahani",
        "قصة قديمة", "Qissa qadima", "Cuento viejo", "KWEHN-toh VYEH-hoh",
        "Vieux conte", "Vyuh kohnt", "Alte Geschichte", "AHL-teh geh-SHIKH-teh",
        "Vecchia favola", "VEHK-kyah FAH-voh-lah", "História antiga", "Ees-TAW-ryah ahn-CHEE-gah",
        "Старая сказка", "STAH-rah-yah SKAHS-kah", "Eski masal", "Es-kee mah-sahl",
        "Cerita lama", "Cheh-ree-tah lah-mah", "古 故事", "Gǔ gùshi",
        "昔の お話", "Mukashi no ohanashi", "옛날 이야기", "Yennal iyagi"
    )
]

w2["grandparents-chat"] = [
    item(
        "Hold hands", "ہاتھ پکڑو", "Haath pakro", "हाथ पकड़ो", "Haath pakdo",
        "أمسك يديهما", "Amsik yadayhima", "Toma manos", "TOH-mah MAH-nohs",
        "Serre mains", "Sehr man", "Halt Hände", "HAHLT HEN-deh",
        "Stringi mani", "STREEN-jee MAH-nee", "Segura mãos", "Seh-GOO-rah mowns",
        "Держи руку", "Dyehr-ZHY ROO-koo", "Elini tut", "Eh-lee-nee toot",
        "Genggam tangan", "Gehng-gahm tahng-ahn", "牵 手", "Qiān shǒu",
        "手 握る", "Te nigiru", "손 잡아", "Son jaba"
    ),
    item(
        "Listen closely", "غور سے سنو", "Ghor se suno", "ध्यान से सुनो", "Dhyaan se suno",
        "استمع جيداً", "Istami' jayyidan", "Escucha atento", "Ehs-KOO-chah ah-TEHN-toh",
        "Écoute bien", "Ay-koot byan", "Hör aufmerksam", "HER owf-merk-zahm",
        "Ascolta bene", "Ahs-KOHL-tah BEH-neh", "Escuta com atenção", "Ehs-KOO-tah kohn ah-teng-SOWN",
        "Слушай внимательно", "SLOO-shy vnee-MAH-tyel-nah", "Dikkatle dinle", "Deek-kaht-leh deen-leh",
        "Dengarkan baik", "Dehng-ahr-kahn by-eek", "认真 听", "Rènzhēn tīng",
        "しっかり 聞く", "Shikkari kiku", "잘 들어", "Jal deureo"
    ),
    item(
        "Share fruit", "پھل کھلاؤ", "Phal khilao", "फल खिलाओ", "Phal khilaao",
        "قدم فاكهة", "Qaddim fakiha", "Comparte fruta", "Kohm-PAR-teh FROO-tah",
        "Partage fruits", "Pahr-tahzh frwee", "Teile Früchte", "TY-leh FROOTSH-teh",
        "Condividi frutta", "Kohn-dee-VEE-dee FROOT-tah", "Divide frutas", "Jee-VEE-jee FROO-tahs",
        "Угости фруктами", "Oo-gahs-TEE FROOK-tah-mee", "Meyve ikram et", "Mey-veh eek-rahm et",
        "Bagi buah", "Bah-gee boo-ah", "分 水果", "Fēn shuǐguǒ",
        "果物 分ける", "Kudamono wakeru", "과일 나눠", "Gwail nanwo"
    )
]

# 9. morning-with-aunt
w1["morning-with-aunt"] = [
    item(
        "Cheerful aunt", "ہنس مکھ خالہ", "Hans-mukh khaala", "हँसमुख मौसी", "Hansmukh mausi",
        "خالة مرحة", "Khala mariha", "Tía alegre", "TEE-ah ah-LEH-greh",
        "Tante joyeuse", "Tahnt zhwah-yuhz", "Fröhliche Tante", "FRER-likh-eh TAHN-teh",
        "Zia solare", "DZEE-ah soh-LAH-reh", "Tia alegre", "CHEE-ah ah-LEH-gree",
        "Весёлая тётя", "Vyeh-SYOH-lah-yah TYOH-tyah", "Neşeli teyze", "Neh-sheh-lee teyz-deh",
        "Tante ceria", "Tahn-teh cheh-ree-ah", "和 姑姑", "Hé gūgu",
        "陽気な おばさん", "Yōkina obasan", "밝은 이모", "Balgeun imo"
    ),
    item(
        "Sweet pastry", "میٹھی پیسٹری", "Meethi pastry", "मीठी पेस्ट्री", "Meethi pastry",
        "فطيرة حلوة", "Fatira hulwa", "Pastel dulce", "Pahs-TEHL DOOL-seh",
        "Gâteau sucré", "Gah-toh soo-kray", "Süßes Gebäck", "ZYOO-ses geh-BEK",
        "Dolce squisito", "DOHL-cheh skwee-ZEE-toh", "Doce gostoso", "DOH-see gohs-TOH-zoo",
        "Сладкая выпечка", "SLAHT-kah-yah VY-pyech-kah", "Tatlı çörek", "Taht-luh cher-rek",
        "Kue manis", "Koo-eh mah-nees", "甜 点心", "Tián diǎnxin",
        "甘い お菓子", "Amai okashi", "달콤한 과자", "Dalkom-han gwaja"
    ),
    item(
        "Sunny balcony", "دھوپ والی بالکونی", "Dhoop wali balcony", "धूपदार बालकनी", "Dhoopdaar balcony",
        "شرفة مشمسة", "Shurfa mushmisa", "Balcón soleado", "Bahl-KOHN soh-leh-AH-doh",
        "Balcon ensoleillé", "Bahl-kohn ahn-soh-lay-yay", "Sonniger Balkon", "ZON-nee-ger bahl-KOHN",
        "Balcone soleggiato", "Bahl-KOH-neh soh-lehd-JAH-toh", "Varanda ensolarada", "Vah-RAHN-dah eng-soh-lah-RAH-dah",
        "Солнечный балкон", "SOHL-neech-nyy bahl-KOHN", "Güneşli balkon", "Gew-nesh-lee bahl-kohn",
        "Balkon cerah", "Bahl-kohn cheh-rah", "晴 阳台", "Qíng yángtái",
        "日当たりの 良いベランダ", "Hiatari no yoiberanda", "햇살든 발코니", "Haetsaldeun balkoni"
    )
]

w2["morning-with-aunt"] = [
    item(
        "Greet aunt", "خالہ کو سلام", "Khaala ko salaam", "मौसी को नमस्ते", "Mausi ko namaste",
        "رحب بخالتك", "Rahhib bi-khalatik", "Saluda tía", "Sah-LOO-dah TEE-ah",
        "Salue tante", "Sah-loo tahnt", "Grüß Tante", "GREESS TAHN-teh",
        "Saluta zia", "Sah-LOO-tah DZEE-ah", "Cumprimente tia", "Koom-pree-MEHN-chee CHEE-ah",
        "Поприветствуй тётю", "Pah-pree-VYEHT-stwooy TYOH-tyoo", "Teyzeni selamla", "Tey-zeh-nee seh-lahm-lah",
        "Sapa tante", "Sah-pah tahn-teh", "问候 姑姑", "Wènhòu gūgu",
        "おばさん 挨拶する", "Obasan aisatsu-suru", "이모께 인사해", "Imokke insahae"
    ),
    item(
        "Bake cookies", "بسکٹ بناؤ", "Biscuit banao", "बिस्कुट बनाओ", "Biscuit banaao",
        "اخبز حلوى", "Ikhbiz halwa", "Hornea galletas", "Ohr-NEH-ah gah-YEH-tahs",
        "Cuis biscuits", "Kwee bees-kwee", "Back Kekse", "BAHK KEK-seh",
        "Inforna biscotti", "Een-FOHR-nah bees-KOHT-tee", "Asse biscoitos", "AH-see bees-KOY-toos",
        "Пеки печенье", "Pyeh-KEE pyeh-CHEHN-yeh", "Kurabiye pişir", "Koo-rah-bee-yeh pee-sheer",
        "Panggang kue", "Pahng-gahng koo-eh", "做 饼干", "Zuò bǐnggān",
        "クッキー 焼く", "Kukkī yaku", "쿠키 구워", "Kuki guwo"
    ),
    item(
        "Water flowers", "پھولوں کو پانی", "Phoolon ko paani", "फूलों को पानी", "Phoolon ko paani",
        "اسق أزهاراً", "Isqi azharan", "Riega flores", "RYEH-gah FLOH-rehs",
        "Arrose fleurs", "Ah-rohz fluhr", "Gieß Blumen", "GEESS BLOO-men",
        "Innaffia fiori", "Een-NAHF-fyah FYOH-ree", "Rega flores", "HEH-gah FLAW-rees",
        "Полей цветы", "Pah-LEY tsvyeh-TY", "Çiçek sula", "Chee-chek soo-lah",
        "Siram bunga", "See-rahm boo-ngah", "浇 花", "Jiāo huā",
        "お花 水やり", "Ohana mizuyari", "화초에 물줘", "Hwachoe muljwo"
    )
]

# 10. dinner-with-uncle
w1["dinner-with-uncle"] = [
    item(
        "Tall uncle", "لمبے چچا", "Lambe chacha", "लंबे चाचा", "Lambe chacha",
        "عم طويل", "'Amm tawil", "Tío alto", "TEE-oh AHL-toh",
        "Oncle grand", "Ohn-kluh grahn", "Großer Onkel", "GROHS-ser OHN-kel",
        "Zio alto", "DZEE-oh AHL-toh", "Tio alto", "CHEE-oo AHL-too",
        "Высокий дядя", "Vy-SOH-kiy DYAH-dyah", "Uzun amca", "Oo-zoon ahm-jah",
        "Paman jangkung", "Pah-mahn jahng-koong", "高 叔叔", "Gāo shūshu",
        "背の高い おじさん", "Se no takai ojisan", "키큰 삼촌", "Kikeun samchon"
    ),
    item(
        "Grilled meat", "بھنا گوشت", "Bhuna gosht", "भुना गोश्त", "Bhuna gosht",
        "لحم مشوي", "Lahm mashwi", "Carne asada", "KAR-neh ah-SAH-dah",
        "Viande grillée", "Vyahn-duh gree-yay", "Gegrilltes Fleisch", "Geh-GRILT-es flysh",
        "Carne arrostita", "KAHR-neh ahr-rohs-TEE-tah", "Carne assada", "KAR-nee ah-SAH-dah",
        "Жареное мясо", "ZHAH-ryeh-nah-yeh MYAH-sah", "Kızarmış et", "Kuh-zahr-mush et",
        "Daging bakar", "Dah-geeng bah-kahr", "烤 肉", "Kǎo ròu",
        "美味しい 焼肉", "Oishii yakiniku", "구운 고기", "Guun gogi"
    ),
    item(
        "Loud laugh", "زوردار قہقہہ", "Zordaar qehqaha", "ज़ोरदार ठहाका", "Zordaar thahaaka",
        "ضحكة عالية", "Dihka 'aliya", "Risa fuerte", "REE-sah FWEHR-teh",
        "Rire sonore", "Reer soh-nohr", "Lautes Lachen", "LOW-tes LAH-khen",
        "Risata fragorosa", "Ree-ZAH-tah frah-goh-ROH-zah", "Risada alta", "Hee-ZAH-dah AHL-tah",
        "Громкий смех", "GROHM-kiy smyekh", "Şen kahkaha", "Shen kahk-hah-hah",
        "Tawa riang", "Tah-wah ree-ahng", "爽朗 笑声", "Shuǎnglǎng xiàoshēng",
        "豪快な 笑い声", "Gōkaina waraigoe", "호탕한 웃음", "Hotang-han useum"
    )
]

w2["dinner-with-uncle"] = [
    item(
        "Pass plate", "پلیٹ بڑھاؤ", "Plate barhao", "प्लेट बढ़ाओ", "Plate badhaao",
        "ناول صحناً", "Nawil sahna", "Pasa plato", "PAH-sah PLAH-toh",
        "Passe assiette", "Pahs ah-syet", "Reich Teller", "RYE-kh TEL-ler",
        "Passa piatto", "PAHS-sah PYAHT-toh", "Passa prato", "PAHS-sah PRAH-too",
        "Передай тарелку", "Pyeh-ryeh-DAY tah-RYEL-koo", "Tabağı uzat", "Tah-bah-uh oo-zaht",
        "Oper piring", "Oh-pehr pee-reeng", "递 盘子", "Dì pánzi",
        "お皿 渡す", "Osara watasu", "접시 건네", "Jeopsi geonne"
    ),
    item(
        "Share joke", "لطیفہ سناؤ", "Lateefa sunao", "चुटकुला सुनाओ", "Chutkula sunaao",
        "احك نكتة", "Ihk nukta", "Cuenta chiste", "KWEHN-tah CHEES-teh",
        "Raconte blague", "Rah-kohnt blahg", "Erzähl Witz", "Ehr-TSAYL vits",
        "Racconta barzelletta", "Rahk-KOHN-tah bahr-dzehl-LEHT-tah", "Conte piada", "KOHN-chee PYA-dah",
        "Расскажи шутку", "Rahs-skah-ZHY SHOOT-koo", "Fıkra anlat", "Fuhk-rah ahn-laht",
        "Bercanda seru", "Behr-chahn-dah seh-roo", "讲 笑话", "Jiǎng xiàohuà",
        "冗談 言い合う", "Jōdan iiau", "농담 나눠", "Nongdam nanwo"
    ),
    item(
        "Drink water", "پانی پیو", "Paani peeyo", "पानी पियो", "Paani piyo",
        "اشرب ماءً", "Ishrab ma'", "Toma agua", "TOH-mah AH-gwah",
        "Bois eau", "Bwah oh", "Trink Wasser", "TRINK VAHS-ser",
        "Bevi acqua", "BEH-vee AHK-wah", "Bebe água", "BEH-bee AH-gwah",
        "Пей воду", "Pey vah-DOO", "Su iç", "Soo eech",
        "Minum air", "Mee-noom ah-yeer", "喝 水", "Hē shuǐ",
        "お水 飲む", "Omizu nomu", "물 마셔", "Mul masyeo"
    )
]

# 11. big-feelings
w1["big-feelings"] = [
    item(
        "Happy smile", "پیاری مسکراہٹ", "Pyaari muskurahat", "प्यारी मुस्कान", "Pyaari muskaan",
        "ابتسامة حلوة", "Ibtisama hulwa", "Sonrisa linda", "Sohn-REE-sah LEEN-dah",
        "Doux sourire", "Doo soo-reer", "Frohes Lächeln", "FROH-es LEKH-eln",
        "Sorriso dolce", "Sohr-REE-zoh DOHL-cheh", "Sorriso meigo", "Sohr-HEE-zoo MAY-goo",
        "Радостная улыбка", "RAH-dahst-nah-yah oo-LYP-kah", "Tatlı tebessüm", "Taht-luh teh-behs-sewm",
        "Senyum manis", "Sehn-yoom mah-nees", "甜 微笑", "Tián wēixiào",
        "にこやかな 笑顔", "Nikoyakana egao", "밝은 미소", "Balgeun miso"
    ),
    item(
        "Calm mind", "پرسکون دل", "Pursukoon dil", "शांत मन", "Shaant mann",
        "قلب مطمئن", "Qalb mutma'inn", "Mente calma", "MEHN-teh KAHL-mah",
        "Esprit calme", "Ehs-pree kahlm", "Ruhiger Geist", "ROO-hee-ger gyste",
        "Mente serena", "MEHN-teh seh-REH-nah", "Mente serena", "MEHN-chee seh-REH-nah",
        "Спокойное сердце", "Spah-KOY-nah-yeh SYEHRD-tseh", "Huzurlu gönül", "Hoo-zoor-loo ger-newl",
        "Hati tenang", "Hah-tee teh-nahng", "平 心态", "Píng xīntài",
        "穏やかな 心", "Odayakana kokoro", "차분한 마음", "Chabun-han maeum"
    ),
    item(
        "Gentle hug", "نرم جھپی", "Naram jhappi", "प्यारा आलिंगन", "Pyaara aalingan",
        "عناق لطيف", "'Inaq latif", "Abrazo tierno", "Ah-BRAH-zoh TYEHR-noh",
        "Câlin doux", "Kah-lan doo", "Sanfte Umarmung", "ZAHN-fteh oom-AHR-moong",
        "Abbraccio tenero", "Ahb-BRAHT-choh TEH-neh-roh", "Abraço suave", "Ah-BRAH-soo SWAH-vee",
        "Нежные объятия", "NYEZH-ny-yeh ahb-YAH-tyah", "Şefkatli kucak", "Shehf-kaht-lee koo-jahk",
        "Pelukan hangat", "Peh-look-ahn hahng-aht", "温 拥抱", "Wēn yǒngbào",
        "優しい 抱擁", "Yasashii hōyō", "따스한 포옹", "Ttaseu-han poong"
    )
]

w2["big-feelings"] = [
    item(
        "Feel calm", "سکون پاؤ", "Sukoon paao", "शांति पाओ", "Shaanti paao",
        "اشعر براحة", "Ish'ur bi-raha", "Siente calma", "SYEHN-teh KAHL-mah",
        "Sois calme", "Swah kahlm", "Werde ruhig", "VEHR-deh ROO-hikh",
        "Trova calma", "TROH-vah KAHL-mah", "Sinta calma", "SEEN-tah KAHL-mah",
        "Успокойся скорее", "Oos-pah-KOY-syah skah-RYEY", "Sakin kal", "Sah-keen kahl",
        "Merasa tenang", "Meh-rah-sah teh-nahng", "放 平心态", "Fàng píngxīntài",
        "心 落ち着かせる", "Kokoro ochitsukaseru", "마음 가라앉혀", "Maeum garaanjhyeo"
    ),
    item(
        "Take breath", "سانس لو", "Saans lo", "साँस लो", "Saans lo",
        "تنفس بعمق", "Tanaffas bi-'umq", "Respira hondo", "Hehs-PEE-rah OHN-doh",
        "Respire bien", "Rehs-peer byan", "Atme tief", "AHT-meh teef",
        "Respira a fondo", "Hehs-PEE-rah ah FOHN-doh", "Respira fundo", "Hehs-PEE-rah FOON-doo",
        "Дыши глубоко", "Dy-SHY gloo-bah-KOH", "Derin soluk", "Deh-reen soh-look",
        "Tarik napas", "Tah-reek nah-pahs", "深 呼吸", "Shēn hūxī",
        "息 吸う", "Iki suu", "숨 들이쉬어", "Sum deuriswieo"
    ),
    item(
        "Share love", "پیار بانٹو", "Pyaar baanto", "प्यार बाँटो", "Pyaar baanto",
        "انشر حباً", "Inshur hubban", "Da cariño", "DAH kah-REE-nyoh",
        "Donne amour", "Dohn ah-moor", "Schenke Liebe", "SHEN-keh LEE-beh",
        "Dona amore", "DOH-nah ah-MOH-reh", "Espalhe amor", "Ehs-PAHL-yee ah-MOHR",
        "Дари тепло", "Dah-REE tyep-LOH", "Sevgi paylaş", "Sehv-gee pie-lahsh",
        "Tebar kasih", "Teh-bahr kah-seeh", "传 爱心", "Chuán àixīn",
        "愛 分け与える", "Ai wakeataeru", "사랑 나눠", "Sarang nanwo"
    )
]

# 12. bus-station
w1["bus-station"] = [
    item(
        "Big bus", "بڑی بس", "Bari bus", "बड़ी बस", "Badi bus",
        "حافلة كبيرة", "Hafila kabira", "Autobús grande", "Ow-toh-BOOS GRAHN-deh",
        "Grand bus", "Grahn boos", "Großer Bus", "GROHS-ser boos",
        "Grande autobus", "GRAHN-deh OW-toh-boos", "Ônibus grande", "OH-nee-boos GRAHN-jee",
        "Большой автобус", "Bahl-SHOY ahv-TOH-boos", "Büyük otobüs", "Bew-yewk oh-toh-bews",
        "Bus besar", "Boos beh-sahr", "大 巴士", "Dà bāshì",
        "大きな バス", "Ōkina basu", "큰 버스", "Keun beoseu"
    ),
    item(
        "Fast ride", "تیز سفر", "Tez safar", "तेज़ सफ़र", "Tez safar",
        "رحلة سريعة", "Rihla sari'a", "Viaje rápido", "VYAH-heh RAH-pee-doh",
        "Trajet rapide", "Trah-zhay rah-peed", "Schnelle Fahrt", "SHNEL-leh fahrt",
        "Corsa veloce", "KOHR-sah veh-LOH-cheh", "Viagem rápida", "VYAH-zheng HAH-pee-dah",
        "Быстрая поездка", "BYS-trah-yah pah-YEZD-kah", "Hızlı sefer", "Huhz-luh seh-fehr",
        "Perjalanan cepat", "Pehr-jah-lahn-ahn cheh-paht", "快 车次", "Kuài chēcì",
        "速い ドライブ", "Hayai doraibu", "빠른 주행", "Ppareun juhaeng"
    ),
    item(
        "Front seat", "اگلی نشست", "Agli nisheest", "आगे वाली सीट", "Aage wali seat",
        "مقعد أمامي", "Maq'ad amami", "Asiento delantero", "Ah-SYEHN-toh deh-lahn-TEH-roh",
        "Siège avant", "Syehzh ah-vahn", "Vordersitz frei", "FOR-der-zits fry",
        "Sedile anteriore", "Seh-DEE-leh ahn-teh-RYOH-reh", "Banco dianteiro", "BAHN-koo dyan-TAY-roo",
        "Переднее место", "Pyeh-RYEHD-nyeh-yeh MYEHS-tah", "Ön koltuk", "Ern kohl-took",
        "Kursi depan", "Koor-see deh-pahn", "前 排座位", "Qiánpái zuòwèi",
        "前の 席", "Mae no seki", "앞쪽 좌석", "Apjjok jwaseok"
    )
]

w2["bus-station"] = [
    item(
        "Catch bus", "بس پکڑو", "Bus pakro", "बस पकड़ो", "Bus pakdo",
        "الحق بالحافلة", "Ilhaq bil-hafila", "Toma autobús", "TOH-mah ow-toh-BOOS",
        "Prends bus", "Prahn boos", "Nimm Bus", "NIM boos",
        "Prendi autobus", "PREHN-dee OW-toh-boos", "Pegue ônibus", "PEH-gee OH-nee-boos",
        "Садись в автобус", "Sah-DEES v ahv-TOH-boos", "Otobüse bin", "Oh-toh-bew-seh been",
        "Naik bus", "Nye-eek boos", "乘 公交", "Chéng gōngjiāo",
        "バス 乗る", "Basu noru", "버스 타", "Beoseu ta"
    ),
    item(
        "Show ticket", "ٹکٹ دکھاؤ", "Ticket dikhao", "टिकट दिखाओ", "Ticket dikhaao",
        "أظهر تذكرة", "Azhhir tadhkira", "Muestra boleto", "MWEHS-trah boh-LEH-toh",
        "Montre billet", "Mohn-truh bee-yay", "Zeig Ticket", "TSYGH TIK-et",
        "Mostra biglietto", "MOHS-trah beel-YEHT-toh", "Mostre bilhete", "MOHS-tree beel-YAY-chee",
        "Покажи билет", "Pah-kah-ZHY bee-LYEHT", "Bileti göster", "Bee-leh-tee gerz-tehr",
        "Tunjukkan tiket", "Toon-jook-kahn tee-keht", "出示 车票", "Chūshì chēpiào",
        "切符 見せる", "Kippu miseru", "표 보여줘", "Pyo boyeojwo"
    ),
    item(
        "Find seat", "سیٹ ڈھونڈو", "Seat dhoondo", "सीट ढूँढो", "Seat dhoondho",
        "جد مقعداً", "Jid maq'adan", "Busca asiento", "BOOS-kah ah-SYEHN-toh",
        "Trouve place", "Troov plahs", "Finde Platz", "FIN-deh plahts",
        "Cerca posto", "CHEHR-kah POHS-toh", "Ache lugar", "AH-shee loo-GAHR",
        "Найди место", "Nye-DEE MYEHS-tah", "Koltuk bul", "Kohl-took bool",
        "Cari kursi", "Chah-ree koor-see", "找 座位", "Zhǎo zuòwèi",
        "席 探す", "Seki sagasu", "자리 찾아", "Jari chaja"
    )
]

# 13. train-tickets
w1["train-tickets"] = [
    item(
        "Fast train", "تیز ٹرین", "Tez train", "तेज़ ट्रेन", "Tez train",
        "قطار سريع", "Qitar sari'", "Tren veloz", "TREHN veh-LOHS",
        "Train rapide", "Tran rah-peed", "Schneller Zug", "SHNEL-ler tsook",
        "Treno rapido", "TREH-noh RAH-pee-doh", "Trem rápido", "TREHNG HAH-pee-doo",
        "Скорый поезд", "SKOH-ryy POY-yezd", "Hızlı tren", "Huhz-luh trehn",
        "Kereta cepat", "Keh-reh-tah cheh-paht", "快 火车", "Kuài huǒchē",
        "速い 列車", "Hayai ressha", "고속 열차", "Gosok yeolcha"
    ),
    item(
        "Long track", "لمبی پٹری", "Lambi patri", "लंबी पटरी", "Lambi patri",
        "سكة طويلة", "Sikka tawila", "Vía larga", "VEE-ah LAHR-gah",
        "Long rail", "Lohn rye", "Langes Gleis", "LAHN-ges glyss",
        "Binario lungo", "Bee-NAH-ryoh LOON-goh", "Trilho longo", "TREEL-yoo LOHN-goo",
        "Длинный путь", "DLEEN-nyy poot", "Uzun demiryolu", "Oo-zoon deh-meer-yoh-loo",
        "Rel panjang", "Rehl pahn-jahng", "长 铁轨", "Cháng tiěguǐ",
        "長い 線路", "Nagai senro", "긴 철길", "Gin cheolgil"
    ),
    item(
        "Window view", "کھڑکی کا نظارہ", "Khirki ka nazaara", "खिड़की का नज़ारा", "Khidki ka nazaara",
        "مشهد نافذة", "Mashhad nafida", "Linda vista", "LEEN-dah VEES-tah",
        "Belle vue", "Bel voo", "Schöne Aussicht", "SHER-neh OWS-zikht",
        "Bella vista", "BEHL-lah VEES-tah", "Bela vista", "BEH-lah VEES-tah",
        "Красивый вид", "Krah-SEE-vyy veed", "Güzel manzara", "Gew-zel mahn-zah-rah",
        "Pemandangan jendela", "Peh-mahn-dahng-ahn jehn-deh-lah", "美 风景", "Měi fēngjǐng",
        "窓からの 景色", "Mado kara no keshiki", "창밖 풍경", "Changbak punggyeong"
    )
]

w2["train-tickets"] = [
    item(
        "Board train", "ٹرین پر چڑھو", "Train par charho", "ट्रेन पर चढ़ो", "Train par chadho",
        "اركب قطاراً", "Irkab qitaran", "Sube tren", "SOO-beh trehn",
        "Monte train", "Mohnt tran", "Steig ein", "SHTYGH yn",
        "Sali treno", "SAH-lee TREH-noh", "Embarque trem", "Ehm-BAR-kee trehng",
        "Садись в поезд", "Sah-DEES v POY-yezd", "Trene bin", "Treh-neh been",
        "Naik kereta", "Nye-eek keh-reh-tah", "登 火车", "Dēng huǒchē",
        "電車 乗る", "Densha noru", "기차 타", "Gicha ta"
    ),
    item(
        "Hold ticket", "ٹکٹ سنبھالو", "Ticket sambhaalo", "टिकट सँभालो", "Ticket sambhaalo",
        "احتفظ بالتذكرة", "Ihtafidh bit-tadhkira", "Guarda boleto", "GWAHR-dah boh-LEH-toh",
        "Garde billet", "Gahrd bee-yay", "Halt Ticket", "HAHLT TIK-et",
        "Tieni biglietto", "TYEH-nee beel-YEHT-toh", "Guarde bilhete", "GWAHR-jee beel-YAY-chee",
        "Держи билет", "Dyehr-ZHY bee-LYEHT", "Bileti sakla", "Bee-leh-tee sahk-lah",
        "Pegang tiket", "Peh-gahng tee-keht", "拿 好车票", "Ná hǎochēpiào",
        "切符 持つ", "Kippu motsu", "표 잘챙겨", "Pyo jalchaenggyeo"
    ),
    item(
        "Hear whistle", "سیٹی سنو", "Seeti suno", "सीटी सुनो", "Seeti suno",
        "استمع لصفارة", "Istami' lisaffara", "Oye silbato", "OH-yeh seel-BAH-toh",
        "Écoute sifflet", "Ay-koot seef-lay", "Hör Pfeife", "HER PFY-feh",
        "Senti fischio", "SEHN-tee FEES-kyoh", "Ouça apito", "OH-sah ah-PEE-too",
        "Слушай гудок", "SLOO-shy goo-DOHK", "Düdüğü duy", "Dew-dew-ew dooy",
        "Dengar peluit", "Dehng-ahr peh-loo-eet", "听 鸣笛", "Tīng míngdí",
        "汽笛 聞く", "Kiteki kiku", "경적 들어", "Gyeongjeok deureo"
    )
]

# 14. in-a-taxi
w1["in-a-taxi"] = [
    item(
        "Yellow cab", "پیلی ٹیکسی", "Peeli taxi", "पीली टैक्सी", "Peeli taxi",
        "سيارة صفراء", "Sayyara safra'", "Taxi amarillo", "TAHK-see ah-mah-REE-yoh",
        "Taxi jaune", "Tahk-see zhohn", "Gelbes Taxi", "GEL-bes TAHK-see",
        "Taxi giallo", "TAHK-see JAHL-loh", "Táxi amarelo", "TAHK-see ah-mah-REH-loo",
        "Жёлтое такси", "ZHOHL-tah-yeh tahk-SEE", "Sarı taksi", "Sah-ruh tahk-see",
        "Taksi kuning", "Tahk-see koo-neeng", "黄 出租车", "Huáng chūzūchē",
        "黄色い タクシー", "Kiiroi takushī", "노란 택시", "Noran taeksi"
    ),
    item(
        "Friendly driver", "مہربان ڈرائیور", "Meherbaan driver", "मिलनसार ड्राइवर", "Milansaar driver",
        "سائق ودود", "Sa'iq wadud", "Conductor amable", "Kohn-dook-TOHR ah-MAH-bleh",
        "Chauffeur poli", "Shoh-fuhr poh-lee", "Netter Fahrer", "NET-ter FAH-rer",
        "Autista gentile", "Ow-TEES-tah jehn-TEE-leh", "Motorista gentil", "Moh-toh-REES-tah zheng-TEEL",
        "Приветливый шофёр", "Pree-VYEHT-lee-vyy shah-FYOHR", "Güler yüzlü şoför", "Gew-lehr yewz-lew shoh-fehr",
        "Sopir ramah", "Soh-peer rah-mah", "善 司机", "Shàn sījī",
        "優しい 運転手", "Yasashii untenshu", "친절한 기사님", "Chinjeol-han gissanim"
    ),
    item(
        "Fast ride", "آرام دہ سواری", "Aaram deh sawaari", "आरामदेह सवारी", "Aaraamdeh sawaari",
        "رحلة مريحة", "Rihla muriha", "Viaje cómodo", "VYAH-heh KOH-moh-doh",
        "Trajet doux", "Trah-zhay doo", "Bequeme Fahrt", "Beh-KVAY-meh fahrt",
        "Corsa comoda", "KOHR-sah KOH-moh-dah", "Passeio confortável", "Pah-SAY-oo kohn-for-TAH-vehl",
        "Удобная поездка", "Oo-DOHB-nah-yah pah-YEZD-kah", "Rahat yolculuk", "Rah-haht yohl-joo-look",
        "Tumpangan nyaman", "Toom-pahng-ahn nyah-mahn", "畅 行程", "Chàng xíngchéng",
        "快適な ドライブ", "Kaitekina doraibu", "편안한 주행", "Pyeon-an-han juhaeng"
    )
]

w2["in-a-taxi"] = [
    item(
        "Call taxi", "ٹیکسی بلاؤ", "Taxi bulao", "टैक्सी बुलाओ", "Taxi bulaao",
        "اطلب سيارة", "Itlub sayyara", "Pide taxi", "PEE-deh TAHK-see",
        "Appelle taxi", "Ah-pehl tahk-see", "Ruf Taxi", "ROOF TAHK-see",
        "Chiama taxi", "KYAH-mah TAHK-see", "Chame táxi", "SHAH-mee TAHK-see",
        "Вызови такси", "VY-zah-vee tahk-SEE", "Taksi çağır", "Tahk-see chah-uhr",
        "Panggil taksi", "Pahng-geel tahk-see", "打 出租车", "Dǎ chūzūchē",
        "タクシー 呼ぶ", "Takushī yobu", "택시 불러", "Taeksi bulleo"
    ),
    item(
        "Wear belt", "بیلٹ باندھو", "Belt baandho", "बेल्ट बाँधो", "Belt baandho",
        "اربط حزاماً", "Irbat hizaman", "Ponte cinturón", "POHN-teh seen-too-ROHN",
        "Mets ceinture", "Meh san-toor", "Schnall an", "SHNAHL ahn",
        "Allaccia cintura", "Ahl-LAHT-chah cheen-TOO-rah", "Coloque cinto", "Koh-LAW-kee SEEN-too",
        "Пристегни ремень", "Pree-styehg-NEE ryeh-MYEN", "Kemeri tak", "Keh-meh-ree tahk",
        "Pasang sabuk", "Pah-sahng sah-book", "系 安全带", "Jì ānquándài",
        "ベルト 締める", "Beruto shimeru", "안전벨트 매", "Anjeonbelteu mae"
    ),
    item(
        "Tell address", "پتہ بتاؤ", "Pata batao", "पता बताओ", "Pata bataao",
        "قل عنواناً", "Qul 'unwanan", "Di dirección", "DEE dee-rehk-SYOHN",
        "Donne adresse", "Dohn ah-drehs", "Sag Adresse", "ZAHK ah-DRES-seh",
        "Dì indirizzo", "DEE een-dee-REET-tsoh", "Diga endereço", "JEE-gah eng-deh-REH-soo",
        "Назови адрес", "Nah-zah-VEE AH-dryes", "Adresi söyle", "Ahd-reh-see seri-leh",
        "Sebut alamat", "Seh-boot ah-lah-maht", "说 地址", "Shuō dìzhǐ",
        "行き先 伝える", "Ikisaki tsutaeru", "주소 말해", "Juso malhae"
    )
]

# 15. airplane-flight
w1["airplane-flight"] = [
    item(
        "Huge airplane", "بڑا جہاز", "Bara jahaaz", "बड़ा हवाईजहाज़", "Bada hawaijahaaz",
        "طائرة ضخمة", "Ta'ira dakhma", "Avión gigante", "Ah-VYOHN hee-GAHN-teh",
        "Grand avion", "Grahn ah-vyohn", "Großes Flugzeug", "GROHS-ses FLOOK-tsoyk",
        "Aereo grande", "Ah-EH-reh-oh GRAHN-deh", "Avião enorme", "Ah-VYEE-ow eh-NOHR-mee",
        "Большой самолёт", "Bahl-SHOY sah-mah-LYOHT", "Büyük uçak", "Bew-yewk oo-chahk",
        "Pesawat besar", "Peh-sah-waht beh-sahr", "大 飞机", "Dà fēijī",
        "大きな 飛行機", "Ōkina hikōki", "큰 비행기", "Keun bihaenggi"
    ),
    item(
        "Fluffy clouds", "روئی جیسے بادل", "Rooyi jaise baadal", "रुई जैसे बादल", "Ruyi jaise baadal",
        "غيوم بيضاء", "Ghuyum bayda'", "Nubes blancas", "NOO-behs BLAHN-kahs",
        "Nuages blancs", "Noo-ahzh blahn", "Weiße Wolken", "VY-seh VOL-ken",
        "Nuvole soffici", "NOO-voh-leh SOHF-fee-chee", "Nuvens fofas", "NOO-vengs FAW-fahs",
        "Белые облака", "BYEH-ly-yeh ah-blah-KAH", "Beyaz bulutlar", "Beh-yahz boo-loot-lahr",
        "Awan putih", "Ah-wahn poo-teeh", "白 云朵", "Bái yúnduǒ",
        "ふわふわな 雲", "Fuwafuwana kumo", "새하얀 구름", "Saehayan gureum"
    ),
    item(
        "Safe flight", "محفوظ پرواز", "Mehfooz parwaaz", "सुरक्षित उड़ान", "Surakshit udaan",
        "رحلة آمنة", "Rihla amina", "Vuelo seguro", "BWEH-loh seh-GOO-roh",
        "Bon vol", "Bohn vohl", "Guter Flug", "GOO-ter flook",
        "Volo sicuro", "VOH-loh see-KOO-roh", "Voo tranquilo", "VOH-oo trahng-KEE-loo",
        "Приятный полёт", "Pree-YAHT-nyy pah-LYOHT", "Hayırlı uçuşlar", "Hah-yuhr-luh oo-choosh-lahr",
        "Penerbangan lancar", "Peh-nehr-bahng-ahn lahn-chahr", "顺 航班", "Shùn hángbān",
        "快適な 空の旅", "Kaitekina soranotabi", "안전한 비행", "Anjeon-han bihaeng"
    )
]

w2["airplane-flight"] = [
    item(
        "Fly high", "اونچا اڑو", "Ooncha uro", "ऊँचा उड़ो", "Ooncha udo",
        "حلق عالياً", "Halliq 'aliyan", "Vuela alto", "BWEH-lah AHL-toh",
        "Vole haut", "Vohl oh", "Flieg hoch", "FLEEKH hohkh",
        "Vola alto", "VOH-lah AHL-toh", "Voe alto", "VAW-ee AHL-too",
        "Лети высоко", "Lyeh-TEE vy-sah-KOH", "Yüksekten uç", "Yewk-sek-tehn ooch",
        "Terbang tinggi", "Tehr-bahng teeng-gee", "高 飞", "Gāo fēi",
        "高く 飛ぶ", "Takaku tobu", "높이 날아", "Nopi nara"
    ),
    item(
        "Fasten belt", "بیلٹ کسو", "Belt kaso", "बेल्ट बाँधो", "Belt baandho",
        "اربط حزامك", "Irbat hizamak", "Ajusta cinturón", "Ah-HOOS-tah seen-too-ROHN",
        "Boucle ceinture", "Book-luh san-toor", "Schnall fest", "SHNAHL fehst",
        "Allaccia cintura", "Ahl-LAHT-chah cheen-TOO-rah", "Afivele cinto", "Ah-fee-VEH-lee SEEN-too",
        "Застегни ремень", "Zahs-styehg-NEE ryeh-MYEN", "Kemeri bağla", "Keh-meh-ree bah-lah",
        "Kencangkan sabuk", "Kehn-chahng-kahn sah-book", "扣好 安全带", "Kòuhǎo ānquándài",
        "シートベルト 締める", "Shītoberuto shimeru", "안전벨트 조여", "Anjeonbelteu joyeo"
    ),
    item(
        "Look outside", "باہر دیکھو", "Bahar dekho", "बाहर देखो", "Baahar dekho",
        "انظر خارجاً", "Undhur kharijan", "Mira fuera", "MEE-rah FWEH-rah",
        "Regarde dehors", "Ruh-gahrd duh-ohr", "Schau raus", "SHOW rowss",
        "Guarda fuori", "GWAHR-dah FWAW-ree", "Olhe fora", "AW-lyee FAW-rah",
        "Смотри наружу", "Smah-TREE nah-ROO-zhoo", "Dışarıya bak", "Duh-shah-ruh-yah bahk",
        "Lihat keluar", "Lee-haht keh-loo-ahr", "看 窗外", "Kàn chuāngwài",
        "外 見る", "Soto miru", "밖을 봐", "Bakkeul bwa"
    )
]

# 16. asking-directions
w1["asking-directions"] = [
    item(
        "Clear map", "صاف نقشہ", "Saaf naqsha", "साफ़ नक्शा", "Saaf naksha",
        "خريطة واضحة", "Kharita wadiha", "Mapa claro", "MAH-pah KLAH-roh",
        "Carte claire", "Kahrt klehr", "Übersichtliche Karte", "OO-ber-zikht-likh-eh KAHR-teh",
        "Mappa chiara", "MAHP-pah KYAH-rah", "Mapa claro", "MAH-pah KLAH-roo",
        "Чёткая карта", "CHOHT-kah-yah KAHR-tah", "Net harita", "Net hah-ree-tah",
        "Peta jelas", "Peh-tah jeh-lahs", "准 地图", "Zhǔn dìtú",
        "分かりやすい 地図", "Wakariyasui chizu", "한눈의 지도", "Hannun-ui jido"
    ),
    item(
        "Near park", "قریبی پارک", "Qareebi park", "पास वाला पार्क", "Paas wala park",
        "حديقة قريبة", "Hadiqa qariba", "Parque cercano", "PAR-keh sehr-KAH-noh",
        "Parc proche", "Pahrk prohsh", "Naher Park", "NAH-her pahrk",
        "Parco vicino", "PAR-koh vee-CHEE-noh", "Parque perto", "PAR-kee PEHR-too",
        "Близкий парк", "BLEEZ-kiy pahrk", "Yakın park", "Yah-kuhn pahrk",
        "Taman dekat", "Tah-mahn deh-kaht", "近 公园", "Jìn gōngyuán",
        "近くの 公園", "Chikaku no kōen", "가까운 공원", "Gakkaun gongwon"
    ),
    item(
        "Right corner", "دایاں موڑ", "Daayan mor", "दायाँ कोना", "Daayan kona",
        "زاوية يمنى", "Zawiya yumna", "Esquina derecha", "Ehs-KEE-nah deh-REH-chah",
        "Coin droit", "Kwan drwah", "Rechte Ecke", "REKH-teh EK-keh",
        "Angolo destro", "AHN-goh-loh DEHS-troh", "Esquina direita", "Ehs-KEE-nah jee-RAY-tah",
        "Правый угол", "PRAH-vyy OO-gahl", "Sağ köşe", "Sah ker-sheh",
        "Sudut kanan", "Soo-doot kah-nahn", "右 拐角", "Yòu guǎijiǎo",
        "右の 角", "Migi no kado", "오른쪽 모퉁이", "Oreunjjok motung-i"
    )
]

w2["asking-directions"] = [
    item(
        "Turn right", "دائیں مڑو", "Daein muro", "दाएँ मुड़ो", "Daaen mudo",
        "انعطف يميناً", "In'atif yaminan", "Gira derecha", "HEE-rah deh-REH-chah",
        "Tourne à droite", "Toorn ah drwaht", "Bieg rechts ab", "BEEKH rekhts ahp",
        "Gira a destra", "JEE-rah ah DEHS-trah", "Vire à direita", "VEE-ree ah jee-RAY-tah",
        "Поверни направо", "Pah-vyehr-NEE nah-PRAH-vah", "Sağa dön", "Sah-ah dern",
        "Belok kanan", "Beh-lohk kah-nahn", "向 右转", "Xiàng yòuzhuǎn",
        "右 曲がる", "Migi magaru", "우회전 해", "Uhoejeon hae"
    ),
    item(
        "Walk straight", "سیدھا چلو", "Seedha chalo", "सीधा चलो", "Seedha chalo",
        "امش للأمام", "Imshi lil-amam", "Camina recto", "Kah-MEE-nah REHK-toh",
        "Va tout droit", "Vah too drwah", "Geh geradeaus", "GAY geh-RAH-deh-ows",
        "Cammina dritto", "Kahm-MEE-nah DREET-toh", "Siga em frente", "SEE-gah eng FREN-chee",
        "Иди прямо", "Ee-DEE PRYAH-mah", "Düz yürü", "Dewz yew-rew",
        "Jalan lurus", "Jah-lahn loo-roos", "直 走", "Zhí zǒu",
        "まっすぐ 歩く", "Massugu aruku", "곧장 걸어가", "Gotjang georeoga"
    ),
    item(
        "Ask helper", "مدد مانگو", "Madad maango", "मदद माँगो", "Madad maango",
        "اطلب مساعدة", "Itlub musa'ada", "Pide ayuda", "PEE-deh ah-YOO-dah",
        "Demande aide", "Duh-mahnd ehd", "Frag jemanden", "FRAHK YAY-mahn-den",
        "Chiedi aiuto", "KYEH-dee ah-YOO-toh", "Peça ajuda", "PEH-sah ah-ZHOO-dah",
        "Попроси о помощи", "Pah-prah-SEE ah POH-mah-shee", "Yardım iste", "Yahr-duhm ees-teh",
        "Minta tolong", "Meen-tah toh-lohng", "求 帮助", "Qiú bāngzhù",
        "助けを 求める", "Tasuke o motomeru", "도움을 청해", "Doumeul cheonghae"
    )
]

output_path = os.path.join(os.path.dirname(__file__), "..", "src", "data", "multilingual", "cat1_home_family_travel.ts")
export_ts_module(output_path, "CAT1_W1", "CAT1_W2", w1, w2)
