# Category 2: Shopping & Food (6), Health & Doctor (5), School & Study (5) = 16 topics
import os
import sys
sys.path.append(os.path.dirname(__file__))
from helper import item, export_ts_module

w1 = {}
w2 = {}

# 17. grocery-store
w1["grocery-store"] = [
    item(
        "Red apple", "سرخ سیب", "Surkh saib", "लाल सेब", "Laal seb",
        "تفاحة حمراء", "Tuffaha hamra'", "Manzana roja", "Mahn-ZAH-nah ROH-hah",
        "Pomme rouge", "Puhm roozh", "Roter Apfel", "ROH-ter AHP-fel",
        "Mela rossa", "MEH-lah ROHS-sah", "Maçã vermelha", "Mah-SAHN vehr-MEHL-yah",
        "Красное яблоко", "KRAHS-nah-yeh YAH-blah-kah", "Kırmızı elma", "Kuhr-muh-zuh el-mah",
        "Apel merah", "Ah-pehl meh-rah", "红 苹果", "Hóng píngguǒ",
        "赤い リンゴ", "Akai ringo", "빨간 사과", "Ppalgan sagwa"
    ),
    item(
        "Green pear", "سبز ناشپاتی", "Sabz naashpati", "हरी नाशपाती", "Hari naashpati",
        "كمثرى خضراء", "Kummathra khadra'", "Pera verde", "PEH-rah VEHR-deh",
        "Poire verte", "Pwahr vehrt", "Grüne Birne", "GREW-neh BEER-neh",
        "Pera verde", "PEH-rah VEHR-deh", "Pera verde", "PEH-rah VEHR-jee",
        "Зелёная груша", "Zyeh-LYOH-nah-yah GROO-shah", "Yeşil armut", "Yeh-sheel ahr-moot",
        "Pir hijau", "Peer hee-jow", "绿 梨子", "Lǜ lízi",
        "青い 洋梨", "Aoi yōnashi", "초록 배", "Chorok bae"
    ),
    item(
        "Full cart", "بھری ٹوکری", "Bhari tokri", "भरी टोकरी", "Bhari tokri",
        "عربة ممتلئة", "'Araba mumtali'a", "Carrito lleno", "Kah-RREE-toh YEH-noh",
        "Chariot plein", "Shah-ryoh plan", "Voller Wagen", "FOL-ler VAH-gen",
        "Carrello pieno", "Kahr-REHL-loh PYEH-noh", "Carrinho cheio", "Kahr-HEEN-yoo SHAY-oo",
        "Полная тележка", "POHL-nah-yah tyeh-LYEZH-kah", "Dolu sepet", "Doh-loo seh-pet",
        "Keranjang penuh", "Keh-rahn-jahng peh-nooh", "满 购物车", "Mǎn gòuwùchē",
        "いっぱいの カート", "Ippai no kāto", "가득찬 카트", "Gadeukchan kateu"
    )
]

w2["grocery-store"] = [
    item(
        "Pick fruit", "پھل چنو", "Phal chuno", "फल चुनो", "Phal chuno",
        "اختر فاكهة", "Ikhtar fakiha", "Escoge fruta", "Ehs-KOH-heh FROO-tah",
        "Choisis fruits", "Shwah-zee frwee", "Wähle Obst", "VAY-leh ohpst",
        "Scegli frutta", "SHEH-lyee FROOT-tah", "Escolha fruta", "Ehs-KOHL-yah FROO-tah",
        "Выбирай фрукты", "Vy-bee-RYE FROOK-ty", "Meyve seç", "Mey-veh sech",
        "Pilih buah", "Pee-leeh boo-ah", "挑 水果", "Tiāo shuǐguǒ",
        "果物 選ぶ", "Kudamono erabu", "과일 골라", "Gwail golla"
    ),
    item(
        "Push cart", "ٹرالی دھکیلو", "Trolley dhakelo", "ट्राली धकेलो", "Trolley dhakelo",
        "ادفع عربة", "Idfa' 'araba", "Empuja carrito", "Ehm-POO-hah kah-RREE-toh",
        "Pousse chariot", "Poos shah-ryoh", "Schieb Wagen", "SHEEP VAH-gen",
        "Spingi carrello", "SPEEN-jee kahr-REHL-loh", "Empurre carrinho", "Ehm-POO-hee kahr-HEEN-yoo",
        "Толкай тележку", "Tahl-KYE tyeh-LYEZH-koo", "Arabayı sür", "Ah-rah-bah-yuh sewr",
        "Dorong troli", "Doh-rohng troh-lee", "推 购物车", "Tuī gòuwùchē",
        "カート 押す", "Kāto osu", "카트 밀어", "Kateu mireo"
    ),
    item(
        "Count items", "چیزیں گنو", "Cheezein gino", "चीज़ें गिनो", "Cheezein gino",
        "عد الأغراض", "'Udd al-aghrad", "Cuenta cosas", "KWEHN-tah KOH-sahs",
        "Compte articles", "Kohnt ahr-teekl", "Zähl Sachen", "TSAYL ZAH-khen",
        "Conta cose", "KOHN-tah KOH-zeh", "Conte itens", "KOHN-chee EE-tehns",
        "Считай покупки", "Schee-TYE pah-KOOP-kee", "Ürünleri say", "Ew-rewn-leh-ree sigh",
        "Hitung belanjaan", "Hee-toong beh-lahn-jah-ahn", "数 物品", "Shǔ wùpǐn",
        "品物 数える", "Shinamono kazoeru", "물건 세어봐", "Mulgeon seobwa"
    )
]

# 18. buying-toys
w1["buying-toys"] = [
    item(
        "Shiny robot", "چمکدار روبوٹ", "Chamakdaar robot", "चमकदार रोबोट", "Chamakdaar robot",
        "روبوت لامع", "Rubut lami'", "Robot brillante", "ROH-boht bree-YAHN-teh",
        "Robot brillant", "Roh-boh bree-yahn", "Glänzender Roboter", "GLEN-tsen-der roh-BOH-ter",
        "Robot luccicante", "ROH-boht loot-chee-KAHN-teh", "Robô brilhante", "Hoh-BOH breel-YAHN-chee",
        "Блестящий робот", "Blye-STYAH-shiy ROH-baht", "Parlak robot", "Pahr-lahk roh-boht",
        "Robot mengkilap", "Roh-boht mehng-kee-lahp", "炫 机器人", "Xuàn jīqìrén",
        "ピカピカの ロボット", "Pikapika no robotto", "멋진 로봇", "Meotjin robot"
    ),
    item(
        "Soft teddy", "نرم ٹیڈی", "Naram teddy", "नरम टेडी", "Naram teddy",
        "دب ناعم", "Dubb na'im", "Osito suave", "Oh-SEE-toh SWAH-veh",
        "Nounours doux", "Noo-noors doo", "Weicher Bär", "VY-kher behr",
        "Peluche morbido", "Peh-LOO-sheh MOHR-bee-doh", "Ursinho macio", "Oor-SEEN-yoo mah-SEE-oo",
        "Мягкий мишка", "MYAHK-kiy MEESH-kah", "Yumuşak ayıcık", "Yoo-moo-shahk ah-yuh-juhk",
        "Boneka lembut", "Boh-neh-kah lehm-boot", "软 玩偶", "Ruǎn wán'ǒu",
        "ふわふわな クマ", "Fuwafuwana kuma", "포근한 곰인형", "Pogeun-han gomin-hyeong"
    ),
    item(
        "New puzzle", "نیا پزل", "Naya puzzle", "नई पहेली", "Nayi paheli",
        "لغز جديد", "Lughz jadid", "Rompecabezas nuevo", "Rohm-peh-kah-BEH-zahs NWEH-voh",
        "Nouveau puzzle", "Noo-voh poorz-luh", "Neues Puzzle", "NOY-es POOTS-leh",
        "Puzzle nuovo", "POOD-dzleh NWAW-voh", "Quebra-cabeça novo", "KEH-brah kah-BEH-sah NOH-voo",
        "Новый пазл", "NOH-vyy PAHZ-l", "Yeni yapboz", "Yeh-nee yahp-bohz",
        "Teka-teki baru", "Teh-kah teh-kee bah-roo", "新 拼图", "Xīn pīntú",
        "新しい パズル", "Atarashii pazuru", "새로운 퍼즐", "Saeroun peojeul"
    )
]

w2["buying-toys"] = [
    item(
        "Choose toy", "کھلونا چنو", "Khilona chuno", "खिलौना चुनो", "Khilauna chuno",
        "اختر لعبة", "Ikhtar lu'ba", "Elige juguete", "Eh-LEE-heh hoo-GEH-teh",
        "Choisis jouet", "Shwah-zee zhoo-ay", "Wähl Spielzeug", "VAYL SHPEEL-tsoyk",
        "Scegli giocattolo", "SHEH-lyee joh-KAHT-toh-loh", "Escolha brinquedo", "Ehs-KOHL-yah breen-KAY-doo",
        "Выбери игрушку", "VY-bye-ree eeg-ROOSH-koo", "Oyuncak seç", "Oh-yoon-jahk sech",
        "Pilih mainan", "Pee-leeh my-nahn", "选 玩具", "Xuǎn wánjù",
        "おもちゃ 選ぶ", "Omocha erabu", "장난감 골라", "Jangnamgam golla"
    ),
    item(
        "Hold box", "ڈبہ پکڑو", "Dabba pakro", "डिब्बा पकड़ो", "Dibba pakdo",
        "أمسك علبة", "Amsik 'ulba", "Sostén caja", "Sohs-TEHN KAH-hah",
        "Tiens boîte", "Tyan bwaht", "Halt Schachtel", "HAHLT SHAHKH-tel",
        "Tieni scatola", "TYEH-nee SKAH-toh-lah", "Segure caixa", "Seh-GOO-ree KYE-shah",
        "Держи коробку", "Dyehr-ZHY kah-ROHP-koo", "Kutuyu tut", "Koo-too-yoo toot",
        "Pegang kotak", "Peh-gahng koh-tahk", "拿 盒子", "Ná hézi",
        "箱 持つ", "Hako motsu", "상자 잡아", "Sangja jaba"
    ),
    item(
        "Smile big", "خوش ہو جاؤ", "Khush ho jaao", "खुश हो जाओ", "Khush ho jaao",
        "افرح بالهدية", "Ifrah bil-hadiyya", "Sonríe feliz", "Sohn-REE-eh feh-LEES",
        "Souris grand", "Soo-ree grahn", "Freu dich", "FROY dikh",
        "Sorridi felice", "Sohr-REE-dee feh-LEE-cheh", "Sorria feliz", "Sohr-HEE-ah feh-LEES",
        "Радуйся игрушке", "RAH-dooy-syah eeg-ROOSH-kyeh", "Neşeyle gül", "Neh-shay-leh gewl",
        "Tersenyum girang", "Tehr-sehn-yoom gee-rahng", "开 心笑", "Kāixīn xiào",
        "嬉しく 笑う", "Ureshiku warau", "환하게 웃어", "Hwanhage useo"
    )
]

