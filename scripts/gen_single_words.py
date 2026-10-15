import os
import json

def sword(en, ur, ur_rom, hi, hi_rom, ar, ar_rom, es, es_rom, fr, fr_rom, de, de_rom, it, it_rom, pt, pt_rom, ru, ru_rom, tr, tr_rom, id_val, id_rom, zh, zh_rom, ja, ja_rom, ko, ko_rom):
    return {
        "en": en,
        "target": {
            "en": en,
            "ur": ur,
            "hi": hi,
            "ar": ar,
            "es": es,
            "fr": fr,
            "de": de,
            "it": it,
            "pt": pt,
            "ru": ru,
            "tr": tr,
            "id": id_val,
            "zh": zh,
            "ja": ja,
            "ko": ko
        },
        "romanized": {
            "en": en,
            "ur": ur_rom,
            "hi": hi_rom,
            "ar": ar_rom,
            "es": es_rom,
            "fr": fr_rom,
            "de": de_rom,
            "it": it_rom,
            "pt": pt_rom,
            "ru": ru_rom,
            "tr": tr_rom,
            "id": id_rom,
            "zh": zh_rom,
            "ja": ja_rom,
            "ko": ko_rom
        }
    }

words = {}

# 1. breakfast-chat
words["breakfast-chat"] = [
    sword("Toast", "ٹوسٹ", "Toast", "टोस्ट", "Toast", "خبز", "Khubz", "Pan", "Pahn", "Pain", "Pan", "Toast", "Toast", "Pane", "PAH-neh", "Torrada", "Toh-RAH-dah", "Тост", "Tost", "Tost", "Tost", "Roti", "Roh-tee", "吐司", "Tǔsī", "トースト", "Tōsuto", "토스트", "Toseuteu"),
    sword("Milk", "دودھ", "Doodh", "दूध", "Doodh", "حليب", "Halib", "Leche", "LEH-cheh", "Lait", "Leh", "Milch", "Milkh", "Latte", "LAHT-teh", "Leite", "LAY-chee", "Молоко", "Mah-lah-KOH", "Süt", "Sewt", "Susu", "Soo-soo", "牛奶", "Niúnǎi", "ミルク", "Miruku", "우유", "Uyu"),
    sword("Juice", "جوس", "Juice", "जूस", "Juice", "عصير", "'Asir", "Jugo", "HOO-goh", "Jus", "Zhoo", "Saft", "Zahft", "Succo", "SOOK-koh", "Suco", "SOO-koo", "Сок", "Sohk", "Meyvesuyu", "Mey-veh-soo-yoo", "Jus", "Joos", "果汁", "Guǒzhī", "ジュース", "Jūsu", "주스", "Juseu")
]

# 2. lunch-dinner
words["lunch-dinner"] = [
    sword("Soup", "سوپ", "Soup", "सूप", "Soup", "حساء", "Hisa'", "Sopa", "SOH-pah", "Soupe", "Soop", "Suppe", "ZUP-peh", "Zuppa", "DZOOP-pah", "Sopa", "SOH-pah", "Суп", "Soop", "Çorba", "Chor-bah", "Sup", "Soop", "热汤", "Rètāng", "スープ", "Sūpu", "수프", "Supeu"),
    sword("Rice", "چاول", "Chawal", "चावल", "Chawal", "أرز", "Aruz", "Arroz", "ah-RROHS", "Riz", "Ree", "Reis", "Rye-ss", "Riso", "REE-zoh", "Arroz", "ah-HOYZ", "Рис", "Rees", "Pilav", "Pee-lahv", "Nasi", "Nah-see", "米饭", "Mǐfàn", "ごはん", "Gohan", "밥", "Bap"),
    sword("Bread", "روٹی", "Roti", "रोटी", "Roti", "رغيف", "Raghif", "Pan", "Pahn", "Pain", "Pan", "Brot", "Broht", "Pane", "PAH-neh", "Pão", "Pow", "Хлеб", "Khlyeb", "Ekmek", "Ek-mek", "Roti", "Roh-tee", "面包", "Miànbāo", "パン", "Pan", "빵", "Ppang")
]

