# Generator for TOPIC_SINGLE_WORD_ITEMS across all 77 topics and 15 languages
import json
import os

def sw(en, ur, ur_rom, hi, hi_rom, ar, ar_rom, es, es_rom, fr, fr_rom, de, de_rom, it, it_rom, pt, pt_rom, ru, ru_rom, tr, tr_rom, id_val, id_rom, zh, zh_rom, ja, ja_rom, ko, ko_rom):
    return {
        "en": en,
        "target": {
            "en": en, "ur": ur, "hi": hi, "ar": ar, "es": es,
            "fr": fr, "de": de, "it": it, "pt": pt, "ru": ru,
            "tr": tr, "id": id_val, "zh": zh, "ja": ja, "ko": ko
        },
        "romanized": {
            "en": en, "ur": ur_rom, "hi": hi_rom, "ar": ar_rom, "es": es_rom,
            "fr": fr_rom, "de": de_rom, "it": it_rom, "pt": pt_rom, "ru": ru_rom,
            "tr": tr_rom, "id": id_rom, "zh": zh_rom, "ja": ja_rom, "ko": ko_rom
        }
    }

d = {}

# 1. breakfast-chat
d["breakfast-chat"] = [
    sw("Toast", "ٹوسٹ", "Toast", "टोस्ट", "Toast", "خبز", "Khubz", "Pan", "Pahn", "Pain", "Pan", "Toast", "Toast", "Pane", "PAH-neh", "Torrada", "Toh-RAH-dah", "Тост", "Tost", "Tost", "Tost", "Roti", "Roh-tee", "吐司", "Tǔsī", "トースト", "Tōsuto", "토스트", "Toseuteu"),
    sw("Milk", "دودھ", "Doodh", "दूध", "Doodh", "حليب", "Halib", "Leche", "LEH-cheh", "Lait", "Leh", "Milch", "Milkh", "Latte", "LAHT-teh", "Leite", "LAY-chee", "Молоко", "Mah-lah-KOH", "Süt", "Sewt", "Susu", "Soo-soo", "牛奶", "Niúnǎi", "ミルク", "Miruku", "우유", "Uyu"),
    sw("Juice", "جوس", "Juice", "जूस", "Juice", "عصير", "'Asir", "Jugo", "HOO-goh", "Jus", "Zhoo", "Saft", "Zahft", "Succo", "SOOK-koh", "Suco", "SOO-koo", "Сок", "Sohk", "Meyvesuyu", "Mey-veh-soo-yoo", "Jus", "Joos", "果汁", "Guǒzhī", "ジュース", "Jūsu", "주스", "Juseu")
]

# 2. lunch-dinner
d["lunch-dinner"] = [
    sw("Soup", "سوپ", "Soup", "सूप", "Soup", "حساء", "Hisa'", "Sopa", "SOH-pah", "Soupe", "Soop", "Suppe", "ZUP-peh", "Zuppa", "DZOOP-pah", "Sopa", "SOH-pah", "Суп", "Soop", "Çorba", "Chor-bah", "Sup", "Soop", "热汤", "Rètāng", "スープ", "Sūpu", "수프", "Supeu"),
    sw("Rice", "چاول", "Chawal", "चावल", "Chawal", "أرز", "Aruz", "Arroz", "ah-RROHS", "Riz", "Ree", "Reis", "Rye-ss", "Riso", "REE-zoh", "Arroz", "ah-HOYZ", "Рис", "Rees", "Pilav", "Pee-lahv", "Nasi", "Nah-see", "米饭", "Mǐfàn", "ごはん", "Gohan", "밥", "Bap"),
    sw("Bread", "روٹی", "Roti", "रोटी", "Roti", "رغيف", "Raghif", "Pan", "Pahn", "Pain", "Pan", "Brot", "Broht", "Pane", "PAH-neh", "Pão", "Pow", "Хлеб", "Khlyeb", "Ekmek", "Ek-mek", "Roti", "Roh-tee", "面包", "Miànbāo", "パン", "Pan", "빵", "Ppang")
]