# 19. paying-cashier
w1["paying-cashier"] = [
    item(
        "Friendly cashier", "مہربان کیشیئر", "Meherbaan cashier", "मिलनसार कैशियर", "Milansaar cashier",
        "محاسب ودود", "Muhasib wadud", "Cajero amable", "Kah-HEH-roh ah-MAH-bleh",
        "Caissier poli", "Keh-syay poh-lee", "Netter Kassierer", "NET-ter kah-SEE-rer",
        "Cassiere gentile", "Kahs-SYEH-reh jehn-TEE-leh", "Caixa gentil", "KYE-shah zheng-TEEL",
        "Приветливый кассир", "Pree-VYEHT-lee-vyy kahs-SEER", "Güler yüzlü kasiyer", "Gew-lehr yewz-lew kah-see-yehr",
        "Kasir ramah", "Kah-seer rah-mah", "善 收银员", "Shàn shōuyínyuán",
        "親切な レジ係", "Shinsetsu na rejigakari", "친절한 계산원", "Chinjeol-han gyesanwon"
    ),
    item(
        "Paper bill", "کاغذی نوٹ", "Kaghzi note", "काग़ज़ी नोट", "Kaagzi note",
        "فاتورة ورقية", "Fatura waraqiyya", "Billete limpio", "Beel-YEH-teh LEEM-pyoh",
        "Billet propre", "Bee-yay proh-pruh", "Papierschein heil", "PAH-peer-shyn hyle",
        "Banconota pulita", "Bahn-koh-NOH-tah poo-LEE-tah", "Nota nova", "NAW-tah NOH-vah",
        "Бумажная купюра", "Boo-MAHZH-nah-yah koo-PYOO-rah", "Kâğıt para", "Kah-uht pah-rah",
        "Uang kertas", "Oo-ahng kehr-tahs", "整 纸币", "Zhěng zhǐbì",
        "きれいな お札", "Kireina osatsu", "깨끗한 지폐", "Kkaekkeut-han jipye"
    ),
    item(
        "Neat receipt", "صاف رسید", "Saaf raseed", "साफ़ रसीद", "Saaf raseed",
        "إيصال واضح", "Iysal wadih", "Recibo claro", "Reh-SEE-boh KLAH-roh",
        "Reçu propre", "Ruh-soo proh-pruh", "Gedruckter Beleg", "Geh-DROOK-ter beh-LAYK",
        "Scontrino chiaro", "Skohn-TREE-noh KYAH-roh", "Recibo limpo", "Heh-SEE-boo LEEM-poo",
        "Чёткий чек", "CHOHT-kiy cheek", "Açık fiş", "Ah-chuhk feesh",
        "Struk belanja", "Strook beh-lahn-jah", "清 小票", "Qīng xiǎopiào",
        "印字された レシート", "Injisareta reshīto", "깔끔한 영수증", "Kkalkkeum-han yeongsujeung"
    )
]

w2["paying-cashier"] = [
    item(
        "Give money", "پیسے دو", "Paise do", "पैसे दो", "Paise do",
        "ادفع مالاً", "Idfa' malan", "Paga dinero", "PAH-gah dee-NEH-roh",
        "Donne argent", "Dohn ahr-zhahn", "Gib Geld", "GIP gelt",
        "Paga soldi", "PAH-gah SOHL-dee", "Pague dinheiro", "PAH-gee jee-NYAY-roo",
        "Отдай деньги", "Aht-DYE DYEHN-gee", "Parayı ver", "Pah-rah-yuh vehr",
        "Beri uang", "Beh-ree oo-ahng", "付 钱", "Fù qián",
        "お札 渡す", "Osatsu watasu", "돈 건네", "Don geonne"
    ),
    item(
        "Take change", "بقایا لو", "Baqaaya lo", "बचे पैसे लो", "Bache paise lo",
        "خذ الباقي", "Khudh al-baqi", "Toma cambio", "TOH-mah KAHM-byoh",
        "Prends monnaie", "Prahn mohn-nay", "Nimm Wechselgeld", "NIM VEK-sel-gelt",
        "Prendi resto", "PREHN-dee REHS-toh", "Pegue troco", "PEH-gee TRAW-koo",
        "Возьми сдачу", "Vahz-MEE SDAH-choo", "Para üstü al", "Pah-rah ews-tew ahl",
        "Ambil kembalian", "Ahm-beel kehm-bah-lee-ahn", "找 零钱", "Zhǎo língqián",
        "お釣り 受け取る", "Otsuri uketoru", "거스름돈 받아", "Geoseureumdon bada"
    ),
    item(
        "Say bye", "خدا حافظ", "Khuda hafiz", "अलविदा कहो", "Alvida kaho",
        "قل وداعاً", "Qul wada'an", "Di adiós", "DEE ah-DYOHS",
        "Dis au-revoir", "Dee oh-ruh-vwahr", "Sag Tschüss", "ZAHK chyoos",
        "Dì ciao", "DEE chow", "Diga tchau", "JEE-gah chow",
        "Скажи пока", "Skah-ZHY pah-KAH", "Hoşça kal", "Hohsh-chah kahl",
        "Ucap pamit", "Oo-chahp pah-meet", "说 再见", "Shuō zàijiàn",
        "さようなら 言う", "Sayōnara iu", "안녕히 계세요", "Annyeonghi gyeseyo"
    )
]

# 20. ordering-snacks
w1["ordering-snacks"] = [
    item(
        "Crispy chips", "کرکرے چپس", "Kurkuray chips", "कुरकुरे चिप्स", "Kurkure chips",
        "رقائق مقرمشة", "Raqa'iq muqarmasha", "Papas crujientes", "PAH-pahs kroo-HYEHN-tehs",
        "Chips croustillantes", "Sheeps kroos-tee-yahnt", "Knusprige Chips", "KNOOS-pree-geh chips",
        "Patatine croccanti", "Pah-tah-TEE-neh krohk-KAHN-tee", "Batatas crocantes", "Bah-TAH-tahs kroh-KAHN-tahs",
        "Хрустящие чипсы", "Khroo-STYAH-shye-yeh CHEEP-sy", "Çıtır cips", "Chuh-tuhr jeeps",
        "Keripik renyah", "Keh-ree-peek rehn-yah", "脆 薯片", "Cuì shǔpiàn",
        "カリカリの ポテチ", "Karikari no potechi", "바삭한 칩", "Basak-han chip"
    ),
    item(
        "Sweet cake", "میٹھا کیک", "Meetha cake", "मीठा केक", "Meetha cake",
        "كعكة حلوة", "Ka'ka hulwa", "Pastel dulce", "Pahs-TEHL DOOL-seh",
        "Gâteau doux", "Gah-toh doo", "Süßer Kuchen", "ZYOO-ser KOO-khen",
        "Torta dolce", "TOHR-tah DOHL-cheh", "Bolo gostoso", "BOH-loo gohs-TOH-zoo",
        "Сладкий торт", "SLAHT-kiy tohrt", "Tatlı pasta", "Taht-luh pahs-tah",
        "Kue lezat", "Koo-eh leh-zaht", "甜 蛋糕", "Tián dàngāo",
        "甘い ケーキ", "Amai kēki", "달콤한 케이크", "Dalkom-han keikeu"
    ),
    item(
        "Cold shake", "ٹھنڈا شیک", "Thanda shake", "ठंडा शेक", "Thanda shake",
        "مخفوق بارد", "Makhfuq barid", "Batido frío", "Bah-TEE-doh FREE-oh",
        "Milkshake frais", "Meelk-shayk freh", "Kalter Shake", "KAHL-ter shayk",
        "Frappé fresco", "Frahp-PAY FREHS-koh", "Milkshake gelado", "Meelk-shay-kee zheh-LAH-doo",
        "Холодный коктейль", "Khah-LAHD-nyy kahk-TYEHL", "Soğuk kokteyl", "Soh-ook kohk-teyl",
        "Kocok dingin", "Koh-chohk deeng-een", "冰 奶昔", "Bīng nǎixī",
        "冷たい シェイク", "Tsumetai sheiku", "시원한 셰이크", "Siwon-han syeikeu"
    )
]

w2["ordering-snacks"] = [
    item(
        "Order snack", "ناشتہ مانگو", "Naashta maango", "नाश्ता माँगो", "Naashta maango",
        "اطلب وجبة", "Itlub wajba", "Pide merienda", "PEE-deh meh-RYEHN-dah",
        "Commande goûter", "Koh-mahnd goo-tay", "Bestell Snack", "Beh-SHTEL sneck",
        "Ordina merenda", "OHR-dee-nah meh-REHN-dah", "Peça lanche", "PEH-sah LAHN-shee",
        "Закажи перекус", "Zah-kah-ZHY pyeh-ryeh-KOOS", "Atıştırmalık iste", "Ah-tush-tuhr-mah-luhk ees-teh",
        "Pesan camilan", "Peh-sahn chah-mee-lahn", "点 小吃", "Diǎn xiǎochī",
        "おやつ 頼む", "Oyatsu tanomu", "간식 주문해", "Gansik jumunhae"
    ),
    item(
        "Eat treat", "میٹھی چیز کھاؤ", "Meethi cheez khao", "मिठाई खाओ", "Mithaai khao",
        "تذوق حلوى", "Tadhawwaq halwa", "Come dulce", "KOH-meh DOOL-seh",
        "Mange friandise", "Manzh free-yahn-deez", "Genieß Leckerei", "Geh-NEES LEK-keh-rye",
        "Gusta dolce", "GOOS-tah DOHL-cheh", "Coma doce", "KOH-mah DOH-see",
        "Попробуй лакомство", "Pah-PROH-buy LAH-kahmst-vah", "Tatlıyı tat", "Taht-luh-yuh taht",
        "Nikmati kudapan", "Neek-mah-tee koo-dah-pahn", "品 甜品", "Pǐn tiánpǐn",
        "おやつ 味わう", "Oyatsu ajiwau", "디저트 먹어", "Dijeoteu meogeo"
    ),
    item(
        "Say please", "براہ مہربانی", "Barahe meherbaani", "कृपया कहो", "Kripya kaho",
        "قل من فضلك", "Qul min fadlik", "Di por favor", "DEE pohr fah-VOHR",
        "Dis s'il vous plaît", "Dee seel voo play", "Sag Bitte", "ZAHK BIT-teh",
        "Dì per favore", "DEE pehr fah-VOH-reh", "Diga por favor", "JEE-gah pohr fah-VOHR",
        "Скажи пожалуйста", "Skah-ZHY pah-ZHAH-loo-stah", "Lütfen de", "Lewt-fen deh",
        "Katakan tolong", "Kah-tah-kahn toh-lohng", "请 客气点", "Qǐng kèqidiǎn",
        "「お願いします」と言う", "Onegaishimasu to iu", "부탁한다고 말해", "Butak-handago malhae"
    )
]

