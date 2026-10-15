# Category 3: Friends & Play (5), Nature & Outdoors (5), Manners & Help (5) = 15 topics
import os
import sys
sys.path.append(os.path.dirname(__file__))
from helper import item, export_ts_module

w1 = {}
w2 = {}

# 33. making-friends
w1["making-friends"] = [
    item(
        "New friend", "نیا دوست", "Naya dost", "नया दोस्त", "Naya dost",
        "صديق جديد", "Sadiq jadid", "Nuevo amigo", "NWEH-voh ah-MEE-goh",
        "Nouvel ami", "Noo-vehl ah-mee", "Neuer Freund", "NOY-er froynt",
        "Nuovo amico", "NWAW-voh ah-MEE-koh", "Novo amigo", "NOH-voo ah-MEE-goo",
        "Новый друг", "NOH-vyy drook", "Yeni arkadaş", "Yeh-nee ahr-kah-dahsh",
        "Teman baru", "Teh-mahn bah-roo", "新 朋友", "Xīn péngyǒu",
        "新しい 友達", "Atarashii tomodachi", "새로운 친구", "Saeroun chingu"
    ),
    item(
        "Kind smile", "پیاری مسکراہٹ", "Pyaari muskurahat", "प्यारी मुस्कान", "Pyaari muskaan",
        "ابتسامة لطيفة", "Ibtisama latifa", "Sonrisa amable", "Sohn-REE-sah ah-MAH-bleh",
        "Doux sourire", "Doo soo-reer", "Liebes Lächeln", "LEE-bes LEKH-eln",
        "Sorriso dolce", "Sohr-REE-zoh DOHL-cheh", "Sorriso simpático", "Sohr-HEE-zoo seem-PAH-chee-koo",
        "Добрая улыбка", "DOHB-rah-yah oo-LYP-kah", "Güler yüz", "Gew-lehr yewz",
        "Senyum hangat", "Sehn-yoom hahng-aht", "善 微笑", "Shàn wēixiào",
        "優しい 笑顔", "Yasashii egao", "다정한 미소", "Dajeong-han miso"
    ),
    item(
        "Fun game", "مزیدار کھیل", "Mazedar khel", "मज़ेदार खेल", "Mazedaar khel",
        "لعبة ممتعة", "Lu'ba mumti'a", "Juego divertido", "HWEH-goh dee-vehr-TEE-doh",
        "Jeu amusant", "Zhuh ah-moo-zahn", "Tolles Spiel", "TOL-les shpeel",
        "Gioco bello", "JOH-koh BEHL-loh", "Jogo legal", "ZHOH-goo leh-GAHL",
        "Весёлая игра", "Vyeh-SYOH-lah-yah eeg-RAH", "Eğlenceli oyun", "Eh-lehn-jeh-lee oh-yoon",
        "Permainan asyik", "Pehr-mye-nahn ah-seek", "好 游戏", "Hǎo yóuxì",
        "楽しい 遊び", "Tanoshii asobi", "신나는 놀이", "Sinnaneun nori"
    )
]

w2["making-friends"] = [
    item(
        "Say hi", "ہیلو کہو", "Hello kaho", "नमस्ते कहो", "Namaste kaho",
        "قل مرحباً", "Qul marhaban", "Saluda alegre", "Sah-LOO-dah ah-LEH-greh",
        "Dis salut", "Dee sah-loo", "Sag Hallo", "ZAHK hah-LOH",
        "Dì ciao", "DEE chow", "Diga olá", "JEE-gah oh-LAH",
        "Скажи привет", "Skah-ZHY pree-VYEHT", "Selam ver", "Seh-lahm vehr",
        "Sapa ramah", "Sah-pah rah-mah", "打 招呼", "Dǎ zhāohu",
        "挨拶 する", "Aisatsu suru", "반갑게 인사해", "Bangapge insahae"
    ),
    item(
        "Share name", "نام بتاؤ", "Naam batao", "नाम बताओ", "Naam bataao",
        "قل اسمك", "Qul ismak", "Di nombre", "DEE NOHM-breh",
        "Donne prénom", "Dohn pray-nohm", "Nenn Namen", "NEN NAH-men",
        "Dì nome", "DEE NOH-meh", "Diga nome", "JEE-gah NAW-mee",
        "Назови имя", "Nah-zah-VEE EE-myah", "Adını söyle", "Ah-duh-nuh seri-leh",
        "Beri tahu nama", "Beh-ree tah-hoo nah-mah", "说 名字", "Shuō míngzi",
        "名前 教える", "Namae oshieru", "이름 말해줘", "Ireum malhaejwo"
    ),
    item(
        "Play together", "ساتھ کھیلو", "Saath khelo", "साथ खेलो", "Saath khelo",
        "العب معاً", "Il'ab ma'an", "Juega juntos", "HWEH-gah HOON-tohs",
        "Joue ensemble", "Zhoo ahn-sahn-bluh", "Spiel mit", "SHPEEL mit",
        "Gioca insieme", "JOH-kah een-SYEH-meh", "Brinque junto", "BREEN-kee ZHOON-too",
        "Играйте дружно", "Eeg-RYE-tyeh DROOZH-nah", "Birlikte oyna", "Beer-leek-teh oy-nah",
        "Main bersama", "Mah-een behr-sah-mah", "一起 玩耍", "Yīqǐ wánshuǎ",
        "一緒に 遊ぶ", "Issho ni asobu", "같이 놀자", "Gachi nolja"
    )
]

# 34. birthday-party
w1["birthday-party"] = [
    item(
        "Sweet cake", "میٹھا کیک", "Meetha cake", "मीठा केक", "Meetha cake",
        "كعكة حلوة", "Ka'ka hulwa", "Pastel dulce", "Pahs-TEHL DOOL-seh",
        "Gâteau sucré", "Gah-toh soo-kray", "Süße Geburtstagstorte", "ZYOO-seh geh-BOORTS-tahks-tor-teh",
        "Torta squisita", "TOHR-tah skwee-ZEE-tah", "Bolo gostoso", "BOH-loo gohs-TOH-zoo",
        "Вкусный торт", "VKOOS-nyy tohrt", "Tatlı pasta", "Taht-luh pahs-tah",
        "Kue lezat", "Koo-eh leh-zaht", "香 蛋糕", "Xiāng dàngāo",
        "美味しい ケーキ", "Oishii kēki", "달콤한 케이크", "Dalkom-han keikeu"
    ),
    item(
        "Bright candle", "روشن موم بتی", "Roshan mombatti", "जलती मोमबत्ती", "Jalti mombatti",
        "شمعة مضيئة", "Sham'a mudi'a", "Vela encendida", "VEH-lah ehn-sehn-DEE-dah",
        "Bougie allumée", "Boo-zhee ah-loo-may", "Helle Kerze", "HEL-leh KEHR-tseh",
        "Candela accesa", "Kahn-DEH-lah aht-CHEH-zah", "Vela brilhante", "VEH-lah breel-YAHN-chee",
        "Яркая свечка", "YAHR-kah-yah SVYECH-kah", "Parlak mum", "Pahr-lahk moom",
        "Lilin menyala", "Lee-leen meh-nyah-lah", "明 蜡烛", "Míng làzhú",
        "明るい キャンドル", "Akarui kyandoru", "환한 촛불", "Hwan-han chotbul"
    ),
    item(
        "Colorful balloon", "رنگین غبارہ", "Rangeen gubaara", "रंगीन गुब्बारा", "Rangeen gubbaara",
        "بالون ملون", "Balun mulawwan", "Globo colorido", "GLOH-boh koh-loh-REE-doh",
        "Ballon coloré", "Bah-lohn koh-loh-ray", "Bunter Luftballon", "BOON-ter LOOFT-bah-lon",
        "Palloncino colorato", "Pahl-lohn-CHEE-noh koh-loh-RAH-toh", "Balão colorido", "Bah-LOWN koh-loh-REE-doo",
        "Разноцветный шарик", "Rahz-nah-TSVYEHT-nyy SHAH-reek", "Renkli balon", "Renk-lee bah-lohn",
        "Balon warna-warni", "Bah-lohn wahr-nah wahr-nee", "彩 气球", "Cǎi qìqiú",
        "カラフルな 風船", "Karafuruna fūsen", "알록달록 풍선", "Allokdallok pungseon"
    )
]

w2["birthday-party"] = [
    item(
        "Blow candle", "موم بتی بجھاؤ", "Mombatti bujhao", "मोमबत्ती बुझाओ", "Mombatti bujhaao",
        "أطفئ شمعة", "Atfi' sham'a", "Sopla vela", "SOH-plah VEH-lah",
        "Souffle bougie", "Soo-fluh boo-zhee", "Puste Kerze", "POOS-teh KEHR-tseh",
        "Soffia candela", "SOHF-fyah kahn-DEH-lah", "Assopre vela", "Ah-SAW-pree VEH-lah",
        "Задуй свечу", "Zah-DOOY svyeh-CHOO", "Mumu üfle", "Moo-moo ewf-leh",
        "Tiup lilin", "Tee-oop lee-leen", "吹 蜡烛", "Chuī làzhú",
        "ろうそく 吹き消す", "Rōsoku fukikesu", "촛불 불어", "Chotbul bureo"
    ),
    item(
        "Clap hands", "تالیاں بجاؤ", "Taaliyan bajao", "तालियाँ बजाओ", "Taaliyaan bajaao",
        "صفق بفرح", "Saffiq bi-farah", "Aplaude fuerte", "Ah-PLOW-deh FWEHR-teh",
        "Tape mains", "Tahp man", "Klatsch Beifall", "KLAHTSH BY-fahl",
        "Batti mani", "BAHT-tee MAH-nee", "Bata palmas", "BAH-tah PAHL-mahs",
        "Хлопай в ладоши", "KHLOH-pie v lah-DOH-shee", "El çırp", "Ehl chuhrp",
        "Tepuk tangan", "Teh-pook tahng-ahn", "拍 双手", "Pāi shuāngshǒu",
        "拍手 する", "Hakushu suru", "박수 쳐", "Baksu chyeo"
    ),
    item(
        "Sing song", "گانا گاؤ", "Gaana gao", "गाना गाओ", "Gaana gaao",
        "غن أغنية", "Ghann ughniyya", "Canta alegre", "KAHN-tah ah-LEH-greh",
        "Chante bien", "Shahnt byan", "Sing Lied", "ZING leet",
        "Canta insieme", "KAHN-tah een-SYEH-meh", "Cante parabéns", "KAHN-chee pah-rah-BENGZ",
        "Пой песенку", "Poy PYEH-syen-koo", "Şarkı söyle", "Shahr-kuh seri-leh",
        "Nyanyi lagu", "Nyah-nyee lah-goo", "唱 欢歌", "Chàng huāngē",
        "歌を 歌う", "Uta o utau", "노래 불러", "Norae bulleo"
    )
]