# 3. kitchen-help
d["kitchen-help"] = [
    sw("Plate", "پلیٹ", "Plate", "प्लेट", "Plate", "صحن", "Sahn", "Plato", "PLAH-toh", "Assiette", "Ah-syet", "Teller", "TEL-ler", "Piatto", "PYAHT-toh", "Prato", "PRAH-too", "Тарелка", "Tah-RYEL-kah", "Tabak", "Tah-bahk", "Piring", "Pee-reeng", "盘子", "Pánzi", "お皿", "Osara", "접시", "Jeopsi"),
    sw("Spoon", "چمچ", "Chamach", "चम्मच", "Chammach", "ملعقة", "Mil'aqa", "Cuchara", "Koo-CHAH-rah", "Cuillère", "Kwee-yehr", "Löffel", "LERF-fel", "Cucchiaio", "Kook-KYAH-yoh", "Colher", "Kohl-YEHR", "Ложка", "LOHZH-kah", "Kaşık", "Kah-shuk", "Sendok", "Sehn-dohk", "勺子", "Sháozi", "スプーン", "Supūn", "숟가락", "Sutgarak"),
    sw("Towel", "تولیہ", "Toliya", "तौलिया", "Tauliya", "منشفة", "Minshafa", "Toalla", "Toh-AH-yah", "Serviette", "Sehr-vyet", "Handtuch", "HAHNT-tookh", "Asciugamano", "Ah-shoo-gah-MAH-noh", "Toalha", "Toh-AHL-yah", "Полотенце", "Pah-lah-TYEHN-tseh", "Havlu", "Hahv-loo", "Handuk", "Hahn-dook", "毛巾", "Máojīn", "タオル", "Taoru", "수건", "Sugeon")
]

# 4. bedtime-stories
d["bedtime-stories"] = [
    sw("Pillow", "تکیہ", "Takiya", "तकिया", "Takiya", "وسادة", "Wisada", "Almohada", "Ahl-moh-AH-dah", "Oreiller", "Oh-ray-yay", "Kissen", "KIS-sen", "Cuscino", "Koo-SHEE-noh", "Travesseiro", "Trah-veh-SAY-roo", "Подушка", "Pah-DOOSH-kah", "Yastık", "Yahs-tuk", "Bantal", "Bahn-tahl", "枕头", "Zhěntou", "まくら", "Makura", "베개", "Begae"),
    sw("Blanket", "کمبل", "Kambal", "कंबल", "Kambal", "غطاء", "Ghita'", "Manta", "MAHN-tah", "Couverture", "Koo-vehr-toor", "Decke", "DEK-keh", "Coperta", "Koh-PEHR-tah", "Cobertor", "Koh-behr-TOHR", "Одеяло", "Ah-dyeh-YAH-lah", "Battaniye", "Baht-tah-nee-yeh", "Selimut", "Seh-lee-moot", "被子", "Bèizi", "もうふ", "Mōfu", "담요", "Damyo"),
    sw("Dreams", "خواب", "Khwaab", "सपने", "Sapne", "أحلام", "Ahlam", "Sueños", "SWEH-nyohs", "Rêves", "Rehv", "Träume", "TROY-meh", "Sogni", "SOH-nyee", "Sonhos", "SOHN-yoos", "Сны", "Sny", "Rüyalar", "Rew-yah-lahr", "Mimpi", "Meem-pee", "美梦", "Měimèng", "ゆめ", "Yume", "꿈", "Kkum")
]

# 5. morning-talk
d["morning-talk"] = [
    sw("Sun", "سورج", "Sooraj", "सूरज", "Sooraj", "شمس", "Shams", "Sol", "Sohl", "Soleil", "Soh-lay", "Sonne", "ZON-neh", "Sole", "SOH-leh", "Sol", "SOHL", "Солнце", "SOHN-tseh", "Güneş", "Gew-nesh", "Matahari", "Mah-tah-hah-ree", "太阳", "Tàiyáng", "たいよう", "Taiyō", "햇살", "Haetsal"),
    sw("Air", "ہوا", "Hawa", "हवा", "Hawa", "هواء", "Hawa'", "Aire", "EYE-reh", "Air", "Ehr", "Luft", "Looft", "Aria", "AH-ryah", "Ar", "AHR", "Воздух", "VOHZ-dookh", "Hava", "Hah-vah", "Udara", "Oo-dah-rah", "空气", "Kōngqì", "くうき", "Kūki", "공기", "Gonggi"),
    sw("Morning", "صبح", "Subah", "सुबह", "Subah", "صباح", "Sabah", "Mañana", "Mah-NYAH-nah", "Matin", "Mah-tan", "Morgen", "MOR-gen", "Mattina", "Maht-TEE-nah", "Manhã", "Mahn-YAHN", "Утро", "OO-trah", "Sabah", "Sah-bah", "Pagi", "Pah-gee", "早晨", "Zǎochén", "あさ", "Asa", "아침", "Achim")
]

