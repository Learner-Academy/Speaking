import json
import re
import os
import sys

sys.path.append(os.path.dirname(__file__))
from helper import item

# Load single words
with open('src/data/multilingual/topicSingleWordItems.ts', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'TOPIC_SINGLE_WORD_ITEMS[^{]+=\s*(\{[\s\S]*?\n\};)', text)
single_words = json.loads(m.group(1).rstrip(';'))

# Load W1 and W2
w1_all = {}
w2_all = {}

for cat_name in ['cat1_home_family_travel', 'cat2_shopping_health_school', 'cat3_friends_nature_manners', 'cat4_tech_weather_holidays', 'cat5_sports_clothes_chores']:
    path = f'src/data/multilingual/{cat_name}.ts'
    with open(path, 'r', encoding='utf-8') as f:
        c_text = f.read()
    
    m1 = re.search(r'export const CAT\d_W1[^{]+=\s*(\{[\s\S]*?\n\};)', c_text)
    if m1:
        w1_all.update(json.loads(m1.group(1).rstrip(';')))
    
    m2 = re.search(r'export const CAT\d_W2[^{]+=\s*(\{[\s\S]*?\n\};)', c_text)
    if m2:
        w2_all.update(json.loads(m2.group(1).rstrip(';')))

# List of topics from topics.ts
with open('src/data/topics.ts', 'r', encoding='utf-8') as f:
    topics_text = f.read()

topic_matches = re.findall(r'id:\s*[\'\"]([^\'\"]+)[\'\"]', topics_text)
all_topic_ids = list(dict.fromkeys(topic_matches))

w4_data = {}
tier2_data = {}
tier3_data = {}

# 1. breakfast-chat
w4_data["breakfast-chat"] = [
    item(
        "I want toast", "مجھے ٹوسٹ چاہیے", "Mujhe toast chahiye",
        "मुझे टोस्ट चाहिए", "Mujhe toast chahiye",
        "أريد خبزاً", "Ureed khubzan",
        "Quiero una tostada", "Kyeh-roh tohs-TAH-dah",
        "Je veux pain", "Zhe vuh pan",
        "Ich will Toast", "Ikh vill toast",
        "Voglio del pane", "VOH-lyoh dehl PAH-neh",
        "Quero uma torrada", "KEH-roo toh-RAH-dah",
        "Я хочу тост", "Yah khah-CHOO tost",
        "Tost istiyorum ben", "Tost ees-tee-YOH-room ben",
        "Saya mau roti", "Sah-yah mow roh-tee",
        "我 要 吐司", "Wǒ yào tǔsī",
        "トースト が ほしい", "Tōsuto ga hoshii",
        "토스트 주세요", "Toseuteu juseyo"
    ),
    item(
        "Milk is hot", "دودھ گرم ہے", "Doodh garam hai",
        "दूध गर्म है", "Doodh garm hai",
        "الحليب ساخن جداً", "Al-haleeb sakhin",
        "La leche caliente", "LEH-cheh kah-LYEHN-teh",
        "Le lait chaud", "Leh eh sho",
        "Milch ist warm", "Milkh ist vahrm",
        "Latte è caldo", "LAHT-teh eh KAHL-doh",
        "Leite está quente", "LAY-chee KEHN-chee",
        "Молоко очень горячее", "Mah-lah-KOH gah-RYAH-cheh-yeh",
        "Süt çok sıcaktır", "Sewt chohk suh-dzhak-tuhr",
        "Susu ini hangat", "Soo-soo ee-nee hahng-aht",
        "牛奶 很 温热", "Niúnǎi hěn wēnrè",
        "ミルク が あたたかい", "Miruku ga atatakai",
        "우유가 따뜻해요", "Uyuga ttatteut-haeyo"
    ),
    item(
        "Juice is sweet", "جوس میٹھا ہے", "Juice meetha hai",
        "जूस मीठा है", "Juice meetha hai",
        "العصير حلو جداً", "Al-'asir hilw",
        "El jugo dulce", "HOO-goh ehs DOOL-seh",
        "Le jus doux", "Zhoo eh doo",
        "Saft ist süß", "Zahft ist zews",
        "Succo è dolce", "SOOK-koh eh DOHL-cheh",
        "Suco é doce", "SOO-koo eh DOH-see",
        "Сок очень сладкий", "Sohk SLAHD-kiy",
        "Meyvesuyu çok tatlı", "Mey-veh-soo-yoo taht-luh",
        "Jus ini manis", "Joos ee-nee mah-nees",
        "果汁 很 甜美", "Guǒzhī hěn tiánměi",
        "ジュース が おいしい", "Jūsu ga oishii",
        "주스가 달콤해요", "Juseuga dalkom-haeyo"
    )
]

tier2_data["breakfast-chat"] = [
    item(
        "Please give me warm toast.", "مجھے گرم ٹوسٹ دے دیں۔", "Mujhe garam toast de dein.",
        "मुझे गरम टोस्ट दीजिए।", "Mujhe garam toast deejie.",
        "أعطني الخبز الدافئ رجاءً.", "'A'tini al-khubz al-dafi' raja'an.",
        "Por favor dame tostada caliente.", "Pohr fah-vohr DAH-meh tohs-TAH-dah.",
        "Donne-moi du pain chaud.", "Dohn-mwah dew pan sho.",
        "Gib mir bitte warmen Toast.", "Gib meer BIT-teh VAHR-men toast.",
        "Dammi del pane caldo per favore.", "DAHM-mee dehl PAH-neh KAHL-doh.",
        "Por favor me dê torrada quente.", "Pohr fah-VOHR mee day toh-RAH-dah.",
        "Дай мне пожалуйста тёплый тост.", "Day mnye pah-ZHAH-loo-stah TYOHP-lyy.",
        "Lütfen bana sıcak tost ver.", "LEWT-fen BAH-nah suh-DZHAHK tost vehr.",
        "Tolong beri saya roti hangat.", "TOH-lohng BEH-ree SAH-yah roh-tee.",
        "请 给我 热乎乎的 烤面包。", "Qǐng gěi wǒ rèhūhū de kǎomiànbāo.",
        "あたたかい トースト を ください。", "Atatakai tōsuto o kudasai.",
        "따뜻한 토스트를 주세요." , "Ttatteut-han toseuteu-reul juseyo."
    ),
    item(
        "I like drinking sweet milk.", "مجھے میٹھا دودھ پسند ہے۔", "Mujhe meetha doodh pasand hai.",
        "मुझे मीठा दूध पसंद है।", "Mujhe meetha doodh pasand hai.",
        "أحب شرب الحليب الحلو يومياً.", "Uhibbu shurba al-haleeb al-hulw.",
        "Me gusta tomar leche dulce.", "Meh GOOS-tah toh-MAHR LEH-cheh DOOL-seh.",
        "J'aime boire du lait doux.", "Zhem bwahr dew leh doo.",
        "Ich trinke gerne süße Milch.", "Ikh TRING-keh GER-neh ZEW-seh milkh.",
        "Mi piace bere latte dolce.", "Mee PYAH-cheh BEH-reh LAHT-teh DOHL-cheh.",
        "Eu gosto de beber leite doce.", "Eh-oo GOHS-too jee beh-BEHR LAY-chee.",
        "Я люблю пить сладкое молоко.", "Yah lyoo-BLYOO peet SLAHT-kah-yeh mah-lah-KOH.",
        "Tatlı süt içmeyi çok severim.", "TAHT-luh sewt eech-meh-yee chohk.",
        "Saya suka minum susu manis.", "SAH-yah SOO-kah MEE-noom SOO-soo.",
        "我 喜欢 喝 甜甜的 牛奶。", "Wǒ xǐhuān hē tiántián de niúnǎi.",
        "あまい ミルク を のむのが すき。", "Amai miruku o nomu no ga suki.",
        "달콤한 우유 마시는 것을 좋아해요.", "Dalkom-han uyu masineun geos-eul joahaeyo."
    ),
    item(
        "Let us drink cold juice.", "آئیں ٹھنڈا جوس پیتے ہیں۔", "Aaein thanda juice peete hain.",
        "आओ ठंडा जूस पीते हैं।", "Aao thanda juice peete hain.",
        "دعنا نشرب العصير البارد الآن.", "Da'na nashrab al-'asir al-barid.",
        "Vamos a tomar jugo frío.", "VAH-mohs ah toh-MAHR HOO-goh FREE-oh.",
        "Buvons un bon jus frais.", "Bew-vohn uhn bohn zhoo freh.",
        "Lasst uns kühlen Saft trinken.", "Lahst oons KEW-len zahft TRING-ken.",
        "Beviamo del succo fresco insieme.", "Beh-VYAH-moh dehl SOOK-koh FREHS-koh.",
        "Vamos tomar um suco gelado.", "VAH-moos toh-MAHR oom SOO-koo zheh-LAH-doo.",
        "Давай попьём вкусный холодный сок.", "Dah-VAY pahp-YOM VKOOS-nyy khah-LOHD-nyy.",
        "Hadi soğuk meyve suyu içelim.", "HAH-dee soh-OOK mey-veh soo-yoo.",
        "Ayo kita minum jus dingin.", "AH-yoh KEE-tah MEE-noom joos deeng-een.",
        "我们 一起 喝 冰凉 果汁。", "Wǒmen yīqǐ hē bīngliáng guǒzhī.",
        "つめたい ジュース を のもう。", "Tsumetai jūsu o nomō.",
        "시원한 주스를 함께 마셔요.", "Siwon-han juseu-reul hamkke masyeoyo."
    )
]