# 21. street-food
w1["street-food"] = [
    item(
        "Hot samosa", "گرم سموسہ", "Garam samosa", "गर्म समोसा", "Garm samosa",
        "سمبوسة ساخنة", "Sambusa sakhina", "Empanada caliente", "Ehm-pah-NAH-dah kah-LYEHN-teh",
        "Samoussa chaud", "Sah-moo-sah sho", "Heißer Snack", "HY-ser sneck",
        "Pasticcio caldo", "Pahs-TEET-choh KAHL-doh", "Pastel quente", "Pahs-TEHL KEHN-chee",
        "Горячий пирожок", "Gah-RYAH-chiy pee-rah-ZHOHK", "Sıcak börek", "Suh-dzhak ber-rek",
        "Pastel hangat", "Pahs-tehl hahng-aht", "热 炸角", "Rè zhàjiǎo",
        "揚げたて サモサ", "Agetate samosa", "뜨거운 사모사", "Tteugeoun samosa"
    ),
    item(
        "Spicy sauce", "تیز چٹنی", "Tez chatni", "तीखी चटनी", "Teekhi chatni",
        "صلصة حارة", "Salsa harra", "Salsa picante", "SAHL-sah pee-KAHN-teh",
        "Sauce piquante", "Sohs pee-kahnt", "Scharfe Soße", "SHAHR-feh ZOH-seh",
        "Salsa piccante", "SAHL-sah peek-KAHN-teh", "Molho picante", "MOHL-yoo pee-KAHN-chee",
        "Острый соус", "OHS-tryy SOH-oos", "Acı sos", "Ah-juh sohs",
        "Saus pedas", "Sow-oos peh-dahs", "辣 酱汁", "Là jiàngzhī",
        "ピリ辛 タレ", "Pirikara tare", "매콤한 소스", "Maekom-han soseu"
    ),
    item(
        "Sweet corn", "میٹھی چھلی", "Meethi chhalli", "मीठा भुट्टा", "Meetha bhutta",
        "ذرة حلوة", "Dhurra hulwa", "Maíz tierno", "Mah-EES TYEHR-noh",
        "Maïs doux", "Mah-ees doo", "Süßer Mais", "ZYOO-ser myse",
        "Mais dolce", "MAH-ees DOHL-cheh", "Milho doce", "MEEL-yoo DOH-see",
        "Сладкая кукуруза", "SLAHT-kah-yah koo-koo-ROO-zah", "Tatlı mısır", "Taht-luh muh-suhr",
        "Jagung manis", "Jah-goong mah-nees", "甜 玉米", "Tián yùmǐ",
        "甘い とうもろこし", "Amai tōmorokoshi", "달콤한 옥수수", "Dalkom-han oksusu"
    )
]

w2["street-food"] = [
    item(
        "Smell aroma", "خوشبو سونگھو", "Khushboo soongho", "ख़ुशबू सूँघो", "Khushboo soongho",
        "شم رائحة", "Shumm ra'iha", "Huele aroma", "WEH-leh ah-ROH-mah",
        "Sens arôme", "Sahn ah-rohm", "Riech Duft", "REEKH dooft",
        "Senti profumo", "SEHN-tee proh-FOO-moh", "Sinta cheiro", "SEEN-tah SHAY-roo",
        "Вдохни аромат", "Vdahkh-NEE ah-rah-MAHT", "Kokuyu al", "Koh-koo-yoo ahl",
        "Cium aroma", "Chee-oom ah-roh-mah", "闻 香味", "Wén xiāngwèi",
        "いい匂い 嗅ぐ", "Ii nioi kagu", "냄새 맡아", "Naemsae mata"
    ),
    item(
        "Bite snack", "ایک نوالہ لو", "Aik niwala lo", "एक टुकड़ा खाओ", "Ek tukda khao",
        "تذوق لقمة", "Tadhawwaq luqma", "Muerde bocadillo", "MWEHR-deh boh-kah-DEE-yoh",
        "Mords dedans", "Mohr duh-dahn", "Beiß rein", "BYSS ryne",
        "Mordi boccone", "MOHR-dee bohk-KOH-neh", "Morda lanche", "MOHR-dah LAHN-shee",
        "Укуси кусочек", "Oo-koo-SEE koo-SOH-cheek", "Bir ısırık al", "Beer uh-suh-ruhk ahl",
        "Gigit camilan", "Gee-geet chah-mee-lahn", "咬 一口", "Yǎo yīkǒu",
        "一口 かじる", "Hitokuchi kajiru", "한입 베어물어", "Hannip beeomureo"
    ),
    item(
        "Wipe hands", "ہاتھ صاف کرو", "Haath saaf karo", "हाथ साफ़ करो", "Haath saaf karo",
        "امسح يديك", "Imsah yadayk", "Limpia manos", "LEEM-pyah MAH-nohs",
        "Essuie mains", "Eh-swee man", "Wisch Hände", "VISH HEN-deh",
        "Pulisci mani", "Poo-LEE-shee MAH-nee", "Limpe mãos", "LEEM-pee mowns",
        "Вытри руки", "VY-tree ROO-kee", "Elleri sil", "Ehl-leh-ree seel",
        "Lap tangan", "Lahp tahng-ahn", "擦 手心", "Cā shǒuxīn",
        "手 拭く", "Te fuku", "손 닦아", "Son dakka"
    )
]

# 22. table-booking
w1["table-booking"] = [
    item(
        "Round table", "گول میز", "Gol mez", "गोल मेज़", "Gol mez",
        "طاولة مستديرة", "Tawila mustadira", "Mesa redonda", "MEH-sah reh-DOHN-dah",
        "Table ronde", "Tah-bluh rohnd", "Runder Tisch", "ROON-der tish",
        "Tavolo rotondo", "TAH-voh-loh roh-TOHN-doh", "Mesa redonda", "MEH-zah heh-DOHN-dah",
        "Круглый стол", "KROOG-lyy stohl", "Yuvarlak masa", "Yoo-vahr-lahk mah-sah",
        "Meja bulat", "Meh-jah boo-laht", "圆 餐桌", "Yuán cānzhuō",
        "丸い テーブル", "Marui tēburu", "둥근 식탁", "Dunggeun siktak"
    ),
    item(
        "Soft chair", "آرام دہ کرسی", "Aaram deh kursi", "आरामदेह कुर्सी", "Aaraamdeh kursi",
        "كرسي مريح", "Kursi murih", "Silla cómoda", "SEE-yah KOH-moh-dah",
        "Chaise douce", "Shehz doos", "Bequemer Stuhl", "Beh-KVAY-mer shtool",
        "Sedia comoda", "SEH-dyah KOH-moh-dah", "Cadeira confortável", "Kah-DAY-rah kohn-for-TAH-vehl",
        "Удобный стул", "Oo-DOHB-nyy stool", "Rahat sandalye", "Rah-haht sahn-dahl-yeh",
        "Kursi empuk", "Koor-see ehm-pook", "软 椅子", "Ruǎn yǐzi",
        "座り心地の 良い椅子", "Suwarigokochi no yoiisu", "편한 의자", "Pyeon-han uija"
    ),
    item(
        "Window view", "کھڑکی والی جگہ", "Khirki wali jagah", "खिड़की वाली जगह", "Khidki wali jagah",
        "مكان مطل", "Makan mutill", "Lugar junto ventana", "Loo-GAHR HOON-toh vehn-TAH-nah",
        "Coin fenêtre", "Kwan feh-net-ruh", "Schöner Fensterplatz", "SHER-ner FEN-ster-plahts",
        "Posto finestra", "POHS-toh fee-NEHS-trah", "Lugar na janela", "Loo-GAHR nah zhah-NEH-lah",
        "Место у окна", "MYEHS-tah oo ahk-NAH", "Manzaralı köşe", "Mahn-zah-rah-luh ker-sheh",
        "Pojok jendela", "Poh-johk jehn-deh-lah", "靠 窗位", "Kào chuāngwèi",
        "窓際の 席", "Madogiwa no seki", "창가 자리", "Chang-ga jari"
    )
]

w2["table-booking"] = [
    item(
        "Book table", "میز بُک کرو", "Mez book karo", "मेज़ बुक करो", "Mez book karo",
        "احجز طاولة", "Ihjiz tawila", "Reserva mesa", "Reh-SEHR-vah MEH-sah",
        "Réserve table", "Ray-zehrv tah-bluh", "Reservier Tisch", "Reh-zehr-VEER tish",
        "Prenota tavolo", "Preh-NOH-tah TAH-voh-loh", "Reserve mesa", "Heh-ZEHR-vee MEH-zah",
        "Закажи столик", "Zah-kah-ZHY STOH-leek", "Masa ayırt", "Mah-sah ah-yuht",
        "Pesan meja", "Peh-sahn meh-jah", "订 位子", "Dìng wèizi",
        "席 予約する", "Seki yoyaku-suru", "자리 예약해", "Jari yeyak-hae"
    ),
    item(
        "Sit down", "بیٹھ جاؤ", "Baith jaao", "बैठ जाओ", "Baith jaao",
        "اجلس هنا", "Ijlis huna", "Siéntate ya", "SYEHN-tah-teh yah",
        "Assieds-toi", "Ah-syay twah", "Setz dich", "ZEHTS dikh",
        "Siediti qui", "SYEH-dee-tee kwee", "Sente-se agora", "SEHN-chee-see ah-GAW-rah",
        "Садись сюда", "Sah-DEES syoo-DAH", "Hemen otur", "Heh-men oh-toor",
        "Silakan duduk", "See-lah-kahn doo-dook", "快 坐下", "Kuài zuòxià",
        "椅子に 座る", "Isu ni suwaru", "앉아 어서", "Anja eoseo"
    ),
    item(
        "Check menu", "مینو دیکھو", "Menu dekho", "मेनू देखो", "Menu dekho",
        "انظر قائمة", "Undhur qa'ima", "Mira menú", "MEE-rah meh-NOO",
        "Regarde carte", "Ruh-gahrd kahrt", "Lies Karte", "LEES KAHR-teh",
        "Guarda menù", "GWAHR-dah meh-NOO", "Veja cardápio", "VAY-zhah kar-DAH-pyoo",
        "Смотри меню", "Smah-TREE meh-NYOO", "Menüye bak", "Meh-new-yeh bahk",
        "Lihat menu", "Lee-haht meh-noo", "看 菜单", "Kàn càidān",
        "メニュー 見る", "Menyū miru", "메뉴판 봐", "Menyupan bwa"
    )
]