# 35. sharing-toys
w1["sharing-toys"] = [
    item(
        "Cute car", "پیاری گاڑی", "Pyaari gaadi", "प्यारी गाड़ी", "Pyaari gaadi",
        "سيارة جميلة", "Sayyara jamila", "Cochecito lindo", "Koh-cheh-SEE-toh LEEN-doh",
        "Jolie voiture", "Zhoh-lee vwah-toor", "Schönes Spielzeugauto", "SHER-nes SHPEEL-tsoyk-ow-toh",
        "Macchinina carina", "Mahk-kee-NEE-nah kah-REE-nah", "Carrinho bonito", "Kahr-HEEN-yoo boh-NEE-too",
        "Маленькая машинка", "MAH-lyen-kah-yah mah-SHEEN-kah", "Güzel araba", "Gew-zel ah-rah-bah",
        "Mobil-mobilan lucu", "Moh-beel moh-bee-lahn loo-choo", "萌 小车", "Méng xiǎochē",
        "可愛い ミニカー", "Kawaii minikā", "귀여운 자동차", "Gwiyeoun jadongcha"
    ),
    item(
        "Shared turn", "باری باری", "Baari baari", "बारी-बारी", "Baari-baari",
        "دور مشترك", "Dawr mushtarak", "Turno justo", "TOOR-noh HOOS-toh",
        "Tour partagé", "Toor pahr-tah-zhay", "Faire Runde", "FEH-reh ROON-deh",
        "Turno giusto", "TOOR-noh JOOS-toh", "Vez de cada um", "VEHZ jee KAH-dah oong",
        "Общая очередь", "OHB-shah-yah OH-cheh-ryeht", "Sırayla oynama", "Suh-rye-lah oy-nah-mah",
        "Giliran adil", "Gee-lee-rahn ah-deel", "轮流 玩", "Lúnliú wán",
        "順番の 交代", "Junban no kōtai", "사이좋은 차례", "Saijoeun charye"
    ),
    item(
        "Happy game", "خوشگوار کھیل", "Khushgawar khel", "ख़ुशनुमा खेल", "Khushnuma khel",
        "لعب ممتع", "La'b mumti'", "Juego amigable", "HWEH-goh ah-mee-GAH-bleh",
        "Jeu paisible", "Zhuh peh-zeebl", "Friedliches Spiel", "FREET-likh-es shpeel",
        "Gioco sereno", "JOH-koh seh-REH-noh", "Brincadeira boa", "Breen-kah-DAY-rah BOH-ah",
        "Дружная забава", "DROOZH-nah-yah zah-BAH-vah", "Tatlı eğlence", "Taht-luh eh-lehn-jeh",
        "Bermain damai", "Behr-mye-een dah-mye", "和 乐局", "Hé lèjú",
        "仲良しな 遊び", "Nakayoshina asobi", "즐거운 놀이", "Jeulgeoun nori"
    )
]

w2["sharing-toys"] = [
    item(
        "Pass car", "گاڑی پکڑاؤ", "Gaadi pakrao", "गाड़ी बढ़ाओ", "Gaadi badhaao",
        "مرر السيارة", "Marrir as-sayyara", "Pasa coche", "PAH-sah KOH-cheh",
        "Passe voiture", "Pahs vwah-toor", "Reich Auto", "RYE-kh OW-toh",
        "Passa macchinina", "PAHS-sah mahk-kee-NEE-nah", "Passe carrinho", "PAH-see kahr-HEEN-yoo",
        "Передай машинку", "Pyeh-ryeh-DAY mah-SHEEN-koo", "Arabayı uzat", "Ah-rah-bah-yuh oo-zaht",
        "Oper mainan", "Oh-pehr my-nahn", "递 小车", "Dì xiǎochē",
        "車 渡す", "Kuruma watasu", "자동차 건네줘", "Jadongcha geonneojwo"
    ),
    item(
        "Take turn", "اپنی باری لو", "Apni baari lo", "अपनी बारी लो", "Apni baari lo",
        "خذ دورك", "Khudh dawrak", "Toma turno", "TOH-mah TOOR-noh",
        "Prends tour", "Prahn toor", "Sei dran", "ZY drahn",
        "Tocca a te", "TOHK-kah ah teh", "Vez sua", "VEHZ SOO-ah",
        "Играй по очереди", "Eeg-RYE pah OH-cheh-ryeh-dee", "Sırada bekle", "Suh-rah-dah behk-leh",
        "Ambil giliran", "Ahm-beel gee-lee-rahn", "按 轮次", "Àn lúncì",
        "順番 守る", "Junban mamoru", "차례를 지켜", "Charyereul jikyeo"
    ),
    item(
        "Say thanks", "شکریہ کہو", "Shukriya kaho", "धन्यवाद कहो", "Dhanyavaad kaho",
        "قل شكراً", "Qul shukran", "Da gracias", "DAH GRAH-syahs",
        "Dis merci", "Dee mehr-see", "Sag Danke", "ZAHK DAHN-keh",
        "Dì grazie", "DEE GRAHT-tsyeh", "Diga obrigado", "JEE-gah oh-bree-GAH-doo",
        "Поблагодари от души", "Pah-blah-gah-dah-REE aht doo-SHY", "Teşekkür et", "Teh-shehk-kewr et",
        "Ucap terimakasih", "Oo-chahp teh-ree-mah-kah-seeh", "道 感谢", "Dào gǎnxiè",
        "「ありがとう」と言う", "Arigatō to iu", "고맙다고 전해", "Gomapdago jeonhae"
    )
]

# 36. playground-games
w1["playground-games"] = [
    item(
        "High swing", "اونچا جھولا", "Ooncha jhoola", "ऊँचा झूला", "Ooncha jhoola",
        "أرجوحة عالية", "Urjuha 'aliya", "Columpio alto", "Koh-LOOM-pyoh AHL-toh",
        "Haute balançoire", "Oht bah-lahn-swahr", "Hohe Schaukel", "HOH-heh SHOW-kel",
        "Altalena alta", "Ahl-tah-LEH-nah AHL-tah", "Balanço alto", "Bah-LAHN-soo AHL-too",
        "Высокие качели", "Vy-SOH-kee-yeh kah-CHEH-lee", "Yüksek salıncak", "Yewk-sek sah-luhn-jahk",
        "Ayunan tinggi", "Ah-yoo-nahn teeng-gee", "高 秋千", "Gāo qiūqiān",
        "高く漕ぐ ブランコ", "Takaku kogu buranko", "높은 그네", "Nopeun geune"
    ),
    item(
        "Long slide", "لمبی پھسلن", "Lambi phisaln", "लंबी फिसलपट्टी", "Lambi phisalpatti",
        "زلاقة طويلة", "Zullaqa tawila", "Tobogán largo", "Toh-boh-GAHN LAHR-goh",
        "Grand toboggan", "Grahn toh-boh-gahn", "Lange Rutsche", "LAHN-geh ROOT-sheh",
        "Scivolo lungo", "SHEE-voh-loh LOON-goh", "Escorregador longo", "Ehs-koh-heh-gah-DOHR LOHN-goo",
        "Длинная горка", "DLEEN-nah-yah GOHR-kah", "Uzun kaydırak", "Oo-zoon kie-duh-rahk",
        "Perosotan panjang", "Peh-roh-soh-tahn pahn-jahng", "长 滑梯", "Cháng huátī",
        "長い 滑り台", "Nagai suberidai", "긴 미끄럼틀", "Gin mikkeureomteul"
    ),
    item(
        "Soft sand", "نرم ریت", "Naram rait", "नरम रेत", "Naram ret",
        "رمل ناعم", "Raml na'im", "Arena suave", "Ah-REH-nah SWAH-veh",
        "Sable fin", "Sahbl fan", "Weicher Sand", "VY-kher zahnt",
        "Sabbia morbida", "SAHB-byah MOHR-bee-dah", "Areia fofa", "Ah-RAY-ah FAW-fah",
        "Мягкий песок", "MYAHK-kiy pyeh-SOHK", "İnce kum", "Een-jeh koom",
        "Pasir halus", "Pah-seer hah-loos", "软 沙坑", "Ruǎn shākēng",
        "さらさらの 砂場", "Sarasarano sunaba", "부드러운 모래", "Budeureo-un morae"
    )
]

w2["playground-games"] = [
    item(
        "Swing high", "اونچے جھولو", "Oonchay jhoolo", "ऊँचा झूलो", "Ooncha jhoolo",
        "تأرجح عالياً", "Ta'arjah 'aliyan", "Colúmpiate alto", "Koh-LOOM-pyah-teh AHL-toh",
        "Balance haut", "Bah-lahns oh", "Schaukel hoch", "SHOW-kel hohkh",
        "Dondola alto", "DOHN-doh-lah AHL-toh", "Balança bem", "Bah-LAHN-sah beng",
        "Качайся высоко", "Kah-CHEY-syah vy-sah-KOH", "Yükseğe sallan", "Yewk-seh-eh sahl-lahn",
        "Ayun tinggi", "Ah-yoon teeng-gee", "荡 秋千", "Dàng qiūqiān",
        "ブランコ 漕ぐ", "Buranko kogu", "그네 높이타", "Geune nopi ta"
    ),
    item(
        "Slide down", "نیچے پھسلو", "Neechay phislo", "नीचे फिसलो", "Neeche phislo",
        "تزحلق لأسفل", "Tazahlaq li-asfal", "Deslízate abajo", "Dehs-LEE-zah-teh ah-BAH-hoh",
        "Glisse vite", "Glees veet", "Rutsch runter", "ROOTSH ROON-ter",
        "Scivola giù", "SHEE-voh-lah joo", "Escorregue já", "Ehs-koh-HEH-gee zhah",
        "Скатись вниз", "Skah-TEES vneez", "Aşağıya kay", "Ah-shah-uh-yah kye",
        "Meluncur ke bawah", "Meh-loon-choor keh bah-wah", "滑 下去", "Huá xiàqù",
        "滑り台 滑る", "Suberidai suberu", "미끄럼틀 타", "Mikkeureomteul ta"
    ),
    item(
        "Build castle", "قلعہ بناؤ", "Qila banao", "किला बनाओ", "Kila banaao",
        "ابن قلعة", "Ibni qal'a", "Construye castillo", "Kohn-STROO-yeh kahs-TEE-yoh",
        "Bâtis château", "Bah-tee shah-toh", "Bau Burg", "BOW boork",
        "Costruisci castello", "Kohs-troo-EE-shee kahs-TEHL-loh", "Faça castelo", "FAH-sah kahs-TEH-loo",
        "Строй замок", "STROY ZAH-mahk", "Kaleden yap", "Kah-leh-dehn yahp",
        "Bangun istana", "Bahng-oon ees-tah-nah", "造 城堡", "Zào chéngbǎo",
        "お城 作る", "Oshiro tsukuru", "모래성 쌓아", "Moraeseong ssaha"
    )
]