tier3_data["breakfast-chat"] = [
    item(
        "I eat breakfast with my family.", "میں گھر والوں کے ساتھ ناشتہ کرتا ہوں۔", "Main ghar walon ke sath nashta karta hoon.",
        "मैं परिवार के साथ नाश्ता करता हूँ।", "Main parivaar ke saath naashta karta hoon.",
        "أتناول وجبة الإفطار مع عائلتي دائماً.", "Atanawalu wajbata al-iftari ma'a 'a'ilati da'iman.",
        "Desayuno junto con toda mi familia.", "Deh-sah-YOO-noh HOON-toh kohn TOH-dah mee fah-MEE-lyah.",
        "Je prends le petit-déjeuner en famille.", "Zhuh prahn luh puh-tee-day-zhuh-nay ahn fah-mee.",
        "Ich frühstücke immer mit meiner Familie.", "Ikh FREW-stew-keh IM-mer mit MY-ner fah-MEE-lyeh.",
        "Faccio colazione insieme alla mia famiglia.", "FAHT-choh koh-lah-TSYOH-neh een-SYEH-meh AHL-lah MEE-ah fah-MEE-lyah.",
        "Tomo café da manhã com família.", "TOH-moo kah-FEH dah mahn-YAHN kohn fah-MEE-lyah.",
        "Я завтракаю вместе со своей семьёй.", "Yah ZAHF-trah-kah-yoo VMYES-tyeh sah svah-YEY seem-YOY.",
        "Ailemle birlikte güzel bir kahvaltı yapıyorum.", "Ah-ee-lehm-leh beer-leek-TEH gew-zehl beer kahh-vahl-TUH yah-puh-YOH-room.",
        "Saya sarapan bersama keluarga tercinta saya.", "SAH-yah sah-RAH-pahn behr-SAH-mah keh-loo-AHR-gah tehr-CHEEN-tah SAH-yah.",
        "我 和 家人 一起 吃 早餐。", "Wǒ hé jiārén yīqǐ chī zǎocān.",
        "かぞく と いっしょに あさごはん を たべる。", "Kazoku to issho ni asagohan o taberu.",
        "가족과 함께 아침 식사를 맛있게 해요.", "Gajok-gwa hamkke achim siksareul mas-issge haeyo."
    ),
    item(
        "We all enjoy breakfast together happily.", "ہم سب خوشی سے ناشتہ کرتے ہیں۔", "Hum sab khushi se nashta karte hain.",
        "हम सब खुशी से नाश्ता करते हैं।", "Hum sab khushi se naashta karte hain.",
        "نستمتع جميعاً بوجبة الإفطار بسعادة.", "Nastamti'u jamee'an bi-wajbati al-iftari bi-sa'adah.",
        "Disfrutamos juntos del desayuno con alegría.", "Dees-froo-TAH-mohs HOON-tohs dehl deh-sah-YOO-noh kohn ah-leh-GREE-ah.",
        "Nous profitons du petit-déjeuner tous ensemble.", "Noo proh-fee-tohn dew puh-tee-day-zhuh-nay toos ahn-sahmbl.",
        "Wir genießen das gemeinsame Frühstück sehr.", "Veer geh-NEE-sen dahs geh-MYN-zah-meh FREW-stewk zehr.",
        "Ci godiamo la colazione tutti insieme.", "Chee goh-DYAH-moh lah koh-lah-TSYOH-neh TOOT-tee een-SYEH-meh.",
        "Aproveitamos o café da manhã com alegria.", "Ah-proh-vay-TAH-moos oo kah-FEH dah mahn-YAHN kohn ah-leh-GREE-ah.",
        "Мы дружно наслаждаемся вкусным утренним завтраком.", "My DROOZH-nah nah-slahzh-DAH-yem-syah VKOOS-nym OOT-reen-neem ZAHF-trah-kohm.",
        "Hep birlikte neşeyle kahvaltımızın tadını çıkarıyoruz.", "Hehp beer-leek-TEH neh-shehy-leh kahh-vahl-tuh-muh-ZUN tah-duh-NUH chuh-kah-ruh-YOH-rooz.",
        "Kami menikmati sarapan pagi bersama dengan gembira.", "KAH-mee meh-neek-MAH-tee sah-RAH-pahn PAH-gee behr-SAH-mah dehng-ahn gehm-BEE-rah.",
        "我们 开心地 一起 享用 早餐。", "Wǒmen kāixīn de yīqǐ xiǎngyòng zǎocān.",
        "みんな で たのしく あさごはん を たべる。", "Minna de tanoshiku asagohan o taberu.",
        "우리 모두 즐겁게 아침 식사를 나눠요.", "Uri modu jeulgeopge achim siksareul nanwoyo."
    ),
    item(
        "My family loves drinking fresh milk.", "میرا خاندان تازہ دودھ شوق سے پیتا ہے۔", "Mera khandan taaza doodh shauq se peeta hai.",
        "मेरा परिवार ताज़ा दूध चाव से पीता है।", "Mera parivaar taaza doodh chaav se peeta hai.",
        "تحب عائلتي شرب الحليب الطازج يومياً.", "Tuhibbu 'a'ilati shurba al-haleeb al-tazij yawmiyan.",
        "A mi familia le encanta la leche.", "Ah mee fah-MEE-lyah leh ehn-KAHN-tah lah LEH-cheh.",
        "Ma famille adore boire du lait frais.", "Mah fah-mee ah-dohr bwahr dew leh freh.",
        "Meine Familie trinkt gerne frische Milch.", "MY-neh fah-MEE-lyeh trinkt GER-neh FRISH-eh milkh.",
        "La mia famiglia adora il latte fresco.", "Lah MEE-ah fah-MEE-lyah ah-DOH-rah eel LAHT-teh FREHS-koh.",
        "Minha família adora tomar leite fresco.", "MEEN-yah fah-MEE-lyah ah-DOH-rah toh-MAHR LAY-chee FREHS-koo.",
        "Моя семья очень любит свежее молоко.", "Mah-YAH seem-YAH OH-cheen LYOO-beet SVYEH-zheh-yeh mah-lah-KOH.",
        "Ailem taze süt içmeyi gerçekten çok sever.", "Ah-ee-lehm TAH-zeh sewt eech-meh-yee gehr-chehk-tehn chohk seh-vehr.",
        "Keluarga saya sangat suka minum susu segar.", "Keh-loo-AHR-gah SAH-yah SAHNG-aht SOO-kah MEE-noom SOO-soo seh-gahr.",
        "我的 家人 非常 喜欢 喝 鲜奶。", "Wǒ de jiārén fēicháng xǐhuān hē xiānnǎi.",
        "かぞく は しんせんな ミルク が だいすき。", "Kazoku wa shinsen na miruku ga daisuki.",
        "우리 가족은 신선한 우유를 정말 좋아해요.", "Uri gajog-eun sinseon-han uyureul jeongmal joahaeyo."
    )
]

# 2. morning-talk
w4_data["morning-talk"] = [
    item(
        "I want sun", "مجھے سورج چاہیے", "Mujhe sooraj chahiye",
        "मुझे सूरज चाहिए", "Mujhe sooraj chahiye",
        "أريد شمس الصباح", "Ureed shams al-sabah",
        "Quiero el sol", "Kyeh-roh ehl sohl",
        "Je veux du soleil", "Zhe vuh dew soh-lay",
        "Ich will Sonne", "Ikh vill ZON-neh",
        "Voglio il sole", "VOH-lyoh eel SOH-leh",
        "Quero o sol", "KEH-roo oo sohl",
        "Я хочу солнце", "Yah khah-CHOO SOHN-tseh",
        "Güneş istiyorum ben", "Gew-nesh ees-tee-YOH-room",
        "Saya mau matahari", "Sah-yah mow mah-tah-hah-ree",
        "我 要 太阳", "Wǒ yào tàiyáng",
        "たいよう が ほしい", "Taiyō ga hoshii",
        "햇살이 보고 싶어요", "Haessar-i bogo sipeoyo"
    ),
    item(
        "Air is fresh", "ہوا تازہ ہے", "Hawa taaza hai",
        "हवा ताज़ा है", "Hawa taaza hai",
        "الهواء نقي جداً", "Al-hawa' naqiy",
        "El aire es fresco", "Ehl EYE-reh ehs FREHS-koh",
        "L'air est frais", "Lehr eh freh",
        "Luft ist frisch", "Looft ist frish",
        "L'aria è fresca", "LAH-ryah eh FREHS-kah",
        "O ar é fresco", "Oo ahr eh FREHS-koo",
        "Воздух очень свежий", "VOHZ-dookh SVYEH-zhyy",
        "Hava çok temizdir", "Hah-vah teh-meez-deer",
        "Udara ini segar", "Oo-dah-rah ee-nee seh-gahr",
        "空气 很 清新", "Kōngqì hěn qīngxīn",
        "くうき が おいしい", "Kūki ga oishii",
        "공기가 참 맑아요", "Gonggiga cham malg-ayo"
    ),
    item(
        "Morning is bright", "صبح روشن ہے", "Subah roshan hai",
        "सुबह सुहानी है", "Subah suhani hai",
        "الصباح مشرق وجميل", "Al-sabahu mushriq",
        "La mañana es linda", "Lah mah-NYAH-nah ehs LEEN-dah",
        "Le matin est beau", "Luh mah-tan eh boh",
        "Der Morgen ist schön", "Dehr MOR-gen ist shern",
        "La mattina è bella", "Lah maht-TEE-nah eh BEHL-lah",
        "A manhã é linda", "Ah mahn-YAHN eh LEEN-dah",
        "Утро очень светлое", "OO-trah SVYEHT-lah-yeh",
        "Sabah çok aydınlıktır", "Sah-bah eye-duhn-luhk-tuhr",
        "Pagi ini cerah", "PAH-gee ee-nee cheh-rah",
        "早晨 很 明亮", "Zǎochén hěn míngliàng",
        "あさ が あかるい", "Asa ga akarui",
        "아침이 참 밝아요", "Achim-i cham balg-ayo"
    )
]