# 23. feeling-sick
w1["feeling-sick"] = [
    item(
        "Warm forehead", "گرم ماتھا", "Garam maatha", "गर्म माथा", "Garm maatha",
        "جبين دافئ", "Jabin dafi'", "Frente tibia", "FREHN-teh TEE-byah",
        "Front chaud", "Frohn sho", "Warme Stirn", "VAHR-meh SHTEERN",
        "Fronte calda", "FROHN-teh KAHL-dah", "Testa quente", "TEHS-tah KEHN-chee",
        "Тёплый лоб", "TYOHP-lyy lohb", "Ilık alın", "Uh-luhk ah-luhn",
        "Dahi hangat", "Dah-hee hahng-aht", "微 额头发烫", "Wēi étóufātàng",
        "熱っぽい おでこ", "Netsuppoi odeko", "미열있는 이마", "Miyeorinneun ima"
    ),
    item(
        "Soft pillow", "نرم تکیہ", "Naram takiya", "नरम तकिया", "Naram takiya",
        "وسادة مريحة", "Wisada muriha", "Almohada cómoda", "Ahl-moh-AH-dah KOH-moh-dah",
        "Coussin doux", "Koo-san doo", "Weiches Polster", "VY-khes POHL-ster",
        "Cuscino morbido", "Koo-SHEE-noh MOHR-bee-doh", "Travesseiro fofo", "Trah-veh-SAY-roo FAW-foo",
        "Мягкая подушка", "MYAHK-kah-yah pah-DOOSH-kah", "Yumuşak yastık", "Yoo-moo-shahk yahs-tuk",
        "Bantal empuk", "Bahn-tahl ehm-pook", "软 靠枕", "Ruǎn kàozhěn",
        "心地よい 枕", "Kokochiyoi makura", "편안한 베개", "Pyeon-an-han begae"
    ),
    item(
        "Quiet rest", "مکمل آرام", "Mukammal aaraam", "पूरा आराम", "Poora aaraam",
        "راحة هادئة", "Raha hadi'a", "Descanso tranquilo", "Dehs-KAHN-soh trahn-KEE-loh",
        "Repos tranquille", "Ruh-poh trahn-keel", "Ruhige Erholung", "ROO-hee-geh ehr-HOH-loong",
        "Riposo tranquillo", "Ree-POH-zoh trahn-KWEEL-loh", "Repouso calmo", "Heh-POH-zoo KAHL-moo",
        "Тихий покой", "TEE-khiy pah-KOY", "Sakin dinlenme", "Sah-keen deen-lehn-meh",
        "Istirahat tenang", "Ees-tee-rah-haht teh-nahng", "静 休养", "Jìng xiūyǎng",
        "静かな 休養", "Shizukana kyūyō", "조용한 휴식", "Joyong-han hyusik"
    )
]

w2["feeling-sick"] = [
    item(
        "Rest now", "آرام کرو", "Aaraam karo", "आराम करो", "Aaraam karo",
        "استرح الآن", "Istarih al-an", "Descansa ahora", "Dehs-KAHN-sah ah-OH-rah",
        "Repose-toi", "Ruh-pohz twah", "Ruh dich aus", "ROO dikh owss",
        "Riposati ora", "Ree-POH-zah-tee OH-rah", "Descanse agora", "Dehs-KAHN-see ah-GAW-rah",
        "Отдыхай больше", "Aht-dy-KHY BOHL-sheh", "Güzelce dinlen", "Gew-zel-jeh deen-lehn",
        "Istirahatlah dulu", "Ees-tee-rah-haht-lah doo-loo", "多 休息", "Duō xiūxi",
        "ゆっくり 休む", "Yukkuri yasumu", "푹 쉬어", "Puk swieo"
    ),
    item(
        "Sip water", "پانی پیو", "Paani peeyo", "पानी पियो", "Paani piyo",
        "اشرب ماءً", "Ishrab ma'", "Toma agua", "TOH-mah AH-gwah",
        "Bois de l'eau", "Bwah duh loh", "Trink Wasser", "TRINK VAHS-ser",
        "Bevi acqua", "BEH-vee AHK-wah", "Beba água", "BEH-bah AH-gwah",
        "Пей водичку", "Pey vah-DEECH-koo", "Ilık su iç", "Uh-luhk soo eech",
        "Minum air putih", "Mee-noom ah-yeer poo-teeh", "多 喝水", "Duō hēshuǐ",
        "水分 補給する", "Suibun hokyū-suru", "물 자주마셔", "Mul jajumasyeo"
    ),
    item(
        "Tell mom", "امی کو بتاؤ", "Ammi ko batao", "माँ को बताओ", "Maa ko bataao",
        "أخبر أمك", "Akhbir ummak", "Avisa a mamá", "Ah-VEE-sah ah mah-MAH",
        "Préviens maman", "Pray-vyan mah-mahn", "Sag's Mama", "ZAHKS MAH-mah",
        "Dillo a mamma", "DEEL-loh ah MAHM-mah", "Avise mamãe", "Ah-VEE-zee mah-MYE",
        "Скажи маме", "Skah-ZHY MAH-myeh", "Annene söyle", "Ahn-neh-neh seri-leh",
        "Beri tahu ibu", "Beh-ree tah-hoo ee-boo", "告诉 妈妈", "Gàosù māmā",
        "お母さんに 伝える", "Okāsan ni tsutaeru", "엄마께 알려", "Eommakke alryeo"
    )
]

# 24. at-the-clinic
w1["at-the-clinic"] = [
    item(
        "Kind doctor", "مہربان ڈاکٹر", "Meherbaan doctor", "दयालु डॉक्टर", "Dayaalu doctor",
        "طبيب لطيف", "Tabib latif", "Médico amable", "MEH-dee-koh ah-MAH-bleh",
        "Docteur gentil", "Dohk-tuhr zhan-tee", "Lieber Arzt", "LEE-ber ahrtst",
        "Dottore bravo", "Doht-TOH-reh BRAH-voh", "Médico gentil", "MEH-jee-koo zheng-TEEL",
        "Добрый доктор", "DOHB-ryy DOHK-tahr", "İyi doktor", "Ee-yee dohk-tohr",
        "Dokter ramah", "Dohk-tehr rah-mah", "和 医生", "Hé yīshēng",
        "優しい お医者さん", "Yasashii oishasan", "다정한 의사선생님", "Dajeong-han uisaseonsaengnim"
    ),
    item(
        "Clean room", "صاف کمرہ", "Saaf kamra", "साफ़ कमरा", "Saaf kamra",
        "غرفة نظيفة", "Ghurfa nadhifa", "Sala limpia", "SAH-lah LEEM-pyah",
        "Salle propre", "Sahl proh-pruh", "Helles Zimmer", "HEL-les TSIM-mer",
        "Stanza pulita", "STAHN-tsah poo-LEE-tah", "Sala limpa", "SAH-lah LEEM-pah",
        "Чистая палата", "CHEES-tah-yah pah-LAH-tah", "Temiz oda", "Teh-meez oh-dah",
        "Ruang bersih", "Roo-ahng behr-seeh", "净 诊室", "Jìng zhěnshì",
        "清潔な 診察室", "Seiketsuna shinsatsushitsu", "깨끗한 진료실", "Kkaekkeut-han jinryosil"
    ),
    item(
        "Brave smile", "پراعتماد مسکراہٹ", "Pur-aetemad muskurahat", "हिम्मत भरी मुस्कान", "Himmat bhari muskaan",
        "ابتسامة شجاعة", "Ibtisama shuja'a", "Sonrisa valiente", "Sohn-REE-sah vah-LYEHN-teh",
        "Courageux sourire", "Koo-rah-zhuh soo-reer", "Tapferes Lächeln", "TAHP-feh-res LEKH-eln",
        "Sorriso coraggioso", "Sohr-REE-zoh koh-rahd-JOH-zoh", "Sorriso corajoso", "Sohr-HEE-zoo koh-rah-ZHOH-zoo",
        "Смелая улыбка", "SMYEH-lah-yah oo-LYP-kah", "Cesur tebessüm", "Jeh-soor teh-behs-sewm",
        "Senyum berani", "Sehn-yoom beh-rah-nee", "勇 微笑", "Yǒng wēixiào",
        "頼もしい 笑顔", "Tanomoshii egao", "씩씩한 미소", "Ssikssik-han miso"
    )
]

w2["at-the-clinic"] = [
    item(
        "Say ah", "آہ کہو", "Aah kaho", "आह कहो", "Aah kaho",
        "قل آآه", "Qul aah", "Di ah", "DEE ah",
        "Fais ah", "Feh ah", "Sag Aaa", "ZAHK ahh",
        "Dì ah", "DEE ah", "Diga ah", "JEE-gah ah",
        "Скажи ааа", "Skah-ZHY ah-ah-AH", "Aaa de", "Ah-ah-ah deh",
        "Katakan aaa", "Kah-tah-kahn ah-ah-ah", "张 嘴啊", "Zhāng zuǐ'a",
        "「あー」と 口開ける", "Aa to kuchiakeru", "입벌려 아", "Ipbeollyeo a"
    ),
    item(
        "Breathe deep", "گہرا سانس لو", "Gehra saans lo", "गहरी साँस लो", "Gahari saans lo",
        "تنفس بعمق", "Tanaffas bi-'umq", "Respira profundo", "Hehs-PEE-rah proh-FOON-doh",
        "Respire fort", "Rehs-peer fohr", "Atme tief", "AHT-meh teef",
        "Respira a fondo", "Hehs-PEE-rah ah FOHN-doh", "Respire fundo", "Hehs-PEE-ree FOON-doo",
        "Дыши глубоко", "Dy-SHY gloo-bah-KOH", "Derin nefes al", "Deh-reen neh-fehs ahl",
        "Tarik napas panjang", "Tah-reek nah-pahs pahn-jahng", "深 呼吸", "Shēn hūxī",
        "深く 息吸う", "Fukaku ikisuu", "숨 깊게쉬어", "Sum gipgeswieo"
    ),
    item(
        "Be brave", "بہادر بنو", "Bahadur bano", "बहादुर बनो", "Bahaadur bano",
        "كن شجاعاً", "Kun shuja'an", "Sé valiente", "SEH vah-LYEHN-teh",
        "Sois courageux", "Swah koo-rah-zhuh", "Sei tapfer", "ZY tahp-fer",
        "Sii forte", "SEE FOHR-teh", "Seja forte", "SAY-zhah FAWR-chee",
        "Будь смелым", "BOOD SMYEH-lym", "Cesur ol", "Jeh-soor ohl",
        "Jadilah pemberani", "Jah-dee-lah pehm-beh-rah-nee", "做 勇敢孩子", "Zuò yǒnggǎnháizi",
        "強く がんばる", "Tsuyoku ganbaru", "용기 내어봐", "Yonggi naeobwa"
    )
]