# 6. evening-tea
d["evening-tea"] = [
    sw("Tea", "چائے", "Chai", "चाय", "Chai", "شاي", "Shay", "Té", "Teh", "Thé", "Tay", "Tee", "Tay", "Tè", "Teh", "Chá", "Shah", "Чай", "Chy", "Çay", "Chy", "Teh", "Teh", "茶", "Chá", "おちゃ", "Ocha", "차", "Cha"),
    sw("Biscuit", "بسکٹ", "Biscuit", "बिस्कुट", "Biscuit", "بسكويت", "Baskawit", "Galleta", "Gah-YEH-tah", "Biscuit", "Bees-kwee", "Keks", "Kayks", "Biscotto", "Bees-KOHT-toh", "Biscoito", "Bees-KOY-too", "Печенье", "Pyeh-CHEHN-yeh", "Bisküvi", "Bees-kew-vee", "Biskuit", "Bees-koo-eet", "饼干", "Bǐnggān", "クッキー", "Kukkī", "과자", "Gwaja"),
    sw("Evening", "شام", "Shaam", "शाम", "Shaam", "مساء", "Masa'", "Tarde", "TAR-deh", "Soir", "Swahr", "Abend", "AH-bent", "Sera", "SEH-rah", "Tarde", "TAHR-jee", "Вечер", "VYEH-cheer", "Akşam", "Ahk-shahm", "Sore", "Soh-reh", "傍晚", "Bàngwǎn", "ゆうがた", "Yūgata", "저녁", "Jeonyeok")
]

# 7. mom-and-dad
d["mom-and-dad"] = [
    sw("Mom", "امی", "Ammi", "माँ", "Maa", "أم", "Umm", "Mamá", "Mah-MAH", "Maman", "Mah-mahn", "Mama", "MAH-mah", "Mamma", "MAHM-mah", "Mãe", "Mye", "Мама", "MAH-mah", "Anne", "Ahn-neh", "Ibu", "Ee-boo", "妈妈", "Māmā", "おかあさん", "Okāsan", "엄마", "Eomma"),
    sw("Dad", "ابو", "Abbu", "पापा", "Papa", "أب", "Ab", "Papá", "Pah-PAH", "Papa", "Pah-pah", "Papa", "PAH-pah", "Papà", "Pah-PAH", "Pai", "Pye", "Папа", "PAH-pah", "Baba", "Bah-bah", "Ayah", "Ah-yah", "爸爸", "Bàba", "おとうさん", "Otōsan", "아빠", "Appa"),
    sw("Home", "گھر", "Ghar", "घर", "Ghar", "بيت", "Bayt", "Hogar", "Oh-GAHR", "Foyer", "Fwah-yay", "Zuhause", "Tsoo-HOW-zeh", "Casa", "KAH-zah", "Lar", "Lahr", "Дом", "Dohm", "Ev", "Ev", "Rumah", "Roo-mah", "家", "Jiā", "おうち", "Ouchi", "우리집", "Urijip")
]

# 8. grandparents-chat
d["grandparents-chat"] = [
    sw("Grandpa", "دادا", "Daada", "दादा", "Dada", "جد", "Jadd", "Abuelo", "Ah-BWEH-loh", "Papi", "Pah-pee", "Opa", "OH-pah", "Nonno", "NOHN-noh", "Vovô", "Voh-VOH", "Дедушка", "DYEH-doosh-kah", "Dede", "Deh-deh", "Kakek", "Kah-kehk", "爷爷", "Yéyé", "おじいちゃん", "Ojiichan", "할아버지", "Harabeoji"),
    sw("Grandma", "دادی", "Daadi", "दादी", "Daadi", "جدة", "Jadda", "Abuela", "Ah-BWEH-lah", "Mamie", "Mah-mee", "Oma", "OH-mah", "Nonna", "NOHN-nah", "Vovó", "Voh-VAW", "Бабушка", "BAH-boosh-kah", "Nine", "Nee-neh", "Nenek", "Neh-nehk", "奶奶", "Nǎinai", "おばあちゃん", "Obāchan", "할머니", "Halmeoni"),
    sw("Story", "کہانی", "Kahani", "कहानी", "Kahani", "قصة", "Qissa", "Cuento", "KWEHN-toh", "Conte", "Kohnt", "Märchen", "MEHR-khen", "Favola", "FAH-voh-lah", "História", "Ees-TAW-ryah", "Сказка", "SKAHS-kah", "Masal", "Mah-sahl", "Cerita", "Cheh-ree-tah", "故事", "Gùshi", "おはなし", "Ohanashi", "이야기", "Iyagi")
]