tier2_data["morning-talk"] = [
    item(
        "Please open window for sun.", "سورج کے لیے کھڑکی کھول دیں۔", "Sooraj ke liye khirki khol dein.",
        "सूरज के लिए खिड़की खोलिए।", "Sooraj ke liye khidki kholiye.",
        "افتح النافذة للشمس من فضلك.", "Iftah al-nafidhata li-sh-shams.",
        "Por favor abre la ventana al sol.", "Pohr fah-vohr AH-breh lah vehn-TAH-nah.",
        "Ouvre la fenêtre pour le soleil.", "Oovruh lah feh-netr poor luh soh-lay.",
        "Öffne bitte das Fenster zur Sonne.", "ERF-neh das FEN-ster tsoor ZON-neh.",
        "Apri la finestra per il sole.", "AH-pree lah fee-NEHS-trah pehr eel SOH-leh.",
        "Por favor abra a janela para o sol.", "Pohr fah-VOHR AH-brah ah zhah-NEH-lah.",
        "Открой окно навстречу тёплому солнцу.", "Aht-KROY ahk-NOH nahf-STRYEH-choo SOHN-tsoo.",
        "Güneş için lütfen pencereyi aç.", "Gew-nesh ee-cheen pehn-djeh-reh-yee ahch.",
        "Tolong buka jendela untuk sinar matahari.", "TOH-lohng BOO-kah jehn-DEH-lah.",
        "请 为 阳光 打开 窗户。", "Qǐng wèi yángguāng dǎkāi chuānghù.",
        "たいよう の ために まど を あけて。", "Taiyō no tame ni mado o akete.",
        "따스한 햇살을 위해 창문을 열어요.", "Ttaseuhan haessar-eul wihae changmun-eul yeoroyo."
    ),
    item(
        "I like breathing fresh morning air.", "مجھے صبح کی تازہ ہوا پسند ہے۔", "Mujhe subah ki taaza hawa pasand hai.",
        "मुझे सुबह की ताज़ा हवा पसंद है।", "Mujhe subah ki taaza hawa pasand hai.",
        "أحب تنفس هواء الصباح النقي.", "Uhibbu tanaffusa hawa'i al-sabah.",
        "Me gusta respirar aire fresco matutino.", "Meh GOOS-tah rehs-pee-RAHR EYE-reh FREHS-koh.",
        "J'aime respirer l'air frais du matin.", "Zhem rehs-pee-ray lehr freh dew mah-tan.",
        "Ich atme gerne frische Morgenluft.", "Ikh AHT-meh GER-neh FRISH-eh MOR-gen-looft.",
        "Mi piace respirare aria fresca mattutina.", "Mee PYAH-cheh rehs-pee-RAH-reh AH-ryah FREHS-kah.",
        "Eu gosto de respirar ar fresco.", "Eh-oo GOHS-too jee rehs-pee-RAHR ahr FREHS-koo.",
        "Я люблю дышать свежим утренним воздухом.", "Yah lyoo-BLYOO dy-SHAHT SVYEH-zheem OOT-reen-neem.",
        "Sabahın temiz havasını solumayı çok severim.", "Sah-bah-hun teh-meez hah-vah-suh-nuh chohk seh-vehr-eem.",
        "Saya suka menghirup udara pagi yang segar.", "SAH-yah mehng-HEE-roop oo-DAH-rah PAH-gee.",
        "我 喜欢 呼吸 早晨 新鲜 空气。", "Wǒ xǐhuān hūxī zǎochén xīnxiān kōngqì.",
        "あさ の しんせんな くうき が すき。", "Asa no shinsen na kūki ga suki.",
        "아침의 맑은 공기 마시는 걸 좋아해요.", "Achim-ui malgeun gonggi masineun geol joahaeyo."
    ),
    item(
        "Let us enjoy beautiful sunny morning.", "آئیں خوبصورت روشن صبح کا مزہ لیں۔", "Aaein khoobsurat roshan subah ka maza lein.",
        "आओ सुंदर सुनहरी सुबह का आनंद लें।", "Aao sundar sunahri subah ka anand lein.",
        "دعنا نستمتع بهذا الصباح المشرق الجميل.", "Da'na nastamti' bi-hadha al-sabahi al-mushriq.",
        "Vamos a disfrutar esta hermosa mañana.", "VAH-mohs ah dees-froo-TAHR EHS-tah ehr-MOH-sah.",
        "Profitons bien de ce beau matin ensoleillé.", "Proh-fee-tohn byan duh suh boh mah-tan.",
        "Lasst uns den schönen sonnigen Morgen genießen.", "Lahst oons dehn SHER-nen ZON-nee-gen MOR-gen.",
        "Godiamoci questa splendida mattinata di sole.", "Goh-DYAH-moh-chee KWEHS-tah SPLEHN-dee-dah.",
        "Vamos aproveitar esta linda manhã ensolarada.", "VAH-moos ah-proh-vay-TAHR EHS-tah LEEN-dah.",
        "Давай порадуемся этому прекрасному солнечному утру.", "Dah-VAY pah-RAH-dooy-syah eh-TOO-moo pryeh-KRAHS-nah-moo.",
        "Hadi bu güzel güneşli sabahın tadını çıkaralım.", "HAH-dee boo gew-zehl gew-nesh-lee sah-bah-hun.",
        "Ayo kita nikmati pagi cerah yang indah ini.", "AH-yoh KEE-tah neek-MAH-tee PAH-gee cheh-rah.",
        "我们 一起 享受 美丽 晴朗 早晨。", "Wǒmen yīqǐ xiǎngshòu měilì qínglǎng zǎochén.",
        "うつくしい はれの あさ を たのしもう。", "Utsukushii hare no asa o tanoshimō.",
        "아름답고 화창한 아침을 함께 즐겨요.", "Areumdapgo hwachang-han achim-eul hamkke jeulgyeoyo."
    )
]

tier3_data["morning-talk"] = [
    item(
        "I greet morning with my family.", "میں گھر والوں کے ساتھ صبح کا آغاز کرتا ہوں۔", "Main ghar walon ke sath subah ka aaghaz karta hoon.",
        "मैं परिवार के साथ सुबह की शुरुआत करता हूँ।", "Main parivaar ke saath subah ki shuruat karta hoon.",
        "أبدأ صباحي الجميل مع عائلتي كل يوم.", "Abda'u sabahi al-jameel ma'a 'a'ilati kulla yawm.",
        "Empiezo la mañana feliz junto a mi familia.", "Ehm-PYEH-soh lah mah-NYAH-nah feh-LEES kohn mee fah-MEE-lyah.",
        "Je commence le matin heureux avec ma famille.", "Zhuh koh-mahns luh mah-tan uh-ruh ah-vehk mah fah-mee.",
        "Ich beginne den Morgen glücklich mit meiner Familie.", "Ikh beh-GIN-neh dehn MOR-gen GLEWK-leekh mit MY-ner.",
        "Inizio la bella mattina insieme alla mia famiglia.", "Ee-NEE-tsyoh lah BEHL-lah maht-TEE-nah een-SYEH-meh.",
        "Começo a manhã feliz com a minha família.", "Koh-MEH-soo ah mahn-YAHN feh-LEES kohn ah MEEN-yah.",
        "Я встречаю доброе утро вместе со своей семьёй.", "Yah fstryeh-CHAH-yoo DOHB-rah-yeh OO-trah VMYES-tyeh.",
        "Her sabahı ailemle birlikte neşeyle karşılıyorum.", "Hehr sah-bah-huh ah-ee-lehm-leh beer-leek-TEH.",
        "Saya menyambut pagi hari ceria bersama keluarga saya.", "SAH-yah mehn-YAHM-boot PAH-gee HAH-ree cheh-REE-ah.",
        "我 每天 都 和 家人 一起 迎接 早晨。", "Wǒ měitiān dōu hé jiārén yīqǐ yíngjiē zǎochén.",
        "まいにち かぞく と いっしょに あさ を むかえる。", "Mainichi kazoku to issho ni asa o mukaeru.",
        "매일 아침을 가족과 함께 기쁘게 맞이해요.", "Maeil achim-eul gajok-gwa hamkke gippeuge majihaeyo."
    ),
    item(
        "We all enjoy fresh morning air together.", "ہم سب مل کر صبح کی تازہ ہوا کا مزہ لیتے ہیں۔", "Hum sab mil kar subah ki taaza hawa ka maza lete hain.",
        "हम सब मिलकर सुबह की ताज़ा हवा का आनंद लेते हैं।", "Hum sab milkar subah ki taaza hawa ka anand lete hain.",
        "نستمتع جميعاً بهواء الصباح المنعش النقي في البيت.", "Nastamti'u jamee'an bi-hawa'i al-sabah.",
        "Disfrutamos todos juntos del aire fresco matinal.", "Dees-froo-TAH-mohs TOH-dohs HOON-tohs dehl EYE-reh.",
        "Nous profitons tous ensemble de l'air frais matinal.", "Noo proh-fee-tohn toos ahn-sahmbl duh lehr freh.",
        "Wir genießen alle gemeinsam die frische gesunde Morgenluft.", "Veer geh-NEE-sen AHL-leh geh-MYN-zahm dee FRISH-eh.",
        "Ci godiamo tutti insieme la fresca aria mattutina.", "Chee goh-DYAH-moh TOOT-tee een-SYEH-meh lah FREHS-kah.",
        "Aproveitamos todos juntos o ar fresco da manhã.", "Ah-proh-vay-TAH-moos TOH-doos ZHOON-toos oo ahr FREHS-koo.",
        "Мы дружно дышим свежим бодрящим утренним воздухом.", "My DROOZH-nah DY-sheem SVYEH-zheem bahd-RYAH-shcheem.",
        "Hep birlikte sabahın tertemiz taze havasının tadını çıkarıyoruz.", "Hehp beer-leek-TEH sah-bah-hun tehr-teh-meez tah-duh-nuh.",
        "Kami bersama-sama menikmati udara pagi yang sejuk dan segar.", "KAH-mee behr-SAH-mah meh-neek-MAH-tee oo-DAH-rah PAH-gee.",
        "我们 全家 一起 呼吸 清晨 湿润 新鲜 空气。", "Wǒmen quánjiā yīqǐ hūxī qīngchén shīrùn xīnxiān kōngqì.",
        "みんな で あさ の すがすがしい くうき を たのしむ。", "Minna de asa no sugasugashii kūki o tanoshimu.",
        "우리 모두 함께 아침의 상쾌한 공기를 마셔요.", "Uri modu hamkke achim-ui sangkwaehan gonggireul masyeoyo."
    ),
    item(
        "My family loves starting early bright morning.", "میرا خاندان صبح سویرے اٹھنا اور ہنسنا پسند کرتا ہے۔", "Mera khandan subah sawere uthna aur hansna pasand karta hai.",
        "मेरा परिवार सुबह जल्दी उठकर मुस्कुराना पसंद करता है।", "Mera parivaar subah jaldi uthkar muskurana pasand karta hai.",
        "تحب عائلتي الاستيقاظ مبكراً مع شروق الشمس يومياً.", "Tuhibbu 'a'ilati al-istiyqadha mubakkiran.",
        "A mi familia le encanta levantarse temprano con alegría.", "Ah mee fah-MEE-lyah leh ehn-KAHN-tah leh-vahn-TAHR-seh.",
        "Ma famille adore se réveiller tôt dans la joie.", "Mah fah-mee ah-DOHR suh ray-vay-yay toh dahn lah zhwah.",
        "Meine Familie steht morgens gerne früh und fröhlich auf.", "MY-neh fah-MEE-lyeh shtayt MOR-gens GER-neh frew.",
        "La mia famiglia ama svegliarsi presto ogni bella mattina.", "Lah MEE-ah fah-MEE-lyah AH-mah svehl-YAHR-see PREHS-toh.",
        "Minha família adora acordar cedo com muita alegria.", "MEEN-yah fah-MEE-lyah ah-DOH-rah ah-kohr-DAHR SEH-doo.",
        "Моя семья очень любит встречать рассвет ранним утром.", "Mah-YAH seem-YAH OH-cheen LYOO-beet fstryeh-CHAHT.",
        "Ailem her sabah erken ve neşeyle uyanmayı sever.", "Ah-ee-lehm hehr sah-bah ehr-kehn vey neh-shehy-leh.",
        "Keluarga saya sangat senang bangun pagi-pagi dengan ceria.", "Keh-loo-AHR-gah SAH-yah SAHNG-aht SEH-nahng.",
        "我的 家人 非常 喜欢 每天 清晨 早早 起床。", "Wǒ de jiārén fēicháng xǐhuān měitiān qīngchén zǎozǎo qǐchuáng.",
        "かぞく は まいにち あさ はやく おきるのが だいすき。", "Kazoku wa mainichi asa hayaku okiru no ga daisuki.",
        "우리 가족은 매일 아침 일찍 일어나는 것을 좋아해요.", "Uri gajog-eun maeil achim iljjik ireonaneun geos-eul joahaeyo."
    )
]