# 25. pharmacy-visit
w1["pharmacy-visit"] = [
    item(
        "Sweet syrup", "میٹھا شربت", "Meetha sharbat", "मीठा सिरप", "Meetha syrup",
        "شراب حلو", "Sharab hulw", "Jarabe dulce", "Hah-RAH-beh DOOL-seh",
        "Sirop doux", "See-roh doo", "Süßer Hustensaft", "ZYOO-ser HOOS-ten-zahft",
        "Sciroppo dolce", "Shee-ROHP-poh DOHL-cheh", "Xarope docinho", "Shah-RAW-pee doh-SEEN-yoo",
        "Сладкий сироп", "SLAHT-kiy see-ROHP", "Tatlı şurup", "Taht-luh shoo-roop",
        "Sirup manis", "See-roop mah-nees", "甜 糖浆", "Tián tángjiāng",
        "飲みやすい シロップ", "Nomiyasui shiroppu", "달콤한 시럽", "Dalkom-han sireop"
    ),
    item(
        "Cute bandage", "پیاری پٹی", "Pyaari patti", "प्यारी पट्टी", "Pyaari patti",
        "ضمادة ملونة", "Dimada mulawwana", "Curita bonita", "Koo-REE-tah boh-NEE-tah",
        "Pansement doux", "Pahns-mahn doo", "Buntes Pflaster", "BOON-tes PFLAHS-ter",
        "Cerotto colorato", "Cheh-ROHT-toh koh-loh-RAH-toh", "Curativo bonito", "Koo-rah-CHEE-voo boh-NEE-too",
        "Детский пластырь", "DYEHT-skiy PLAH-styr", "Renkli yara bandı", "Renk-lee yah-rah bahn-duh",
        "Plester lucu", "Pleh-stehr loo-choo", "萌 创口贴", "Méng chuāngkǒutiē",
        "可愛い 絆創膏", "Kawaii bansōkō", "귀여운 밴드", "Gwiyeoun baendeu"
    ),
    item(
        "Green bag", "سبز تھیلی", "Sabz thaili", "हरा थैला", "Hara thaila",
        "حقيبة خضراء", "Haqiba khadra'", "Bolsa verde", "BOHL-sah VEHR-deh",
        "Sachet vert", "Sah-shay vehr", "Kleine Papiertüte", "KLY-neh pah-PEER-too-teh",
        "Busta verde", "BOOS-tah VEHR-deh", "Sacola verde", "Sah-KAW-lah VEHR-jee",
        "Зелёный пакетик", "Zyeh-LYOH-nyy pah-KYEH-teek", "Yeşil torba", "Yeh-sheel tohr-bah",
        "Kantong hijau", "Kahn-tohng hee-jow", "绿 药袋", "Lǜ yàodài",
        "清潔な 薬袋", "Seiketsuna yakutai", "초록 약봉투", "Chorok yakbongtu"
    )
]

w2["pharmacy-visit"] = [
    item(
        "Take medicine", "دوا پیو", "Dawa peeyo", "दवा पीओ", "Dawa piyo",
        "تناول دواء", "Tanawal dawa'", "Toma jarabe", "TOH-mah hah-RAH-beh",
        "Prends remède", "Prahn ruh-mehd", "Nimm Medizin", "NIM meh-dee-TSEEN",
        "Prendi medicina", "PREHN-dee meh-dee-CHEE-nah", "Tome remédio", "TOH-mee heh-MEH-jyoo",
        "Выпей лекарство", "VY-pyey lyeh-KAHRST-vah", "İlacını iç", "Ee-lah-juh-nuh eech",
        "Minum obat", "Mee-noom oh-baht", "按时 吃药", "Ànshí chīyào",
        "お薬 飲む", "Okusuri nomu", "약 잘먹어", "Yak jalmeogeo"
    ),
    item(
        "Put bandage", "پٹی لگاؤ", "Patti lagao", "पट्टी लगाओ", "Patti lagaao",
        "ضع ضمادة", "Da' dimada", "Pon curita", "POHN koo-REE-tah",
        "Mets pansement", "Meh pahns-mahn", "Kleb Pflaster", "KLAYP PFLAHS-ter",
        "Metti cerotto", "MEHT-tee cheh-ROHT-toh", "Ponha curativo", "POHN-yah koo-rah-CHEE-voo",
        "Наклей пластырь", "Nah-KLEY PLAH-styr", "Bandaj yapıştır", "Bahn-dahzh yah-puhsh-tuhr",
        "Pasang plester", "Pah-sahng pleh-stehr", "贴 创口贴", "Tiē chuāngkǒutiē",
        "絆創膏 貼る", "Bansōkō haru", "반창고 붙여", "Banchanggo buchyeo"
    ),
    item(
        "Feel better", "صحت یاب ہو جاؤ", "Sehat yaab ho jaao", "जल्दी ठीक हो", "Jaldi theek ho",
        "تعاف سريعاً", "Ta'afa sari'an", "Mejora pronto", "Meh-HOH-rah PROHN-toh",
        "Guéris vite", "Gay-ree veet", "Werd gesund", "VEHRT geh-ZOONT",
        "Guarisci presto", "Gwah-REE-shee PREHS-toh", "Melhore logo", "Mehl-YAW-ree LOH-goo",
        "Поправляйся скорее", "Pah-prahv-LYAY-syah skah-RYEY", "Geçmiş olsun", "Gech-meesh ohl-soon",
        "Lekas sembuh", "Leh-kahs sehm-booh", "快点 好起来", "Kuàidiǎn hǎoqǐlái",
        "早く 元気になる", "Hayaku genkini-naru", "얼른 나아", "Eolleun naa"
    )
]

# 26. describing-pain
w1["describing-pain"] = [
    item(
        "Sore tummy", "پیٹ کا درد", "Pait ka dard", "पेट का दर्द", "Pet ka dard",
        "بطن مؤلم", "Batn mu'lim", "Pancita adolorida", "Pahn-SEE-tah ah-doh-loh-REE-dah",
        "Ventre douloureux", "Vahnt-ruh doo-loo-ruh", "Bauchweh spürbar", "BOWKH-vay shpoor-bahr",
        "Pancino dolente", "Pahn-CHEE-noh doh-LEHN-teh", "Barriguinha dolorida", "Bah-hee-GEEN-yah doh-loh-REE-dah",
        "Больной животик", "Bahl-NOY zhy-VOH-teek", "Ağrıyan karın", "Ah-ruh-yahn kah-ruhn",
        "Perut sakit", "Peh-root sah-keet", "肚 隐隐痛", "Dù yǐnyǐntòng",
        "痛い お腹", "Itai onaka", "아픈 배", "Apeun bae"
    ),
    item(
        "Warm compress", "گرم ٹکور", "Garam takore", "गर्म सिंकाई", "Garm sinkaai",
        "كمادة دافئة", "Kammada dafi'a", "Compresa tibia", "Kohm-PREH-sah TEE-byah",
        "Compresse tiède", "Kohn-prehs tyehd", "Warme Kompresse", "VAHR-meh kohm-PRES-seh",
        "Impacco tiepido", "Eem-PAHK-koh TYEH-pee-doh", "Compressa morna", "Kohm-PREH-sah MOHR-nah",
        "Тёплый компресс", "TYOHP-lyy kahm-PRYEHS", "Ilık bez", "Uh-luhk bez",
        "Kompres hangat", "Kohm-prehs hahng-aht", "温 热敷包", "Wēn rèfūbāo",
        "温かい タオル", "Atatakai taoru", "따뜻한 찜질", "Ttatteut-han jjimjil"
    ),
    item(
        "Gentle touch", "پیارا لمس", "Pyaara lams", "प्यारा स्पर्श", "Pyaara sparsh",
        "لمسة لطيفة", "Lamsa latifa", "Caricia suave", "Kah-REE-syah SWAH-veh",
        "Touche douce", "Toosh doos", "Sanfte Berührung", "ZAHN-fteh beh-ROO-roong",
        "Tocco leggero", "TOHK-koh lehd-JEH-roh", "Toque suave", "TOH-kee SWAH-vee",
        "Нежное прикосновение", "NYEZH-nah-yeh pree-kahs-nah-VYEH-nyee-yeh", "Yumuşak dokunuş", "Yoo-moo-shahk doh-koo-noosh",
        "Sentuhan lembut", "Sehn-too-hahn lehm-boot", "柔 安抚", "Róu ānfǔ",
        "優しい なでなで", "Yasashii nadenade", "다정한 손길", "Dajeong-han songgil"
    )
]

w2["describing-pain"] = [
    item(
        "Point spot", "جگہ دکھاؤ", "Jagah dikhao", "जगह दिखाओ", "Jagah dikhaao",
        "أشر للألم", "Ashir lil-alam", "Señala dónde", "Seh-NYAH-lah DOHN-deh",
        "Montre endroit", "Mohn-truh ahn-drwah", "Zeig Stelle", "TSYGH SHTEL-leh",
        "Mostra dove", "MOHS-trah DOH-veh", "Mostre onde", "MOHS-tree OHN-jee",
        "Покажи пальцем", "Pah-kah-ZHY PAHL-tseem", "Ağrıyan yeri göster", "Ah-ruh-yahn yeh-ree gerz-tehr",
        "Tunjukkan letaknya", "Toon-jook-kahn leh-tahk-nyah", "指 痛处", "Zhǐ tòngchù",
        "痛い所 指差す", "Itaitokoro yubisasu", "아픈곳 가리켜", "Apeungot garikyeo"
    ),
    item(
        "Hold soft", "آہستہ سے پکڑو", "Aahista se pakro", "हल्के से पकड़ो", "Halke se pakdo",
        "امسك برفق", "Imsik bi-rifq", "Toca despacio", "TOH-kah dehs-PAH-syoh",
        "Touche doucement", "Toosh doos-mahn", "Fass sanft an", "FAHS zahnft ahn",
        "Tocca piano", "TOHK-kah PYAH-noh", "Segure devagar", "Seh-GOO-ree deh-vah-GAHR",
        "Держи аккуратно", "Dyehr-ZHY ahk-koo-RAHT-nah", "Yavaşça dokun", "Yah-vahsh-chah doh-koon",
        "Pegang perlahan", "Peh-gahng pehr-lah-hahn", "轻 摸摸", "Qīng mōmō",
        "そっと 触れる", "Sotto fureru", "살며시 만져", "Salmyeosi manjyeo"
    ),
    item(
        "Breathe slow", "آرام سے سانس لو", "Aaraam se saans lo", "धीरे साँस लो", "Dheere saans lo",
        "تنفس ببطء", "Tanaffas bi-but'", "Respira suave", "Hehs-PEE-rah SWAH-veh",
        "Respire calmement", "Rehs-peer kahlm-mahn", "Atme ruhig", "AHT-meh ROO-hikh",
        "Respira lentamente", "Hehs-PEE-rah lehn-tah-MEHN-teh", "Respire calmo", "Hehs-PEE-ree KAHL-moo",
        "Дыши ровно", "Dy-SHY ROHV-nah", "Yavaş nefes al", "Yah-vahsh neh-fehs ahl",
        "Bernapas perlahan", "Behr-nah-pahs pehr-lah-hahn", "慢 呼吸", "Màn hūxī",
        "ゆっくり 呼吸する", "Yukkuri kokyū-suru", "천천히 숨쉬어", "Cheoncheonhi sumswieo"
    )
]