# 3. kitchen-help
words["kitchen-help"] = [
    sword("Plate", "پلیٹ", "Plate", "प्लेट", "Plate", "صحن", "Sahn", "Plato", "PLAH-toh", "Assiette", "Ah-syet", "Teller", "TEL-ler", "Piatto", "PYAHT-toh", "Prato", "PRAH-too", "Тарелка", "Tah-RYEL-kah", "Tabak", "Tah-bahk", "Piring", "Pee-reeng", "盘子", "Pánzi", "お皿", "Osara", "접시", "Jeopsi"),
    sword("Spoon", "چمچ", "Chamach", "चम्मच", "Chammach", "ملعقة", "Mil'aqa", "Cuchara", "Koo-CHAH-rah", "Cuillère", "Kwee-yehr", "Löffel", "LERF-fel", "Cucchiaio", "Kook-KYAH-yoh", "Colher", "Kohl-YEHR", "Ложка", "LOHZH-kah", "Kaşık", "Kah-shuk", "Sendok", "Sehn-dohk", "勺子", "Sháozi", "スプーン", "Supūn", "숟가락", "Sutgarak"),
    sword("Towel", "تولیہ", "Toliya", "तौलिया", "Tauliya", "منشفة", "Minshafa", "Toalla", "Toh-AH-yah", "Serviette", "Sehr-vyet", "Handtuch", "HAHNT-tookh", "Asciugamano", "Ah-shoo-gah-MAH-noh", "Toalha", "Toh-AHL-yah", "Полотенце", "Pah-lah-TYEHN-tseh", "Havlu", "Hahv-loo", "Handuk", "Hahn-dook", "毛巾", "Máojīn", "タオル", "Taoru", "수건", "Sugeon")
]

# 4. bedtime-stories
words["bedtime-stories"] = [
    sword("Pillow", "تکیہ", "Takiya", "तकिया", "Takiya", "وسادة", "Wisada", "Almohada", "Ahl-moh-AH-dah", "Oreiller", "Oh-ray-yay", "Kissen", "KIS-sen", "Cuscino", "Koo-SHEE-noh", "Travesseiro", "Trah-veh-SAY-roo", "Подушка", "Pah-DOOSH-kah", "Yastık", "Yahs-tuk", "Bantal", "Bahn-tahl", "枕头", "Zhěntou", "まくら", "Makura", "베개", "Begae"),
    sword("Blanket", "کمبل", "Kambal", "कंबल", "Kambal", "بطانية", "Bataniya", "Manta", "MAHN-tah", "Couverture", "Koo-vehr-toor", "Decke", "DEK-keh", "Coperta", "Koh-PEHR-tah", "Cobertor", "Koh-behr-TOHR", "Одеяло", "Ah-dyeh-YAH-lah", "Battaniye", "Baht-tah-nee-yeh", "Selimut", "Seh-lee-moot", "被子", "Bèizi", "もうふ", "Mōfu", "담요", "Damyo"),
    sword("Dreams", "خواب", "Khwaab", "सपने", "Sapne", "أحلام", "Ahlam", "Sueños", "SWEH-nyohs", "Rêves", "Rehv", "Träume", "TROY-meh", "Sogni", "SOH-nyee", "Sonhos", "SOHN-yoos", "Сны", "Sny", "Rüyalar", "Rew-yah-lahr", "Mimpi", "Meem-pee", "美梦", "Měimèng", "ゆめ", "Yume", "꿈", "Kkum")
]

# 5. morning-talk
words["morning-talk"] = [
    sword("Sun", "سورج", "Sooraj", "सूरज", "Sooraj", "شمس", "Shams", "Sol", "Sohl", "Soleil", "Soh-lay", "Sonne", "ZON-neh", "Sole", "SOH-leh", "Sol", "SOHL", "Солнце", "SOHN-tseh", "Güneş", "Gew-nesh", "Matahari", "Mah-tah-hah-ree", "太阳", "Tàiyáng", "たいよう", "Taiyō", "햇살", "Haetsal"),
    sword("Air", "ہوا", "Hawa", "हवा", "Hawa", "هواء", "Hawa'", "Aire", "EYE-reh", "Air", "Ehr", "Luft", "Looft", "Aria", "AH-ryah", "Ar", "AHR", "Воздух", "VOHZ-dookh", "Hava", "Hah-vah", "Udara", "Oo-dah-rah", "空气", "Kōngqì", "くうき", "Kūki", "공기", "Gonggi"),
    sword("Morning", "صبح", "Subah", "सुबह", "Subah", "صباح", "Sabah", "Mañana", "Mah-NYAH-nah", "Matin", "Mah-tan", "Morgen", "MOR-gen", "Mattina", "Maht-TEE-nah", "Manhã", "Mahn-YAHN", "Утро", "OO-trah", "Sabah", "Sah-bah", "Pagi", "Pah-gee", "早晨", "Zǎochén", "あさ", "Asa", "아침", "Achim")
]