# 3. describing-pain
w4_data["describing-pain"] = [
    item(
        "My tummy hurts", "میرا پیٹ درد", "Mera pait dard",
        "मेरा पेट दर्द", "Mera pet dard",
        "بطني يؤلمني جداً", "Batni yu'limuni",
        "Me duele la pancita", "Meh DWEH-leh pahn-SEE-tah",
        "J'ai mal ventre", "Zhay mahl vahntr",
        "Mein Bauch tut-weh", "Myn bowkh toot-vay",
        "Mi fa male pancino", "Mee fah MAH-leh pahn-CHEE-noh",
        "Minha barriga dói", "MEEN-yah bah-HEE-gah doy",
        "У меня болит животик", "Oo mehn-YAH bah-LEET zhy-VOH-teek",
        "Karnım çok ağrıyor", "Kahr-nuhm chohk ah-ruh-yohr",
        "Perut saya sakit", "Peh-root sah-yah sah-keet",
        "我 肚子 疼", "Wǒ dùzi téng",
        "おなか が いたい", "Onaka ga itai",
        "배가 너무 아파요", "Baega neomu apayo"
    ),
    item(
        "It hurts here", "یہاں درد ہے", "Yahan dard hai",
        "यहाँ दर्द है", "Yahan dard hai",
        "يؤلمني هنا بالضبط", "Yu'limuni huna",
        "Me duele aquí", "Meh DWEH-leh ah-KEE",
        "Ça fait mal ici", "Sah feh mahl ee-see",
        "Hier tut es weh", "Heer toot ehs vay",
        "Fa male proprio qui", "Fah MAH-leh PROH-pryoh kwee",
        "Dói bem aqui", "Doy behm ah-KEE",
        "Болит вот здесь", "Bah-LEET voht zdyes",
        "Tam burası ağrıyor", "Tahm boo-rah-suh ah-ruh-yohr",
        "Sakit di sebelah sini", "Sah-keet dee seh-beh-lah see-nee",
        "这里 很 疼", "Zhèlǐ hěn téng",
        "ここ が いたい", "Koko ga itai",
        "여기가 콕콕 아파요", "Yeogiga kokkok apayo"
    ),
    item(
        "Please help me", "میری مدد کریں", "Meri madad karein",
        "मेरी मदद करो", "Meri madad karo",
        "ساعدني أرجوك الآن", "Sa'idni arjook",
        "Por favor ayúdame", "Pohr fah-vohr ah-YOO-dah-meh",
        "Aide-moi s'il-te-plaît", "Ehd-mwah seel-tuh-pleh",
        "Hilf mir bitte", "Hilf meer BIT-teh",
        "Aiutami per favore", "Ah-YOO-tah-mee pehr fah-VOH-reh",
        "Por favor me ajude", "Pohr fah-VOHR mee ah-ZHOO-jee",
        "Помоги мне пожалуйста", "Pah-mah-GEE mnye pah-ZHAH-loo-stah",
        "Lütfen bana yardım et", "LEWT-fen BAH-nah yahr-duhm eht",
        "Tolong bantu saya", "TOH-lohng BAHN-too SAH-yah",
        "请 帮帮 我", "Qǐng bāngbāng wǒ",
        "たすけて ください ね", "Tasukete kudasai ne",
        "저를 좀 도와주세요", "Jeoreul jom dowajuseyo"
    )
]

tier2_data["describing-pain"] = [
    item(
        "My tummy hurts so much.", "میرا پیٹ بہت دکھتا ہے۔", "Mera pait bohat dukhta hai.",
        "मेरा पेट बहुत दुखता है।", "Mera pet bahut dukhta hai.",
        "بطني يؤلمني كثيراً اليوم.", "Batni yu'limuni katheeran al-yawm.",
        "Me duele mucho la pancita.", "Meh DWEH-leh MOO-choh lah pahn-SEE-tah.",
        "J'ai très mal au ventre.", "Zhay treh mahl oh vahntr.",
        "Mein Bauch tut so weh.", "Myn bowkh toot zoh vay.",
        "Il mio pancino duole molto.", "Eel MEE-oh pahn-CHEE-noh DWAW-leh.",
        "A minha barriguinha dói muito.", "Ah MEEN-yah bah-hee-GEEN-yah doy MOON-too.",
        "У меня очень сильно болит животик.", "Oo mehn-YAH OH-cheen SEEL-nah bah-LEET.",
        "Karnım gerçekten çok fazla ağrıyor.", "Kahr-nuhm gehr-chehk-tehn chohk fahz-lah.",
        "Perut saya terasa sangat sakit sekali.", "Peh-root SAH-yah teh-RAH-sah sahng-aht.",
        "我的 肚子 现在 疼得 很 厉害。", "Wǒ de dùzi xiànzài téng de hěn lìhài.",
        "おなか が とても いたい の。", "Onaka ga totemo itai no.",
        "배가 정말 너무 많이 아파요.", "Baega jeongmal neomu mani apayo."
    ),
    item(
        "Please put warm compress here.", "یہاں پر گرم ٹکور کریں۔", "Yahan par garam takore karein.",
        "यहाँ पर गर्म सिंकाई कीजिए।", "Yahan par garm sinkaai keejiye.",
        "ضع كمادة دافئة هنا رجاءً.", "Da' kammadatan dafi'atan huna.",
        "Por favor pon compresa tibia aquí.", "Pohr fah-vohr pohn kohm-PREH-sah TEE-byah.",
        "Mets une compresse tiède ici.", "Meh ewn kohn-prehs tyehd ee-see.",
        "Lege bitte eine warme Kompresse hierher.", "LEH-geh BIT-teh eye-neh VAHR-meh.",
        "Metti un impacco caldo qui per favore.", "MEHT-tee oon eem-PAHK-koh KAHL-doh.",
        "Por favor coloque compressa morna aqui.", "Pohr fah-VOHR koh-LOH-kee kohm-PREH-sah.",
        "Положи тёплый компресс вот сюда пожалуйста.", "Pah-lah-ZHY TYOHP-lyy kahm-PRYEHS.",
        "Lütfen buraya ılık bir bez koy.", "LEWT-fen boo-rah-yah uh-LUHK beer bez koy.",
        "Tolong letakkan kompres hangat di sini.", "TOH-lohng leh-TAHK-kahn kohm-PREHS.",
        "请 在 这里 敷上 温热的 毛巾。", "Qǐng zài zhèlǐ fūshàng wēnrè de máojīn.",
        "ここ に あたたかい タオル を あてて。", "Koko ni atatakai taoru o atete.",
        "여기에 따뜻한 찜질을 해 주세요.", "Yeogie ttatteut-han jjimjil-eul hae juseyo."
    ),
    item(
        "Mom rubs my sore tummy.", "امی میرے پیٹ کو سہلاتی ہیں۔", "Ammi mere pait ko sehlaati hain.",
        "माँ मेरे पेट को सहलाती हैं।", "Maa mere pet ko sahlaati hain.",
        "أمي تدلك بطني برفق وحنان.", "Ummi tudalliku batni bi-rifq.",
        "Mamá frota suavemente mi pancita.", "Mah-MAH FROH-tah swah-veh-MEHN-teh.",
        "Maman frotte doucement mon ventre.", "Mah-mahn froht doos-mahn mohn vahntr.",
        "Mama streichelt sanft meinen Bauch.", "MAH-mah SHTRY-khelt zahnft MY-nen.",
        "Mamma accarezza dolcemente il pancino.", "MAHM-mah ahk-kah-REHT-tsah dohl-cheh-MEHN-teh.",
        "Mamãe faz carinho na barriguinha.", "Mah-MYEN fahz kah-REEN-yoo nah bah-hee-GEEN-yah.",
        "Мама нежно гладит мой животик.", "MAH-mah NYEZH-nah GLAH-deet moy zhy-VOH-teek.",
        "Annem ağrıyan karnımı şefkatle okşar.", "Ahn-nehm ah-ruh-yahn kahr-nuh-muh.",
        "Ibu mengusap lembut perut saya yang sakit.", "EE-boo mehng-OO-sahp lehm-BOOT peh-root.",
        "妈妈 温柔地 轻轻 揉揉 我的 肚子。", "Māma wēnróu de qīngqīng róuróu wǒ de dùzi.",
        "おかあさん が おなか を なでてくれる。", "Okāsan ga onaka o nadetekureru.",
        "엄마가 아픈 배를 살살 문질러 줘요.", "Eommaga apeun baereul salsal munjilleo jwoyo."
    )
]