# 27. comforting-family
w1["comforting-family"] = [
    item(
        "Sweet hug", "پیاری جپھی", "Pyaari jhappi", "प्यारी झप्पी", "Pyaari jhappi",
        "عناق دافئ", "'Inaq dafi'", "Abrazo cálido", "Ah-BRAH-zoh KAH-lee-doh",
        "Câlin tendre", "Kah-lan tahnd-ruh", "Liebe Umarmung", "LEE-beh oom-AHR-moong",
        "Abbraccio affettuoso", "Ahb-BRAHT-choh ahf-feht-TWOH-zoh", "Abraço gostoso", "Ah-BRAH-soo gohs-TOH-zoo",
        "Тёплое объятие", "TYOHP-lah-yeh ahb-YAH-tyeh", "Sıcacık sarılma", "Suh-jah-juhk sah-ruhl-mah",
        "Pelukan tulus", "Peh-look-ahn too-loos", "暖 抱抱", "Nuǎn bàobào",
        "ぎゅっと 抱きしめる", "Gyutto dakishimeru", "따뜻한 안아주기", "Ttatteut-han anajugi"
    ),
    item(
        "Kind words", "تسلی بخش باتیں", "Tasalli bakhsh baatein", "मीठे बोल", "Meethe bol",
        "كلمات طيبة", "Kalimat tayyiba", "Palabras lindas", "Pah-LAH-brahs LEEN-dahs",
        "Mots gentils", "Moh zhan-tee", "Tröstende Worte", "TRER-sten-deh VOR-teh",
        "Parole dolci", "Pah-ROH-leh DOHL-chee", "Palavras doces", "Pah-LAH-vrahs DOH-sees",
        "Добрые слова", "DOHB-ry-yeh slah-VAH", "Güzel sözler", "Gew-zel serz-lehr",
        "Kata penghibur", "Kah-tah pehng-hee-boor", "暖 心话", "Nuǎn xīnhuà",
        "優しい 言葉", "Yasashii kotoba", "따뜻한 위로", "Ttatteut-han wiro"
    ),
    item(
        "Happy smile", "کھلتی مسکراہٹ", "Khilti muskurahat", "खिलती मुस्कान", "Khilti muskaan",
        "بسمة مشرقة", "Basma mushriqa", "Sonrisa alegre", "Sohn-REE-sah ah-LEH-greh",
        "Sourire radieux", "Soo-reer rah-dyuh", "Fröhliches Gesicht", "FRER-likh-es geh-ZIKHT",
        "Sorriso radioso", "Sohr-REE-zoh rah-DYOH-zoh", "Sorriso radiante", "Sohr-HEE-zoo hah-DYAHN-chee",
        "Светлая улыбка", "SVYEHT-lah-yah oo-LYP-kah", "Parlak tebessüm", "Pahr-lahk teh-behs-sewm",
        "Senyum bahagia", "Sehn-yoom bah-hah-gee-ah", "喜 笑容", "Xǐ xiàoróng",
        "晴れやかな 笑顔", "Hareyakana egao", "환한 미소", "Hwan-han miso"
    )
]

w2["comforting-family"] = [
    item(
        "Give hug", "گلے لگاؤ", "Galay lagao", "गले लगाओ", "Gale lagaao",
        "عانق بحب", "'Aniq bi-hubb", "Dale un abrazo", "DAH-leh oon ah-BRAH-zoh",
        "Fais câlin", "Feh kah-lan", "Drück fest", "DROOK fehst",
        "Dai abbraccio", "DYE ahb-BRAHT-choh", "Dê abraço", "DAY ah-BRAH-soo",
        "Обними крепко", "Ahb-nee-MEE KRYEHP-kah", "Sıkıca sarıl", "Suh-kuh-jah sah-ruhl",
        "Beri pelukan", "Beh-ree peh-look-ahn", "送 拥抱", "Sòng yǒngbào",
        "ハグを する", "Hagu o suru", "꼭 안아줘", "Kkok anajwo"
    ),
    item(
        "Wipe tear", "آنسو پونچھو", "Aansoo pooncho", "आँसू पोंछो", "Aansoo poncho",
        "امسح دمعة", "Imsah dam'a", "Seca lágrimas", "SEH-kah LAH-gree-mahs",
        "Essuie larmes", "Eh-swee lahrm", "Trockne Tränen", "TROK-neh TRAY-nen",
        "Asciuga lacrime", "Ah-SHOO-gah LAH-kree-meh", "Enxugue lágrimas", "Eng-SHOO-gee LAH-gree-mahs",
        "Вытри слёзы", "VY-tree SLYOH-zy", "Gözyaşını sil", "Gerz-yah-shuh-nuh seel",
        "Usap air mata", "Oo-sahp ah-yeer mah-tah", "擦 眼泪", "Cā yǎnlèi",
        "涙 拭く", "Namida fuku", "눈물 닦아줘", "Nunmul dakkajwo"
    ),
    item(
        "Hold hand", "ہاتھ تھامو", "Haath thaamo", "हाथ थामो", "Haath thaamo",
        "أمسك اليد", "Amsik al-yad", "Toma mano", "TOH-mah MAH-noh",
        "Prends main", "Prahn man", "Halt Hand", "HAHLT hahnt",
        "Stringi mano", "STREEN-jee MAH-noh", "Segure mão", "Seh-GOO-ree mown",
        "Возьми за руку", "Vahz-MEE zah ROO-koo", "Elinden tut", "Eh-leen-dehn toot",
        "Genggam tangan", "Gehng-gahm tahng-ahn", "握 手心", "Wò shǒuxīn",
        "手 握りしめる", "Te nigirishimeru", "손 잡아줘", "Son jabajwo"
    )
]

# 28. greeting-teachers
w1["greeting-teachers"] = [
    item(
        "Polite bow", "ادب سے جھکاؤ", "Adab se jhukao", "आदर से नमन", "Aadar se naman",
        "تحية مؤدبة", "Tahiyya mu'addaba", "Saludo respetuoso", "Sah-LOO-doh rehs-peh-TWOH-soh",
        "Salut poli", "Sah-loo poh-lee", "Höfliche Verbeugung", "HERF-likh-eh fehr-BOY-goong",
        "Saluto cortese", "Sah-LOO-toh kohr-TEH-zeh", "Cumprimento educado", "Koom-pree-MEHN-too eh-doo-KAH-doo",
        "Вежливый поклон", "VYEHZH-lee-vyy pahk-LOHN", "Kibar selam", "Kee-bahr seh-lahm",
        "Salam hormat", "Sah-lahm hohr-maht", "礼 问候", "Lǐ wènhòu",
        "丁寧な 挨拶", "Teineina aisatsu", "공손한 인사", "Gongson-han insa"
    ),
    item(
        "Clear voice", "صاف آواز", "Saaf aawaaz", "साफ़ आवाज़", "Saaf aawaaz",
        "صوت واضح", "Sawt wadih", "Voz clara", "VOHS KLAH-rah",
        "Voix claire", "Vwah klehr", "Klare Stimme", "KLAH-reh SHTIM-meh",
        "Voce chiara", "VOH-cheh KYAH-rah", "Voz audível", "VAWZ ow-JEE-vehl",
        "Чёткий голос", "CHOHT-kiy GOH-lahs", "Açık ses", "Ah-chuhk sehs",
        "Suara jelas", "Swah-rah jeh-lahs", "响 声音", "Xiǎng shēngyīn",
        "はっきりした 声", "Hakirishita koe", "또렷한 목소리", "Ttoryeot-han moksori"
    ),
    item(
        "Bright eyes", "چمکتی آنکھیں", "Chamakti aankhein", "चमकती आँखें", "Chamakti aankhein",
        "عيون مشرقة", "'Uyun mushriqa", "Ojos atentos", "OH-hohs ah-TEHN-tohs",
        "Regard attentif", "Ruh-gahr ah-tahn-teef", "Wache Augen", "VAH-kheh OW-gen",
        "Sguardo attento", "ZGWAHR-doh aht-TEHN-toh", "Olhar atento", "Ohl-YAHR ah-TEHN-too",
        "Внимательный взгляд", "Vnee-MAH-tyel-nyy vzglyaht", "Işıl ışıl gözler", "Uh-shuhl uh-shuhl gerz-lehr",
        "Mata bersinar", "Mah-tah behr-see-nahr", "亮 眼神", "Liàng yǎnshén",
        "生き生きした 瞳", "Ikiikishita hitomi", "초롱초롱한 눈빛", "Chorongchorong-han nunbit"
    )
]

w2["greeting-teachers"] = [
    item(
        "Say hello", "سلام کہو", "Salaam kaho", "नमस्ते कहो", "Namaste kaho",
        "قل مرحباً", "Qul marhaban", "Di hola", "DEE OH-lah",
        "Dis bonjour", "Dee bohn-zhoor", "Sag Hallo", "ZAHK hah-LOH",
        "Dì buongiorno", "DEE bwohn-JOHR-noh", "Diga olá", "JEE-gah oh-LAH",
        "Поздоровайся вежливо", "Pahz-dah-ROH-vyey-syah VYEHZH-lee-vah", "Hocana selam ver", "Hoh-jah-nah seh-lahm vehr",
        "Ucapkan salam", "Oo-chahp-kahn sah-lahm", "说 老师好", "Shuō lǎoshīhǎo",
        "先生に 挨拶する", "Sensei ni aisatsu-suru", "선생님께 인사해", "Seonsaengnimkke insahae"
    ),
    item(
        "Bow nice", "جھک کر سلام", "Jhuk kar salaam", "झुककर प्रणाम", "Jhukkar pranaam",
        "انحن باحترام", "Inhani bi-htiram", "Haz reverencia", "AHS reh-veh-REHN-syah",
        "Incline-toi bien", "An-kleen twah byan", "Verbeug dich", "Fehr-BOYKH dikh",
        "Fai inchino", "FYE een-KEE-noh", "Curve respeitoso", "KOOR-vee hehs-pay-TOH-zoo",
        "Поклонись уважительно", "Pahk-lah-NEES oo-vah-ZHEE-tyel-nah", "Saygıyla eğil", "Sigh-guhy-lah eh-yeel",
        "Membungkuk hormat", "Mehm-boong-kook hohr-maht", "鞠躬 行礼", "Jūgōng xínglǐ",
        "お辞儀を する", "Ojigi o suru", "고개숙여 인사", "Gogaesugyeo insa"
    ),
    item(
        "Listen well", "غور سے سنو", "Ghor se suno", "ध्यान से सुनो", "Dhyaan se suno",
        "استمع بتركيز", "Istami' bi-tarkiz", "Escucha atento", "Ehs-KOO-chah ah-TEHN-toh",
        "Écoute attentivement", "Ay-koot ah-tahn-teev-mahn", "Hör aufmerksam", "HER owf-merk-zahm",
        "Ascolta attento", "Ahs-KOHL-tah aht-TEHN-toh", "Ouça atento", "OH-sah ah-TEHN-too",
        "Внимательно слушай", "Vnee-MAH-tyel-nah SLOO-shy", "Dikkatle dinle", "Deek-kaht-leh deen-leh",
        "Simak baik-baik", "See-mahk by-eek by-eek", "专心 听讲", "Zhuānxīn tīngjiǎng",
        "話を 聞く", "Hanashi o kiku", "귀기울여 들어", "Gwigieulryeo deureo"
    )
]