# 37. inviting-a-friend
w1["inviting-a-friend"] = [
    item(
        "Warm welcome", "شاندار استقبال", "Shaandaar isteqbaal", "गर्मजोशी से स्वागत", "Garmjoshi se swaagat",
        "ترحيب حار", "Tarhib harr", "Bienvenida cálida", "Byehn-veh-NEE-dah KAH-lee-dah",
        "Accueil chaleureux", "Ah-kuy shah-luh-ruh", "Herzliches Willkommen", "HEHRTS-likh-es vil-KOM-men",
        "Benvenuto caloroso", "Behn-veh-NOO-toh kah-loh-ROH-zoh", "Boas-vindas calorosas", "BAW-ahs VEEN-dahs kah-loh-RAW-zahs",
        "Тёплый приём", "TYOHP-lyy pree-YOHM", "Sıcak karşılama", "Suh-dzhak kahr-shuh-lah-mah",
        "Sambutan hangat", "Sahm-boo-tahn hahng-aht", "诚 欢迎", "Chéng huānyíng",
        "温かい もてなし", "Atatakai motenashi", "따뜻한 환영", "Ttatteut-han hwanyeong"
    ),
    item(
        "Cozy room", "آرام دہ کمرہ", "Aaram deh kamra", "आरामदेह कमरा", "Aaraamdeh kamra",
        "غرفة مريحة", "Ghurfa muriha", "Cuarto acogedor", "KWAHR-toh ah-koh-heh-DOHR",
        "Chambre douillette", "Shahmb-ruh dwee-yeht", "Gemütliches Zimmer", "Geh-MYOOT-likh-es TSIM-mer",
        "Camera accogliente", "KAH-meh-rah ahk-kohl-YEHN-teh", "Quarto aconchegante", "KWAHR-too ah-kohn-sheh-GAHN-chee",
        "Уютная комната", "Oo-YOOT-nah-yah KOHM-nah-tah", "Sıcacık oda", "Suh-jah-juhk oh-dah",
        "Kamar nyaman", "Kah-mahr nyah-mahn", "暖 房间", "Nuǎn fángjiān",
        "居心地の 良い部屋", "Igokochi no yoi heya", "아늑한 방", "Aneuk-han bang"
    ),
    item(
        "Sweet snack", "میٹھی مٹھائی", "Meethi mithaai", "मीठी मिठाई", "Meethi mithaai",
        "حلوى لذيذة", "Halwa ladhidha", "Merienda rica", "Meh-RYEHN-dah REE-kah",
        "Goûter savoureux", "Goo-tay sah-voo-ruh", "Leckerer Imbiss", "LEK-keh-rer IM-bis",
        "Spuntino squisito", "Spoon-TEE-noh skwee-ZEE-toh", "Lanchinho doce", "Lahn-SHEEN-yoo DOH-see",
        "Вкусное угощение", "VKOOS-nah-yeh oo-gah-SHYEH-nyee-yeh", "Güzel ikram", "Gew-zel eek-rahm",
        "Camilan manis", "Chah-mee-lahn mah-nees", "甜 点心", "Tián diǎnxin",
        "おいしい おやつ", "Oishii oyatsu", "맛있는 다과", "Mas-inneun dagwa"
    )
]

w2["inviting-a-friend"] = [
    item(
        "Open door", "دروازہ کھولو", "Darwaza kholo", "दरवाज़ा खोलो", "Darwaaza kholo",
        "افتح الباب", "Iftah al-bab", "Abre puerta", "AH-breh PWEHR-tah",
        "Ouvre porte", "Oo-vruh pohrt", "Öffne Tür", "ERF-neh toor",
        "Apri porta", "AH-pree POHR-tah", "Abra porta", "AH-brah PAWR-tah",
        "Открой дверь", "Aht-KROY dvyer", "Kapıyı aç", "Kah-puh-yuh ahch",
        "Buka pintu", "Boo-kah peen-too", "开 房门", "Kāi fángmén",
        "ドア 開ける", "Doa akeru", "문 열어줘", "Mun yeoreojwo"
    ),
    item(
        "Come inside", "اندر آؤ", "Andar aao", "अंदर आओ", "Andar aao",
        "ادخل بالداخل", "Udkhul bid-dakhil", "Pasa adentro", "PAH-sah ah-DEHN-troh",
        "Entre vite", "Ahnt-ruh veet", "Komm rein", "KOM ryne",
        "Entra pure", "EHN-trah POO-reh", "Entre aqui", "EHN-tree ah-KEE",
        "Заходи скорее", "Zah-khah-DEE skah-RYEY", "İçeri buyur", "Ee-cheh-ree boo-yoor",
        "Masuklah ke dalam", "Mah-sook-lah keh dah-lahm", "快 进屋", "Kuài jìnwū",
        "どうぞ 入る", "Dōzo hairu", "어서 들어와", "Eoseo deureowa"
    ),
    item(
        "Show toys", "کھلونے دکھاؤ", "Khilone dikhao", "खिलौने दिखाओ", "Khilaune dikhaao",
        "اعرض ألعابك", "I'rid al'abak", "Muestra juguetes", "MWEHS-trah hoo-GEH-tehs",
        "Montre jouets", "Mohn-truh zhoo-ay", "Zeig Spielsachen", "TSYGH SHPEEL-zah-khen",
        "Mostra giochi", "MOHS-trah JOH-kee", "Mostre brinquedos", "MOHS-tree breen-KAY-doos",
        "Покажи игрушки", "Pah-kah-ZHY eeg-ROOSH-kee", "Oyuncaklarını göster", "Oh-yoon-jahk-lah-ruh-nuh gerz-tehr",
        "Pamerkan mainan", "Pah-mehr-kahn my-nahn", "拿出 玩具", "Náchū wánjù",
        "おもちゃ 見せる", "Omocha miseru", "장난감 구경시켜줘", "Jangnamgam gugyeongsikyeojwo"
    )
]

# 38. park-walks
w1["park-walks"] = [
    item(
        "Green grass", "ہری گھاس", "Hari ghaas", "हरी घास", "Hari ghaas",
        "عشب أخضر", "'Ushb akhdar", "Pasto verde", "PAHS-toh VEHR-deh",
        "Herbe verte", "Ehrb vehrt", "Grünes Gras", "GREW-nes grahs",
        "Erba verde", "EHR-bah VEHR-deh", "Grama verde", "GRAH-mah VEHR-jee",
        "Зелёная трава", "Zyeh-LYOH-nah-yah trah-VAH", "Yeşil çimen", "Yeh-sheel chee-men",
        "Rumput hijau", "Room-poot hee-jow", "绿 草坪", "Lǜ cǎopíng",
        "青い 芝生", "Aoi shibafu", "푸른 잔디", "Pureun jandi"
    ),
    item(
        "Tall tree", "لمبا درخت", "Lamba darakht", "लंबा पेड़", "Lamba ped",
        "شجرة طويلة", "Shajara tawila", "Árbol alto", "AHR-bohl AHL-toh",
        "Grand arbre", "Grahn ahr-bruh", "Hoher Baum", "HOH-her bowm",
        "Albero alto", "AHL-beh-roh AHL-toh", "Árvore alta", "AHR-voh-ree AHL-tah",
        "Высокое дерево", "Vy-SOH-kah-yeh DYEH-ryeh-vah", "Yüksek ağaç", "Yewk-sek ah-ahch",
        "Pohon rindang", "Poh-hohn reen-dahng", "高 大树", "Gāo dàshù",
        "高い 木", "Takai ki", "키큰 나무", "Kikeun namu"
    ),
    item(
        "Sunny bench", "دھوپ والی بنچ", "Dhoop wali bench", "धूपदार बेंच", "Dhoopdaar bench",
        "مقعد مشمس", "Maq'ad mushmis", "Banco soleado", "BAHN-koh soh-leh-AH-doh",
        "Banc au soleil", "Bahn oh soh-lay", "Sonnige Bank", "ZON-nee-geh bahnk",
        "Panchina al sole", "Pahn-KEE-nah ahl SOH-leh", "Banco no sol", "BAHN-koo noo sohl",
        "Солнечная скамейка", "SOHL-neech-nah-yah skah-MYEY-kah", "Güneşli bank", "Gew-nesh-lee bahnk",
        "Bangku taman", "Bahng-koo tah-mahn", "阳 暖座", "Yáng nuǎnzuò",
        "日当たりの 良いベンチ", "Hiatari no yoibenchi", "따뜻한 벤치", "Ttatteut-han benchi"
    )
]

w2["park-walks"] = [
    item(
        "Smell flower", "پھول سونگھو", "Phool soongho", "फूल सूँघो", "Phool soongho",
        "شم زهرة", "Shumm zahra", "Huele flor", "WEH-leh flohr",
        "Sens fleur", "Sahn fluhr", "Riech Blume", "REEKH BLOO-meh",
        "Annusa fiore", "Ahn-NOO-zah FYOH-reh", "Cheire flor", "SHAY-ree flohr",
        "Понюхай цветок", "Pah-NYOO-khye tsvyeh-TOHK", "Çiçeği kokla", "Chee-cheh-ee kohk-lah",
        "Cium bunga", "Chee-oom boo-ngah", "闻 花香", "Wén huāxiāng",
        "花の 匂いを嗅ぐ", "Hana no nioi o kagu", "꽃향기 맡아", "Kkothyanggi mata"
    ),
    item(
        "Watch bird", "پرندہ دیکھو", "Parinda dekho", "चिड़िया देखो", "Chidiya dekho",
        "راقب طائراً", "Raqib ta'iran", "Mira pájaro", "MEE-rah PAH-hah-roh",
        "Regarde oiseau", "Ruh-gahrd wah-zoh", "Beobachte Vogel", "Beh-OH-bahkh-teh FOH-gel",
        "Guarda uccello", "GWAHR-dah oot-CHEHL-loh", "Olhe passarinho", "AW-lyee pah-sah-REEN-yoo",
        "Смотри на птичку", "Smah-TREE nah PTEECH-koo", "Kuşu izle", "Koo-shoo eez-leh",
        "Amati burung", "Ah-mah-tee boo-roong", "看 小鸟", "Kàn xiǎoniǎo",
        "小鳥 眺める", "Kotori nagameru", "새를 관찰해", "Saereul gwanchalhae"
    ),
    item(
        "Walk path", "راستے پر چلو", "Raaste par chalo", "पगडंडी पर चलो", "Pagdandi par chalo",
        "امش في المسار", "Imshi fil-masar", "Camina sendero", "Kah-MEE-nah sehn-DEH-roh",
        "Suis chemin", "Swee shuh-man", "Geh Weg", "GAY vayk",
        "Segui sentiero", "SEH-gwee sehn-TYEH-roh", "Siga trilha", "SEE-gah TREE-lyah",
        "Иди по тропинке", "Ee-DEE pah trah-PEEN-kyeh", "Patikada yürü", "Pah-tee-kah-dah yew-rew",
        "Susuri jalan", "Soo-soo-ree jah-lahn", "走 小径", "Zǒu xiǎojìng",
        "小道を 歩く", "Komichi o aruku", "오솔길 걸어", "Osolgil georeo"
    )
]