tier3_data["describing-pain"] = [
    item(
        "Doctor helps my tummy feel better.", "ڈاکٹر پیٹ کا درد ٹھیک کرتا ہے۔", "Doctor pait ka dard theek karta hai.",
        "डॉक्टर पेट का दर्द ठीक करते हैं।", "Doctor pet ka dard theek karte hain.",
        "الطبيب يساعد بطني حتى يشفى تماماً.", "Al-tabeeb yusa'idu batni hatta yashfa.",
        "El doctor ayuda a curar mi pancita.", "Ehl dohk-TOHR ah-YOO-dah ah koo-RAHR.",
        "Le médecin soigne bien mon ventre douloureux.", "Luh mayd-san swahn byan mohn vahntr.",
        "Der Arzt hilft meinem kranken Bauch schnell.", "Dehr AHRTST hilft MY-nem KRAHN-ken bowkh.",
        "Il dottore aiuta il mio pancino guarire.", "Eel doht-TOH-reh ah-YOO-tah eel MEE-oh.",
        "O médico ajuda a sarar a barriguinha.", "Oo MEH-jee-koo ah-ZHOO-dah ah sah-RAHR.",
        "Добрый доктор помогает вылечить мой животик.", "DOHB-ryy DOHK-tahr pah-mah-GAH-yet.",
        "Doktor karnımın iyileşmesine çok yardımcı olur.", "Dohk-TOHR kahr-nuh-muhn ee-yee-lehsh-meh-see-neh.",
        "Dokter membantu perut saya agar lekas sembuh.", "DOHK-tehr mehm-BAHN-too peh-root SAH-yah.",
        "医生 叔叔 帮助 我 治好 肚子的 疼痛。", "Yīshēng shūshu bāngzhù wǒ zhìhǎo dùzi de téngtòng.",
        "おいしゃさん が おなか を なおして くれる。", "Oishasan ga onaka o naoshite kureru.",
        "의사 선생님이 아픈 배를 낫게 도와주세요.", "Uisa seonsaengnimi apeun baereul natge dowajuseyo."
    ),
    item(
        "I rest quietly until pain stops.", "میں درد رکنے تک آرام کرتا ہوں۔", "Main dard rukne tak aaraam karta hoon.",
        "मैं दर्द रुकने तक आराम करता हूँ।", "Main dard rukne tak aaraam karta hoon.",
        "أرتاح بهدوء حتى يزول الألم تماماً.", "Artahu bi-hudoo'in hatta yazoola al-alam.",
        "Descanso tranquilo hasta que pase el dolor.", "Dehs-KAHN-soh trahn-KEE-loh AHS-tah.",
        "Je me repose calmement jusqu'à guérison.", "Zhuh muh ruh-pohz kahl-muh-mahn zhews-kah.",
        "Ich ruhe mich aus bis Schmerzen aufhören.", "Ikh ROO-eh meekh ows bis SHMEHRT-tsen.",
        "Riposo tranquillo finché il dolore passa del tutto.", "Ree-POH-zoh trahn-KWEEL-loh feen-KEH.",
        "Eu descanso calmo até que a dor passe.", "Eh-oo dehs-KAHN-soo KAHL-moo ah-TEH.",
        "Я спокойно отдыхаю пока животик не пройдёт.", "Yah spah-KOY-nah aht-dy-KHAH-yoo.",
        "Ağrı tamamen geçene kadar sakince dinleniyorum.", "Ah-ruh tah-mah-mehn geh-cheh-neh kah-dahr.",
        "Saya beristirahat tenang sampai rasa sakitnya hilang.", "SAH-yah behr-ees-tee-RAH-haht teh-nahng.",
        "我 安静地 躺着 休息 直到 肚子 不疼。", "Wǒ ānjìng de tǎngzhe xiūxi zhídào dùzi bùténg.",
        "いたみ が おさまる まで しずかに やすむ。", "Itami ga osamaru made shizuka ni yasumu.",
        "통증이 가라앉을 때까지 얌전히 누워 쉬어요.", "Tongjeungi garaanjeul ttaekkaji yamjeonhi nuwo swieoyo."
    ),
    item(
        "A gentle touch brings sweet relief.", "پیار بھرا لمس سکون لاتا ہے۔", "Pyaar bhara lams sukoon laata hai.",
        "प्यार भरा स्पर्श आराम लाता है।", "Pyaar bhara sparsh aaraam laata hai.",
        "اللمسة الحنونة تمنحني الراحة والشفاء الدائم.", "Al-lamsatu al-hanoonatu tamnahuni al-rahah.",
        "Una caricia suave me da mucho alivio.", "OO-nah kah-REE-syah SWAH-veh meh dah.",
        "Une douce caresse apporte un grand réconfort.", "Ewn doos kah-rehs ah-pohrt uhn grahn ray-kohn-fohr.",
        "Eine sanfte Berührung bringt mir viel Linderung.", "Eye-neh ZAHN-fteh beh-ROO-roong bringt.",
        "Una carezza dolce dona subito grande sollievo.", "OO-nah kah-REHT-tsah DOHL-cheh DOH-nah.",
        "Um carinho suave traz muito alívio gostoso.", "Oom kah-REEN-yoo SWAH-vee trahz.",
        "Нежное прикосновение приносит долгожданное облегчение.", "NYEZH-nah-yeh pree-kahs-nah-VYEH-nyee-yeh.",
        "Nazik bir dokunuş bana büyük ferahlık verir.", "Nah-ZEEK beer doh-koo-noosh BAH-nah.",
        "Sentuhan penuh kasih sayang memberikan rasa nyaman.", "Sehn-TOO-hahn peh-NOOH KAH-seeh SAH-yahng.",
        "温柔的 安抚 让 我 感觉 舒服 多了。", "Wēnróu de ānfǔ ràng wǒ gǎnjué shūfu duō le.",
        "やさしい なでなで で すぐに らくになる。", "Yasashii nadenade de sugu ni raku ni naru.",
        "부드러운 손길이 포근하고 편안하게 해 줘요.", "Budeureoun songgiri pogeunhago pyeon-anhage hae jwoyo."
    )
]

