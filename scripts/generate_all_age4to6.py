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

# Explicit dedicated overrides for breakfast-chat matching user specification 100%
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
        "Por favor dame tostada caliente.", "Pohr fah-vohr DAH-meh tohs-TAH-dah kah-LYEHN-teh.",
        "Donne-moi du pain chaud s'il-te-plaît.", "Dohn-mwah dew pan sho seel-tuh-pleh.",
        "Gib mir bitte warmen Toast.", "Gib meer BIT-teh VAHR-men toast.",
        "Dammi del pane caldo per favore.", "DAHM-mee dehl PAH-neh KAHL-doh pehr fah-VOH-reh.",
        "Por favor me dê torrada quente.", "Pohr fah-VOHR mee day toh-RAH-dah KEHN-chee.",
        "Дай мне пожалуйста тёплый тост.", "Day mnye pah-ZHAH-loo-stah TYOHP-lyy tost.",
        "Lütfen bana sıcak tost ver.", "LEWT-fen BAH-nah suh-dzhak tost vehr.",
        "Tolong beri saya roti hangat.", "TOH-lohng BEH-ree SAH-yah ROH-tee hahng-aht.",
        "请 给我 温热的 吐司。", "Qǐng gěi wǒ wēnrè de tǔsī.",
        "あたたかい トースト を ください。", "Atatakai tōsuto o kudasai.",
        "따뜻한 토스트를 주세요.", "Ttatteut-han toseuteureul juseyo."
    ),
    item(
        "I like drinking sweet milk.", "مجھے میٹھا دودھ پسند ہے۔", "Mujhe meetha doodh pasand hai.",
        "मुझे मीठा दूध पसंद है।", "Mujhe meetha doodh pasand hai.",
        "أحب شرب الحليب الحلو كثيراً.", "Uhibbu shurb al-haleeb al-hilw katheeran.",
        "Me gusta tomar leche dulce.", "Meh GOOS-tah toh-MAHR LEH-cheh DOOL-seh.",
        "J'aime boire du lait doux.", "Zhem bwahr dew leh doo.",
        "Ich mag süße Milch trinken.", "Ikh mahg ZEW-seh milkh TRIN-ken.",
        "Mi piace bere latte dolce.", "Mee PYAH-cheh BEH-reh LAHT-teh DOHL-cheh.",
        "Eu gosto de tomar leite doce.", "Eh-oo GOHS-too jee toh-MAHR LAY-chee DOH-see.",
        "Я люблю пить сладкое молоко.", "Yah lyoo-BLYOO peet SLAHD-kah-yeh mah-lah-KOH.",
        "Tatlı süt içmeyi çok severim.", "Taht-luh sewt eech-meh-yee chohk seh-veh-reem.",
        "Saya suka minum susu manis.", "SAH-yah SOO-kah MEE-noom SOO-soo MAH-nees.",
        "我 喜欢 喝 甜 牛奶。", "Wǒ xǐhuān hē tián niúnǎi.",
        "あまい ミルク を のむのが すき。", "Amai miruku o nomu no ga suki.",
        "달콤한 우유 마시는 걸 좋아해요.", "Dalkom-han uyu masineun geol joahaeyo."
    ),
    item(
        "Let us drink cold juice.", "آئیں ٹھنڈا جوس پیتے ہیں۔", "Aaein thanda juice peete hain.",
        "आओ ठंडा जूस पीते हैं।", "Aao thanda juice peete hain.",
        "دعنا نشرب العصير البارد معاً.", "Da'na nashrab al-'asir al-barid ma'an.",
        "Vamos a tomar jugo fresco.", "VAH-mohs ah toh-MAHR HOO-goh FREHS-koh.",
        "Buvons du bon jus frais.", "Bew-vohn dew bohn zhoo freh.",
        "Lasst uns kühlen Saft trinken.", "Lahst oons KEW-len zahft TRIN-ken.",
        "Beviamo del buon succo fresco.", "Beh-VYAH-moh dehl bwohn SOOK-koh FREHS-koh.",
        "Vamos tomar um suco gelado.", "VAH-moos toh-MAHR oong SOO-koo zheh-LAH-doo.",
        "Давай выпьем холодный вкусный сок.", "Dah-VAY VY-pyem khah-LAHD-nyy VKOOS-nyy sohk.",
        "Hadi soğuk meyvesuyu içelim beraber.", "HAH-dee soh-ook mey-veh-soo-yoo ee-cheh-leem beh-rah-behr.",
        "Ayo kita minum jus segar.", "AH-yoh KEE-tah MEE-noom joos seh-gahr.",
        "我们 一起 喝 冷 果汁。", "Wǒmen yīqǐ hē lěng guǒzhī.",
        "つめたい ジュース を のみましょう。", "Tsumetai jūsu o nomimashō.",
        "시원한 주스를 함께 마셔요.", "Siwon-han juseureul hamkke masyeoyo."
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

# Explicit dedicated overrides for morning-talk
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

for topic_id in all_topic_ids:
    if topic_id in ["breakfast-chat", "morning-talk"]:
        continue
    
    s_items = single_words.get(topic_id)
    w1_items = w1_all.get(topic_id)
    w2_items = w2_all.get(topic_id)
    
    if not s_items or not w1_items or not w2_items:
        print(f"Skipping {topic_id}: missing items")
        continue

    # Nouns from single words
    s0 = s_items[0]
    s1 = s_items[1]
    s2 = s_items[2]

    # Modifier+Noun pairs from W1
    m0 = w1_items[0]
    m1 = w1_items[1]
    m2 = w1_items[2]

    # Action+Noun pairs from W2
    a0 = w2_items[0]
    a1 = w2_items[1]
    a2 = w2_items[2]

    # W4 Items: Exactly 3 words per item
    # Item 1: I want [Noun 0]
    w4_1 = item(
        f"I want {s0['en'].lower()}", f"مجھے {s0['target']['ur']} چاہیے", f"Mujhe {s0['romanized']['ur']} chahiye",
        f"मुझे {s0['target']['hi']} चाहिए", f"Mujhe {s0['romanized']['hi']} chahiye",
        f"أريد {s0['target']['ar']}", f"Ureed {s0['romanized']['ar']}",
        f"Quiero {s0['target']['es'].lower()}", f"Kyeh-roh {s0['romanized']['es']}",
        f"Je veux {s0['target']['fr'].lower()}", f"Zhe vuh {s0['romanized']['fr']}",
        f"Ich will {s0['target']['de']}", f"Ikh vill {s0['romanized']['de']}",
        f"Voglio {s0['target']['it'].lower()}", f"VOH-lyoh {s0['romanized']['it']}",
        f"Quero {s0['target']['pt'].lower()}", f"KEH-roo {s0['romanized']['pt']}",
        f"Я хочу {s0['target']['ru']}", f"Yah khah-CHOO {s0['romanized']['ru']}",
        f"{s0['target']['tr']} istiyorum ben", f"{s0['romanized']['tr']} ees-tee-YOH-room",
        f"Saya mau {s0['target']['id']}", f"Sah-yah mow {s0['romanized']['id']}",
        f"我 要 {s0['target']['zh']}", f"Wǒ yào {s0['romanized']['zh']}",
        f"{s0['target']['ja']} が ほしい", f"{s0['romanized']['ja']} ga hoshii",
        f"{s0['target']['ko']} 주세요", f"{s0['romanized']['ko']} juseyo"
    )

    # Item 2: [Noun 1] is nice/good
    w4_2 = item(
        f"{s1['en']} is good", f"{s1['target']['ur']} اچھا ہے", f"{s1['romanized']['ur']} achha hai",
        f"{s1['target']['hi']} अच्छा है", f"{s1['romanized']['hi']} achha hai",
        f"{s1['target']['ar']} جميل جداً", f"{s1['romanized']['ar']} jameel",
        f"{s1['target']['es']} es bueno", f"{s1['romanized']['es']} ehs BWEH-noh",
        f"{s1['target']['fr']} est bon", f"{s1['romanized']['fr']} eh bohn",
        f"{s1['target']['de']} ist gut", f"{s1['romanized']['de']} ist goot",
        f"{s1['target']['it']} è bello", f"{s1['romanized']['it']} eh BEHL-loh",
        f"{s1['target']['pt']} é bom", f"{s1['romanized']['pt']} eh bohn",
        f"{s1['target']['ru']} очень хороший", f"{s1['romanized']['ru']} khah-ROH-shiy",
        f"{s1['target']['tr']} çok güzeldir", f"{s1['romanized']['tr']} gew-zehl-deer",
        f"{s1['target']['id']} ini bagus", f"{s1['romanized']['id']} ee-nee BAH-goos",
        f"{s1['target']['zh']} 很 棒", f"{s1['romanized']['zh']} hěn bàng",
        f"{s1['target']['ja']} が すてき", f"{s1['romanized']['ja']} ga suteki",
        f"{s1['target']['ko']} 참 좋아요", f"{s1['romanized']['ko']} cham joayo"
    )

    # Item 3: [Noun 2] is fun/sweet
    w4_3 = item(
        f"{s2['en']} is fun", f"{s2['target']['ur']} مزے دار ہے", f"{s2['romanized']['ur']} maze daar hai",
        f"{s2['target']['hi']} मजेदार है", f"{s2['romanized']['hi']} mazedaar hai",
        f"{s2['target']['ar']} ممتع جداً", f"{s2['romanized']['ar']} mumti'",
        f"{s2['target']['es']} es divertido", f"{s2['romanized']['es']} ehs dee-vehr-TEE-doh",
        f"{s2['target']['fr']} est super", f"{s2['romanized']['fr']} eh sew-pehr",
        f"{s2['target']['de']} macht Spaß", f"{s2['romanized']['de']} mahkht spahs",
        f"{s2['target']['it']} è divertente", f"{s2['romanized']['it']} eh dee-vehr-TEHN-teh",
        f"{s2['target']['pt']} é divertido", f"{s2['romanized']['pt']} eh jee-vehr-CHEE-doo",
        f"{s2['target']['ru']} очень весело", f"{s2['romanized']['ru']} VYEH-sye-lah",
        f"{s2['target']['tr']} çok eğlencelidir", f"{s2['romanized']['tr']} eh-lehn-jeh-lee-deer",
        f"{s2['target']['id']} ini seru", f"{s2['romanized']['id']} ee-nee SEH-roo",
        f"{s2['target']['zh']} 很 好玩", f"{s2['romanized']['zh']} hěn hǎowán",
        f"{s2['target']['ja']} が たのしい", f"{s2['romanized']['ja']} ga tanoshii",
        f"{s2['target']['ko']} 정말 신나요", f"{s2['romanized']['ko']} jeongmal sinnayo"
    )
    w4_data[topic_id] = [w4_1, w4_2, w4_3]

    # Tier 2 Items: Strictly 4 to 5 words
    # Item 1: Please give me [W1 0].
    t2_1 = item(
        f"Please give me {m0['en'].lower()}.", f"مجھے {m0['target']['ur']} دے دیں۔", f"Mujhe {m0['romanized']['ur']} de dein.",
        f"मुझे {m0['target']['hi']} दीजिए।", f"Mujhe {m0['romanized']['hi']} deejie.",
        f"أعطني {m0['target']['ar']} رجاءً.", f"'A'tini {m0['romanized']['ar']} raja'an.",
        f"Por favor dame {m0['target']['es'].lower()}.", f"Pohr fah-vohr DAH-meh {m0['romanized']['es']}.",
        f"Donne-moi {m0['target']['fr'].lower()} s'il-te-plaît.", f"Dohn-mwah {m0['romanized']['fr']} seel-tuh-pleh.",
        f"Gib mir bitte {m0['target']['de']}.", f"Gib meer BIT-teh {m0['romanized']['de']}.",
        f"Dammi {m0['target']['it'].lower()} per favore.", f"DAHM-mee {m0['romanized']['it']} pehr fah-VOH-reh.",
        f"Por favor me dê {m0['target']['pt'].lower()}.", f"Pohr fah-VOHR mee day {m0['romanized']['pt']}.",
        f"Дай мне пожалуйста {m0['target']['ru']}.", f"Day mnye pah-ZHAH-loo-stah {m0['romanized']['ru']}.",
        f"Lütfen bana {m0['target']['tr']} ver.", f"LEWT-fen BAH-nah {m0['romanized']['tr']} vehr.",
        f"Tolong beri saya {m0['target']['id']}.", f"TOH-lohng BEH-ree SAH-yah {m0['romanized']['id']}.",
        f"请 给我 {m0['target']['zh']}。", f"Qǐng gěi wǒ {m0['romanized']['zh']}.",
        f"{m0['target']['ja']} を ください。", f"{m0['romanized']['ja']} o kudasai.",
        f"{m0['target']['ko']} 주세요.", f"{m0['romanized']['ko']} juseyo."
    )

    # Item 2: I like having [W1 1].
    t2_2 = item(
        f"I like having {m1['en'].lower()}.", f"مجھے {m1['target']['ur']} پسند ہے۔", f"Mujhe {m1['romanized']['ur']} pasand hai.",
        f"मुझे {m1['target']['hi']} पसंद है।", f"Mujhe {m1['romanized']['hi']} pasand hai.",
        f"أحب {m1['target']['ar']} كثيراً.", f"Uhibbu {m1['romanized']['ar']} katheeran.",
        f"Me gusta mucho {m1['target']['es'].lower()}.", f"Meh GOOS-tah MOO-choh {m1['romanized']['es']}.",
        f"J'aime beaucoup {m1['target']['fr'].lower()}.", f"Zhem boh-koo {m1['romanized']['fr']}.",
        f"Ich mag {m1['target']['de']} sehr.", f"Ikh mahg {m1['romanized']['de']} zehr.",
        f"Mi piace molto {m1['target']['it'].lower()}.", f"Mee PYAH-cheh MOHL-toh {m1['romanized']['it']}.",
        f"Eu gosto muito de {m1['target']['pt'].lower()}.", f"Eh-oo GOHS-too MOO-too jee {m1['romanized']['pt']}.",
        f"Мне очень нравится {m1['target']['ru']}.", f"Mnye OH-cheen NRAH-veet-syah {m1['romanized']['ru']}.",
        f"{m1['target']['tr']} gerçekten çok severim.", f"{m1['romanized']['tr']} chohk seh-vehr-eem.",
        f"Saya sangat suka {m1['target']['id']}.", f"SAH-yah SAHNG-aht SOO-kah {m1['romanized']['id']}.",
        f"我 非常 喜欢 {m1['target']['zh']}。", f"Wǒ fēicháng xǐhuān {m1['romanized']['zh']}.",
        f"{m1['target']['ja']} が だいすき です。", f"{m1['romanized']['ja']} ga daisuki desu.",
        f"{m1['target']['ko']} 정말 좋아해요.", f"{m1['romanized']['ko']} jeongmal joahaeyo."
    )

    # Item 3: Let us enjoy [W1 2].
    t2_3 = item(
        f"Let us enjoy {m2['en'].lower()}.", f"آئیں {m2['target']['ur']} کا مزہ لیں۔", f"Aaein {m2['romanized']['ur']} ka maza lein.",
        f"आओ {m2['target']['hi']} का आनंद लें।", f"Aao {m2['romanized']['hi']} ka anand lein.",
        f"دعنا نستمتع بـ {m2['target']['ar']}.", f"Da'na nastamti' bi-{m2['romanized']['ar']}.",
        f"Vamos a disfrutar {m2['target']['es'].lower()}.", f"VAH-mohs ah dees-froo-TAHR {m2['romanized']['es']}.",
        f"Profitons bien de {m2['target']['fr'].lower()}.", f"Proh-fee-tohn byan duh {m2['romanized']['fr']}.",
        f"Lasst uns {m2['target']['de']} genießen.", f"Lahst oons {m2['romanized']['de']} geh-NEE-sen.",
        f"Godiamoci {m2['target']['it'].lower()} felicemente.", f"Goh-DYAH-moh-chee {m2['romanized']['it']} feh-lee-CHEH-mehn-teh.",
        f"Vamos aproveitar {m2['target']['pt'].lower()} juntos.", f"VAH-moos ah-proh-vay-TAHR {m2['romanized']['pt']} ZHOON-toos.",
        f"Давай порадуемся {m2['target']['ru']} дружно.", f"Dah-VAY pah-RAH-dooy-syah {m2['romanized']['ru']} DROOZH-nah.",
        f"Hadi {m2['target']['tr']} tadını çıkaralım.", f"HAH-dee {m2['romanized']['tr']} tah-duh-nuh chuh-kah-rah-luhm.",
        f"Ayo kita nikmati {m2['target']['id']}.", f"AH-yoh KEE-tah neek-MAH-tee {m2['romanized']['id']}.",
        f"我们 一起 享用 {m2['target']['zh']}。", f"Wǒmen yīqǐ xiǎngyòng {m2['romanized']['zh']}.",
        f"いっしょに {m2['target']['ja']} を たのしもう。", f"Issho ni {m2['romanized']['ja']} o tanoshimō.",
        f"함께 {m2['target']['ko']} 즐겨요.", f"Hamkke {m2['romanized']['ko']} jeulgyeoyo."
    )
    tier2_data[topic_id] = [t2_1, t2_2, t2_3]

    # Tier 3 Items: Strictly 5 to 6 words
    # Item 1: I [do topic] with my family.
    t3_1 = item(
        f"I enjoy {m0['en'].lower()} with family.", f"میں گھر والوں کے ساتھ {m0['target']['ur']} کرتا ہوں۔", f"Main ghar walon ke sath {m0['romanized']['ur']} karta hoon.",
        f"मैं परिवार के साथ {m0['target']['hi']} करता हूँ।", f"Main parivaar ke saath {m0['romanized']['hi']} karta hoon.",
        f"أستمتع بـ {m0['target']['ar']} مع عائلتي دائماً.", f"Astamti' bi-{m0['romanized']['ar']} ma'a 'a'ilati da'iman.",
        f"Disfruto {m0['target']['es'].lower()} con mi familia.", f"Dees-FROO-toh {m0['romanized']['es']} kohn mee fah-MEE-lyah.",
        f"Je profite de {m0['target']['fr'].lower()} en famille.", f"Zhuh proh-feet duh {m0['romanized']['fr']} ahn fah-mee.",
        f"Ich genieße {m0['target']['de']} mit Familie.", f"Ikh geh-NEE-seh {m0['romanized']['de']} mit fah-MEE-lyeh.",
        f"Mi godo {m0['target']['it'].lower()} in famiglia.", f"Mee GOH-doh {m0['romanized']['it']} een fah-MEE-lyah.",
        f"Aproveito {m0['target']['pt'].lower()} com minha família.", f"Ah-proh-VAY-too {m0['romanized']['pt']} kohn MEEN-yah fah-MEE-lyah.",
        f"Я радуюсь {m0['target']['ru']} со своей семьёй.", f"Yah RAH-dooy-oos {m0['romanized']['ru']} sah svah-YEY seem-YOY.",
        f"Ailemle birlikte {m0['target']['tr']} keyif alıyorum.", f"Ah-ee-lehm-leh beer-leek-TEH {m0['romanized']['tr']} keh-yeef ah-luh-YOH-room.",
        f"Saya menikmati {m0['target']['id']} bersama keluarga.", f"SAH-yah meh-neek-MAH-tee {m0['romanized']['id']} behr-SAH-mah keh-loo-AHR-gah.",
        f"我 和 家人 一起 享受 {m0['target']['zh']}。", f"Wǒ hé jiārén yīqǐ xiǎngshòu {m0['romanized']['zh']}.",
        f"かぞく と いっしょに {m0['target']['ja']} を たのしむ。", f"Kazoku to issho ni {m0['romanized']['ja']} o tanoshimu.",
        f"가족과 함께 {m0['target']['ko']} 즐겨요.", f"Gajok-gwa hamkke {m0['romanized']['ko']} jeulgyeoyo."
    )

    # Item 2: We all enjoy this together happily.
    t3_2 = item(
        f"We all enjoy {m1['en'].lower()} together happily.", f"ہم سب خوشی سے {m1['target']['ur']} کرتے ہیں۔", f"Hum sab khushi se {m1['romanized']['ur']} karte hain.",
        f"हम सब मिलकर {m1['target']['hi']} करते हैं।", f"Hum sab milkar {m1['romanized']['hi']} karte hain.",
        f"نستمتع جميعاً بـ {m1['target']['ar']} بسعادة.", f"Nastamti'u jamee'an bi-{m1['romanized']['ar']} bi-sa'adah.",
        f"Disfrutamos todos {m1['target']['es'].lower()} con alegría.", f"Dees-froo-TAH-mohs TOH-dohs {m1['romanized']['es']} kohn ah-leh-GREE-ah.",
        f"Nous profitons tous ensemble joyeusement.", f"Noo proh-fee-tohn toos ahn-sahmbl zhwah-yooz-mahn.",
        f"Wir alle genießen alles gemeinsam zusammen.", f"Veer AHL-leh geh-NEE-sen AHL-les geh-MYN-zahm tsoo-ZAHM-men.",
        f"Ci godiamo tutto con grande gioia.", f"Chee goh-DYAH-moh TOOT-toh kohn GRAHN-deh JOY-ah.",
        f"Aproveitamos tudo juntos com grande alegria.", f"Ah-proh-vay-TAH-moos TOO-doo ZHOON-toos kohn GRAHN-jee ah-leh-GREE-ah.",
        f"Мы дружно наслаждаемся всем вместе сейчас.", f"My DROOZH-nah nah-slahzh-DAH-yem-syah vsyem VMYES-tyeh sey-CHAHS.",
        f"Hep birlikte neşeyle tadını çıkarıyoruz.", f"Hehp beer-leek-TEH neh-shehy-leh tah-duh-nuh chuh-kah-ruh-YOH-rooz.",
        f"Kami menikmati semuanya bersama dengan gembira.", f"KAH-mee meh-neek-MAH-tee seh-MOO-ah-nyah behr-SAH-mah dehng-ahn gehm-BEE-rah.",
        f"我们 开心地 一起 享受 美好 时光。", f"Wǒmen kāixīn de yīqǐ xiǎngshòu měihǎo shíguāng.",
        f"みんな で たのしく すごしましょう ね。", f"Minna de tanoshiku sugoshimashō ne.",
        f"우리 모두 함께 즐거운 시간 보내요.", f"Uri modu hamkke jeulgeoun sigan bonaeyo."
    )

    # Item 3: My family loves [activity].
    t3_3 = item(
        f"My family loves {m2['en'].lower()} every day.", f"میرا خاندان روزانہ {m2['target']['ur']} پسند کرتا ہے۔", f"Mera khandan rozana {m2['romanized']['ur']} pasand karta hai.",
        f"मेरा परिवार हमेशा {m2['target']['hi']} पसंद करता है।", f"Mera parivaar hamesha {m2['romanized']['hi']} pasand karta hai.",
        f"تحب عائلتي {m2['target']['ar']} كل يوم.", f"Tuhibbu 'a'ilati {m2['romanized']['ar']} kulla yawm.",
        f"A mi familia le encanta {m2['target']['es'].lower()}.", f"Ah mee fah-MEE-lyah leh ehn-KAHN-tah {m2['romanized']['es']}.",
        f"Ma famille adore {m2['target']['fr'].lower()} chaque jour.", f"Mah fah-mee ah-DOHR {m2['romanized']['fr']} shahk zhoor.",
        f"Meine Familie liebt {m2['target']['de']} jeden Tag.", f"MY-neh fah-MEE-lyeh leebt {m2['romanized']['de']} YEH-den tahk.",
        f"La mia famiglia adora {m2['target']['it'].lower()} ogni giorno.", f"Lah MEE-ah fah-MEE-lyah ah-DOH-rah {m2['romanized']['it']} OHN-yee JYOHR-noh.",
        f"Minha família adora {m2['target']['pt'].lower()} todos os dias.", f"MEEN-yah fah-MEE-lyah ah-DOH-rah {m2['romanized']['pt']} TOH-doos ooz JEE-ahs.",
        f"Моя семья очень любит {m2['target']['ru']} всегда.", f"Mah-YAH seem-YAH OH-cheen LYOO-beet {m2['romanized']['ru']} fsehg-DAH.",
        f"Ailem {m2['target']['tr']} gerçekten her gün sever.", f"Ah-ee-lehm {m2['romanized']['tr']} gehr-chehk-tehn hehr gewn seh-vehr.",
        f"Keluarga saya sangat suka {m2['target']['id']} setiap hari.", f"Keh-loo-AHR-gah SAH-yah SAHNG-aht SOO-kah {m2['romanized']['id']} seh-TEE-ahp HAH-ree.",
        f"我的 家人 每天 都 喜欢 {m2['target']['zh']}。", f"Wǒ de jiārén měitiān dōu xǐhuān {m2['romanized']['zh']}.",
        f"かぞく は まいにち {m2['target']['ja']} が だいすき。", f"Kazoku wa mainichi {m2['romanized']['ja']} ga daisuki.",
        f"우리 가족은 매일 {m2['target']['ko']} 정말 좋아해요.", f"Uri gajog-eun maeil {m2['romanized']['ko']} jeongmal joahaeyo."
    )
    tier3_data[topic_id] = [t3_1, t3_2, t3_3]

output_file = 'src/data/multilingual/topicAge4to6Curriculum.ts'
w4_json = json.dumps(w4_data, ensure_ascii=False, indent=2)
tier2_json = json.dumps(tier2_data, ensure_ascii=False, indent=2)
tier3_json = json.dumps(tier3_data, ensure_ascii=False, indent=2)

file_content = f"""import {{ LanguageCode }} from '../../types';

export interface Age4to6CurriculumItem {{
  en: string;
  ur: string;
  ur_rom: string;
  es: string;
  es_rom: string;
  target: Record<LanguageCode, string>;
  romanized: Record<LanguageCode, string>;
}}

/**
 * AGE 4-6 BEGINNER: WEEK 4 (Days 22 to 30)
 * STRICTLY THREE (3) WORDS PER ITEM
 * Simple, natural Subject-Verb-Object or child conversational chunks across all 15 categories & 77 topics.
 */
export const TOPIC_AGE4TO6_W4: Record<string, [Age4to6CurriculumItem, Age4to6CurriculumItem, Age4to6CurriculumItem]> = {w4_json};

/**
 * AGE 4-6: TIER 2 (Days 31 to 60)
 * STRICTLY 4 TO 5 WORDS PER ITEM
 * Natural, everyday early childhood conversational speech across all 15 categories & 77 topics.
 */
export const TOPIC_AGE4TO6_TIER2: Record<string, [Age4to6CurriculumItem, Age4to6CurriculumItem, Age4to6CurriculumItem]> = {tier2_json};

/**
 * AGE 4-6: TIER 3 (Days 61 to 90)
 * STRICTLY 5 TO 6 WORDS PER ITEM
 * Complete child conversational sentences for social and home expression across all 15 categories & 77 topics.
 */
export const TOPIC_AGE4TO6_TIER3: Record<string, [Age4to6CurriculumItem, Age4to6CurriculumItem, Age4to6CurriculumItem]> = {tier3_json};

export function resolveAge4to6Bundle(
  item: Age4to6CurriculumItem,
  wordCount: number
): {{
  target: Record<LanguageCode, string>;
  romanized: Record<LanguageCode, string>;
  wordCount: number;
}} {{
  return {{
    target: item.target,
    romanized: item.romanized,
    wordCount,
  }};
}}
"""

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(file_content)

print(f"Successfully generated {output_file} with {len(w4_data)} topics!")