# 9. morning-with-aunt
d["morning-with-aunt"] = [
    sw("Aunt", "خالہ", "Khaala", "मौसी", "Mausi", "خالة", "Khala", "Tía", "TEE-ah", "Tante", "Tahnt", "Tante", "TAHN-teh", "Zia", "DZEE-ah", "Tia", "CHEE-ah", "Тётя", "TYOH-tyah", "Teyze", "Tey-zeh", "Tante", "Tahn-teh", "姑姑", "Gūgu", "おばさん", "Obasan", "이모", "Imo"),
    sw("Pastry", "پیسٹری", "Pastry", "पेस्ट्री", "Pastry", "فطيرة", "Fatira", "Pastel", "Pahs-TEHL", "Gâteau", "Gah-toh", "Gebäck", "Geh-BEK", "Dolce", "DOHL-cheh", "Doce", "DOH-see", "Выпечка", "VY-pyech-kah", "Çörek", "Cher-rek", "Kue", "Koo-eh", "点心", "Diǎnxin", "おかし", "Okashi", "과자", "Gwaja"),
    sw("Balcony", "بالکونی", "Balcony", "बालकनी", "Balcony", "شرفة", "Shurfa", "Balcón", "Bahl-KOHN", "Balcon", "Bahl-kohn", "Balkon", "bahl-KOHN", "Balcone", "Bahl-KOH-neh", "Varanda", "Vah-RAHN-dah", "Балкон", "Bahl-KOHN", "Balkon", "Bahl-kohn", "Balkon", "Bahl-kohn", "阳台", "Yángtái", "ベランダ", "Beranda", "발코니", "Balkoni")
]

# 10. dinner-with-uncle
d["dinner-with-uncle"] = [
    sw("Uncle", "چچا", "Chacha", "चाचा", "Chacha", "عم", "'Amm", "Tío", "TEE-oh", "Oncle", "Ohn-kluh", "Onkel", "OHN-kel", "Zio", "DZEE-oh", "Tio", "CHEE-oo", "Дядя", "DYAH-dyah", "Amca", "Ahm-jah", "Paman", "Pah-mahn", "叔叔", "Shūshu", "おじさん", "Ojisan", "삼촌", "Samchon"),
    sw("Meat", "گوشت", "Gosht", "गोश्त", "Gosht", "لحم", "Lahm", "Carne", "KAR-neh", "Viande", "Vyahn-duh", "Fleisch", "Flysh", "Carne", "KAHR-neh", "Carne", "KAR-nee", "Мясо", "MYAH-sah", "Et", "Et", "Daging", "Dah-geeng", "烤肉", "Kǎoròu", "おにく", "Oniku", "고기", "Gogi"),
    sw("Laugh", "قہقہہ", "Qehqaha", "ठहाका", "Thahaaka", "ضحكة", "Dihka", "Risa", "REE-sah", "Rire", "Reer", "Lachen", "LAH-khen", "Risata", "Ree-ZAH-tah", "Risada", "Hee-ZAH-dah", "Смех", "Smyekh", "Kahkaha", "Kahk-hah-hah", "Tawa", "Tah-wah", "笑声", "Xiàoshēng", "わらい", "Warai", "웃음", "Useum")
]

# 11. big-feelings
d["big-feelings"] = [
    sw("Smile", "مسکراہٹ", "Muskurahat", "मुस्कान", "Muskaan", "بسمة", "Basma", "Sonrisa", "Sohn-REE-sah", "Sourire", "Soo-reer", "Lächeln", "LEKH-eln", "Sorriso", "Sohr-REE-zoh", "Sorriso", "Sohr-HEE-zoo", "Улыбка", "Oo-LYP-kah", "Tebessüm", "Teh-behs-sewm", "Senyum", "Sehn-yoom", "微笑", "Wēixiào", "えがお", "Egao", "미소", "Miso"),
    sw("Peace", "سکون", "Sukoon", "शांति", "Shaanti", "راحة", "Raha", "Calma", "KAHL-mah", "Calme", "Kahlm", "Ruhe", "ROO-heh", "Calma", "KAHL-mah", "Paz", "Pahs", "Покой", "Pah-KOY", "Huzur", "Hoo-zoor", "Tenang", "Teh-nahng", "心境", "Xīnjìng", "おだやか", "Odayaka", "평온", "Pyeong-on"),
    sw("Hug", "جھپی", "Jhappi", "झप्पी", "Jhappi", "عناق", "'Inaq", "Abrazo", "Ah-BRAH-zoh", "Câlin", "Kah-lan", "Umarmung", "Oom-AHR-moong", "Abbraccio", "Ahb-BRAHT-choh", "Abraço", "Ah-BRAH-soo", "Объятия", "Ahb-YAH-tyah", "Kucak", "Koo-jahk", "Pelukan", "Peh-look-ahn", "抱抱", "Bàobào", "ハグ", "Hagu", "포옹", "Poong")
]