# 39. rainy-days
w1["rainy-days"] = [
    item(
        "Wet puddle", "پانی کا گڑھا", "Paani ka garha", "पानी का गड्ढा", "Paani ka gaddha",
        "بركة ماء", "Birkat ma'", "Charco brillante", "CHAR-koh bree-YAHN-teh",
        "Flaque d'eau", "Flahk doh", "Kleine Wasserpfütze", "KLY-neh VAHS-ser-pfoot-tseh",
        "Pozzanghera d'acqua", "Poht-TSAHN-geh-rah DAHK-wah", "Poça d'água", "PAW-sah DAH-gwah",
        "Большая лужа", "Bahl-SHAH-yah LOO-zhah", "Su birikintisi", "Soo bee-ree-keen-tee-see",
        "Genangan air", "Geh-nahng-ahn ah-yeer", "小 水坑", "Xiǎo shuǐkēng",
        "水たまり", "Mizutamari", "빗물 웅덩이", "Binmul ungdeong-i"
    ),
    item(
        "Blue boots", "نیلے بوٹ", "Neele boot", "नीले जूते", "Neele joote",
        "حذاء أزرق", "Hitha' azraq", "Botas azules", "BOH-tahs ah-SOO-lehs",
        "Bottes bleues", "Boht bluh", "Blaue Gummistiefel", "BLOW-eh GOOM-mee-shtee-fel",
        "Stivaletti blu", "Stee-vah-LEHT-tee bloo", "Botas azuis", "BAW-tahs ah-ZOO-ees",
        "Синие сапожки", "SEE-nyee-yeh sah-POHZH-kee", "Mavi çizmeler", "Mah-vee cheez-meh-lehr",
        "Sepatu bot biru", "Seh-pah-too boht bee-roo", "蓝 雨靴", "Lán yǔxuē",
        "青い 長靴", "Aoi nagagutsu", "파란 장화", "Paran janghwa"
    ),
    item(
        "Bright umbrella", "چمکیلی چھتری", "Chamkeeli chhatri", "चमकीली छतरी", "Chamkeeli chhatri",
        "مظلة ملونة", "Mizalla mulawwana", "Paraguas bonito", "Pah-RAH-gwahs boh-NEE-toh",
        "Joli parapluie", "Zhoh-lee pah-rah-plwee", "Bunter Regenschirm", "BOON-ter RAY-gen-sheerm",
        "Ombrello allegro", "Ohm-BREHL-loh ahl-LEH-groh", "Guarda-chuva colorido", "GWAHR-dah SHOO-vah koh-loh-REE-doo",
        "Яркий зонтик", "YAHR-kiy ZOHN-teek", "Renkli şemsiye", "Renk-lee shehm-see-yeh",
        "Payung terang", "Pah-yoong teh-rahng", "亮 雨伞", "Liàng yǔsǎn",
        "カラフルな 傘", "Karafuruna kasa", "예쁜 우산", "Yeppeun usan"
    )
]

w2["rainy-days"] = [
    item(
        "Splash puddle", "پانی میں چھپ چھپ", "Paani mein chhap chhap", "पानी में छपछप", "Paani mein chhap chhap",
        "اقفز بالماء", "Iqfiz bil-ma'", "Salta charcos", "SAHL-tah CHAR-kohs",
        "Saute flaque", "Soht flahk", "Patsch Pfütze", "PAHTSH PFOOT-tseh",
        "Salta pozzanghere", "SAHL-tah poht-TSAHN-geh-reh", "Pule poça", "POO-lee PAW-sah",
        "Шлёпай по лужам", "SHLYOH-pie pah LOO-zhahm", "Suya sıçrat", "Soo-yah suhch-raht",
        "Kecipak air", "Keh-chee-pahk ah-yeer", "踩 水坑", "Cǎi shuǐkēng",
        "水たまり バシャバシャ", "Mizutamari basha-basha", "웅덩이 첨벙", "Ungdeong-i cheombeong"
    ),
    item(
        "Open umbrella", "چھتری کھولو", "Chhatri kholo", "छतरी खोलो", "Chhatri kholo",
        "افتح المظلة", "Iftah al-mizalla", "Abre paraguas", "AH-breh pah-RAH-gwahs",
        "Ouvre parapluie", "Oo-vruh pah-rah-plwee", "Spann Schirm", "SHPAHN sheerm",
        "Apri ombrello", "AH-pree ohm-BREHL-loh", "Abra guarda-chuva", "AH-brah GWAHR-dah SHOO-vah",
        "Открой зонт", "Aht-KROY zohnt", "Şemsiyeni aç", "Shehm-see-yeh-nee ahch",
        "Buka payung", "Boo-kah pah-yoong", "撑 雨伞", "Chēng yǔsǎn",
        "傘 開く", "Kasa hiraku", "우산 펼쳐", "Usan pyeolchyeo"
    ),
    item(
        "Hear rain", "بارش سنو", "Baarish suno", "बारिश सुनो", "Baarish suno",
        "استمع للمطر", "Istami' lil-matar", "Escucha lluvia", "Ehs-KOO-chah YOO-vyah",
        "Écoute pluie", "Ay-koot plwee", "Lausch Regen", "LOWSH RAY-gen",
        "Ascolta pioggia", "Ahs-KOHL-tah PYAHD-jah", "Ouça chuva", "OH-sah SHOO-vah",
        "Слушай дождик", "SLOO-shy DOHZH-deek", "Yağmuru dinle", "Yah-moo-roo deen-leh",
        "Dengar hujan", "Dehng-ahr hoo-jahn", "听 雨声", "Tīng yǔshēng",
        "雨音 聞く", "Amaoto kiku", "빗소리 들어", "Bitsori deureo"
    )
]

# 40. pet-animals
w1["pet-animals"] = [
    item(
        "Fluffy kitten", "نرم بلی کا بچہ", "Naram billi ka bachha", "प्यारा बिल्ली का बच्चा", "Pyaara billi ka bachha",
        "قطة ناعمة", "Qitta na'ima", "Gatito suave", "Gah-TEE-toh SWAH-veh",
        "Chaton doux", "Shah-tohn doo", "Kuscheliges Kätzchen", "KOOSH-eh-lee-ges KETS-khen",
        "Gattino morbido", "Gaht-TEE-noh MOHR-bee-doh", "Gatinho fofo", "Gah-CHEEN-yoo FAW-foo",
        "Пушистый котёнок", "Poo-SHEES-tyy kah-TYOH-nahk", "Yumuşak kedi", "Yoo-moo-shahk keh-dee",
        "Anak kucing lucu", "Ah-nahk koo-cheeng loo-choo", "萌 小猫", "Méng xiǎomāo",
        "ふわふわの 子猫", "Fuwafuwano koneko", "보드라운 아기고양이", "Bodeuraun agigoyangi"
    ),
    item(
        "Playful puppy", "چنچل کتے کا بچہ", "Chanchal kuttay ka bachha", "चंचल पिल्ला", "Chanchal pilla",
        "جرو لعوب", "Jarw la'ub", "Perrito juguetón", "Peh-RREE-toh hoo-geh-TOHN",
        "Chiot joueur", "Shee-oh zhoo-uhr", "Verspielter Welpe", "Fehr-SHPEEL-ter VEHL-peh",
        "Cagnolino vispo", "Kahn-nyoh-LEE-noh VEES-poh", "Cachorrinho brincalhão", "Kah-shoh-HEEN-yoo breeng-kahl-YOWN",
        "Игривый щенок", "Ee-GREE-vyy shchyeh-NOHK", "Oyuncu köpek", "Oh-yoon-joo ker-pek",
        "Anak anjing lincah", "Ah-nahk ahn-jeeng leen-chah", "活泼 幼犬", "Huópō yòuquǎn",
        "元気な 子犬", "Genkina koinu", "장난꾸러기 강아지", "Jangnankkureogi gangaji"
    ),
    item(
        "Soft bunny", "نرم خرگوش", "Naram khargosh", "नरम खरगोश", "Naram khargosh",
        "أرنب لطيف", "Arnab latif", "Conejito blanco", "Koh-neh-HEE-toh BLAHN-koh",
        "Lapin doux", "Lah-pan doo", "Zahmes Häschen", "TSAH-mes HES-khen",
        "Coniglietto tenero", "Koh-neel-YEHT-toh TEH-neh-roh", "Coelhinho macio", "Koo-ehl-YEEN-yoo mah-SEE-oo",
        "Белый кролик", "BYEH-lyy KROH-leek", "Sevimli tavşan", "Seh-veem-lee tahv-shahn",
        "Kelinci jinak", "Keh-leen-chee jee-nahk", "白 兔儿", "Bái tùr",
        "白い うさぎ", "Shiroi usagi", "하얀 토끼", "Hayan tokki"
    )
]