# 4. big-feelings
w4_data["big-feelings"] = [
    item(
        "Smile so bright", "پیاری مسکراہٹ ہے", "Pyaari muskurahat hai",
        "प्यारी मुस्कान है", "Pyaari muskaan hai",
        "ابتسامة مشرقة جداً", "Ibtisama mushriqa",
        "Sonrisa muy linda", "Sohn-REE-sah MOOY LEEN-dah",
        "Sourire si éclatant", "Soo-reer see ay-klah-tahn",
        "Lächeln so hell", "LEKH-eln zoh hel",
        "Sorriso tanto luminoso", "Sohr-REE-zoh TAHN-toh",
        "Sorriso tão lindo", "Sohr-HEE-zoo town LEEN-doo",
        "Улыбка очень светлая", "Oo-LYP-kah OH-cheen",
        "Tebessüm çok parlak", "Teh-behs-sewm chohk",
        "Senyum begitu cerah", "Sehn-yoom beh-gee-too",
        "微笑 多 明亮", "Wēixiào duō míngliàng",
        "えがお が まぶしい", "Egao ga mabushii",
        "미소가 참 밝아요", "Misoga cham balg-ayo"
    ),
    item(
        "Heart is happy", "دل خوش ہے", "Dil khush hai",
        "दिल खुश है", "Dil khush hai",
        "القلب سعيد ومطمئن", "Al-qalbu sa'eed",
        "Corazón muy alegre", "Koh-rah-SOHN MOOY ah-LEH-greh",
        "Cœur tout joyeux", "Kuhr too zhwah-yuh",
        "Herz ist froh", "Herts ist froh",
        "Cuore è felice", "KWOH-reh eh feh-LEE-cheh",
        "Coração está feliz", "Koh-rah-SOWN eh-STAH feh-LEES",
        "Сердце радостно бьётся", "SYEHRD-tseh RAH-dahst-nah",
        "Kalbim çok neşelidir", "Kahl-beem chohk neh-sheh-lee-deer",
        "Hati merasa gembira", "Hah-tee meh-RAH-sah gehm-BEE-rah",
        "心里 很 欢喜", "Xīnlǐ hěn huānxǐ",
        "こころ が うれしい", "Kokoro ga ureshii",
        "마음이 참 기뻐요", "Maeumi cham gippeoyo"
    ),
    item(
        "Give big hug", "بڑی جپھی دو", "Bari jhappi do",
        "बड़ी झप्पी दो", "Badi jhappi do",
        "أعطني عناقاً كبيراً", "'A'tini 'inaqan kabeeran",
        "Dame gran abrazo", "DAH-meh grahn ah-BRAH-zoh",
        "Fais grand câlin", "Feh grahn kah-lan",
        "Gib große Umarmung", "Gib GROH-seh oom-AHR-moong",
        "Dammi grande abbraccio", "DAHM-mee GRAHN-deh ahb-BRAHT-choh",
        "Dê grande abraço", "Day GRAHN-jee ah-BRAH-soo",
        "Обними меня крепко", "Ahb-nee-MEE mehn-YAH KRYEHP-kah",
        "Bana sımsıkı sarıl", "BAH-nah suhm-suh-KUH sah-ruhl",
        "Beri pelukan hangat", "BEH-ree peh-LOOK-ahn hahng-aht",
        "给 个 拥抱", "Gěi gè yǒngbào",
        "ぎゅっと だきしめて ね", "Gyutto dakishimete ne",
        "크게 꼭 안아줘요", "Keuge kkok anajwoyo"
    )
]

tier2_data["big-feelings"] = [
    item(
        "A big smile spreads joy.", "پیاری مسکراہٹ خوشی پھیلاتی ہے۔", "Pyaari muskurahat khushi phailaati hai.",
        "प्यारी मुस्कान खुशी फैलाती है।", "Pyaari muskaan khushi phailati hai.",
        "الابتسامة الحلوة تنشر الفرح والسرور.", "Al-ibtisamatu al-hulwatu tanshur.",
        "Una gran sonrisa comparte alegría.", "OO-nah grahn sohn-REE-sah kohm-PAHR-teh.",
        "Un grand sourire répand la joie.", "Uhn grahn soo-reer ray-pahn lah zhwah.",
        "Ein breites Lächeln schenkt Freude.", "Eye-n BRAY-tes LEKH-eln shenkt FROY-deh.",
        "Un bel sorriso diffonde tanta gioia.", "Oon behl sohr-REE-zoh deef-FOHN-deh.",
        "Um grande sorriso espalha muita alegria.", "Oom GRAHN-jee sohr-HEE-zoo ehs-PAH-lyah.",
        "Широкая улыбка дарит всем радость.", "Shee-ROH-kah-yah oo-LYP-kah DAH-reet.",
        "Kocaman bir gülümseme neşe saçar.", "Koh-JAH-mahn beer gew-lewms-eh-meh.",
        "Senyuman yang lebar membagikan kegembiraan.", "Sehn-YOO-mahn yahng LEH-bahr mehm-bah-GEE-kahn.",
        "灿烂的 笑容 把 快乐 传递。", "Cànlàn de xiàoróng bǎ kuàilè chuándì.",
        "あかるい えがお が よろこび を ひろげる。", "Akarui egao ga yorokobi o hirogeru.",
        "환한 미소가 온 세상에 기쁨을 전해요.", "Hwanhan misoga on sesange gippeumeul jeonhaeyo."
    ),
    item(
        "My heart feels calm today.", "میرا دل آج پرسکون ہے۔", "Mera dil aaj pursukoon hai.",
        "मेरा दिल आज शांत है।", "Mera dil aaj shaant hai.",
        "قلبي يشعر بالطمأنينة والهدوء اليوم.", "Qalbi yash'uru bi-l-tum'aneenah.",
        "Mi corazón se siente sereno.", "Mee koh-rah-SOHN seh SYEHN-teh.",
        "Mon cœur se sent très calme.", "Mohn kuhr suh sahn treh kahlm.",
        "Mein Herz ist heute ruhig.", "Myn herts ist HOY-teh ROO-heekh.",
        "Il mio cuore si sente tranquillo.", "Eel MEE-oh KWOH-reh see SYEHN-teh.",
        "O meu coração sente muita calma.", "Oo may-oo koh-rah-SOWN SEHN-chee.",
        "Моё сердце сегодня чувствует спокойствие.", "Mah-YOH SYEHRD-tseh see-VOHD-nyah.",
        "Bugün kalbim tamamen huzurla doludur.", "BOO-gewn kahl-beem tah-MAH-mehn.",
        "Hati saya terasa sangat tenang hari ini.", "Hah-tee SAH-yah teh-RAH-sah SAHNG-aht.",
        "今天 我的 心里 感到 十分 平静。", "Jīntiān wǒ de xīnlǐ gǎndào shífēn píngjìng.",
        "きょう こころ が とても おだやか。", "Kyō kokoro ga totemo odayaka.",
        "오늘 제 마음이 참 편안하고 차분해요.", "Oneul je maeumi cham pyeon-anhago chabunhaeyo."
    ),
    item(
        "Give mom a warm hug.", "امی کو پیاری جپھی دیں۔", "Ammi ko pyaari jhappi dein.",
        "माँ को प्यारी झप्पी दीजिए।", "Maa ko pyaari jhappi deejie.",
        "أعطِ أمك عناقاً دافئاً ومحباً.", "'A'ti ummaka 'inaqan dafi'an.",
        "Dale a mamá un abrazo tierno.", "DAH-leh ah mah-MAH oon ah-BRAH-zoh.",
        "Fais un doux câlin à maman.", "Feh uhn doo kah-lan ah mah-mahn.",
        "Gib Mama eine warme Umarmung.", "Gib MAH-mah eye-neh VAHR-meh.",
        "Dai alla mamma un abbraccio affettuoso.", "Dye AHL-lah MAHM-mah oon ahb-BRAHT-choh.",
        "Dê um abraço quentinho na mamãe.", "Day oom ah-BRAH-soo kehn-CHEEN-yoo.",
        "Обними маму крепко и ласково.", "Ahb-nee-MEE MAH-moo KRYEHP-kah.",
        "Annene sıcacık tatlı bir sarıl.", "Ahn-neh-neh suh-DZHAH-juhk taht-luh.",
        "Berikan pelukan hangat untuk ibu tersayang.", "Beh-REE-kahn peh-LOOK-ahn hahng-aht.",
        "给 妈妈 一个 温暖的 大大 拥抱。", "Gěi māma yī gè wēnnuǎn de dàdà yǒngbào.",
        "おかあさん に あたたかい ハグ を しよう。", "Okāsan ni atatakai hagu o shiyō.",
        "엄마에게 따뜻한 포옹을 꼭 선물해요.", "Eomma-ege ttatteut-han po-ong-eul kkok seonmulhaeyo."
    )
]