# 12. bus-station
d["bus-station"] = [
    sw("Bus", "بس", "Bus", "बस", "Bus", "حافلة", "Hafila", "Autobús", "Ow-toh-BOOS", "Bus", "Boos", "Bus", "Boos", "Autobus", "OW-toh-boos", "Ônibus", "OH-nee-boos", "Автобус", "Ahv-TOH-boos", "Otobüs", "Oh-toh-bews", "Bus", "Boos", "巴士", "Bāshì", "バス", "Basu", "버스", "Beoseu"),
    sw("Ride", "سفر", "Safar", "सफ़र", "Safar", "رحلة", "Rihla", "Viaje", "VYAH-heh", "Trajet", "Trah-zhay", "Fahrt", "Fahrt", "Corsa", "KOHR-sah", "Passeio", "Pah-SAY-oo", "Поездка", "Pah-YEZD-kah", "Yolculuk", "Yohl-joo-look", "Perjalanan", "Pehr-jah-lahn-ahn", "车次", "Chēcì", "ドライブ", "Doraibu", "주행", "Juhaeng"),
    sw("Seat", "سیٹ", "Seat", "सीट", "Seat", "مقعد", "Maq'ad", "Asiento", "Ah-SYEHN-toh", "Place", "Plahs", "Sitz", "Zits", "Posto", "POHS-toh", "Lugar", "Loo-GAHR", "Место", "MYEHS-tah", "Koltuk", "Kohl-took", "Kursi", "Koor-see", "座位", "Zuòwèi", "せき", "Seki", "좌석", "Jwaseok")
]

# 13. train-tickets
d["train-tickets"] = [
    sw("Train", "ٹرین", "Train", "ट्रेन", "Train", "قطار", "Qitar", "Tren", "Trehn", "Train", "Tran", "Zug", "Tsook", "Treno", "TREH-noh", "Trem", "Trehng", "Поезд", "POY-yezd", "Tren", "Trehn", "Kereta", "Keh-reh-tah", "火车", "Huǒchē", "でんしゃ", "Densha", "기차", "Gicha"),
    sw("Track", "پٹری", "Patri", "पटरी", "Patri", "سكة", "Sikka", "Vía", "VEE-ah", "Rail", "Rye", "Gleis", "Glyss", "Binario", "Bee-NAH-ryoh", "Trilho", "TREEL-yoo", "Рельсы", "RYEHL-sy", "Ray", "Rye", "Rel", "Rehl", "铁轨", "Tiěguǐ", "せんろ", "Senro", "철길", "Cheolgil"),
    sw("Window", "کھڑکی", "Khirki", "खिड़की", "Khidki", "نافذة", "Nafida", "Ventana", "Vehn-TAH-nah", "Fenêtre", "Feh-net-ruh", "Fenster", "FEN-ster", "Finestra", "Fee-NEHS-trah", "Janela", "Zhah-NEH-lah", "Окно", "Ahk-NOH", "Pencere", "Pen-djeh-reh", "Jendela", "Jehn-deh-lah", "车窗", "Chēchuāng", "まど", "Mado", "창문", "Changmun")
]