w2["pet-animals"] = [
    item(
        "Pet gently", "پیار سے سہلاؤ", "Pyaar se sehlao", "प्यार से सहलाओ", "Pyaar se sahlaao",
        "داعب بلطف", "Da'ib bi-lutf", "Acaricia suave", "Ah-kah-REE-syah SWAH-veh",
        "Caresse bien", "Kah-rehs byan", "Streichle sanft", "SHTRYKH-leh zahnft",
        "Accarezza piano", "Ahk-kah-REHT-tsah PYAH-noh", "Acaricie com carinho", "Ah-kah-REE-see kohn kah-REEN-yoo",
        "Погладь осторожно", "Pah-GLYAHT ahs-tah-ROHZH-nah", "Yavaşça sev", "Yah-vahsh-chah sehv",
        "Elus pelan", "Eh-loos peh-lahn", "轻 抚摸", "Qīng fǔmō",
        "優しく なでる", "Yasashiku naderu", "부드럽게 쓰다듬어", "Budeureopge sseudadeumeo"
    ),
    item(
        "Feed food", "کھانا کھلاؤ", "Khaana khilao", "खाना खिलाओ", "Khaana khilaao",
        "أطعم حيوانك", "At'im hayawanak", "Dale comida", "DAH-leh koh-MEE-dah",
        "Donne à manger", "Dohn ah mahn-zhay", "Füttere gut", "FOOT-teh-reh goot",
        "Dai pappa", "DYE PAHP-pah", "Dê comidinha", "DAY koh-mee-JEEN-yah",
        "Покорми питомца", "Pah-kahr-MEE pee-TOHM-tsah", "Yemini ver", "Yeh-mee-nee vehr",
        "Beri makan", "Beh-ree mah-kahn", "喂 狗粮", "Wèi gǒuliáng",
        "ご飯 あげる", "Gohan ageru", "밥을 챙겨줘", "Babeul chaenggyeojwo"
    ),
    item(
        "Play catch", "گیند پھینکو", "Gend phenko", "गेंद फेंको", "Gend phenko",
        "ارم الكرة", "Irmi al-kura", "Lanza pelota", "LAHN-sah peh-LOH-tah",
        "Lance balle", "Lahns bahl", "Wirf Ball", "VEERF bahl",
        "Lancia palla", "LAHN-chah PAHL-lah", "Jogue bola", "ZHOH-gee BOH-lah",
        "Бросай мячик", "Brah-SYE MYAH-cheek", "Topu fırlat", "Toh-poo fuhr-laht",
        "Lempar bola", "Lehm-pahr boh-lah", "扔 飞盘", "Rēng fēipán",
        "ボール 投げる", "Bōru nageru", "공 던져봐", "Gong deonjeobwa"
    )
]

# 41. beach-fun
w1["beach-fun"] = [
    item(
        "Warm sand", "گرم ریت", "Garam rait", "गर्म रेत", "Garm ret",
        "رمل دافئ", "Raml dafi'", "Arena tibia", "Ah-REH-nah TEE-byah",
        "Sable chaud", "Sahbl sho", "Warmer Sandstrand", "VAHR-mer ZAHNT-shtrahnt",
        "Sabbia calda", "SAHB-byah KAHL-dah", "Areia quentinha", "Ah-RAY-ah ken-CHEEN-yah",
        "Тёплый песок", "TYOHP-lyy pyeh-SOHK", "Sıcak kumsal", "Suh-dzhak koom-sahl",
        "Pasir hangat", "Pah-seer hahng-aht", "暖 沙滩", "Nuǎn shātān",
        "あたたかい 砂浜", "Atatakai sunahama", "따뜻한 모래사장", "Ttatteut-han moraesajang"
    ),
    item(
        "Blue wave", "نیلی لہر", "Neeli lehar", "नीली लहर", "Neeli lehar",
        "موجة زرقاء", "Mawja zarqa'", "Ola azul", "OH-lah ah-SOOL",
        "Vague bleue", "Vahg bluh", "Blaue Meereswelle", "BLOW-eh MAY-res-vel-leh",
        "Onda blu", "OHN-dah bloo", "Onda azul", "OHN-dah ah-ZOOL",
        "Синяя волна", "SEE-nyah-yah vahl-NAH", "Mavi dalga", "Mah-vee dahl-gah",
        "Ombak biru", "Ohm-bahk bee-roo", "蓝 海浪", "Lán hǎilàng",
        "青い 波", "Aoi nami", "푸른 파도", "Pureun pado"
    ),
    item(
        "Pretty shell", "خوبصورت سیپی", "Khoobsurat seepi", "सुंदर सीप", "Sundar seep",
        "صدفة جميلة", "Sadafa jamila", "Concha bonita", "KOHN-chah boh-NEE-tah",
        "Joli coquillage", "Zhoh-lee koh-kee-yahzh", "Hübsche Muschel", "HOOP-sheh MOOSH-el",
        "Bella conchiglia", "BEHL-lah kohn-KEEL-yah", "Conchinha linda", "Kohn-SHEEN-yah LEEN-dah",
        "Красивая ракушка", "Krah-SEE-vah-yah rah-KOOSH-kah", "Güzel denizkabuğu", "Gew-zel deh-neez-kah-boo-oo",
        "Kerang cantik", "Keh-rahng chahn-teek", "美 贝壳", "Měi bèiké",
        "綺麗な 貝殻", "Kireina kaigara", "예쁜 조개껍질", "Yeppeun jogaekkeopjil"
    )
]

w2["beach-fun"] = [
    item(
        "Jump wave", "لہروں پر اچھلو", "Lehron par uchhlo", "लहरों पर कूदो", "Lehron par koodo",
        "اقفز فوق الموج", "Iqfiz fawq al-mawj", "Salta olas", "SAHL-tah OH-lahs",
        "Saute vagues", "Soht vahg", "Hüpf Welle", "HOOPF VEL-leh",
        "Salta onde", "SAHL-tah OHN-deh", "Pule ondas", "POO-lee OHN-dahs",
        "Прыгай через волны", "PRY-guy CHYEH-ryez VOHL-ny", "Dalgalardan atla", "Dahl-gah-lahr-dahn aht-lah",
        "Lompati ombak", "Lohm-pah-tee ohm-bahk", "跳 浪花", "Tiào lànghuā",
        "波を 飛び越える", "Nami o tobikoeru", "파도를 뛰어넘어", "Padoreul ttwieoneomeo"
    ),
    item(
        "Find shell", "سیپیاں ڈھونڈو", "Seepiyan dhoondo", "सीप ढूँढो", "Seep dhoondho",
        "ابحث عن صدف", "Ibhath 'an sadaf", "Busca conchas", "BOOS-kah KOHN-chahs",
        "Trouve coquillages", "Troov koh-kee-yahzh", "Sammle Muscheln", "ZAHM-leh MOOSH-eln",
        "Raccogli conchiglie", "Rahk-KOHL-yee kohn-KEEL-yeh", "Ache conchinhas", "AH-shee kohn-SHEEN-yahs",
        "Ищи ракушки", "Ee-SHCHEE rah-KOOSH-kee", "Denizkabuğu topla", "Deh-neez-kah-boo-oo toh-plah",
        "Cari kerang", "Chah-ree keh-rahng", "捡 贝壳", "Jiǎn bèiké",
        "貝殻 拾う", "Kaigara hirou", "조개 주워", "Jogae juwo"
    ),
    item(
        "Dig sand", "ریت کھودو", "Rait khodo", "रेत खोदो", "Ret khodo",
        "احفر بالرمل", "Ihfir bir-raml", "Cava arena", "KAH-vah ah-REH-nah",
        "Creuse sable", "Kruhz sahbl", "Grab Sand", "GRAHP zahnt",
        "Scava sabbia", "SKAH-vah SAHB-byah", "Cave areia", "KAH-vee ah-RAY-ah",
        "Копай песочек", "Kah-PYE pyeh-SOH-cheek", "Kumu kaz", "Koo-moo kahz",
        "Gali pasir", "Gah-lee pah-seer", "挖 沙坑", "Wā shākēng",
        "砂を 掘る", "Suna o horu", "모래를 파봐", "Moraereul pabwa"
    )
]

# 42. camping-trip
w1["camping-trip"] = [
    item(
        "Green tent", "سبز خیمہ", "Sabz khaima", "हरा तंबू", "Hara tamboo",
        "خيمة خضراء", "Khayma khadra'", "Tienda verde", "TYEHN-dah VEHR-deh",
        "Tente verte", "Tahnt vehrt", "Grünes Zelt", "GREW-nes tselt",
        "Tenda verde", "TEHN-dah VEHR-deh", "Barraca verde", "Bah-HAH-kah VEHR-jee",
        "Зелёная палатка", "Zyeh-LYOH-nah-yah pah-LAHT-kah", "Yeşil çadır", "Yeh-sheel chah-duhr",
        "Tenda hijau", "Tehn-dah hee-jow", "绿 帐篷", "Lǜ zhàngpéng",
        "緑の テント", "Midori no tento", "초록 텐트", "Chorok tenteu"
    ),
    item(
        "Bright stars", "روشن ستارے", "Roshan sitaare", "चमकते सितारे", "Chamakte sitaare",
        "نجوم لامعة", "Nujum lami'a", "Estrellas brillantes", "Ehs-TREH-yahs bree-YAHN-tehs",
        "Étoiles brillantes", "Ay-twahl bree-yahnt", "Helle Sterne", "HEL-leh SHTEHR-neh",
        "Stelle brillanti", "STEHL-leh breel-LAHN-tee", "Estrelas brilhantes", "Ehs-TREH-lahs breel-YAHN-chees",
        "Яркие звёзды", "YAHR-kee-yeh ZVYOHZ-dy", "Işıl ışıl yıldızlar", "Uh-shuhl uh-shuhl yuhl-duhz-lahr",
        "Bintang gemerlap", "Been-tahng geh-mehr-lahp", "亮 星星", "Liàng xīngxīng",
        "輝く 星空", "Kagayaku hoshizora", "빛나는 별들", "Binnaneun byeoldeul"
    ),
    item(
        "Warm campfire", "گرم الاؤ", "Garam alao", "गर्म अलाव", "Garm alaav",
        "نار دافئة", "Nar dafi'a", "Fogata cálida", "Foh-GAH-tah KAH-lee-dah",
        "Feu chaleureux", "Fuh shah-luh-ruh", "Warmes Lagerfeuer", "VAHR-mes LAH-ger-foy-er",
        "Falò caldo", "Fah-LOH KAHL-doh", "Fogueira quentinha", "Foh-GAY-rah ken-CHEEN-yah",
        "Тёплый костёр", "TYOHP-lyy kahs-TYOHR", "Sıcak kamp ateşi", "Suh-dzhak kahmp ah-teh-shee",
        "Api unggun hangat", "Ah-pee oong-goon hahng-aht", "暖 篝火", "Nuǎn gōuhuǒ",
        "パチパチ 焚き火", "Pachipachi takibi", "따뜻한 모닥불", "Ttatteut-han modakbul"
    )
]