# 29. homework-help
w1["homework-help"] = [
    item(
        "Sharp pencil", "تیز پنسل", "Tez pencil", "तेज़ पेंसिल", "Tez pencil",
        "قلم مبري", "Qalam mabriy", "Lápiz afilado", "LAH-pees ah-fee-LAH-doh",
        "Crayon taillé", "Kreh-yohn tie-yay", "Spitzer Bleistift", "SHPIT-ser BLY-shtift",
        "Matita appuntita", "Mah-TEE-tah ahp-poon-TEE-tah", "Lápis apontado", "LAH-pees ah-pohn-TAH-doo",
        "Острый карандаш", "OHS-tryy kah-rahn-DAHSH", "Sivri kurşunkalem", "Seev-ree koor-shoon-kah-lem",
        "Pensil runcing", "Pehn-seel roon-cheeng", "利 铅笔", "Lì qiānbǐ",
        "削った 鉛筆", "Kezutta enpitsu", "잘깎인 연필", "Jalkkakkin yeonpil"
    ),
    item(
        "Clean book", "صاف کتاب", "Saaf kitab", "साफ़ किताब", "Saaf kitab",
        "دفتر نظيف", "Daftar nadhif", "Cuaderno limpio", "Kwah-DEHR-noh LEEM-pyoh",
        "Cahier propre", "Kah-yay proh-pruh", "Ordentliches Heft", "OHR-dent-likh-es heft",
        "Quaderno ordinato", "Kwah-DEHR-noh ohr-dee-NAH-toh", "Caderno caprichado", "Kah-DEHR-noo kah-pree-SHAH-doo",
        "Аккуратная тетрадь", "Ahk-koo-RAHT-nah-yah tyeh-TRAHT", "Temiz defter", "Teh-meez def-tehr",
        "Buku rapi", "Boo-koo rah-pee", "整 作业本", "Zhěng zuòyèběn",
        "きれいな ノート", "Kireina nōto", "깔끔한 공책", "Kkalkkeum-han gongchaek"
    ),
    item(
        "Big question", "اہم سوال", "Ahem sawaal", "बड़ा सवाल", "Bada sawaal",
        "سؤال مهم", "Su'al muhimm", "Duda pendiente", "DOO-dah pehn-DYEHN-teh",
        "Grande question", "Grahnd kehs-tyohn", "Wichtige Frage", "VIKH-tee-geh FRAH-geh",
        "Domanda importante", "Doh-MAHN-dah eem-pohr-TAHN-teh", "Dúvida importante", "DOO-vee-dah eem-pohr-TAHN-chee",
        "Интересный вопрос", "Een-tyeh-RYEHS-nyy vahp-ROHS", "Önemli soru", "Er-nehm-lee soh-roo",
        "Pertanyaan penting", "Pehr-tahn-yah-ahn pehn-teeng", "难 思考题", "Nán sīkǎotí",
        "大切な 質問", "Taisetsuna shitsumon", "중요한 질문", "Jung-yohan jilmun"
    )
]

w2["homework-help"] = [
    item(
        "Write neat", "صاف لکھو", "Saaf likho", "साफ़ लिखो", "Saaf likho",
        "اكتب بوضوح", "Uktub bi-wuduh", "Escribe claro", "Ehs-KREE-beh KLAH-roh",
        "Écris bien", "Ay-kree byan", "Schreib ordentlich", "SHRYP OHR-dent-likh",
        "Scrivi bene", "SKREE-vee BEH-neh", "Escreva caprichado", "Ehs-KRAY-vah kah-pree-SHAH-doo",
        "Пиши аккуратно", "Pee-SHY ahk-koo-RAHT-nah", "Güzelce yaz", "Gew-zel-jeh yahz",
        "Tulis rapi", "Too-lees rah-pee", "字 写好", "Zì xiěhǎo",
        "綺麗に 書く", "Kireini kaku", "예쁘게 적어", "Yeppeuge jeogeo"
    ),
    item(
        "Ask help", "مدد لو", "Madad lo", "मदद लो", "Madad lo",
        "اطلب عوناً", "Itlub 'awnan", "Pide apoyo", "PEE-deh ah-POH-yoh",
        "Demande explication", "Duh-mahnd ehks-plee-kah-syohn", "Frag nach", "FRAHK nahkh",
        "Chiedi consiglio", "KYEH-dee kohn-SEE-lyoh", "Peça ajuda", "PEH-sah ah-ZHOO-dah",
        "Спроси совета", "Sprah-SEE sah-VYEH-tah", "Yardım sor", "Yahr-duhm sohr",
        "Tanya bantuan", "Tahn-yah bahn-too-ahn", "请教 老师", "Qǐngjiào lǎoshī",
        "先生に 聞く", "Sensei ni kiku", "선생님께 물어", "Seonsaengnimkke mureo"
    ),
    item(
        "Check sum", "حساب چیک کرو", "Hisaab check karo", "उत्तर जाँँचो", "Uttar jaancho",
        "راجع الحساب", "Raji' al-hisab", "Revisa cuenta", "Reh-VEE-sah KWEHN-tah",
        "Vérifie calcul", "Vay-ree-fee kahl-kool", "Prüf Rechnung", "PROOF REKH-noong",
        "Controlla calcolo", "Kohn-TROHL-lah KAHL-koh-loh", "Confira conta", "Kohn-FEE-rah KOHN-tah",
        "Проверь решение", "Prah-VYEHR ryeh-SHEH-nyee-yeh", "Sonucu denetle", "Soh-noo-joo deh-net-leh",
        "Periksa hitungan", "Peh-reek-sah hee-toong-ahn", "核对 答案", "Héduì dá'àn",
        "計算 見直す", "Keisan minaosu", "정답 검토해", "Jeongdap geomtohae"
    )
]

# 30. classroom-chat
w1["classroom-chat"] = [
    item(
        "Big desk", "بڑی میز", "Bari mez", "बड़ी मेज़", "Badi mez",
        "طاولة واسعة", "Tawila wasi'a", "Pupitre espacioso", "Poo-PEE-treh ehs-pah-SYOH-soh",
        "Grand pupitre", "Grahn poo-peet-ruh", "Breiter Schultisch", "BRY-ter SHOOL-tish",
        "Banco grande", "BAHN-koh GRAHN-deh", "Carteira espaçosa", "Kahr-TAY-rah ehs-pah-SAW-zah",
        "Удобная парта", "Oo-DOHB-nah-yah PAHR-tah", "Geniş sıra", "Geh-neesh suh-rah",
        "Meja belajar", "Meh-jah beh-lah-jahr", "宽 课桌", "Kuān kèzhuō",
        "広い 机", "Hiroi tsukue", "넓은 책상", "Neolbeun chaeksang"
    ),
    item(
        "Green board", "سبز بورڈ", "Sabz board", "हरा बोर्ड", "Hara board",
        "سبورة خضراء", "Sabbura khadra'", "Pizarra verde", "Pee-SAH-rrah VEHR-deh",
        "Tableau vert", "Tah-bloh vehr", "Grüne Tafel", "GREW-neh TAH-fel",
        "Lavagna verde", "Lah-VAH-nyah VEHR-deh", "Quadro verde", "KWAH-droo VEHR-jee",
        "Зелёная доска", "Zyeh-LYOH-nah-yah dahs-KAH", "Yeşil tahta", "Yeh-sheel tahk-tah",
        "Papan hijau", "Pah-pahn hee-jow", "黑 黑板", "Hēi hēibǎn",
        "大きな 黒板", "Ōkina kokuban", "초록 칠판", "Chorok chilpan"
    ),
    item(
        "Sunny room", "روشن کلاس", "Roshan class", "उजला कमरा", "Ujla kamra",
        "فصل مشرق", "Fasl mushriq", "Aula luminosa", "OW-lah loo-mee-NOH-sah",
        "Classe éclairée", "Klahs ay-kleh-ray", "Helles Klassenzimmer", "HEL-les KLAH-sen-tsim-mer",
        "Aula luminosa", "OW-lah loo-mee-NOH-zah", "Sala arejada", "SAH-lah ah-reh-ZHAH-dah",
        "Светлый класс", "SVYEHT-lyy klahs", "Ferah sınıf", "Feh-rah suh-nuhf",
        "Kelas terang", "Keh-lahs teh-rahng", "明 教室", "Míng jiàoshì",
        "明るい 教室", "Akarui kyōshitsu", "밝은 교실", "Balgeun gyosil"
    )
]

w2["classroom-chat"] = [
    item(
        "Raise hand", "ہاتھ اٹھاؤ", "Haath uthao", "हाथ उठाओ", "Haath uthaao",
        "ارفع يدك", "Irfa' yadak", "Levanta mano", "Leh-VAHN-tah MAH-noh",
        "Lève main", "Lehv man", "Meld dich", "MELT dikh",
        "Alza mano", "AHL-tsah MAH-noh", "Levante mão", "Leh-VAHN-chee mown",
        "Подними руку", "Pahd-nee-MEE ROO-koo", "Parmak kaldır", "Pahr-mahk kahl-duhr",
        "Angkat tangan", "Ahng-kaht tahng-ahn", "先 举手", "Xiān jǔshǒu",
        "手 挙げる", "Te ageru", "손 들어", "Son deureo"
    ),
    item(
        "Share pencil", "پنسل شیئر کرو", "Pencil share karo", "पेंसिल बाँटो", "Pencil baanto",
        "شارك القلم", "Sharik al-qalam", "Presta lápiz", "PREHS-tah LAH-pees",
        "Prête crayon", "Preht kreh-yohn", "Leih Stift", "LYE shtift",
        "Presta matita", "PREHS-tah mah-TEE-tah", "Empreste lápiz", "Ehm-PREHS-chee LAH-pees",
        "Одолжи карандаш", "Ah-dahl-ZHY kah-rahn-DAHSH", "Kalemini paylaş", "Kah-leh-mee-nee pie-lahsh",
        "Pinjamkan pensil", "Peen-jahm-kahn pehn-seel", "借 铅笔", "Jiè qiānbǐ",
        "鉛筆 貸す", "Enpitsu kasu", "연필 빌려줘", "Yeonpil billyeojwo"
    ),
    item(
        "Open bag", "بستہ کھولو", "Basta kholo", "बस्ता खोलो", "Basta kholo",
        "افتح حقيبتك", "Iftah haqibatak", "Abre mochila", "AH-breh moh-CHEE-lah",
        "Ouvre cartable", "Oo-vruh kahr-tahbl", "Öffne Ranzen", "ERF-neh RAHN-tsen",
        "Apri zaino", "AH-pree DZY-noh", "Abra mochila", "AH-brah moh-SHEE-lah",
        "Открой портфель", "Aht-KROY pahrt-FYEHL", "Çantayı aç", "Chahn-tah-yuh ahch",
        "Buka tas", "Boo-kah tahs", "打 书包", "Dǎ shūbāo",
        "ランドセル 開ける", "Randoseru akeru", "책가방 열어", "Chaekgabang yeoreo"
    )
]