tier3_data["big-feelings"] = [
    item(
        "I share happy feelings with friends.", "میں دوستوں کے ساتھ خوشیاں بانٹتا ہوں۔", "Main doston ke sath khushiyan baant-ta hoon.",
        "मैं दोस्तों के साथ खुशियाँ बाँटता हूँ।", "Main doston ke saath khushiyan baant-ta hoon.",
        "أشارك المشاعر السعيدة مع أصدقائي دائماً.", "Ushariku al-masha'ira al-sa'eedata.",
        "Comparto sentimientos felices con mis amigos.", "Kohm-PAHR-toh sehn-tee-MYEHN-tohs feh-LEE-sehs.",
        "Je partage mes joies avec mes amis.", "Zhuh pahr-tahzh may zhwah ah-vehk may-zah-mee.",
        "Ich teile glückliche Gefühle mit meinen Freunden.", "Ikh TY-leh GLEWK-likh-eh geh-FEW-leh.",
        "Condivido sentimenti felici con i miei amici.", "Kohn-dee-VEE-doh sehn-tee-MEHN-tee feh-LEE-chee.",
        "Eu compartilho sentimentos felizes com amigos.", "Eh-oo kohm-pahr-CHEEL-yoo sehn-chee-MEHN-toos.",
        "Я делюсь радостными чувствами со своими друзьями.", "Yah deh-LYOOS RAH-dahst-ny-mee CHOOF-stvah-mee.",
        "Güzel duygularımı arkadaşlarımla neşeyle paylaşırım.", "Gew-zehl dooy-goo-lah-ruh-muh ahr-kah-dahsh-lah-ruhm-lah.",
        "Saya berbagi perasaan bahagia bersama sahabat saya.", "SAH-yah behr-BAH-gee peh-rah-SAH-ahn bah-HAH-gyah.",
        "我 和 好朋友们 一起 分享 快乐 感受。", "Wǒ hé hǎopéngyǒumen yīqǐ fēnxiǎng kuàilè gǎnshòu.",
        "ともだち と うれしい きもち を わけあう。", "Tomodachi to ureshii kimochi o wakeau.",
        "친구들과 함께 행복한 감정을 다정하게 나눠요.", "Chingudeul-gwa hamkke haengbok-han gamjeong-eul dajeong-hage nanwoyo."
    ),
    item(
        "A calm heart brings sweet peace.", "پرسکون دل سچی راحت لاتا ہے۔", "Pursukoon dil sacchi rahat laata hai.",
        "शांत दिल सच्ची शांति लाता है।", "Shaant dil sacchi shaanti laata hai.",
        "القلب الهادئ يجلب السكينة والسلام للجميع.", "Al-qalbu al-hadi'u yajlibu al-sakeenah.",
        "Un corazón sereno siempre trae paz.", "Oon koh-rah-SOHN seh-REH-noh SYEHM-preh trah-eh.",
        "Un cœur calme apporte une douce paix.", "Uhn kuhr kahlm ah-pohrt ewn doos peh.",
        "Ein ruhiges Herz bringt echten Frieden.", "Eye-n ROO-hee-ges herts bringt EKH-ten.",
        "Un cuore sereno porta sempre tanta pace.", "Oon KWOH-reh seh-REH-noh POHR-tah SYEHM-preh.",
        "Um coração tranquilo traz muita paz boa.", "Oom koh-rah-SOWN trahn-KWEE-loo trahz.",
        "Спокойное сердце приносит в дом настоящий мир.", "Spah-KOY-nah-yeh SYEHRD-tseh pree-NOH-seet.",
        "Huzurlu bir kalp her zaman barış getirir.", "Hoo-zoor-loo beer kahlp hehr zah-mahn.",
        "Hati yang tenang membawa kedamaian yang indah.", "Hah-tee yahng teh-nahng mehm-BAH-wah keh-dah-MY-ahn.",
        "平静的 内心 能 带来 甜美的 安宁。", "Píngjìng de nèixīn néng dàilái tiánměi de ānníng.",
        "おだやかな こころ は やすらぎ を はこぶ。", "Odayakana kokoro wa yasuragi o hakobu.",
        "차분한 마음은 언제나 달콤한 평화를 가져다줘요.", "Chabunhan maeumeun eonjena dalkomhan pyeonghwareul gajyeodajwoyo."
    ),
    item(
        "Warm hugs comfort all big feelings.", "پیاری جپھیاں سارے دکھ مٹاتی ہیں۔", "Pyaari jhappiyan saare dukh mitaati hain.",
        "प्यारी झप्पियाँ सारे दुख मिटाती हैं।", "Pyaari jhappiyaan saare dukh mitaati hain.",
        "العناق الدافئ يريح كل المشاعر القوية.", "Al-'inaqu al-dafi'u yureehu kulla al-masha'ir.",
        "Los abrazos cálidos calman cualquier emoción.", "Lohs ah-BRAH-zohs KAH-lee-dohs KAHL-mahn.",
        "Les doux câlins consolent les gros chagrins.", "Lay doo kah-lan kohn-sohl lay groh shah-gran.",
        "Warme Umarmungen trösten bei allen Gefühlen.", "VAHR-meh oom-AHR-moong-en TRERS-ten.",
        "I caldi abbracci confortano tutti i sentimenti.", "Ee KAHL-dee ahb-BRAHT-chee kohn-FOHR-tah-noh.",
        "Abraços quentinhos confortam todos os sentimentos.", "Ah-BRAH-soos kehn-CHEEN-yoos kohn-FOHR-tahn.",
        "Тёплые объятия успокаивают любые сильные переживания.", "TYOHP-ly-yeh ahb-YAH-tyah oos-pah-KAH-ee-vah-yoot.",
        "Sıcak sarılmalar bütün yoğun duyguları yatıştırır.", "Suh-dzhahk sah-ruhl-mah-lahr bew-tewn dooy-goo-lah-ruh.",
        "Pelukan yang hangat menenangkan semua rasa gundah.", "Peh-LOOK-ahn yahng hahng-aht meh-neh-NAHNG-kahn.",
        "温暖的 拥抱 能 安慰 所有 情绪。", "Wēnnuǎn de yǒngbào néng ānwèi suǒyǒu qíngxù.",
        "あたたかい ハグ は すべての きもち を いやす。", "Atatakai hagu wa subete no kimochi o iyasu.",
        "따뜻한 포옹은 모든 벅찬 감정을 다독여 줘요.", "Ttatteut-han po-ongeun modeun beokchan gamjeongeul dadogyeo jwoyo."
    )
]

# 5. lost-in-public
w4_data["lost-in-public"] = [
    item(
        "Stay right here", "یہیں ٹھہرے رہو", "Waheen thehre raho",
        "वहीं रुके रहो", "Waheen ruke raho",
        "ابقَ هنا بهدوء", "Ibqa huna bi-hudoo'",
        "Quédate justo aquí", "KEH-dah-teh HOOS-toh ah-KEE",
        "Reste bien ici", "Rehst byan ee-see",
        "Bleib genau hier", "Blyb geh-NOW heer",
        "Resta proprio qui", "REHS-tah PROH-pryoh kwee",
        "Fique bem aqui", "FEE-kee behm ah-KEE",
        "Стой прямо здесь", "Stoy PRYAH-mah zdyes",
        "Tam burada dur", "Tahm boo-rah-dah door",
        "Tetap di sini", "Teh-tahp dee see-nee",
        "留 在 原地", "Liú zài yuándì",
        "ここ に いて", "Koko ni ite",
        "여기 그대로 있어요", "Yeogi geudaero isseoyo"
    ),
    item(
        "Ask the guard", "گارڈ سے پوچھو", "Guard se poochho",
        "गार्ड से पूछो", "Guard se poochho",
        "اسأل الحارس الأمين", "Is'al al-haris al-ameen",
        "Pregunta al guardia", "Preh-GOON-tah ahl GWAHR-dyah",
        "Demande au gardien", "Duh-mahnd oh gahr-dyan",
        "Frag den Wächter", "Frahg dehn VEKH-ter",
        "Chiedi alla guardia", "KYEH-dee AHL-lah GWAHR-dyah",
        "Pergunte ao guarda", "Pehr-GOON-chee ow GWAHR-dah",
        "Спроси у охранника", "Sprah-SEE oo ahkh-RAHN-nee-kah",
        "Güvenlik görevlisine sor", "Gew-vehn-leek ger-rev-lee-see-neh",
        "Tanya petugas keamanan", "TAH-nyah peh-TOO-gahs keh-ah-mah-nahn",
        "请问 穿 制服 保安", "Qǐngwèn chuān zhìfú bǎo'ān",
        "けいびいんさん に きく", "Keibiinsan ni kiku",
        "경비 아저씨께 물어봐요", "Gyeongbi ajeossikke mureobwayo"
    ),
    item(
        "Ask for help", "مدد طلب کرو", "Madad talab karo",
        "मदद माँगो तुम", "Madad maango tum",
        "اطلب المساعدة فوراً", "Utlub al-musa'adah",
        "Pide ayuda ahora", "PEE-deh ah-YOO-dah ah-OH-rah",
        "Demande de l'aide", "Duh-mahnd duh lehd",
        "Bitte um Hilfe", "BIT-teh oom HIL-feh",
        "Chiedi aiuto subito", "KYEH-dee ah-YOO-toh SOO-bee-toh",
        "Peça ajuda logo", "PEH-sah ah-ZHOO-dah LOH-goo",
        "Попроси о помощи", "Pah-prah-SEE ah POH-mah-shchee",
        "Hemen yardım iste", "Heh-mehn yahr-duhm ees-teh",
        "Minta bantuan sekarang", "MEEN-tah bahn-TOO-ahn",
        "主动 寻求 帮助", "Zhǔdòng xúnqiú bāngzhù",
        "たすけ を もとめよう", "Tasuke o motomeyō",
        "도움을 요청해요 어서", "Doumeul yocheonghaeyo eoseo"
    )
]