w2["camping-trip"] = [
    item(
        "Pitch tent", "خیمہ لگاؤ", "Khaima lagao", "तंबू लगाओ", "Tamboo lagaao",
        "انصب خيمة", "Insib khayma", "Arma tienda", "AHR-mah TYEHN-dah",
        "Monte tente", "Mohnt tahnt", "Bau Zelt", "BOW tselt",
        "Monta tenda", "MOHN-tah TEHN-dah", "Monte barraca", "MOHN-chee bah-HAH-kah",
        "Ставь палатку", "STAHV pah-LAHT-koo", "Çadırı kur", "Chah-duh-ruh koor",
        "Pasang tenda", "Pah-sahng tehn-dah", "搭 帐篷", "Dā zhàngpéng",
        "テント 張る", "Tento haru", "텐트 쳐", "Tenteu chyeo"
    ),
    item(
        "Roast treat", "بھون کر کھاؤ", "Bhoon kar khao", "भून कर खाओ", "Bhoon kar khao",
        "اشو حلوى", "Ishwi halwa", "Asa dulce", "AH-sah DOOL-seh",
        "Grille guimauve", "Gree-yuh gee-mohv", "Röste Marshmallow", "RERS-teh marsh-MEHL-loh",
        "Arrostisci dolce", "Ahr-rohs-TEE-shee DOHL-cheh", "Asse doce", "AH-see DOH-see",
        "Жарь зефир", "ZHAHR zyeh-FEER", "Ateşte tatlı pişir", "Ah-tesh-teh taht-luh pee-sheer",
        "Panggang makanan", "Pahng-gahng mah-kah-nahn", "烤 甜点", "Kǎo tiándiǎn",
        "マシュマロ 焼く", "Mashumaro yaku", "마시멜로 구워", "Masimello guwo"
    ),
    item(
        "Spot star", "ستارے دیکھو", "Sitaare dekho", "तारे देखो", "Taare dekho",
        "تأمل النجوم", "Ta'ammal an-nujum", "Mira estrellas", "MEE-rah ehs-TREH-yahs",
        "Regarde étoiles", "Ruh-gahrd ay-twahl", "Zähl Sterne", "TSAYL SHTEHR-neh",
        "Osserva stelle", "Ohs-SEHR-vah STEHL-leh", "Conte estrelas", "KOHN-chee ehs-TREH-lahs",
        "Считай звёзды", "Schee-TYE ZVYOHZ-dy", "Yıldızları say", "Yuhl-duhz-lah-ruh sigh",
        "Pandang bintang", "Pahn-dahng been-tahng", "数 星星", "Shǔ xīngxīng",
        "星 見上げる", "Hoshi miageru", "별을 세어봐", "Byeoreul seeobwa"
    )
]

# 43. saying-thank-you
w1["saying-thank-you"] = [
    item(
        "Warm heart", "ممنون دل", "Mamnoon dil", "कृतज्ञ दिल", "Kritagya dil",
        "قلب ممتن", "Qalb mumtann", "Corazón agradecido", "Koh-rah-SOHN ah-grah-deh-SEE-doh",
        "Cœur reconnaissant", "Kuhr ruh-koh-neh-sahn", "Dankbares Herz", "DAHNK-bah-res herts",
        "Cuore grato", "KWAW-reh GRAH-toh", "Coração grato", "Koh-rah-SOWN GRAH-too",
        "Благодарное сердце", "Blah-gah-DAHR-nah-yeh SYEHRD-tseh", "Minnettar gönül", "Meen-neht-tahr ger-newl",
        "Hati bersyukur", "Hah-tee behr-shoo-koor", "真 感恩", "Zhēn gǎn'ēn",
        "感謝の 心", "Kansha no kokoro", "고마운 마음", "Gomaun maeum"
    ),
    item(
        "Sweet gift", "پیارا تحفہ", "Pyaara tohfa", "प्यारा उपहार", "Pyaara upahaar",
        "هدية جميلة", "Hadiyya jamila", "Lindo regalo", "LEEN-doh reh-GAH-loh",
        "Joli cadeau", "Zhoh-lee kah-doh", "Schönes Geschenk", "SHER-nes geh-SHENK",
        "Bel regalo", "BEHL reh-GAH-loh", "Lindo presente", "LEEN-doo preh-ZEHN-chee",
        "Приятный подарок", "Pree-YAHT-nyy pah-DAH-rahk", "Güzel hediye", "Gew-zel heh-dee-yeh",
        "Hadiah manis", "Hah-dee-ah mah-nees", "美 礼物", "Měi lǐwù",
        "素敵な 贈り物", "Sutekina okurimono", "예쁜 선물", "Yeppeun seonmul"
    ),
    item(
        "Kind act", "اچھا کام", "Achha kaam", "नेक काम", "Nek kaam",
        "صنيع طيب", "Sani' tayyib", "Gesto generoso", "HEHS-toh heh-neh-ROH-soh",
        "Geste gentil", "Zhehst zhan-tee", "Liebe Geste", "LEE-beh GEHS-teh",
        "Bel gesto", "BEHL JEHS-toh", "Boa ação", "BOH-ah ah-SOWN",
        "Доброе дело", "DOHB-rah-yeh DYEH-lah", "Güzel iyilik", "Gew-zel ee-yee-leek",
        "Kebaikan tulus", "Keh-by-ee-kahn too-loos", "善 举动", "Shàn jǔdòng",
        "親切な 行い", "Shinsetsu na okonai", "착한 행동", "Chak-han haengdong"
    )
]

w2["saying-thank-you"] = [
    item(
        "Say thanks", "شکریہ بولو", "Shukriya bolo", "धन्यवाद बोलो", "Dhanyavaad bolo",
        "قل شكراً", "Qul shukran", "Di gracias", "DEE GRAH-syahs",
        "Dis merci", "Dee mehr-see", "Sag Danke", "ZAHK DAHN-keh",
        "Dì grazie", "DEE GRAHT-tsyeh", "Diga obrigado", "JEE-gah oh-bree-GAH-doo",
        "Скажи спасибо", "Skah-ZHY spah-SEE-bah", "Teşekkür et", "Teh-shehk-kewr et",
        "Ucap terimakasih", "Oo-chahp teh-ree-mah-kah-seeh", "说 谢谢", "Shuō xièxie",
        "お礼 言う", "Orei iu", "고맙다고 말해", "Gomapdago malhae"
    ),
    item(
        "Smile back", "مسکرا دو", "Muskura do", "मुस्कुरा दो", "Muskura do",
        "رد بابتسامة", "Rudd bi-btisama", "Sonríe alegre", "Sohn-REE-eh ah-LEH-greh",
        "Souris aussi", "Soo-ree oh-see", "Lächle zurück", "LEKH-leh tsoo-ROOK",
        "Sorridi lieto", "Sohr-REE-dee LYEH-toh", "Sorria de volta", "Sohr-HEE-ah jee VAWL-tah",
        "Улыбнись в ответ", "Oo-lyb-NEES v aht-VYEHT", "Gülümsemeyle karşılık", "Gew-lewm-seh-mey-leh kahr-shuh-luhk",
        "Balas tersenyum", "Bah-lahs tehr-sehn-yoom", "微笑 回礼", "Wēixiào huílǐ",
        "にっこり 笑い返す", "Nikkori waraikaesu", "미소로 화답해", "Misoro hwadaphae"
    ),
    item(
        "Give hug", "گلے لگاؤ", "Galay lagao", "गले लगाओ", "Gale lagaao",
        "قدم عناقاً", "Qaddim 'inaqan", "Dale abrazo", "DAH-leh ah-BRAH-zoh",
        "Fais câlin", "Feh kah-lan", "Umarme fest", "Oom-AHR-meh fehst",
        "Abbraccia forte", "Ahb-BRAHT-chah FOHR-teh", "Dê um abraço", "DAY oong ah-BRAH-soo",
        "Обними крепко", "Ahb-nee-MEE KRYEHP-kah", "Kucakla sevgiyle", "Koo-jahk-lah sehv-gee-leh",
        "Beri pelukan", "Beh-ree peh-look-ahn", "送 拥抱", "Sòng yǒngbào",
        "ぎゅっと 抱きつく", "Gyutto dakitsuku", "꼭 안아줘", "Kkok anajwo"
    )
]

# 44. saying-sorry
w1["saying-sorry"] = [
    item(
        "Sad mistake", "نادانستہ غلطی", "Nadaanista ghalti", "अनजानी भूल", "Anjaani bhool",
        "خطأ غير مقصود", "Khata' ghayr maqsud", "Error involuntario", "Ehr-ROHR een-voh-loon-TAH-ryoh",
        "Simple maladresse", "Sam-pluh mah-lah-drehs", "Kleines Versehen", "KLY-nes fehr-ZAY-en",
        "Piccolo sbaglio", "PEEK-koh-loh ZBAH-lyoh", "Pequeno descuido", "Peh-KAY-noo dehs-KWEE-doo",
        "Случайная ошибка", "Sloo-CHY-nah-yah ah-SHEEB-kah", "İstemeden olan hata", "Ees-teh-meh-dehn oh-lahn hah-tah",
        "Ketidaksengajaan", "Keh-tee-dahk-sehng-ah-jah-ahn", "不 小心", "Bù xiǎoxīn",
        "うっかり ミス", "Ukkari misu", "실수였어", "Silsuyeosseo"
    ),
    item(
        "True regret", "سچی پشیمانی", "Sachhi pashemaani", "सच्चा पछतावा", "Sachha pachhtaawa",
        "أسف صادق", "Asaf sadiq", "Disculpa sincera", "Dees-KOOL-pah seen-SEH-rah",
        "Vrai regret", "Vreh ruh-greh", "Aufrichtige Reue", "OWF-rikh-tee-geh ROY-eh",
        "Pentimento sincero", "Pen-tee-MEHN-toh seen-CHEH-roh", "Arrependimento sincero", "Ah-heh-pen-jee-MEHN-too seen-SEH-roo",
        "Искреннее раскаяние", "EES-kryen-nyeh-yeh rahs-KAH-yah-nyee-yeh", "İçten pişmanlık", "Eech-tehn peesh-mahn-luhk",
        "Penyesalan tulus", "Peh-nyeh-sah-lahn too-loos", "真 歉意", "Zhēn qiànyì",
        "心からの 反省", "Kokorokara no hansei", "진심어린 사과", "Jinsimeorin sagwa"
    ),
    item(
        "Kind peace", "پیار بھری صلح", "Pyaar bhari sulah", "सद्भावना", "Sadbhaawana",
        "سلام ومودة", "Salam wa-mawadda", "Paz amistosa", "PAHS ah-mees-TOH-sah",
        "Douce paix", "Doos peh", "Gute Versöhnung", "GOO-teh fehr-ZERN-oong",
        "Pace ritrovata", "PAH-cheh ree-troh-VAH-tah", "Paz restaurada", "PAHS hehs-tow-RAH-dah",
        "Добрый мир", "DOHB-ryy meer", "Tatlı barış", "Taht-luh bah-ruhsh",
        "Damai kembali", "Dah-mye kehm-bah-lee", "言 归于好", "Yán guīyúhǎo",
        "仲直りの 握手", "Nakanaori no akushu", "다정한 화해", "Dajeong-han hwahae"
    )
]