# 14. in-a-taxi
d["in-a-taxi"] = [
    sw("Taxi", "ٹیکسی", "Taxi", "टैक्सी", "Taxi", "تاكسي", "Taksi", "Taxi", "TAHK-see", "Taxi", "Tahk-see", "Taxi", "TAHK-see", "Taxi", "TAHK-see", "Táxi", "TAHK-see", "Такси", "Tahk-SEE", "Taksi", "Tahk-see", "Taksi", "Tahk-see", "出租车", "Chūzūchē", "タクシー", "Takushī", "택시", "Taeksi"),
    sw("Driver", "ڈرائیور", "Driver", "ड्राइवर", "Driver", "سائق", "Sa'iq", "Chofer", "Choh-FEHR", "Chauffeur", "Shoh-fuhr", "Fahrer", "FAH-rer", "Autista", "Ow-TEES-tah", "Motorista", "Moh-toh-REES-tah", "Шофёр", "Shah-FYOHR", "Şoför", "Shoh-fehr", "Sopir", "Soh-peer", "司机", "Sījī", "うんてんしゅ", "Untenshu", "기사님", "Gissanim"),
    sw("Belt", "بیلٹ", "Belt", "बेल्ट", "Belt", "حزام", "Hizam", "Cinturón", "Seen-too-ROHN", "Ceinture", "San-toor", "Gurt", "Goort", "Cintura", "Cheen-TOO-rah", "Cinto", "SEEN-too", "Ремень", "Ryeh-MYEN", "Kemer", "Keh-mehr", "Sabuk", "Sah-book", "安全带", "Ānquándài", "ベルト", "Beruto", "안전벨트", "Anjeonbelteu")
]

# 15. airplane-flight
d["airplane-flight"] = [
    sw("Plane", "جہاز", "Jahaaz", "हवाईजहाज़", "Hawaijahaaz", "طائرة", "Ta'ira", "Avión", "Ah-VYOHN", "Avion", "Ah-vyohn", "Flugzeug", "FLOOK-tsoyk", "Aereo", "Ah-EH-reh-oh", "Avião", "Ah-VYEE-ow", "Самолёт", "Sah-mah-LYOHT", "Uçak", "Oo-chahk", "Pesawat", "Peh-sah-waht", "飞机", "Fēijī", "ひこうき", "Hikōki", "비행기", "Bihaenggi"),
    sw("Cloud", "بادل", "Baadal", "बादल", "Baadal", "سحاب", "Sahab", "Nube", "NOO-beh", "Nuage", "Noo-ahzh", "Wolke", "VOL-keh", "Nuvola", "NOO-voh-lah", "Nuvem", "NOO-veng", "Облако", "OHB-lah-kah", "Bulut", "Boo-loot", "Awan", "Ah-wahn", "云朵", "Yúnduǒ", "くも", "Kumo", "구름", "Gureum"),
    sw("Sky", "آسمان", "Aasmaan", "आसमान", "Aasmaan", "سماء", "Sama'", "Cielo", "SYEH-loh", "Ciel", "Syel", "Himmel", "HIM-mel", "Cielo", "CHEH-loh", "Céu", "SEH-oo", "Небо", "NYEH-bah", "Gökyüzü", "Gerk-yew-zew", "Langit", "Lahng-eet", "天空", "Tiānkōng", "そら", "Sora", "하늘", "Haneul")
]

# 16. asking-directions
d["asking-directions"] = [
    sw("Map", "نقشہ", "Naqsha", "नक्शा", "Naksha", "خريطة", "Kharita", "Mapa", "MAH-pah", "Carte", "Kahrt", "Karte", "KAHR-teh", "Mappa", "MAHP-pah", "Mapa", "MAH-pah", "Карта", "KAHR-tah", "Harita", "Hah-ree-tah", "Peta", "Peh-tah", "地图", "Dìtú", "ちず", "Chizu", "지도", "Jido"),
    sw("Park", "پارک", "Park", "पार्क", "Park", "حديقة", "Hadiqa", "Parque", "PAR-keh", "Parc", "Pahrk", "Park", "Pahrk", "Parco", "PAR-koh", "Parque", "PAR-kee", "Парк", "Pahrk", "Park", "Pahrk", "Taman", "Tah-mahn", "公园", "Gōngyuán", "こうえん", "Kōen", "공원", "Gongwon"),
    sw("Street", "سڑک", "Sarak", "सड़क", "Sadak", "شارع", "Shari'", "Calle", "KAH-yeh", "Rue", "Roo", "Straße", "SHTRAH-seh", "Strada", "STRAH-dah", "Rua", "HOO-ah", "Улица", "OO-lee-tsah", "Sokak", "Soh-kahk", "Jalan", "Jah-lahn", "街道", "Jiēdào", "みち", "Michi", "거리", "Geori")
]

# Helper for other categories
# We can load the nouns directly from all 77 topics in cat1..cat5!