# 31. playground-bell
w1["playground-bell"] = [
    item(
        "Loud bell", "تیز گھنٹی", "Tez ghanti", "तेज़ घंटी", "Tez ghanti",
        "جرس عال", "Jaras 'alin", "Timbre alegre", "TEEM-breh ah-LEH-greh",
        "Cloche sonore", "Klohsh soh-nohr", "Laute Klingel", "LOW-teh KLING-el",
        "Campanella squillante", "Kahm-pah-NEHL-lah skweel-LAHN-teh", "Sino alto", "SEE-noo AHL-too",
        "Громкий звонок", "GROHM-kiy zvah-NOHK", "Gür zil", "Gewr zeel",
        "Bel nyaring", "Behl nyah-reeng", "响 铃声", "Xiǎng língshēng",
        "響く チャイム", "Hibiku chaimu", "우렁찬 종소리", "Ureongchan jongsori"
    ),
    item(
        "Sunny yard", "کھلا میدان", "Khula maidan", "धूप भरा मैदान", "Dhoop bhara maidaan",
        "ساحة مشمسة", "Saha mushmisa", "Patio soleado", "PAH-tyoh soh-leh-AH-doh",
        "Cour ensoleillée", "Koor ahn-soh-lay-yay", "Sonniger Schulhof", "ZON-nee-ger SHOOL-hohf",
        "Cortile soleggiato", "Kohr-TEE-leh soh-lehd-JAH-toh", "Pátio ensolarado", "PAH-tyoo eng-soh-lah-RAH-doo",
        "Солнечный двор", "SOHL-neech-nyy dvohr", "Güneşli bahçe", "Gew-nesh-lee bahh-cheh",
        "Halaman cerah", "Hah-lah-mahn cheh-rah", "亮 操场", "Liàng cāochǎng",
        "陽当たりの 良い校庭", "Hiatari no yoi kōtei", "햇살가득 운동장", "Haetsalgadeuk undongjang"
    ),
    item(
        "Fun game", "مزیدار کھیل", "Mazedar khel", "मज़ेदार खेल", "Mazedaar khel",
        "لعبة ممتعة", "Lu'ba mumti'a", "Juego divertido", "HWEH-goh dee-vehr-TEE-doh",
        "Jeu joyeux", "Zhuh zhwah-yuh", "Lustiges Fangspiel", "LOOS-tee-ges FAHNG-shpeel",
        "Gioco divertente", "JOH-koh dee-vehr-TEHN-teh", "Brincadeira divertida", "Breen-kah-DAY-rah jee-vehr-CHEE-dah",
        "Весёлая игра", "Vyeh-SYOH-lah-yah eeg-RAH", "Eğlenceli oyun", "Eh-lehn-jeh-lee oh-yoon",
        "Permainan seru", "Pehr-mye-nahn seh-roo", "趣 游戏", "Qù yóuxì",
        "楽しい 遊び", "Tanoshii asobi", "신나는 놀이", "Sinnaneun nori"
    )
]

w2["playground-bell"] = [
    item(
        "Run fast", "تیز دوڑو", "Tez doro", "तेज़ दौड़ो", "Tez daudo",
        "اركض سريعاً", "Irkud sari'an", "Corre rápido", "KOHR-reh RAH-pee-doh",
        "Cours vite", "Koor veet", "Lauf schnell", "LOWF shnel",
        "Corri veloce", "KOHR-ree veh-LOH-cheh", "Corra depressa", "KOH-hah jee-PREH-sah",
        "Беги быстрее", "Byeh-GEE bys-TRYEY", "Hızlı koş", "Huhz-luh kohsh",
        "Lari cepat", "Lah-ree cheh-paht", "快 跑步", "Kuài pǎobù",
        "速く 走る", "Hayaku hashiru", "빨리 뛰어", "Ppalli ttwieo"
    ),
    item(
        "Line up", "قطار بناؤ", "Qataar banao", "लाइन लगाओ", "Line lagaao",
        "اصطف بنظام", "Istaff bi-nitham", "Forma fila", "FOHR-mah FEE-lah",
        "Fais la queue", "Feh lah kuh", "Stell an", "SHTEL ahn",
        "Fai fila", "FYE FEE-lah", "Faça fila", "FAH-sah FEE-lah",
        "Становись в ряд", "Stah-nah-VEES v ryaht", "Sıraya geç", "Suh-rah-yah gech",
        "Berbaris rapi", "Behr-bah-rees rah-pee", "整齐 排队", "Zhěngqí páiduì",
        "きちんと 並ぶ", "Kichinto narabu", "줄을 서", "Jureul seo"
    ),
    item(
        "Drink juice", "جوس پیو", "Juice peeyo", "जूस पियो", "Juice piyo",
        "اشرب عصيراً", "Ishrab 'asiran", "Toma jugo", "TOH-mah HOO-goh",
        "Bois jus", "Bwah zhoo", "Trink Saft", "TRINK zahft",
        "Bevi succo", "BEH-vee SOOK-koh", "Beba suco", "BEH-bah SOO-koo",
        "Пей сок", "Pey sohk", "Meyvesuyu iç", "Mey-veh-soo-yoo eech",
        "Minum jus", "Mee-noom joos", "喝 果汁", "Hē guǒzhī",
        "ジュース 飲む", "Jūsu nomu", "주스 마셔", "Juseu masyeo"
    )
]

# 32. group-projects
w1["group-projects"] = [
    item(
        "Team work", "مل جل کر کام", "Mil jul kar kaam", "मिलकर काम", "Milkar kaam",
        "عمل جماعي", "'Amal jama'iy", "Trabajo en equipo", "Trah-BAH-hoh ehn eh-KEE-poh",
        "Travail d'équipe", "Trah-vie day-keep", "Gemeinsame Arbeit", "Geh-MYN-zah-meh AHR-byte",
        "Lavoro di squadra", "Lah-VOH-roh dee SKWAH-drah", "Trabalho em grupo", "Trah-BAHL-yoo eng GROO-poo",
        "Дружная команда", "DROOZH-nah-yah kah-MAHN-dah", "Birlikte çalışma", "Beer-leek-teh chah-luhsh-mah",
        "Kerja kelompok", "Kehr-jah keh-lohm-pohk", "合 团队", "Hé tuánduì",
        "みんなの 協力", "Minna no kyōryoku", "멋진 협동", "Meotjin hyeopdong"
    ),
    item(
        "Color pens", "رنگین قلم", "Rangeen qalam", "रंगीन कलम", "Rangeen kalam",
        "أقلام ملونة", "Aqlam mulawwana", "Plumones vivos", "Ploo-MOH-nehs VEE-vohs",
        "Feutres vifs", "Fuh-truh veef", "Bunte Filzstifte", "BOON-teh FILTS-shtif-teh",
        "Pennarelli colorati", "Pen-nah-REHL-lee koh-loh-RAH-tee", "Canetinhas coloridas", "Kah-neh-CHEEN-yahs koh-loh-REE-dahs",
        "Яркие фломастеры", "YAHR-kee-yeh flah-MAHS-tye-ry", "Renkli keçeli kalemler", "Renk-lee keh-cheh-lee kah-lem-lehr",
        "Spidol warna", "Spee-dohl wahr-nah", "彩 画笔", "Cǎi huàbǐ",
        "色とりどりの サインペン", "Irotoridori no sainpen", "알록달록 색연필", "Allokdallok saegyeonpil"
    ),
    item(
        "Big poster", "بڑا پوسٹر", "Bara poster", "बड़ा पोस्टर", "Bada poster",
        "ملصق رائع", "Mulsaq ra'i'", "Póster grande", "POHS-tehr GRAHN-deh",
        "Grande affiche", "Grahnd ah-feesh", "Großes Plakat", "GROHS-ses plah-KAHT",
        "Cartellone grande", "Kahr-tehl-LOH-neh GRAHN-deh", "Cartaz bonito", "Kahr-TAHZ boh-NEE-too",
        "Красивый плакат", "Krah-SEE-vyy plah-KAHT", "Büyük afiş", "Bew-yewk ah-feesh",
        "Poster besar", "Pohs-tehr beh-sahr", "大 海报", "Dà hǎibào",
        "大きな ポスター", "Ōkina posutā", "커다란 포스터", "Keodaran poseuteo"
    )
]

w2["group-projects"] = [
    item(
        "Cut paper", "کاغذ کاٹو", "Kaghaz kaato", "काग़ज़ काटो", "Kaagaz kaato",
        "قص الورق", "Quss al-waraq", "Corta papel", "KOHR-tah pah-PEHL",
        "Découpe feuille", "Day-koop fuh-yuh", "Schneide Papier", "SHNY-deh pah-PEER",
        "Taglia foglio", "TAH-lyah FOH-lyoh", "Corte papel", "KOHR-chee pah-PEHL",
        "Режь бумагу", "Ryezh boo-MAH-goo", "Kâğıdı kes", "Kah-uh-duh kes",
        "Gunting kertas", "Goon-teeng kehr-tahs", "裁 纸片", "Cái zhǐpiàn",
        "紙 切り取る", "Kami kiritoru", "종이 오려", "Jongi oryeo"
    ),
    item(
        "Glue piece", "ٹکڑا چپکاؤ", "Tukra chipkao", "टुकड़ा चिपकाओ", "Tukda chipkaao",
        "الصق القطعة", "Ilsiaq al-qit'a", "Pega figura", "PEH-gah fee-GOO-rah",
        "Colle dessin", "Kohl deh-san", "Kleb Schnipsel", "KLAYP SHNIP-sel",
        "Incolla pezzo", "Een-KOHL-lah PEHT-tsoh", "Cole figura", "KOH-lee fee-GOO-rah",
        "Приклей картинку", "Pree-KLEY kahr-TEEN-koo", "Parçayı yapıştır", "Pahr-chah-yuh yah-puhsh-tuhr",
        "Tempel potongan", "Tehm-pehl poh-tohng-ahn", "粘 图画", "Zhān túhuà",
        "糊で 貼る", "Nori de haru", "풀로 붙여", "Pullo buchyeo"
    ),
    item(
        "Draw picture", "تصویر بناؤ", "Tasweer banao", "चित्र बनाओ", "Chitra banaao",
        "ارسم لوحة", "Irsum lawha", "Dibuja bonito", "Dee-BOO-hah boh-NEE-toh",
        "Dessine image", "Deh-seen ee-mahzh", "Mal Bild", "MAHL bilt",
        "Disegna disegno", "Dee-ZEH-nyah dee-ZEH-nyoh", "Desenhe lindo", "Deh-ZEHN-yee LEEN-doo",
        "Рисуй рисунок", "Ree-SOOY ree-SOO-nahk", "Resim çiz", "Reh-seem cheez",
        "Gambar rapi", "Gahm-bahr rah-pee", "画 插图", "Huà chātú",
        "絵 描く", "E kaku", "그림 그려", "Geurim geuryeo"
    )
]

output_path = os.path.join(os.path.dirname(__file__), "..", "src", "data", "multilingual", "cat2_shopping_health_school.ts")
export_ts_module(output_path, "CAT2_W1", "CAT2_W2", w1, w2)