w2["saying-sorry"] = [
    item(
        "Say sorry", "معافی مانگو", "Maafi maango", "माफ़ी माँगो", "Maafi maango",
        "اعتذر بصدق", "I'tadhir bi-sidq", "Pide disculpas", "PEE-deh dees-KOOL-pahs",
        "Dis pardon", "Dee pahr-dohn", "Sag Entschuldigung", "ZAHK ent-SHOOL-dee-goong",
        "Chiedi scusa", "KYEH-dee SKOO-zah", "Peça desculpas", "PEH-sah dehs-KOOL-pahs",
        "Попроси прощения", "Pah-prah-SEE prah-SHCHYEH-nyee-yah", "Özür dile", "Er-zewr dee-leh",
        "Minta maaf", "Meen-tah mah-ahf", "说 对不起", "Shuō duìbuqǐ",
        "「ごめんね」と言う", "Gomenne to iu", "미안하다고 해", "Mianhadago hae"
    ),
    item(
        "Fix mistake", "غلطی سدھارو", "Ghalti sudhaaro", "ग़लती सुधारो", "Galti sudhaaro",
        "أصلح الخطأ", "Aslih al-khata'", "Arregla error", "Ah-RREH-glah ehr-ROHR",
        "Répare bêtise", "Ray-pahr beh-teez", "Mach's gut", "MAHKHS goot",
        "Rimedia subito", "Ree-MEH-dyah SOO-bee-toh", "Corrija erro", "Koh-HEE-zhah EHR-roo",
        "Исправь всё", "Ees-PRAHF fsyoh", "Hatayı düzelt", "Hah-tah-yuh dew-zelt",
        "Perbaiki kesalahan", "Pehr-bye-kee keh-sah-lah-hahn", "改 正错误", "Gǎi zhèngcuòwù",
        "きちんと 直す", "Kichinto naosu", "실수를 바로잡아", "Silsureul barojaba"
    ),
    item(
        "Make peace", "دوستی کرو", "Dosti karo", "दोस्ती कर लो", "Dosti kar lo",
        "تصالح سريعاً", "Tasalah sari'an", "Haz las paces", "AHS lahs PAH-sehs",
        "Fais la paix", "Feh lah peh", "Vertragt euch", "Fehr-TRAHKT oysh",
        "Fai la pace", "FYE lah PAH-cheh", "Faça as pazes", "FAH-sah ahs PAH-zees",
        "Помиритесь дружно", "Pah-mee-REE-tyes DROOZH-nah", "Hemen barış", "Heh-men bah-ruhsh",
        "Berdamai lagi", "Behr-dah-mye lah-gee", "重新 和好", "Chóngxīn héhǎo",
        "また 仲直りする", "Mata nakanaori-suru", "다시 화해해", "Dasi hwahaehae"
    )
]

# 45. asking-for-help
w1["asking-for-help"] = [
    item(
        "Heavy box", "بھاری ڈبہ", "Bhaari dabba", "भारी डिब्बा", "Bhaari dibba",
        "صندوق ثقيل", "Sunduk thaqil", "Caja pesada", "KAH-hah peh-SAH-dah",
        "Boîte lourde", "Bwaht loord", "Schwere Kiste", "SHVAY-reh KIS-teh",
        "Scatola pesante", "SKAH-toh-lah peh-ZAHN-teh", "Caixa pesada", "KYE-shah peh-ZAH-dah",
        "Тяжёлая коробка", "Tyah-ZHOH-lah-yah kah-ROHP-kah", "Ağır kutu", "Ah-uhr koo-too",
        "Kotak berat", "Koh-tahk beh-raht", "沉 箱子", "Chén xiāngzi",
        "重い 箱", "Omoi hako", "무거운 상자", "Mugeoun sangja"
    ),
    item(
        "Kind helper", "مہربان مددگار", "Meherbaan madadgaar", "दयालु मददगार", "Dayaalu madadgaar",
        "مساعد لطيف", "Musa'id latif", "Persona amable", "Pehr-SOH-nah ah-MAH-bleh",
        "Aide bienveillante", "Ehd byan-vay-yahnt", "Hilfsbereiter Mensch", "HILFS-beh-rye-ter mensh",
        "Persona gentile", "Pehr-SOH-nah jehn-TEE-leh", "Ajudante bom", "Ah-zhoo-DAHN-chee bohn",
        "Добрый помощник", "DOHB-ryy pah-MOHSHCH-neek", "Yardımsever kişi", "Yahr-duhm-seh-vehr kee-shee",
        "Penolong ramah", "Peh-noh-lohng rah-mah", "好 帮手", "Hǎo bāngshou",
        "親切な お手伝い", "Shinsetsu na otetsudai", "친절한 도우미", "Chinjeol-han doumi"
    ),
    item(
        "High shelf", "اونچا طاق", "Ooncha taaq", "ऊँची शेल्फ", "Oonchi shelf",
        "رف عال", "Raff 'alin", "Estante alto", "Ehs-TAHN-teh AHL-toh",
        "Haute étagère", "Oht ay-tah-zhehr", "Hohes Regal", "HOH-hes reh-GAHL",
        "Scaffale alto", "Skahf-FAH-leh AHL-toh", "Prateleira alta", "Prah-teh-LAY-rah AHL-tah",
        "Высокая полка", "Vy-SOH-kah-yah POHL-kah", "Yüksek raf", "Yewk-sek rahf",
        "Rak tinggi", "Rahk teeng-gee", "高 书架", "Gāo shūjià",
        "高い 棚", "Takai tana", "높은 선반", "Nopeun seonban"
    )
]

w2["asking-for-help"] = [
    item(
        "Ask nicely", "ادب سے کہو", "Adab se kaho", "आदर से कहो", "Aadar se kaho",
        "اطلب بأدب", "Itlub bi-adab", "Pide con educación", "PEE-deh kohn eh-doo-kah-SYOHN",
        "Demande poliment", "Duh-mahnd poh-lee-mahn", "Frag höflich", "FRAHK HERF-likh",
        "Chiedi cortesemente", "KYEH-dee kohr-teh-seh-MEHN-teh", "Peça educado", "PEH-sah eh-doo-KAH-doo",
        "Вежливо попроси", "VYEHZH-lee-vah pah-prah-SEE", "Kibarca iste", "Kee-bahr-jah ees-teh",
        "Minta dengan santun", "Meen-tah deh-ngahn sahn-toon", "客气 请教", "Kèqi qǐngjiào",
        "丁寧に 頼む", "Teineini tanomu", "정중하게 부탁해", "Jeongjunghage butakhae"
    ),
    item(
        "Point shelf", "شیلف کی طرف اشارہ", "Shelf ki taraf ishaara", "ऊपर इशारा करो", "Oopar ishaara karo",
        "أشر للرف", "Ashir lir-raff", "Señala arriba", "Seh-NYAH-lah ah-RREE-bah",
        "Montre en haut", "Mohn-truh ahn oh", "Zeig nach oben", "TSYGH nahkh OH-ben",
        "Indica in alto", "Een-DEE-kah een AHL-toh", "Aponte prateleira", "Ah-POHN-chee prah-teh-LAY-rah",
        "Покажи наверх", "Pah-kah-ZHY nah-VYEHRKH", "Yukarıyı göster", "Yoo-kah-ruh-yuh gerz-tehr",
        "Tunjuk ke atas", "Toon-jook keh ah-tahs", "指 高处", "Zhǐ gāochù",
        "棚を 指差す", "Tana o yubisasu", "선반 가리켜", "Seonban garikyeo"
    ),
    item(
        "Say thanks", "شکریہ ادا کرو", "Shukriya ada karo", "धन्यवाद कहो", "Dhanyavaad kaho",
        "اشكر المساعد", "Ushkur al-musa'id", "Agradece apoyo", "Ah-grah-DEH-seh ah-POH-yoh",
        "Remercie bien", "Ruh-mehr-see byan", "Bedank dich", "Beh-DAHNK dikh",
        "Ringrazia subito", "Reen-GRAHT-tsyah SOO-bee-toh", "Agradeça ajuda", "Ah-grah-DEH-sah ah-ZHOO-dah",
        "Поблагодари искренне", "Pah-blah-gah-dah-REE EES-kryen-nyeh", "Teşekkürlerini sun", "Teh-shehk-kewr-leh-ree-nee soon",
        "Katakan terimakasih", "Kah-tah-kahn teh-ree-mah-kah-seeh", "连声道谢", "Liánshēng dàoxiè",
        "お礼を 伝える", "Orei o tsutaeru", "고맙다고 인사해", "Gomapdago insahae"
    )
]