# 6. evening-tea
words["evening-tea"] = [
    sword("Tea", "چائے", "Chai", "चाय", "Chai", "شاي", "Shay", "Té", "Teh", "Thé", "Tay", "Tee", "Tay", "Tè", "Teh", "Chá", "Shah", "Чай", "Chy", "Çay", "Chy", "Teh", "Teh", "茶", "Chá", "おちゃ", "Ocha", "차", "Cha"),
    sword("Biscuit", "بسکٹ", "Biscuit", "बिस्कुट", "Biscuit", "بسكويت", "Baskawit", "Galleta", "Gah-YEH-tah", "Biscuit", "Bees-kwee", "Keks", "Kayks", "Biscotto", "Bees-KOHT-toh", "Biscoito", "Bees-KOY-too", "Печенье", "Pyeh-CHEHN-yeh", "Bisküvi", "Bees-kew-vee", "Biskuit", "Bees-koo-eet", "饼干", "Bǐnggān", "クッキー", "Kukkī", "과자", "Gwaja"),
    sword("Evening", "شام", "Shaam", "शाम", "Shaam", "مساء", "Masa'", "Tarde", "TAR-deh", "Soir", "Swahr", "Abend", "AH-bent", "Sera", "SEH-rah", "Tarde", "TAHR-jee", "Вечер", "VYEH-cheer", "Akşam", "Ahk-shahm", "Sore", "Soh-reh", "傍晚", "Bàngwǎn", "ゆうがた", "Yūgata", "저녁", "Jeonyeok")
]

# 7. mom-and-dad
words["mom-and-dad"] = [
    sword("Mom", "امی", "Ammi", "माँ", "Maa", "أم", "Umm", "Mamá", "Mah-MAH", "Maman", "Mah-mahn", "Mama", "MAH-mah", "Mamma", "MAHM-mah", "Mãe", "Mye", "Мама", "MAH-mah", "Anne", "Ahn-neh", "Ibu", "Ee-boo", "妈妈", "Māmā", "おかあさん", "Okāsan", "엄마", "Eomma"),
    sword("Dad", "ابو", "Abbu", "पापा", "Papa", "أب", "Ab", "Papá", "Pah-PAH", "Papa", "Pah-pah", "Papa", "PAH-pah", "Papà", "Pah-PAH", "Pai", "Pye", "Папа", "PAH-pah", "Baba", "Bah-bah", "Ayah", "Ah-yah", "爸爸", "Bàba", "おとうさん", "Otōsan", "아빠", "Appa"),
    sword("Home", "گھر", "Ghar", "घर", "Ghar", "بيت", "Bayt", "Hogar", "Oh-GAHR", "Foyer", "Fwah-yay", "Zuhause", "Tsoo-HOW-zeh", "Casa", "KAH-zah", "Lar", "Lahr", "Дом", "Dohm", "Ev", "Ev", "Rumah", "Roo-mah", "家", "Jiā", "おうち", "Ouchi", "우리집", "Urijip")
]

# 8. grandparents-chat
words["grandparents-chat"] = [
    sword("Grandpa", "دادا", "Daada", "दादा", "Dada", "جد", "Jadd", "Abuelo", "Ah-BWEH-loh", "Papi", "Pah-pee", "Opa", "OH-pah", "Nonno", "NOHN-noh", "Vovô", "Voh-VOH", "Дедушка", "DYEH-doosh-kah", "Dede", "Deh-deh", "Kakek", "Kah-kehk", "爷爷", "Yéyé", "おじいちゃん", "Ojiichan", "할아버지", "Harabeoji"),
    sword("Grandma", "دادی", "Daadi", "दादी", "Daadi", "جدة", "Jadda", "Abuela", "Ah-BWEH-lah", "Mamie", "Mah-mee", "Oma", "OH-mah", "Nonna", "NOHN-nah", "Vovó", "Voh-VAW", "Бабушка", "BAH-boosh-kah", "Nine", "Nee-neh", "Nenek", "Neh-nehk", "奶奶", "Nǎinai", "おばあちゃん", "Obāchan", "할머니", "Halmeoni"),
    sword("Story", "کہانی", "Kahani", "कहानी", "Kahani", "قصة", "Qissa", "Cuento", "KWEHN-toh", "Conte", "Kohnt", "Märchen", "MEHR-khen", "Favola", "FAH-voh-lah", "História", "Ees-TAW-ryah", "Сказка", "SKAHS-kah", "Masal", "Mah-sahl", "Cerita", "Cheh-ree-tah", "故事", "Gùshi", "おはなし", "Ohanashi", "이야기", "Iyagi")
]