tier2_data["lost-in-public"] = [
    item(
        "Stay in a safe place.", "محفوظ جگہ پر ٹھہرے رہیں۔", "Mehfooz jagah par thehre rahein.",
        "सुरक्षित जगह पर रुके रहिए।", "Surakshit jagah par ruke rahiye.",
        "ابقَ في مكان آمن دائماً.", "Ibqa fee makanin amin da'iman.",
        "Quédate en un lugar seguro.", "KEH-dah-teh ehn oon loo-GAHR seh-GOO-roh.",
        "Reste dans un endroit sûr.", "Rehst dahnz uhn ahn-drwah soor.",
        "Bleib an einem sicheren Ort.", "Blyb ahn EYE-nem ZIKH-er-en ohrt.",
        "Resta in un posto sicuro.", "REHS-tah een oon POHS-toh see-KOO-roh.",
        "Fique em um lugar seguro.", "FEE-kee ehyn oom loo-GAHR seh-GOO-roo.",
        "Всегда оставайся в безопасном месте.", "Fsyeg-DAH ahs-tah-VAY-syah v bye-zah-PAHS-nahm.",
        "Her zaman güvenli bir yerde bekle.", "Hehr zah-mahn gew-vehn-LEE beer yehr-deh.",
        "Tetaplah berada di tempat yang aman.", "Teh-TAHP-lah beh-RAH-dah dee tehm-paht.",
        "请 留在 安全的 明显 地方。", "Qǐng liú zài ānquán de míngxiǎn dìfang.",
        "あんぜんな ばしょ で まとう ね。", "Anzenna basho de matō ne.",
        "안전한 장소에 얌전히 머물러 있어요.", "Anjeon-han jangsoe yamjeonhi meomulleo isseoyo."
    ),
    item(
        "Tell security guard my name.", "گارڈ کو اپنا نام بتائیں۔", "Guard ko apna naam batayein.",
        "गार्ड को अपना नाम बताइए।", "Guard ko apna naam bataiye.",
        "أخبر رجل الأمن باسمك الكامل.", "Akhbir rajula al-amni bi-ismik.",
        "Dile al guardia tu nombre.", "DEE-leh ahl GWAHR-dyah too NOHM-breh.",
        "Dis ton nom au gardien.", "Dee tohn nohm oh gahr-dyan.",
        "Sag dem Wachmann deinen Namen.", "Zahg dehm VAHKH-mahn DY-nen NAH-men.",
        "Di' il tuo nome alla guardia.", "Dee eel TOO-oh NOH-meh AHL-lah GWAHR-dyah.",
        "Diga o seu nome ao guarda.", "JEE-gah oo say-oo NOH-mee ow GWAHR-dah.",
        "Назови охраннику своё полное имя.", "Nah-zah-VEE ahkh-RAHN-nee-koo svah-YOH.",
        "Güvenlik görevlisine hemen adını söyle.", "Gew-vehn-leek ger-rev-lee-see-neh ah-duh-nuh.",
        "Katakan nama lengkapmu kepada petugas keamanan.", "Kah-tah-kahn NAH-mah LEHNG-kahp-moo.",
        "告诉 保安 叔叔 你的 名字。", "Gàosu bǎo'ān shūshu nǐ de míngzi.",
        "けいびいんさん に なまえ を つたえて。", "Keibiinsan ni namae o tsutaete.",
        "보안관 아저씨께 내 이름을 차분히 말해요.", "Boangwan ajeossikke nae ireumeul chabunhi malhaeyo."
    ),
    item(
        "Brave child asks for help.", "بہادر بچہ مدد مانگتا ہے۔", "Bahadur baccha madad maangta hai.",
        "बहादुर बच्चा मदद माँगता है।", "Bahaadur baccha madad maangta hai.",
        "الطفل الشجاع يطلب المساعدة بثقة.", "Al-tiflu al-shuja'u yatlubu al-musa'adah.",
        "Un niño valiente pide ayuda.", "Oon NEEN-yoh vah-LYEHN-teh PEE-deh ah-YOO-dah.",
        "L'enfant courageux demande de l'aide.", "Lahn-fahn koo-rah-zhuh duh-mahnd duh lehd.",
        "Ein tapferes Kind bittet um Hilfe.", "Eye-n TAHP-fer-es kint BIT-tet oom HIL-feh.",
        "Un bambino coraggioso chiede aiuto subito.", "Oon bahm-BEE-noh koh-rahd-JOH-zoh KYEH-deh.",
        "Uma criança corajosa pede ajuda sempre.", "OO-mah kree-AHN-sah koh-rah-ZHOH-zah PEH-jee.",
        "Смелый ребёнок уверенно просит о помощи.", "SMYEH-lyy ryeh-BYOH-nahk oo-VYEH-ryen-nah.",
        "Cesur çocuk hemen yardım istemeyi bilir.", "Jeh-soor choh-dzhook heh-mehn yahr-duhm.",
        "Anak yang berani berani meminta bantuan.", "AH-nahk yahng beh-RAH-nee meh-MEEN-tah.",
        "勇敢的 孩子 会 主动 求助。", "Yǒnggǎn de háizi huì zhǔdòng qiúzhù.",
        "ゆうかんな こ は たすけ を もとめる。", "Yūkanna ko wa tasuke o motomeru.",
        "용감한 어린이는 망설이지 않고 도움을 청해요.", "Yonggamhan eorin-ineun mangseoriji anko doumeul cheonghaeyo."
    )
]

tier3_data["lost-in-public"] = [
    item(
        "Stay calm until my mom arrives.", "امی کے آنے تک صبر کریں۔", "Ammi ke aane tak sabr karein.",
        "माँ के आने तक धीरज रखें।", "Maa ke aane tak dheeraj rakhein.",
        "ابقَ هادئاً حتى تصل والدتك إليك.", "Ibqa hadi'an hatta tasila walidatuk.",
        "Mantén la calma hasta que llegue mamá.", "Mahn-TEHN lah KAHL-mah AHS-tah.",
        "Reste calme jusqu'à l'arrivée de maman.", "Rehst kahlm zhews-kah lah-ree-vay duh mah-mahn.",
        "Bleib ruhig bis deine Mama sicher kommt.", "Blyb ROO-heekh bis DY-neh MAH-mah.",
        "Stai calmo finché la mamma non arriva.", "Stye KAHL-moh feen-KEH lah MAHM-mah.",
        "Mantenha a calma até a mamãe chegar.", "Mahn-TEHN-yah ah KAHL-mah ah-TEH.",
        "Сохраняй спокойствие пока мама не придёт за тобой.", "Sah-khrah-NYAY spah-KOY-stvee-yeh.",
        "Annem güvenle gelene kadar sakin ve sabırlı kal.", "Ahn-nehm gew-vehn-leh geh-leh-neh kah-dahr.",
        "Tetap tenang sampai ibu datang menjemput dengan aman.", "Teh-tahp teh-nahng sahm-pie EE-boo.",
        "保持 冷静 乖乖 等待 妈妈 过来 接我。", "Bǎochí lěngjìng guāiguāi děngdài māma guòlái jiē wǒ.",
        "おかあさん が くる まで しずかに まつ。", "Okāsan ga kuru made shizuka ni matsu.",
        "엄마가 안전하게 올 때까지 침착하게 기다려요.", "Eommaga anjeonhage ol ttaekkaji chimchakhage gidaryeoyo."
    ),
    item(
        "Security guard helps find my family.", "سیکیورٹی گارڈ خاندان تلاش کرتا ہے۔", "Security guard khandan talaash karta hai.",
        "सुरक्षा गार्ड परिवार ढूँढने में मदद करते हैं।", "Suraksha guard parivaar dhoondhne mein madad karte hain.",
        "حارس الأمن يساعد في العثور على عائلتي.", "Harisu al-amni yusa'idu fee al-'uthur.",
        "El guardia de seguridad ayuda a mi familia.", "Ehl GWAHR-dyah deh seh-goo-ree-DAHD ah-YOO-dah.",
        "L'agent de sécurité aide à retrouver ma famille.", "Lah-zhahn duh say-kew-ree-tay ehd ah ruh-troo-vay.",
        "Der Wachmann hilft mir meine Familie zu finden.", "Dehr VAHKH-mahn hilft meer MY-neh fah-MEE-lyeh.",
        "La guardia di sicurezza aiuta a trovare famiglia.", "Lah GWAHR-dyah dee see-koo-REHT-tsah ah-YOO-tah.",
        "O segurança ajuda a encontrar a minha família.", "Oo seh-goo-RAHN-sah ah-ZHOO-dah ah ehn-kohn-TRAHR.",
        "Сотрудник охраны помогает быстро найти мою семью.", "Sah-TROOD-neek ahkh-RAH-ny pah-mah-GAH-yet.",
        "Güvenlik görevlisi ailemi hemen bulmama yardım eder.", "Gew-vehn-leek ger-rev-lee-see ah-ee-leh-mee.",
        "Petugas keamanan membantu menemukan keluarga saya dengan cepat.", "Peh-TOO-gahs keh-ah-mah-nahn mehm-BAHN-too.",
        "穿 制服的 保安 叔叔 帮 我 找到 家人。", "Chuān zhìfú de bǎo'ān shūshu bāng wǒ zhǎodào jiārén.",
        "けいびいんさん が かぞく を さがして くれる。", "Keibiinsan ga kazoku o sagashite kureru.",
        "보안관 아저씨가 우리 가족을 신속히 찾아주세요.", "Boangwan ajeossiga uri gajog-eul sinsok-hi chajajuseyo."
    ),
    item(
        "I know my parent phone number.", "مجھے والدین کا فون نمبر یاد ہے۔", "Mujhe walidain ka phone number yaad hai.",
        "मुझे माता-पिता का फोन नंबर याद है।", "Mujhe mata-pita ka phone number yaad hai.",
        "أحفظ رقم هاتف والدي جيداً عن ظهر قلب.", "Ahfazu raqma hatifi walidayya.",
        "Sé el número de teléfono de mis padres.", "Seh ehl NOO-meh-roh deh teh-LEH-foh-noh.",
        "Je connais par cœur le numéro de mes parents.", "Zhuh koh-nay pahr kuhr luh new-may-roh.",
        "Ich weiß die Telefonnummer meiner Eltern ganz genau.", "Ikh vyes dee teh-leh-FOHN-noom-mer.",
        "Conosco a memoria il numero dei miei genitori.", "Koh-NOHS-koh ah meh-MOH-ryah eel NOO-meh-roh.",
        "Eu sei de cor o telefone dos meus pais.", "Eh-oo say jee kohr oo teh-leh-FOH-nee.",
        "Я отлично помню наизусть номер телефона родителей.", "Yah aht-LEECH-nah POHM-nyoo nah-ee-ZOOS-ty.",
        "Anne ve babamın telefon numarasını ezbere biliyorum.", "Ahn-neh vey bah-bah-muhn teh-leh-fohn noo-mah-rah-suh-nuh.",
        "Saya ingat dengan baik nomor telepon orang tua saya.", "SAH-yah EENG-aht dehn-gahn by-eek NOH-mohr.",
        "我 清楚 记得 爸爸 妈妈的 手机 号码。", "Wǒ qīngchǔ jìdé bàba māma de shǒujī hàomǎ.",
        "おとうさん や おかあさん の でんわばんごう を しってる。", "Otōsan ya okāsan no denwabangō o shitteru.",
        "저는 엄마 아빠의 전화번호를 또박또박 외우고 있어요.", "Jeoneun eomma appaui jeonhwabeonhoreul ttobakttobak oewugo isseoyo."
    )
]

print("Defined core critical overrides. Writing bulk builder...")