# 46. lost-in-public
w1["lost-in-public"] = [
    item(
        "Safe place", "محفوظ جگہ", "Mehfooz jagah", "सुरक्षित जगह", "Surakshit jagah",
        "مكان آمن", "Makan amin", "Lugar seguro", "Loo-GAHR seh-GOO-roh",
        "Lieu sûr", "Lyuh soor", "Sicherer Ort", "ZIKH-er-er ohrt",
        "Posto sicuro", "POHS-toh see-KOO-roh", "Lugar seguro", "Loo-GAHR seh-GOO-roo",
        "Безопасное место", "Bye-zah-PAHS-nah-yeh MYEHS-tah", "Güvenli yer", "Gew-vehn-lee yehr",
        "Tempat aman", "Tehm-paht ah-mahn", "安 地点", "Ān dìdiǎn",
        "安全な 場所", "Anzenna basho", "안전한 장소", "Anjeon-han jangso"
    ),
    item(
        "Kind guard", "محافظ گارڈ", "Muhaafiz guard", "सुरक्षा गार्ड", "Suraksha guard",
        "حارس أمين", "Haris amin", "Guardia de seguridad", "GWAHR-dyah deh seh-goo-ree-DAHD",
        "Agent rassurant", "Ah-zhahn rah-soo-rahn", "Freundlicher Wächter", "FROYNT-likh-er VEKH-ter",
        "Guardia gentile", "GWAHR-dyah jehn-TEE-leh", "Segurança prestativo", "Seh-goo-RAHN-sah preh-stah-CHEE-voo",
        "Охранник в форме", "Ahkh-RAHN-neek v FOHR-myeh", "Güvenlik görevlisi", "Gew-vehn-leek ger-rev-lee-see",
        "Petugas keamanan", "Peh-too-gahs keh-ah-mah-nahn", "敬 保安", "Jìng bǎo'ān",
        "警備員さん", "Keibiinsan", "보안관 아저씨", "Boangwan ajeossi"
    ),
    item(
        "Calm mind", "پرسکون دل", "Pursukoon dil", "शांत मन", "Shaant mann",
        "قلب مطمئن", "Qalb mutma'inn", "Ánimo sereno", "AH-nee-moh seh-REH-noh",
        "Cœur calme", "Kuhr kahlm", "Ruhiger Mut", "ROO-hee-ger moot",
        "Mente lucida", "MEHN-teh LOO-chee-dah", "Mente calma", "MEHN-chee KAHL-mah",
        "Спокойные мысли", "Spah-KOY-ny-yeh MYS-lee", "Sakin duruş", "Sah-keen doo-roosh",
        "Kepala dingin", "Keh-pah-lah deeng-een", "镇 心神", "Zhèn xīnshén",
        "落ち着いた 気持ち", "Ochitsuita kimochi", "침착한 마음", "Chimchak-han maeum"
    )
]

w2["lost-in-public"] = [
    item(
        "Stay still", "وہیں رکو", "Waheen ruko", "वहीं रुको", "Waheen ruko",
        "ابق مكانك", "Ibqa makanak", "Quédate quieto", "KEH-dah-teh KYEH-toh",
        "Reste sur place", "Rehst soor plahs", "Bleib stehen", "BLYP SHTAY-en",
        "Fermati lì", "FEHR-mah-tee lee", "Fique parado", "FEE-kee pah-RAH-doo",
        "Стой на месте", "STOY nah MYEHS-tyeh", "Olduğun yerde dur", "Ohl-doo-oon yehr-deh door",
        "Tetap diam di tempat", "Teh-tahp dee-ahm dee tehm-paht", "原地 站好", "Yuándì zhànhǎo",
        "その場に とどまる", "Sonoba ni todomaru", "그자리에 멈춰", "Geujarie meomchwo"
    ),
    item(
        "Find officer", "گارڈ کو ڈھونڈو", "Guard ko dhoondo", "गार्ड को ढूँढो", "Guard ko dhoondho",
        "ابحث عن حارس", "Ibhath 'an haris", "Busca policía", "BOOS-kah poh-lee-SEE-ah",
        "Cherche agent", "Shehrsh ah-zhahn", "Such Aufsicht", "ZOOKH OWF-zikht",
        "Cerca sorvegliante", "CHEHR-kah sohr-vehl-YAHN-teh", "Procure guarda", "Proh-KOO-ree GWAHR-dah",
        "Найди охранника", "Nye-DEE ahkh-RAHN-nee-kah", "Görevliyi bul", "Ger-rev-lee-yee bool",
        "Cari petugas", "Chah-ree peh-too-gahs", "找 工作人员", "Zhǎo gōngzuò rényuán",
        "店員さんに 声かける", "Ten'insan ni koekakeru", "안내원 찾아", "Annaewon chaja"
    ),
    item(
        "Tell name", "نام بتاؤ", "Naam batao", "नाम बताओ", "Naam bataao",
        "اذكر اسمك", "Idhkur ismak", "Di tu nombre", "DEE too NOHM-breh",
        "Donne identité", "Dohn ee-dahn-tee-tay", "Nenn Namen", "NEN NAH-men",
        "Dì come ti chiami", "DEE KOH-meh tee KYAH-mee", "Diga seu nome", "JEE-gah say-oo NAW-mee",
        "Назови фамилию", "Nah-zah-VEE fah-MEE-lee-yoo", "İsmini söyle", "Ees-mee-nee seri-leh",
        "Sebut nama lengkap", "Seh-boot nah-mah lehng-kahp", "说明 名字", "Shuōmíng míngzi",
        "名前と 番号言う", "Namae to bangō iu", "이름과 연락처 말해", "Ireumgwa yeollakcheo malhae"
    )
]

# 47. polite-requests
w1["polite-requests"] = [
    item(
        "Sweet tone", "شیریں لہجہ", "Sheereen lehja", "मीठा स्वर", "Meetha swar",
        "نبرة لطيفة", "Nabra latifa", "Tono dulce", "TOH-noh DOOL-seh",
        "Ton aimable", "Tohn ay-mahbl", "Freundlicher Ton", "FROYNT-likh-er tohn",
        "Tono gentile", "TOH-noh jehn-TEE-leh", "Tom meigo", "TOHNG MAY-goo",
        "Мягкий тон", "MYAHK-kiy tohn", "Tatlı ses tonu", "Taht-luh sehs toh-noo",
        "Nada santun", "Nah-dah sahn-toon", "温 语调", "Wēn yǔdiào",
        "柔らかな 口調", "Yawarakana kuchō", "부드러운 말투", "Budeureoun maltu"
    ),
    item(
        "Warm smile", "پیاری مسکراہٹ", "Pyaari muskurahat", "प्यारी मुस्कान", "Pyaari muskaan",
        "ابتسامة دافئة", "Ibtisama dafi'a", "Sonrisa cálida", "Sohn-REE-sah KAH-lee-dah",
        "Sourire doux", "Soo-reer doo", "Herzliches Lächeln", "HEHRTS-likh-es LEKH-eln",
        "Sorriso solare", "Sohr-REE-zoh soh-LAH-reh", "Sorriso acolhedor", "Sohr-HEE-zoo ah-kohl-yeh-DOHR",
        "Тёплая улыбка", "TYOHP-lah-yah oo-LYP-kah", "İçten gülüş", "Eech-tehn gew-lewsh",
        "Senyum manis", "Sehn-yoom mah-nees", "亲 笑容", "Qīn xiàoróng",
        "温かい 微笑み", "Atatakai hohoemi", "상냥한 미소", "Sangnyang-han miso"
    ),
    item(
        "Gentle wish", "نیک خواہش", "Nek khwahish", "सुंदर चाहत", "Sundar chaahat",
        "رجاء رقيق", "Raja' raqiq", "Petición cordial", "Peh-tee-SYOHN kohr-DYAHL",
        "Souhait poli", "Soo-ay poh-lee", "Höflicher Wunsch", "HERF-likh-er voonsh",
        "Desiderio espresso", "Deh-zee-DEH-ryoh ehs-PREHS-soh", "Pedido gentil", "Peh-JEE-doo zheng-TEEL",
        "Вежливая просьба", "VYEHZH-lee-vah-yah PROHS-bah", "Nazik rica", "Nah-zeek ree-jah",
        "Permintaan sopan", "Pehr-meen-tah-ahn soh-pahn", "礼 请求", "Lǐ qǐngqiú",
        "控えめな お願い", "Hikaemena onegai", "공손한 부탁", "Gongson-han butak"
    )
]

w2["polite-requests"] = [
    item(
        "Ask nicely", "ادب سے مانگو", "Adab se maango", "विनम्रता से माँगो", "Vinamrata se maango",
        "اطلب بلطف", "Itlub bi-lutf", "Pide por favor", "PEE-deh pohr fah-VOHR",
        "Demande poliment", "Duh-mahnd poh-lee-mahn", "Bitte höflich", "BIT-teh HERF-likh",
        "Chiedi per favore", "KYEH-dee pehr fah-VOH-reh", "Peça com licença", "PEH-sah kohn lee-SEHN-sah",
        "Попроси пожалуйста", "Pah-prah-SEE pah-ZHAH-loo-stah", "Lütfen rica et", "Lewt-fen ree-jah et",
        "Mintalah baik-baik", "Meen-tah-lah by-eek by-eek", "礼貌 请问", "Lǐmào qǐngwèn",
        "「お願いします」と頼む", "Onegaishimasu to tanomu", "부탁한다고 전해", "Butak-handago jeonhae"
    ),
    item(
        "Wait turn", "باری کا انتظار کرو", "Baari ka intezaar karo", "बारी का इंतज़ार करो", "Baari ka intezaar karo",
        "انتظر دورك", "Intadhir dawrak", "Espera turno", "Ehs-PEH-rah TOOR-noh",
        "Patiente sagement", "Pah-syahnt sahzh-mahn", "Warte geduldig", "VAHR-teh geh-DOOL-dikh",
        "Aspetta con calma", "Ahs-PEHT-tah kohn KAHL-mah", "Aguarde sua vez", "Ah-GWAHR-jee SOO-ah vez",
        "Жди очереди", "ZHDEE OH-cheh-ryeh-dee", "Sıranı sabırla bekle", "Suh-rah-nuh sah-buhr-lah behk-leh",
        "Tunggu giliran", "Toon-goo gee-lee-rahn", "耐心 等待", "Nàixīn děngdài",
        "順番を 待つ", "Junban o matsu", "차례를 기다려", "Charyereul gidaryeo"
    ),
    item(
        "Say thanks", "شکریہ کہو", "Shukriya kaho", "धन्यवाद कहो", "Dhanyavaad kaho",
        "اشكر دائماً", "Ushkur da'iman", "Agradece con sonrisa", "Ah-grah-DEH-seh kohn sohn-REE-sah",
        "Dis grand merci", "Dee grahn mehr-see", "Sag Dankeschön", "ZAHK DAHN-keh-shern",
        "Ringrazia di cuore", "Reen-GRAHT-tsyah dee KWAW-reh", "Diga muito obrigado", "JEE-gah MOON-too oh-bree-GAH-doo",
        "Отблагодари искренне", "Aht-blah-gah-dah-REE EES-kryen-nyeh", "Teşekkürünü ilet", "Teh-shehk-kewr-ew-new ee-let",
        "Ucap banyak terimakasih", "Oo-chahp bahn-yahk teh-ree-mah-kah-seeh", "真诚 致谢", "Zhēnchéng zhìxiè",
        "心から 感謝する", "Kokorokara kansha-suru", "진심으로 감사해", "Jinsimeuro gamsahae"
    )
]

output_path = os.path.join(os.path.dirname(__file__), "..", "src", "data", "multilingual", "cat3_friends_nature_manners.ts")
export_ts_module(output_path, "CAT3_W1", "CAT3_W2", w1, w2)