# 9. morning-with-aunt
words["morning-with-aunt"] = [
    sword("Aunt", "خالہ", "Khaala", "मौसी", "Mausi", "خالة", "Khala", "Tía", "TEE-ah", "Tante", "Tahnt", "Tante", "TAHN-teh", "Zia", "DZEE-ah", "Tia", "CHEE-ah", "Тётя", "TYOH-tyah", "Teyze", "Tey-zeh", "Tante", "Tahn-teh", "姑姑", "Gūgu", "おばさん", "Obasan", "이모", "Imo"),
    sword("Pastry", "پیسٹری", "Pastry", "पेस्ट्री", "Pastry", "فطيرة", "Fatira", "Pastel", "Pahs-TEHL", "Gâteau", "Gah-toh", "Gebäck", "Geh-BEK", "Dolce", "DOHL-cheh", "Doce", "DOH-see", "Выпечка", "VY-pyech-kah", "Çörek", "Cher-rek", "Kue", "Koo-eh", "点心", "Diǎnxin", "おかし", "Okashi", "과자", "Gwaja"),
    sword("Balcony", "بالکونی", "Balcony", "बालकनी", "Balcony", "شرفة", "Shurfa", "Balcón", "Bahl-KOHN", "Balcon", "Bahl-kohn", "Balkon", "bahl-KOHN", "Balcone", "Bahl-KOH-neh", "Varanda", "Vah-RAHN-dah", "Балкон", "Bahl-KOHN", "Balkon", "Bahl-kohn", "Balkon", "Bahl-kohn", "阳台", "Yángtái", "ベランダ", "Beranda", "발코니", "Balkoni")
]

# 10. dinner-with-uncle
words["dinner-with-uncle"] = [
    sword("Uncle", "چچا", "Chacha", "चाचा", "Chacha", "عم", "'Amm", "Tío", "TEE-oh", "Oncle", "Ohn-kluh", "Onkel", "OHN-kel", "Zio", "DZEE-oh", "Tio", "CHEE-oo", "Дядя", "DYAH-dyah", "Amca", "Ahm-jah", "Paman", "Pah-mahn", "叔叔", "Shūshu", "おじさん", "Ojisan", "삼촌", "Samchon"),
    sword("Meat", "گوشت", "Gosht", "गोश्त", "Gosht", "لحم", "Lahm", "Carne", "KAR-neh", "Viande", "Vyahn-duh", "Fleisch", "Flysh", "Carne", "KAHR-neh", "Carne", "KAR-nee", "Мясо", "MYAH-sah", "Et", "Et", "Daging", "Dah-geeng", "烤肉", "Kǎoròu", "おにく", "Oniku", "고기", "Gogi"),
    sword("Laugh", "قہقہہ", "Qehqaha", "ठहाका", "Thahaaka", "ضحكة", "Dihka", "Risa", "REE-sah", "Rire", "Reer", "Lachen", "LAH-khen", "Risata", "Ree-ZAH-tah", "Risada", "Hee-ZAH-dah", "Смех", "Smyekh", "Kahkaha", "Kahk-hah-hah", "Tawa", "Tah-wah", "笑声", "Xiàoshēng", "わらい", "Warai", "웃음", "Useum")
]

# Let's populate all 77 topics in single-words systematic dictionary
# Helper to write remaining topics
def add_topic(tid, w1_tuple, w2_tuple, w3_tuple):
    words[tid] = [sword(*w1_tuple), sword(*w2_tuple), sword(*w3_tuple)]

# We will generate all 77 topics systematically with clean 1-word tokens across 15 languages
