# Category 4: Fun & Tech (5), Time & Weather (5), Holidays & Events (5) = 15 topics
import os
import sys
sys.path.append(os.path.dirname(__file__))
from helper import item, export_ts_module

w1 = {}
w2 = {}

# 48. video-games
w1["video-games"] = [
    item(
        "Fun game", "مزیدار کھیل", "Mazedar khel", "मज़ेदार गेम", "Mazedaar game",
        "لعبة فيديو ممتعة", "Lu'ba fidyu mumti'a", "Juego divertido", "HWEH-goh dee-vehr-TEE-doh",
        "Jeu vidéo captivant", "Zhuh vee-day-oh kahp-tee-vahn", "Tolles Videospiel", "TOL-les VEE-day-oh-shpeel",
        "Videogioco divertente", "VEE-deh-oh-joh-koh dee-vehr-TEHN-teh", "Jogo legal", "ZHOH-goo leh-GAHL",
        "Увлекательная игра", "Oov-lyeh-KAH-tyel-nah-yah eeg-RAH", "Eğlenceli oyun", "Eh-lehn-jeh-lee oh-yoon",
        "Permainan seru", "Pehr-mye-nahn seh-roo", "趣 游戏", "Qù yóuxì",
        "楽しい ゲーム", "Tanoshii gēmu", "신나는 게임", "Sinnaneun geim"
    ),
    item(
        "High score", "شاندار اسکور", "Shaandaar score", "बड़ा स्कोर", "Bada score",
        "نقاط عالية", "Nuqat 'aliya", "Puntuación alta", "Poon-twah-SYOHN AHL-tah",
        "Meilleur score", "May-yuhr skohr", "Hoher Rekord", "HOH-her reh-KORT",
        "Punteggio alto", "Poon-TEHD-joh AHL-toh", "Pontuação alta", "Pohn-twah-SOWN AHL-tah",
        "Высокий счёт", "Vy-SOH-kiy shchoht", "Yüksek puan", "Yewk-sek poo-ahn",
        "Skor tertinggi", "Skohr tehr-teeng-gee", "高 得分", "Gāo défēn",
        "ハイスコア", "Haisukoa", "최고 점수", "Choego jeomsu"
    ),
    item(
        "Bright screen", "روشن اسکرین", "Roshan screen", "चमकीली स्क्रीन", "Chamkeeli screen",
        "شاشة ملونة", "Shasha mulawwana", "Pantalla brillante", "Pahn-TAH-yah bree-YAHN-teh",
        "Écran net", "Ay-krahn neht", "Klarer Bildschirm", "KLAH-rer BILT-sheerm",
        "Schermo luminoso", "SKEHR-moh loo-mee-NOH-zoh", "Tela colorida", "TAY-lah koh-loh-REE-dah",
        "Яркий экран", "YAHR-kiy ehk-RAHN", "Parlak ekran", "Pahr-lahk ek-rahn",
        "Layar jernih", "Lah-yahr jehr-neeh", "清 屏幕", "Qīng píngmù",
        "明るい 画面", "Akarui gamen", "선명한 화면", "Seonmyeong-han hwamyeon"
    )
]

w2["video-games"] = [
    item(
        "Press button", "بٹن دباؤ", "Button dabao", "बटन दबाओ", "Button dabaao",
        "اضغط زراً", "Idghat zirran", "Pulsa botón", "POOL-sah boh-TOHN",
        "Appuie bouton", "Ah-pwee boo-tohn", "Drück Knopf", "DROOK knohpf",
        "Premi tasto", "PREH-mee TAHS-toh", "Aperte botão", "Ah-PEHR-chee boh-TOWN",
        "Нажми кнопку", "Nahzh-MEE KNOHP-koo", "Tuşa bas", "Too-shah bahs",
        "Tekan tombol", "Teh-kahn tohm-bohl", "按 按钮", "Àn ànniǔ",
        "ボタン 押す", "Botan osu", "버튼 눌러", "Beoteun nulleo"
    ),
    item(
        "Jump obstacle", "چھلانگ لگاؤ", "Chhlaang lagao", "कूद लगाओ", "Kood lagaao",
        "اقفز للأعلى", "Iqfiz lil-a'la", "Salta obstáculo", "SAHL-tah ohbs-TAH-koo-loh",
        "Saute bien", "Soht byan", "Spring drüber", "SHPRING DREW-ber",
        "Salta sopra", "SAHL-tah SOH-prah", "Pule obstáculo", "POO-lee ohbs-TAH-koo-loo",
        "Перепрыгни препятствие", "Pyeh-ryeh-PRYG-nee pryeh-PYAHT-stvee-yeh", "Engel üstünden atla", "Ehn-gehl ews-tewn-dehn aht-lah",
        "Lompati rintangan", "Lohm-pah-tee reen-tahng-ahn", "跳 障碍", "Tiào zhàng'ài",
        "障害物 飛び越える", "Shōgaibutsu tobikoeru", "장애물 뛰어넘어", "Jang-aemul ttwieoneomeo"
    ),
    item(
        "Take break", "وقفہ لو", "Waqfa lo", "विराम लो", "Viraam lo",
        "خذ استراحة", "Khudh istiraha", "Toma descanso", "TOH-mah dehs-KAHN-soh",
        "Fais pause", "Feh pohz", "Mach Pause", "MAHKH POW-zeh",
        "Fai pausa", "FYE POW-zah", "Faça pausa", "FAH-sah POW-zah",
        "Сделай перерыв", "SDYEH-lye pyeh-ryeh-RYF", "Mola ver", "Moh-lah vehr",
        "Istirahatlah sebentar", "Ees-tee-rah-haht-lah seh-behn-tahr", "休 息下", "Xiūxixia",
        "休憩 する", "Kyūkei suru", "잠깐 쉬어", "Jamkkan swieo"
    )
]

# 49. cartoon-talk
w1["cartoon-talk"] = [
    item(
        "Funny clown", "مضحکہ خیز مسخرا", "Muzhaka khez maskhara", "मज़ेदार जोकर", "Mazedaar joker",
        "مهرج مضحك", "Muharrij mudhik", "Payaso gracioso", "Pah-YAH-soh grah-SYOH-soh",
        "Clown drôle", "Klahn drohl", "Lustiger Clown", "LOOS-tee-ger klown",
        "Pagliaccio buffo", "Pah-LYAHT-choh BOOF-foh", "Palhaço engraçado", "Pahl-YAH-soo eng-grah-SAH-doo",
        "Смешной клоун", "Smyesh-NOY KLOH-oon", "Komik palyaço", "Koh-meek pahl-yah-choh",
        "Badut lucu", "Bah-doot loo-choo", "逗 小丑", "Dòu xiǎochǒu",
        "面白い ピエロ", "Omoshiroi piero", "웃긴 삐에로", "Utgin ppiero"
    ),
    item(
        "Cute hero", "پیارا ہیرو", "Pyaara hero", "प्यारा हीरो", "Pyaara hero",
        "بطل لطيف", "Batal latif", "Héroe simpático", "EH-roh-eh seem-PAH-tee-koh",
        "Héros attachant", "Ay-roh ah-tah-shahn", "Lieber Held", "LEE-ber helt",
        "Eroe simpatico", "Eh-ROH-eh seem-PAH-tee-koh", "Herói fofo", "Eh-RAW-ee FAW-foo",
        "Милый герой", "MEE-lyy gyeh-ROY", "Sevimli kahraman", "Seh-veem-lee kah-hrah-mahn",
        "Pahlawan imut", "Pah-lah-wahn ee-moot", "萌 英雄", "Méng yīngxióng",
        "可愛い ヒーロー", "Kawaii hīrō", "귀여운 영웅", "Gwiyeoun yeong-ung"
    ),
    item(
        "Bright colors", "چمکدار رنگ", "Chamakdaar rang", "चमकीले रंग", "Chamkeele rang",
        "ألوان زاهية", "Alwan zahiya", "Colores vivos", "Koh-LOH-rehs VEE-vohs",
        "Couleurs vives", "Koo-luhr veev", "Bunte Zeichnungen", "BOON-teh TSYKH-noong-en",
        "Colori allegri", "Koh-LOH-ree ahl-LEH-gree", "Cores vibrantes", "KAW-rees vee-BRAHN-chees",
        "Яркие краски", "YAHR-kee-yeh KRAHS-kee", "Canlı renkler", "Jahn-luh renk-lehr",
        "Warna-warni cerah", "Wahr-nah wahr-nee cheh-rah", "亮 画面", "Liàng huàmiàn",
        "鮮やかな 色使い", "Azayakana irozukai", "알록달록 색감", "Allokdallok saekgam"
    )
]

w2["cartoon-talk"] = [
    item(
        "Watch show", "کارٹون دیکھو", "Cartoon dekho", "कार्टून देखो", "Cartoon dekho",
        "شاهد كرتوناً", "Shahid kartunan", "Mira dibujos", "MEE-rah dee-BOO-hohs",
        "Regarde dessin animé", "Ruh-gahrd deh-san ah-nee-may", "Schau Zeichentrick", "SHOW TSY-khen-trik",
        "Guarda cartone", "GWAHR-dah kahr-TOH-neh", "Assista desenho", "Ah-SEES-tah deh-ZEN-yoo",
        "Смотри мультик", "Smah-TREE MOOL-teek", "Çizgi film izle", "Cheez-gee feelm eez-leh",
        "Tonton kartun", "Tohn-tohn kahr-toon", "看 动画", "Kàn dònghuà",
        "アニメ 見る", "Anime miru", "만화 시청해", "Manhwa sicheonghae"
    ),
    item(
        "Laugh loud", "کھلکھلا کر ہنسو", "Khilkhila kar hanso", "खुलकर हँसो", "Khulkar hanso",
        "اضحك بفرح", "Idhak bi-farah", "Ríe alegre", "REE-eh ah-LEH-greh",
        "Ris fort", "Ree fohr", "Lach laut", "LAHKH lowt",
        "Ridi forte", "REE-dee FOHR-teh", "Ria gostoso", "HEE-ah gohs-TOH-zoo",
        "Смейся весело", "SMYEY-syah VYEH-syeh-lah", "Kahkahayla gül", "Kahk-hah-hah-y-lah gewl",
        "Tertawa terbahak", "Tehr-tah-wah tehr-bah-hahk", "开 心笑", "Kāixīn xiào",
        "大声で 笑う", "Ōgoe de warau", "크게 웃어봐", "Keuge useobwa"
    ),
    item(
        "Tell story", "کہانی سناؤ", "Kahani sunao", "कहानी सुनाओ", "Kahaani sunaao",
        "احك حكاية", "Ihk hikaya", "Cuenta episodio", "KWEHN-tah eh-pee-SOH-dyoh",
        "Raconte épisode", "Rah-kohnt ay-pee-zohd", "Erzähl Handlung", "Ehr-TSAYL HAHNT-loong",
        "Racconta trama", "Rahk-KOHN-tah TRAH-mah", "Conte história", "KOHN-chee ees-TAW-ryah",
        "Перескажи сюжет", "Pyeh-ryeh-skah-ZHY syoo-ZHYEHT", "Bölümü anlat", "Ber-lew-mew ahn-laht",
        "Ceritakan ceritanya", "Cheh-ree-tah-kahn cheh-ree-tah-nyah", "讲 故事", "Jiǎng gùshi",
        "話を 教える", "Hanashi o oshieru", "줄거리 말해줘", "Julgeori malhaejwo"
    )
]

# 50. drawing-colors
w1["drawing-colors"] = [
    item(
        "Bright red", "شوخ لال", "Shokh laal", "चमकीला लाल", "Chamkeela laal",
        "أحمر ساطع", "Ahmar sati'", "Rojo brillante", "ROH-hoh bree-YAHN-teh",
        "Rouge vif", "Roozh veef", "Helles Rot", "HEL-les roht",
        "Rosso vivo", "ROHS-soh VEE-voh", "Vermelho vivo", "Vehr-MEHL-yoo VEE-voo",
        "Ярко-красный цвет", "YAHR-kah KRAHS-nyy tsvyet", "Canlı kırmızı", "Jahn-luh kuhr-muh-zuh",
        "Merah terang", "Meh-rah teh-rahng", "鲜 红色", "Xiān hóngsè",
        "鮮やかな 赤色", "Azayakana aka'iro", "선명한 빨강", "Seonmyeong-han ppalgang"
    ),
    item(
        "Deep blue", "گہرا نیلا", "Gehra neela", "गहरा नीला", "Gahara neela",
        "أزرق داكن", "Azraq dakin", "Azul marino", "Ah-SOOL mah-REE-noh",
        "Bleu profond", "Bluh proh-fohn", "Dunkles Blau", "DOON-kles blow",
        "Blu notte", "BLOO NOHT-teh", "Azul escuro", "Ah-ZOOL ehs-KOO-roo",
        "Тёмно-синий цвет", "TYOHM-nah SEE-nyy tsvyet", "Derin mavi", "Deh-reen mah-vee",
        "Biru pekat", "Bee-roo peh-kaht", "深 蓝色", "Shēn lánsè",
        "深みのある 青色", "Fukami no aru aoiro", "깊은 파랑", "Gipeun parang"
    ),
    item(
        "Sunny yellow", "دھوپ جیسا پیلا", "Dhoop jaisa peela", "उजला पीला", "Ujla peela",
        "أصفر مشمس", "Asfar mushmis", "Amarillo sol", "Ah-mah-REE-yoh sohl",
        "Jaune soleil", "Zhohn soh-lay", "Sonniges Gelb", "ZON-nee-ges gelp",
        "Giallo sole", "JAHL-loh SOH-leh", "Amarelo solar", "Ah-mah-REH-loo soh-LAHR",
        "Солнечно-жёлтый", "SOHL-neech-nah ZHOHL-tyy", "Güneş sarısı", "Gew-nesh sah-ruh-suh",
        "Kuning cerah", "Koo-neeng cheh-rah", "亮 黄色", "Liàng huángsè",
        "ひまわり色", "Himawari'iro", "따스한 노랑", "Ttaseuhan norang"
    )
]

w2["drawing-colors"] = [
    item(
        "Mix colors", "رنگ ملاؤ", "Rang milao", "रंग मिलाओ", "Rang milaao",
        "امزج الألوان", "Imzij al-alwan", "Mezcla colores", "MEHS-klah koh-LOH-rehs",
        "Mélange teintes", "May-lahnzh tant", "Misch Farben", "MISH FAHR-ben",
        "Mescola colori", "MEHS-koh-lah koh-LOH-ree", "Misture tintas", "Mees-TOO-ree CHEEN-tahs",
        "Смешай краски", "Smyey-SHY KRAHS-kee", "Renkleri karıştır", "Renk-leh-ree kah-ruhsh-tuhr",
        "Campur warna", "Chahm-poor wahr-nah", "调 颜色", "Tiáo yánsè",
        "絵の具を 混ぜる", "Enogu o mazeru", "색깔 섞어봐", "Saekkkal seokkeobwa"
    ),
    item(
        "Paint rainbow", "دھنک بناؤ", "Dhanak banao", "इंद्रधनुष बनाओ", "Indradhanush banaao",
        "ارسم قوس قزح", "Irsum qaws quzah", "Pinta arcoíris", "PEEN-tah ahr-koh-EE-rees",
        "Peins arc-en-ciel", "Pan ahr-kahn-syel", "Mal Regenbogen", "MAHL RAY-gen-boh-gen",
        "Dipingi arcobaleno", "Dee-PEEN-jee ahr-koh-bah-LEH-noh", "Pinte arco-íris", "PEEN-chee AHR-koo EE-rees",
        "Рисуй радугу", "Ree-SOOY RAH-doo-goo", "Gökkuşağı boya", "Gerk-koo-shah-uh boh-yah",
        "Lukis pelangi", "Loo-kees peh-lahng-gee", "画 彩虹", "Huà cǎihóng",
        "虹 描く", "Niji kaku", "무지개 칠해", "Mujigae chilhae"
    ),
    item(
        "Clean brush", "برش دھوؤ", "Brush dhoo", "ब्रश साफ़ करो", "Brush saaf karo",
        "اغسل الفرشاة", "Ighsil al-fursha", "Lava pincel", "LAH-vah peen-SEHL",
        "Nettoie pinceau", "Neh-twah pan-soh", "Wasch Pinsel", "VAHSH PIN-zel",
        "Pulisci pennello", "Poo-LEE-shee pen-NEHL-loh", "Lave pincel", "LAH-vee peen-SEHL",
        "Промой кисточку", "Prah-MOY KEES-tahch-koo", "Fırçayı yıka", "Fuhr-chah-yuh yuh-kah",
        "Cuci kuas", "Choo-chee koo-ahs", "洗 画笔", "Xǐ huàbǐ",
        "筆を 洗う", "Fude o arau", "붓을 씻어", "Buseul ssiseo"
    )
]

# 51. phone-calls
w1["phone-calls"] = [
    item(
        "Clear sound", "صاف آواز", "Saaf aawaaz", "साफ़ आवाज़", "Saaf aawaaz",
        "صوت واضح", "Sawt wadih", "Voz nítida", "VOHS NEE-tee-dah",
        "Ligne claire", "Leen-yuh klehr", "Klare Verbindung", "KLAH-reh fehr-BIN-doong",
        "Voce squillante", "VOH-cheh skweel-LAHN-teh", "Voz audível", "VAWZ ow-JEE-vehl",
        "Хорошая слышимость", "Khah-ROH-shah-yah SLY-shee-mahst", "Net ses", "Net sehs",
        "Suara jernih", "Swah-rah jehr-neeh", "清 语音", "Qīng yǔyīn",
        "はっきりした 通話", "Hakirishita tsūwa", "선명한 음성", "Seonmyeong-han eumseong"
    ),
    item(
        "Loving voice", "پیارا انداز", "Pyaara andaaz", "प्यारी बोली", "Pyaari boli",
        "صوت محب", "Sawt muhibb", "Tono cariñoso", "TOH-noh kah-ree-NYOH-soh",
        "Voix douce", "Vwah doos", "Liebe Stimme", "LEE-beh SHTIM-meh",
        "Voce affettuosa", "VOH-cheh ahf-feht-TWOH-zah", "Voz carinhosa", "VAWZ kah-reen-YAW-zah",
        "Родной голос", "Rahd-NOY GOH-lahs", "Sevecen konuşma", "Seh-veh-jen koh-noosh-mah",
        "Suara ramah", "Swah-rah rah-mah", "温 问候", "Wēn wènhòu",
        "優しい 声", "Yasashii koe", "다정한 목소리", "Dajeong-han moksori"
    ),
    item(
        "Good news", "اچھی خبر", "Achhi khabar", "अच्छी ख़बर", "Achhi khabar",
        "أخبار سارة", "Akhbar sarra", "Buenas noticias", "BWEH-nahs noh-TEE-syahs",
        "Bonne nouvelle", "Buhn noo-vehl", "Schöne Neuigkeit", "SHER-neh NOY-ikh-kyte",
        "Bella notizia", "BEHL-lah noh-TEET-tsyah", "Boa notícia", "BOH-ah noh-CHEE-syah",
        "Радостная весть", "RAH-dahst-nah-yah vyehst", "Güzel haber", "Gew-zel hah-behr",
        "Kabar gembira", "Kah-bahr gehm-bee-rah", "喜 喜讯", "Xǐ xǐxùn",
        "嬉しい 知らせ", "Ureshii shirase", "기쁜 소식", "Gippeun sosik"
    )
]

w2["phone-calls"] = [
    item(
        "Say hello", "ہیلو بولو", "Hello bolo", "हैलो बोलो", "Hello bolo",
        "قل مرحباً", "Qul marhaban", "Di aló", "DEE ah-LOH",
        "Dis allô", "Dee ah-loh", "Sag Hallo", "ZAHK hah-LOH",
        "Dì pronto", "DEE PROHN-toh", "Diga alô", "JEE-gah ah-LOH",
        "Скажи алло", "Skah-ZHY ahl-LOH", "Alo de", "Ah-loh deh",
        "Ucap halo", "Oo-chahp hah-loh", "说 喂你好", "Shuō wèinǐhǎo",
        "「もしもし」と話す", "Moshimoshi to hanasu", "여보세요 말해", "Yeoboseyo malhae"
    ),
    item(
        "Hear grandma", "دادی کو سنو", "Daadi ko suno", "दादी को सुनो", "Daadi ko suno",
        "استمع لجدتك", "Istami' lijaddatik", "Escucha abuela", "Ehs-KOO-chah ah-BWEH-lah",
        "Écoute mamie", "Ay-koot mah-mee", "Hör Oma", "HER OH-mah",
        "Ascolta nonna", "Ahs-KOHL-tah NOHN-nah", "Ouça vovó", "OH-sah voh-VAW",
        "Послушай бабушку", "Pah-SLOO-shy BAH-boosh-koo", "Nineyi dinle", "Nee-neh-yee deen-leh",
        "Dengarkan nenek", "Dehng-ahr-kahn neh-nehk", "听 奶奶讲", "Tīng nǎinaijiǎng",
        "おばあちゃんの 声聞く", "Obāchan no koekiku", "할머니 말씀들어", "Halmeoni malsseumdeureo"
    ),
    item(
        "Send kiss", "پیار بھیجو", "Pyaar bhejo", "चुंबन भेजो", "Chumban bhejo",
        "أرسل قبلة", "Arsil qubla", "Manda besito", "MAHN-dah beh-SEE-toh",
        "Envoie bisou", "Ahn-vwah bee-zoo", "Schick Kuss", "SHIK koos",
        "Manda bacetto", "MAHN-dah bah-CHEHT-toh", "Mande beijinho", "MAHN-jee bay-ZHEEN-yoo",
        "Пошли поцелуй", "Pahsh-LEE pah-tseh-LOOY", "Öpücük gönder", "Er-pew-jewk gern-dehr",
        "Kirim peluk cium", "Kee-reem peh-look chee-oom", "飞 个吻", "Fēi gèwěn",
        "投げキッス する", "Nagekissu suru", "뽀뽀 날려줘", "Ppoppo nallyeojwo"
    )
]

# 52. video-chats
w1["video-chats"] = [
    item(
        "Clear picture", "صاف تصویر", "Saaf tasweer", "साफ़ वीडियो", "Saaf video",
        "صورة نقية", "Sura naqiyya", "Imagen nítida", "Ee-MAH-hehn NEE-tee-dah",
        "Vidéo fluide", "Vee-day-oh floo-eed", "Scharfes Bild", "SHAHR-fes bilt",
        "Video chiaro", "VEE-deh-oh KYAH-roh", "Imagem nítida", "Ee-MAH-zheng NEE-chee-dah",
        "Чёткая картинка", "CHOHT-kah-yah kahr-TEEN-kah", "Net görüntü", "Net ger-rewn-tew",
        "Gambar jelas", "Gahm-bahr jeh-lahs", "高 视频", "Gāo shìpín",
        "綺麗な ビデオ映像", "Kireina bideo'eizō", "선명한 영상", "Seonmyeong-han yeongsang"
    ),
    item(
        "Happy face", "ہنستا چہرہ", "Hansta chehra", "हँसता चेहरा", "Hansta chehra",
        "وجه مبتسم", "Wajh mubtasim", "Cara sonriente", "KAH-rah sohn-RYEHN-teh",
        "Visage souriant", "Vee-zahzh soo-ryahn", "Fröhliches Gesicht", "FRER-likh-es geh-ZIKHT",
        "Volto allegro", "VOHL-toh ahl-LEH-groh", "Rosto feliz", "HOHS-too feh-LEES",
        "Улыбающееся лицо", "Oo-ly-BAH-yoo-shchyee-yeh-syah lee-TSOH", "Gülen yüz", "Gew-len yewz",
        "Wajah ceria", "Wah-jah cheh-ree-ah", "笑 脸蛋", "Xiào liǎndàn",
        "にこにこ 笑顔", "Nikoniko egao", "웃는 얼굴", "Utneun eolgul"
    ),
    item(
        "Big wave", "بڑا اشارہ", "Bara ishaara", "हाथ हिलाना", "Haath hilaana",
        "تلويحة يد", "Talwihat yad", "Saludo con mano", "Sah-LOO-doh kohn MAH-noh",
        "Signe joyeux", "Seen-yuh zhwah-yuh", "Freundliches Winken", "FROYNT-likh-es VIN-ken",
        "Saluto con la mano", "Sah-LOO-toh kohn lah MAH-noh", "Tchauzinho animado", "Chow-ZEEN-yoo ah-nee-MAH-doo",
        "Приветственный жест", "Pree-VYEHT-stvyen-nyy zhehst", "El sallama", "Ehl sahl-lah-mah",
        "Lambaian ceria", "Lahm-by-ahn cheh-ree-ah", "热 招手", "Rè zhāoshǒu",
        "大きく 手を振る", "Ōkiku te o furu", "반가운 손인사", "Bangaun son-insa"
    )
]

w2["video-chats"] = [
    item(
        "Wave hand", "ہاتھ ہلاؤ", "Haath hilao", "हाथ हिलाओ", "Haath hilaao",
        "لوح بيدك", "Lawwih bi-yadak", "Mueve mano", "MWEH-veh MAH-noh",
        "Fais coucou", "Feh koo-koo", "Winke fröhlich", "VIN-keh FRER-likh",
        "Saluta con mano", "Sah-LOO-tah kohn MAH-noh", "Acene com a mão", "Ah-SEH-nee kohn ah mown",
        "Помаши ручкой", "Pah-mah-SHY ROOCH-koy", "Elinle selamla", "Eh-leen-leh seh-lahm-lah",
        "Lambaikan tangan", "Lahm-bye-kahn tahng-ahn", "招 招手", "Zhāo zhāoshǒu",
        "手を 振る", "Te o furu", "손 흔들어봐", "Son heundeureobwa"
    ),
    item(
        "Smile screen", "کیمرے پر مسکراؤ", "Camera par muskurao", "कैमरे में मुस्कुराओ", "Camera mein muskuraao",
        "ابتسم للكاميرا", "Ibtasim lil-kamira", "Sonríe a cámara", "Sohn-REE-eh ah KAH-mah-rah",
        "Souris à l'écran", "Soo-ree ah lay-krahn", "Lächle in die Kamera", "LEKH-leh in dee KAH-meh-rah",
        "Sorridi allo schermo", "Sohr-REE-dee AHL-loh SKEHR-moh", "Sorria para a tela", "Sohr-HEE-ah PAH-rah ah TAY-lah",
        "Улыбнись в камеру", "Oo-lyb-NEES v KAH-mye-roo", "Kameraya gülümse", "Kah-meh-rah-yah gew-lewm-seh",
        "Tersenyum ke kamera", "Tehr-sehn-yoom keh kah-meh-rah", "对 镜头笑", "Duì jìngtóuxiào",
        "カメラに 笑いかける", "Kamera ni waraikakeru", "카메라 보고 웃어", "Kamera bogo useo"
    ),
    item(
        "Say bye", "بائے بائے کہو", "Bye bye kaho", "बाय बाय कहो", "Bye bye kaho",
        "ودع بحرارة", "Waddi' bi-harara", "Despídete alegre", "Dehs-PEE-deh-teh ah-LEH-greh",
        "Dis au revoir", "Dee oh ruh-vwahr", "Sag Tschüssi", "ZAHK CHYOOS-see",
        "Manda bacio e ciao", "MAHN-dah BAH-choh eh chow", "Dê tchauzinho", "DAY chow-ZEEN-yoo",
        "Скажи пока-пока", "Skah-ZHY pah-KAH pah-KAH", "Hoşça kal de", "Hohsh-chah kahl deh",
        "Dah-dah semua", "Dah-dah seh-moo-ah", "道 再见", "Dào zàijiàn",
        "「バイバイ」と言う", "Baibai to iu", "안녕 손인사", "Annyeong son-insa"
    )
]

# 53. telling-time
w1["telling-time"] = [
    item(
        "Big clock", "بڑی گھڑی", "Bari ghari", "बड़ी घड़ी", "Badi ghadi",
        "ساعة حائط", "Sa'at ha'it", "Reloj grande", "Reh-LOH heh GRAHN-deh",
        "Grande horloge", "Grahnd ohr-lozh", "Große Wanduhr", "GROHS-seh VAHNT-oor",
        "Orologio grande", "Oh-roh-LOH-joh GRAHN-deh", "Relógio de parede", "Heh-LAW-zhyoo jee pah-REH-jee",
        "Большие часы", "Bahl-SHEE-yeh chah-SY", "Büyük duvar saati", "Bew-yewk doo-vahr sah-ah-tee",
        "Jam dinding besar", "Jahm deen-deeng beh-sahr", "大 挂钟", "Dà guàzhōng",
        "大きな 時計", "Ōkina tokei", "커다란 시계", "Keodaran sigye"
    ),
    item(
        "Short hand", "چھوٹی سوئی", "Chhoti sooyi", "छोटी सुई", "Chhoti sooyi",
        "عقرب قصير", "'Aqrab qasir", "Manecilla corta", "Mah-neh-SEE-yah KOHR-tah",
        "Petite aiguille", "Puh-teet ay-gwee-yuh", "Kleiner Zeiger", "KLY-ner TSY-ger",
        "Lancetta corta", "Lahn-CHEHT-tah KOHR-tah", "Ponteiro pequeno", "Pohn-TAY-roo peh-KAY-noo",
        "Короткая стрелка", "Kah-ROHT-kah-yah STRYEHL-kah", "Kısa akrep", "Kuh-sah ahk-rep",
        "Jarum pendek", "Jah-room pehn-dehk", "短 时针", "Duǎn shízhēn",
        "短い 針", "Mijikai hari", "짧은 바늘", "Jjalkeun baneul"
    ),
    item(
        "Right time", "صحیح وقت", "Saheeh waqt", "सही समय", "Sahi samay",
        "وقت محدد", "Waqt muhaddad", "Hora exacta", "OH-rah ehk-SAHK-tah",
        "Heure juste", "Uhr zhoost", "Genaue Zeit", "Geh-NOW-eh tsyt",
        "Ora esatta", "OH-rah eh-ZAHT-tah", "Hora certa", "OH-rah SEHR-tah",
        "Точное время", "TOHCH-nah-yeh VRYEH-myah", "Doğru vakit", "Doh-roo vah-keet",
        "Waktu tepat", "Wahk-too teh-paht", "准 时间", "Zhǔn shíjiān",
        "ぴったりの 時間", "Pittari no jikan", "정확한 시간", "Jeonghwak-han sigan"
    )
]

w2["telling-time"] = [
    item(
        "Look clock", "گھڑی دیکھو", "Ghari dekho", "घड़ी देखो", "Ghadi dekho",
        "انظر للساعة", "Undhur lis-sa'a", "Mira reloj", "MEE-rah reh-LOH",
        "Regarde montre", "Ruh-gahrd mohn-truh", "Schau auf die Uhr", "SHOW owf dee oor",
        "Guarda orologio", "GWAHR-dah oh-roh-LOH-joh", "Olhe as horas", "AW-lyee ahs AW-rahs",
        "Посмотри на часы", "Pah-smah-TREE nah chah-SY", "Saate bak", "Sah-ah-teh bahk",
        "Lihat jam", "Lee-haht jahm", "看 表盘", "Kàn biǎopán",
        "時計 見る", "Tokei miru", "시계 확인해", "Sigye hwaginhae"
    ),
    item(
        "Count numbers", "ہندسے گنو", "Hindse gino", "गिनती गिनो", "Ginti gino",
        "عد الأرقام", "'Udd al-arqam", "Cuenta números", "KWEHN-tah NOO-meh-rohs",
        "Compte chiffres", "Kohnt sheefr", "Zähl Ziffern", "TSAYL TSIF-fern",
        "Conta ore", "KOHN-tah OH-reh", "Conte números", "KOHN-chee NOO-meh-roos",
        "Считай цифры", "Schee-TYE TSEE-fry", "Sayıları say", "Sah-yuh-lah-ruh sigh",
        "Hitung angka", "Hee-toong ahng-kah", "数 钟点", "Shǔ zhōngdiǎn",
        "数字 数える", "Sūji kazoeru", "숫자를 세어봐", "Sutjareul seeobwa"
    ),
    item(
        "Know hour", "وقت جانو", "Waqt jaano", "समय पहचानो", "Samay pehchaano",
        "اعرف الوقت", "I'rif al-waqt", "Sabe hora", "SAH-beh OH-rah",
        "Lis l'heure", "Lee luhr", "Erkenn Stunde", "Ehr-KEN SHTOON-deh",
        "Riconosci l'ora", "Ree-koh-NOH-shee LOH-rah", "Descubra horário", "Dehs-KOO-brah oh-RAH-ryoo",
        "Узнай который час", "Ooz-NYE kah-TOH-ryy chahs", "Zamanı söyle", "Zah-mah-nuh seri-leh",
        "Pahami waktunya", "Pah-hah-mee wahk-too-nyah", "认 点钟", "Rèn diǎnzhōng",
        "時間を 覚える", "Jikan o oboeru", "시각을 알아맞혀", "Sigageul aramatchyeo"
    )
]

# 54. todays-weather (EXACT REQUIREMENT FROM PROMPT SPECIFICATION)
w1["todays-weather"] = [
    item(
        "Sunny morning", "روشن صبح", "Roshan subah", "सुनहरी सुबह", "Sunahari subah",
        "صباح مشرق", "Sabah mushriq", "Mañana soleada", "Mah-NYAH-nah soh-leh-AH-dah",
        "Matin ensoleillé", "Mah-tan ahn-soh-lay-yay", "Sonniger Morgen", "ZON-nee-ger MOR-gen",
        "Mattina soleggiata", "Maht-TEE-nah soh-lehd-JAH-tah", "Manhã ensolarada", "Mahn-YAHN eng-soh-lah-RAH-dah",
        "Солнечное утро", "SOHL-neech-nah-yeh OO-trah", "Güneşli sabah", "Gew-nesh-lee sah-bah",
        "Pagi cerah", "Pah-gee cheh-rah", "晴 朗晨光", "Qínglǎng chénguāng",
        "晴れた 朝", "Hareta asa", "맑은 아침", "Malgeun achim"
    ),
    item(
        "Cold wind", "ٹھنڈی ہوا", "Thandi hawa", "ठंडी हवा", "Thandi hawa",
        "ريح باردة", "Rih barida", "Viento frío", "VYEHN-toh FREE-oh",
        "Vent frais", "Vahn freh", "Kalter Wind", "KAHL-ter vind",
        "Vento freddo", "VEHN-toh FREHD-doh", "Vento frio", "VEHN-too FREE-oo",
        "Холодный ветер", "Khah-LAHD-nyy VYEH-teer", "Soğuk rüzgâr", "Soh-ook rewz-gyar",
        "Angin dingin", "Ahng-een deeng-een", "冷 清风", "Lěng qīngfēng",
        "冷たい 風", "Tsumetai kaze", "찬 바람", "Chan baram"
    ),
    item(
        "Blue sky", "نیلا آسمان", "Neela aasmaan", "नीला आसमान", "Neela aasmaan",
        "سماء زرقاء", "Sama' zarqa'", "Cielo azul", "SYEH-loh ah-SOOL",
        "Ciel bleu", "Syel bluh", "Blauer Himmel", "BLOW-er HIM-mel",
        "Cielo azzurro", "CHEH-loh ahd-DZOOR-roh", "Céu azul", "SEH-oo ah-ZOOL",
        "Синее небо", "SEE-nyee-yeh NYEH-bah", "Mavi gökyüzü", "Mah-vee gerk-yew-zew",
        "Langit biru", "Lahng-eet bee-roo", "蓝 天空", "Lán tiānkōng",
        "青い 空", "Aoi sora", "푸른 하늘", "Pureun haneul"
    )
]

w2["todays-weather"] = [
    item(
        "Feel breeze", "ہوا محسوس کرو", "Hawa mehsoos karo", "हवा महसूस करो", "Hawa mehsoos karo",
        "اشعر بالنسيم", "Ish'ur bin-nasim", "Siente brisa", "SYEHN-teh BREE-sah",
        "Sens brise", "Sahn breez", "Spür Brise", "SHPOOR BREE-zeh",
        "Senti brezza", "SEHN-tee BREHD-dzah", "Sinta brisa", "SEEN-tah BREE-zah",
        "Почувствуй ветерок", "Pah-CHOOFST-vooy vyeh-tye-ROHK", "Rüzgarı hisset", "Rewz-gah-ruh hees-set",
        "Rasakan sepoi angin", "Rah-sah-kahn seh-poy ahng-een", "感受 微风", "Gǎnshòu wēifēng",
        "風を 感じる", "Kaze o kanjiru", "바람을 느껴봐", "Barameul neukkyeobwa"
    ),
    item(
        "Watch clouds", "بادل دیکھو", "Baadal dekho", "बादल देखो", "Baadal dekho",
        "تأمل السحاب", "Ta'ammal as-sahab", "Mira nubes", "MEE-rah NOO-behs",
        "Observe nuages", "Ohb-sehrv noo-ahzh", "Schau Wolken", "SHOW VOL-ken",
        "Osserva nuvole", "Ohs-SEHR-vah NOO-voh-leh", "Olhe as nuvens", "AW-lyee ahs NOO-vengs",
        "Любуйся облаками", "Lyoo-BOOY-syah ah-blah-KAH-mee", "Bulutları izle", "Boo-loot-lah-ruh eez-leh",
        "Pandang awan", "Pahn-dahng ah-wahn", "看 白云", "Kàn báiyún",
        "雲を 眺める", "Kumo o nagameru", "구름 구경해", "Gureum gugyeonghae"
    ),
    item(
        "Wear coat", "کوٹ پہنو", "Coat pehno", "कोट पहनो", "Coat pehno",
        "ارتد معطفاً", "Irtadi mi'tafan", "Ponte abrigo", "POHN-teh ah-BREE-goh",
        "Mets manteau", "Meh mahn-toh", "Zieh Jacke an", "TSEE YAHK-keh ahn",
        "Indossa cappotto", "Een-DOHS-sah kahp-POHT-toh", "Vista casaco", "VEES-tah kah-ZAH-koo",
        "Надень куртку", "Nah-DYEHN KOORT-koo", "Montunu giy", "Mohn-too-noo geey",
        "Pakai jaket", "Pah-kye jah-keht", "穿 外套", "Chuān wàitào",
        "コート 羽織る", "Kōto haoru", "외투 입어", "Oetu ibeo"
    )
]

# 55. hot-and-cold-days
w1["hot-and-cold-days"] = [
    item(
        "Hot afternoon", "تپتی دوپہر", "Tapti dopehar", "तपती दोपहर", "Tapti dopehar",
        "ظهيرة حارة", "Zahira harra", "Tarde calurosa", "TAR-deh kah-loo-ROH-sah",
        "Après-midi chaud", "Ah-preh mee-dee sho", "Heißer Nachmittag", "HY-ser NAHKH-mit-tahk",
        "Pomeriggio afoso", "Poh-meh-REED-joh ah-FOH-zoh", "Tarde quente", "TAR-jee KEHN-chee",
        "Жаркий полдень", "ZHAHR-kiy POHL-dyen", "Sıcak öğleden sonra", "Suh-dzhak er-leh-dehn sohn-rah",
        "Siang terik", "See-ahng teh-reek", "烈 正午", "Liè zhèngwǔ",
        "暑い 午後", "Atsui gogo", "무더운 오후", "Mudeoun ohu"
    ),
    item(
        "Chilly night", "ٹھنڈی رات", "Thandi raat", "ठंडी रात", "Thandi raat",
        "ليلة باردة", "Layla barida", "Noche fresca", "NOH-cheh FREHS-kah",
        "Nuit fraîche", "Nwee frehsh", "Kühle Nacht", "KOO-leh nahkht",
        "Notte fresca", "NOHT-teh FREHS-kah", "Noite fria", "NOY-chee FREE-ah",
        "Прохладная ночь", "Prahkh-LAHD-nah-yah nohch", "Serin gece", "Seh-reen geh-jeh",
        "Malam dingin", "Mah-lahm deeng-een", "凉 夜晚", "Liáng yèwǎn",
        "肌寒い 夜", "Hadasamui yoru", "쌀쌀한 밤", "Ssalssal-han bam"
    ),
    item(
        "Ice treat", "ٹھنڈی قلفی", "Thandi qulfi", "ठंडी कुल्फ़ी", "Thandi kulfi",
        "مثلجات منعشة", "Muthallajat mun'isha", "Helado refrescante", "Eh-LAH-doh reh-frehs-KAHN-teh",
        "Glace fraîche", "Glahs frehsh", "Kühles Eis", "KOO-les yse",
        "Gelato fresco", "Jeh-LAH-toh FREHS-koh", "Picolé geladinho", "Pee-koh-LEH zheh-lah-JEEN-yoo",
        "Освежающее мороженое", "Ahs-vyeh-ZHAH-yoo-shchyeh-yeh mah-ROH-zhyen-nah-yeh", "Buz gibi dondurma", "Booz gee-bee dohn-door-mah",
        "Es segar", "Ehs seh-gahr", "清 冰棒", "Qīng bīngbàng",
        "冷たい アイス", "Tsumetai aisu", "시원한 아이스크림", "Siwon-han aiseukeurim"
    )
]

w2["hot-and-cold-days"] = [
    item(
        "Drink lemonade", "شکنجبین پیو", "Shakanjabeen peeyo", "शिकंजी पियो", "Shikanji piyo",
        "اشرب ليمونادة", "Ishrab laymunada", "Toma limonada", "TOH-mah lee-moh-NAH-dah",
        "Bois citronnade", "Bwah see-troh-nahd", "Trink Limonade", "TRINK lee-moh-NAH-deh",
        "Bevi limonata", "BEH-vee lee-moh-NAH-tah", "Beba limonada", "BEH-bah lee-moh-NAH-dah",
        "Пей лимонад", "Pey lee-mah-NAHT", "Limonata iç", "Lee-moh-nah-tah eech",
        "Minum limun segar", "Mee-noom lee-moon seh-gahr", "喝 柠檬水", "Hē níngméngshuǐ",
        "レモネード 飲む", "Remonēdo nomu", "레모네이드 마셔", "Remoneideu masyeo"
    ),
    item(
        "Wear scarf", "مفلر لپیٹو", "Muffler lapeto", "मफ़लर लपेटो", "Muffler lapeto",
        "لف وشاحاً", "Luff wishahan", "Ponte bufanda", "POHN-teh boo-FAHN-dah",
        "Mets écharpe", "Meh ay-shahrp", "Wickel Schal", "VIK-el shahl",
        "Metti sciarpa", "MEHT-tee SHAHR-pah", "Use cachecol", "OO-zee kah-sheh-KAWL",
        "Завяжи шарф", "Zah-vyah-ZHY shahrf", "Atkını sar", "Aht-kuh-nuh sahr",
        "Pakai syal", "Pah-kye shah-yahl", "围 围巾", "Wéi wéijīn",
        "マフラー 巻く", "Mafurā maku", "목도리 둘러", "Mokdori dulleo"
    ),
    item(
        "Stay shade", "سائے میں بیٹھو", "Saaye mein baitho", "छाया में बैठो", "Chhaya mein baitho",
        "ابق في الظل", "Ibqa fiz-zill", "Busca sombra", "BOOS-kah SOHM-brah",
        "Reste à l'ombre", "Rehst ah lohn-bruh", "Bleib im Schatten", "BLYP im SHAHT-ten",
        "Resta all'ombra", "REHS-tah ahl-LOHM-brah", "Fique na sombra", "FEE-kee nah SOHM-brah",
        "Спрячься в тени", "SPRYACH-syah f tyeh-NEE", "Gölgelik yerde dur", "Gerl-geh-leek yehr-deh door",
        "Berteduh di bawah pohon", "Behr-teh-dooh dee bah-wah poh-hohn", "去 树荫下", "Qù shùyīnxià",
        "日陰で 休む", "Hikage de yasumu", "그늘에서 쉬어", "Geuneureseo swieo"
    )
]

# 56. morning-routine
w1["morning-routine"] = [
    item(
        "Bright day", "روشن دن", "Roshan din", "सुहावना दिन", "Suhaawana din",
        "يوم مشرق", "Yawm mushriq", "Día radiante", "DEE-ah rah-DYAHN-teh",
        "Belle journée", "Bel zhoor-nay", "Schöner Tag", "SHER-ner tahk",
        "Giorno radioso", "JOHR-noh rah-DYOH-zoh", "Dia ensolarado", "JEE-ah eng-soh-lah-RAH-doo",
        "Светлый день", "SVYEHT-lyy dyen", "Aydınlık gün", "Eye-duhn-luhk gewn",
        "Hari cerah", "Hah-ree cheh-rah", "好 白天", "Hǎo báitiān",
        "爽やかな 朝", "Sawayakana asa", "화창한 하루", "Hwachang-han haru"
    ),
    item(
        "Fresh face", "تازہ دم چہرہ", "Taaza dam chehra", "ताज़ा चेहरा", "Taaza chehra",
        "وجه منتعش", "Wajh munta'ish", "Carita fresca", "Kah-REE-tah FREHS-kah",
        "Visage frais", "Vee-zahzh freh", "Frisches Gesicht", "FRISH-es geh-ZIKHT",
        "Viso fresco", "VEE-zoh FREHS-koh", "Rosto lavado", "HOHS-too lah-VAH-doo",
        "Умытое личико", "Oo-MY-tah-yeh LEE-cheek-kah", "Taptaze yüz", "Tahp-tah-zeh yewz",
        "Wajah segar", "Wah-jah seh-gahr", "净 面容", "Jìng miànróng",
        "さっぱりした 顔", "Sappirishita kao", "상쾌한 얼굴", "Sangkwae-han eolgul"
    ),
    item(
        "Clean teeth", "چمکتے دانت", "Chamakte daant", "चमकते दाँत", "Chamakte daant",
        "أسنان نظيفة", "Asnan nadhifa", "Dientes limpios", "DYEHN-tehs LEEM-pyohs",
        "Dents blanches", "Dahn blahnsh", "Weiße Zähne", "VY-seh TSAY-neh",
        "Denti puliti", "DEHN-tee poo-LEE-tee", "Dentes limpinhos", "DEHN-chees leem-PEEN-yoos",
        "Белые зубки", "BYEH-ly-yeh ZOOB-kee", "Bembeyaz dişler", "Behm-beh-yahz deesh-lehr",
        "Gigi bersih", "Gee-gee behr-seeh", "白 牙齿", "Bái yáchǐ",
        "ピカピカの 歯", "Pikapika no ha", "하얗고 깨끗한 이", "Hayako kkaekkeut-han i"
    )
]

w2["morning-routine"] = [
    item(
        "Wash face", "منہ دھوؤ", "Munh dhoo", "मुँह धोओ", "Munh dhoo",
        "اغسل وجهك", "Ighsil wajhak", "Lávate cara", "LAH-vah-teh KAH-rah",
        "Lave visage", "Lahv vee-zahzh", "Wasch Gesicht", "VAHSH geh-ZIKHT",
        "Lava viso", "LAH-vah VEE-zoh", "Lave o rosto", "LAH-vee oo HOHS-too",
        "Умойся чистой водой", "Oo-MOY-syah CHEES-toy vah-DOY", "Yüzünü yıka", "Yew-zew-new yuh-kah",
        "Basuh muka", "Bah-sooh moo-kah", "洗 脸庞", "Xǐ liǎnpáng",
        "顔 洗う", "Kao arau", "세수 깨끗이해", "Sesu kkaekkeut-ihae"
    ),
    item(
        "Brush teeth", "دانت صاف کرو", "Daant saaf karo", "दाँत साफ़ करो", "Daant saaf karo",
        "نظف أسنانك", "Nadhif asnanak", "Cepilla dientes", "Seh-PEE-yah DYEHN-tehs",
        "Brosse dents", "Brohs dahn", "Putz Zähne", "POOTS TSAY-neh",
        "Lava denti", "LAH-vah DEHN-tee", "Escove dentes", "Ehs-KOH-vee DEHN-chees",
        "Почисти зубки", "Pah-CHEES-tee ZOOB-kee", "Dişlerini fırçala", "Deesh-leh-ree-nee fuhr-chah-lah",
        "Gosok gigi", "Goh-sohk gee-gee", "刷 牙齿", "Shuā yáchǐ",
        "歯を 磨く", "Ha o migaku", "양치질 꼼꼼히해", "Yangchijil kkomkkom-hihae"
    ),
    item(
        "Comb hair", "بال سنوارو", "Baal sanwaaro", "बाल बनाओ", "Baal banaao",
        "مشط شعرك", "Mashtit sha'rak", "Peina cabello", "PAY-nah kah-BEH-yoh",
        "Peigne cheveux", "Pen-yuh shuh-vuh", "Kämm Haare", "KEM HAH-reh",
        "Pettina capelli", "PEHT-tee-nah kah-PEHL-lee", "Penteie cabelo", "Pen-TAY-ee kah-BAY-loo",
        "Причеши волосы", "Pree-chyeh-SHY VOH-lah-sy", "Saçını tara", "Sah-chuh-nuh tah-rah",
        "Sisir rambut", "See-seer rahm-boot", "梳 头发", "Shū tóufa",
        "髪を とかす", "Kami o tokasu", "머리 단정히빗어", "Meori danjeong-hibiseo"
    )
]

# 57. night-sky
w1["night-sky"] = [
    item(
        "Bright moon", "چمکتا چاند", "Chamakta chaand", "चमकता चाँद", "Chamakta chaand",
        "قمر مضيء", "Qamar mudi'", "Luna brillante", "LOO-nah bree-YAHN-teh",
        "Lune éclatante", "Loon ay-klah-tahnt", "Heller Mond", "HEL-ler mohnt",
        "Luna splendente", "LOO-nah splehn-DEHN-teh", "Lua brilhante", "LOO-ah breel-YAHN-chee",
        "Яркая луна", "YAHR-kah-yah loo-NAH", "Işıl ışıl ay", "Uh-shuhl uh-shuhl eye",
        "Bulan purnama", "Boo-lahn poor-nah-mah", "明 月亮", "Míng yuèliang",
        "輝く お月様", "Kagayaku otsukisama", "환한 달님", "Hwan-han dalnim"
    ),
    item(
        "Twinkling star", "جھلملاتا ستارہ", "Jhilmilata sitaara", "टिमटिमाता तारा", "Timtimaata taara",
        "نجم وهاج", "Najm wahhaj", "Estrella centelleante", "Ehs-TREH-yah sehn-teh-yeh-AHN-teh",
        "Étoile scintillante", "Ay-twahl san-tee-yahnt", "Funkelnder Stern", "FOON-keln-der shtairn",
        "Stella luccicante", "STEHL-lah loot-chee-KAHN-teh", "Estrela brilhante", "Ehs-TREH-lah breel-YAHN-chee",
        "Мерцающая звёздочка", "Myehr-TSAH-yoo-shchah-yah ZVYOZ-dahch-kah", "Parlayan yıldız", "Pahr-lah-yahn yuhl-duhz",
        "Bintang berkedip", "Been-tahng behr-keh-deep", "闪 星斗", "Shǎn xīngdǒu",
        "きらめく 星", "Kirameku hoshi", "반짝이는 별", "Banjjagineun byeol"
    ),
    item(
        "Dark sky", "تاریک آسمان", "Taareek aasmaan", "रात का आसमान", "Raat ka aasmaan",
        "سماء ساكنة", "Sama' sakina", "Cielo nocturno", "SYEH-loh nohk-TOOR-noh",
        "Ciel étoilé", "Syel ay-twah-lay", "Dunkler Nachthimmel", "DOON-kler NAHKHT-him-mel",
        "Cielo stellato", "CHEH-loh stehl-LAH-toh", "Céu estrelado", "SEH-oo ehs-treh-LAH-doo",
        "Тёмное ночное небо", "TYOHM-nah-yeh nahch-NOH-yeh NYEH-bah", "Karanlık gökyüzü", "Kah-rahn-luhk gerk-yew-zew",
        "Langit malam", "Lahng-eet mah-lahm", "幽 夜空", "Yōu yèkōng",
        "静かな 夜空", "Shizukana yozora", "고요한 밤하늘", "Goyohan bamhaneul"
    )
]

w2["night-sky"] = [
    item(
        "Spot moon", "چاند دیکھو", "Chaand dekho", "चाँद देखो", "Chaand dekho",
        "تأمل القمر", "Ta'ammal al-qamar", "Mira luna", "MEE-rah LOO-nah",
        "Regarde lune", "Ruh-gahrd loon", "Such Mond", "ZOOKH mohnt",
        "Osserva luna", "Ohs-SEHR-vah LOO-nah", "Olhe a lua", "AW-lyee ah LOO-ah",
        "Смотри на луну", "Smah-TREE nah loo-NOO", "Aya bak", "Ah-yah bahk",
        "Pandang bulan", "Pahn-dahng boo-lahn", "望 明月", "Wàng míngyuè",
        "お月様を 眺める", "Otsukisama o nagameru", "달님을 올려다봐", "Dalnimeul ollyeodabwa"
    ),
    item(
        "Count stars", "ستارے گنو", "Sitaare gino", "तारे गिनो", "Taare gino",
        "عد النجوم", "'Udd an-nujum", "Cuenta estrellas", "KWEHN-tah ehs-TREH-yahs",
        "Compte étoiles", "Kohnt ay-twahl", "Zähl Sterne", "TSAYL SHTEHR-neh",
        "Conta stelle", "KOHN-tah STEHL-leh", "Conte estrelas", "KOHN-chee ehs-TREH-lahs",
        "Считай звёздочки", "Schee-TYE ZVYOZ-dahch-kee", "Yıldızları say", "Yuhl-duhz-lah-ruh sigh",
        "Hitung bintang", "Hee-toong been-tahng", "数 繁星", "Shǔ fánxīng",
        "星を 数える", "Hoshi o kazoeru", "별들을 세어봐", "Byeoldeureul seeobwa"
    ),
    item(
        "Make wish", "دعا مانگو", "Dua maango", "दुआ माँगो", "Dua maango",
        "تمن أمنية", "Tamanna umniyya", "Pide deseo", "PEE-deh deh-SEH-oh",
        "Fais vœu", "Feh vuh", "Wünsch dir was", "VOONSH deer vahs",
        "Esprimi desiderio", "Ehs-PREE-mee deh-zee-DEH-ryoh", "Faça pedido", "FAH-sah peh-JEE-doo",
        "Загадай желание", "Zah-gah-DYE zheh-LAH-nyee-yeh", "Bir dilek tut", "Beer dee-lek toot",
        "Ucapkan doa", "Oo-chahp-kahn doh-ah", "许 个愿", "Xǔ gèyuàn",
        "願い事をする", "Negaigoto o suru", "소원을 빌어봐", "Sowoneul bireobwa"
    )
]

# 58. holiday-plans
w1["holiday-plans"] = [
    item(
        "Sunny trip", "شاندار سیر", "Shaandaar sair", "शानदार यात्रा", "Shaandaar yaatra",
        "رحلة ممتعة", "Rihla mumti'a", "Viaje alegre", "VYAH-heh ah-LEH-greh",
        "Beau voyage", "Boh vwah-yahzh", "Schöne Urlaubsreise", "SHER-neh OOR-lowps-rye-seh",
        "Gita splendida", "JEE-tah SPLEHN-dee-dah", "Viagem boa", "VYAH-zheng BOH-ah",
        "Отличная поездка", "Aht-LEECH-nah-yah pah-YEZD-kah", "Harika tatil", "Hah-ree-kah tah-teel",
        "Liburan ceria", "Lee-boo-rahn cheh-ree-ah", "畅 假期", "Chàng jiàqī",
        "楽しい 旅行", "Tanoshii ryokō", "신나는 휴가여행", "Sinnaneun hyugayeohaeng"
    ),
    item(
        "Blue suitcase", "نیلا سوٹ کیس", "Neela suitcase", "नीला सूटकेस", "Neela suitcase",
        "حقيبة زرقاء", "Haqiba zarqa'", "Maleta azul", "Mah-LEH-tah ah-SOOL",
        "Valise bleue", "Vah-leez bluh", "Blauer Koffer", "BLOW-er KOF-fer",
        "Valigia blu", "Vah-LEE-jah bloo", "Mala azul", "MAH-lah ah-ZOOL",
        "Синий чемодан", "SEE-nyy cheh-mah-DAHN", "Mavi bavul", "Mah-vee bah-vool",
        "Koper biru", "Koh-pehr bee-roo", "蓝 行李箱", "Lán xínglǐxiāng",
        "青い スーツケース", "Aoi sūtsukēsu", "파란 캐리어", "Paran kaerieo"
    ),
    item(
        "Happy beach", "خوبصورت ساحل", "Khoobsurat sahil", "सुंदर समुद्री किनारा", "Sundar samudri kinaara",
        "شاطئ جميل", "Shati' jamil", "Playa linda", "PLAH-yah LEEN-dah",
        "Plage ensoleillée", "Plahzh ahn-soh-lay-yay", "Sonniger Strand", "ZON-nee-ger shtrahnt",
        "Spiaggia bella", "SPYAHD-jah BEHL-lah", "Praia bonita", "PRYE-ah boh-NEE-tah",
        "Тёплый пляж", "TYOHP-lyy plyazh", "Kumsal sahil", "Koom-sahl sah-heel",
        "Pantai indah", "Pahn-tye een-dah", "美 海滨", "Měi hǎibīn",
        "美しい 海辺", "Utsukushii umibe", "아름다운 해변", "Areumdaun haebyeon"
    )
]

w2["holiday-plans"] = [
    item(
        "Pack bag", "سامان باندھو", "Saamaan baandho", "सामान बाँधो", "Saamaan baandho",
        "رتب حقيبتك", "Rattib haqibatak", "Prepara maleta", "Preh-PAH-rah mah-LEH-tah",
        "Fais valise", "Feh vah-leez", "Pack Koffer", "PAHK KOF-fer",
        "Prepara valigia", "Preh-PAH-rah vah-LEE-jah", "Arrume mala", "Ah-HOO-mee MAH-lah",
        "Собери вещи", "Sah-bye-REE VYEH-shchee", "Bavulu hazırla", "Bah-voo-loo hah-zuhr-lah",
        "Kemas koper", "Keh-mahs koh-pehr", "收拾 行李", "Shōushi xíngli",
        "荷物 まとめる", "Nimotsu matomeru", "짐 정리해", "Jim jeongnihae"
    ),
    item(
        "Check tickets", "ٹکٹ چیک کرو", "Ticket check karo", "टिकट जाँचो", "Ticket jaancho",
        "تأكد من التذاكر", "Ta'akkad min at-tadhakir", "Revisa boletos", "Reh-VEE-sah boh-LEH-tohs",
        "Prends billets", "Prahn bee-yay", "Prüf Fahrkarten", "PROOF FAHR-kahr-ten",
        "Controlla biglietti", "Kohn-TROHL-lah beel-YEHT-tee", "Confira passagens", "Kohn-FEE-rah pah-SAH-zhengz",
        "Проверь билеты", "Prah-VYEHR bee-LYEH-ty", "Biletleri kontrol et", "Bee-let-leh-ree kohn-trohl et",
        "Periksa tiket", "Peh-reek-sah tee-keht", "备好 车票", "Bèihǎo chēpiào",
        "切符を 確認する", "Kippu o kakunin-suru", "예매표 확인해", "Yemaepyo hwaginhae"
    ),
    item(
        "Fly high", "ہوا میں اڑو", "Hawa mein uro", "हवाई यात्रा करो", "Hawaai yaatra karo",
        "سافر بعيداً", "Safir ba'idan", "Viaja lejos", "VYAH-hah LEH-hohs",
        "Pars loin", "Pahr lwan", "Flieg los", "FLEEKH lohs",
        "Parti sereno", "PAHR-tee seh-REH-noh", "Voe longe", "VAW-ee LOHN-zhee",
        "Лети навстречу", "Lyeh-TEE nahf-STRYEH-choo", "Uzaklara uç", "Oo-zahk-lah-rah ooch",
        "Terbang jauh", "Tehr-bahng jah-ooh", "开心 出发", "Kāixīn chūfā",
        "元気に出発 する", "Genkini shuppatsu suru", "설레며 떠나봐", "Seollemyeo tteonabwa"
    )
]

# 59. festival-greetings
w1["festival-greetings"] = [
    item(
        "Bright lights", "روشن بتیاں", "Roshan battiyan", "चमकती बत्तियाँ", "Chamaktee battiyaan",
        "أضواء ساطعة", "Adwa' sati'a", "Luces de fiesta", "LOO-sehs deh FYEHS-tah",
        "Lumières vives", "Loo-myehr veev", "Bunte Lichterkette", "BOON-teh LIKH-ter-ket-teh",
        "Luci festive", "LOO-chee fehs-TEE-veh", "Luzes festivas", "LOO-zees fehs-CHEE-vahs",
        "Праздничные огни", "PRAHZD-neech-ny-yeh ahg-NEE", "Işıl ışıl fenerler", "Uh-shuhl uh-shuhl feh-nehr-lehr",
        "Lampu hiasan", "Lahm-poo hee-ah-sahn", "彩 街灯", "Cǎi jiēdēng",
        "華やかな イルミネーション", "Hanayakana iruminēshon", "화려한 불빛", "Hwaryeohan bulbit"
    ),
    item(
        "Sweet sweets", "لذیذ مٹھائیاں", "Lazeez mithaiyaan", "स्वादिष्ट मिठाइयाँ", "Swaadisht mithaiyaan",
        "حلويات شهية", "Halawayat shahiyya", "Dulces ricos", "DOOL-sehs REE-kohs",
        "Friandises douces", "Free-yahn-deez doos", "Festliches Gebäck", "FEST-likh-es geh-BEK",
        "Dolcetti tipici", "Dohl-CHEHT-tee TEE-pee-chee", "Docinhos gostosos", "Doh-SEEN-yoos gohs-TOH-zoos",
        "Сладкие угощения", "SLAHT-kee-yeh oo-gah-SHYEH-nyee-yah", "Nefis bayram tatlıları", "Neh-fees by-rahm taht-luh-lah-ruh",
        "Kue perayaan", "Koo-eh peh-rah-yah-ahn", "甜 糕点", "Tián gāodiǎn",
        "祝いの お菓子", "Iwai no okashi", "명절 음식", "Myeongjeol eumsik"
    ),
    item(
        "Warm hugs", "پیاری جپھیاں", "Pyaari jhappiyan", "गले मिलना", "Gale milna",
        "تهان حارة", "Tahani harra", "Abrazos afectuosos", "Ah-BRAH-zohs ah-fehk-TWOH-sohs",
        "Étreintes chaleureuses", "Ay-trant shah-luh-ruhz", "Herzliche Umarmungen", "HEHRTS-likh-eh oom-AHR-moong-en",
        "Abbracci calorosi", "Ahb-BRAHT-chee kah-loh-ROH-zee", "Abraços de festa", "Ah-BRAH-soos jee FEHS-tah",
        "Тёплые объятия", "TYOHP-ly-yeh ahb-YAH-tyah", "Kucaklaşmalar", "Koo-jahk-lahsh-mah-lahr",
        "Pelukan hangat keluarga", "Peh-look-ahn hahng-aht keh-loo-ahr-gah", "亲 拥抱", "Qīn yǒngbào",
        "心温まる 抱擁", "Kokorowatatamaru hōyō", "따뜻한 포옹", "Ttatteut-han poong"
    )
]

w2["festival-greetings"] = [
    item(
        "Say greetings", "مبارکباد دو", "Mubarakbaad do", "बधाई दो", "Badhaai do",
        "هنئ بحرارة", "Hanni' bi-harara", "Felicita alegre", "Feh-lee-SEE-tah ah-LEH-greh",
        "Souhaite bonne fête", "Soo-eht buhn feht", "Wünsch frohes Fest", "VOONSH FROH-es fest",
        "Augura buone feste", "Ow-GOO-rah BWAW-neh FEHS-teh", "Deseje boas festas", "Deh-ZEH-zhee BAW-ahs FEHS-tahs",
        "Поздравь с праздником", "Pahz-DRAHF s PRAHZD-nee-kahm", "Bayram kutla", "By-rahm koot-lah",
        "Beri ucapan selamat", "Beh-ree oo-chah-pahn seh-lah-maht", "送 祝福", "Sòng zhùfú",
        "お祝いを 述べる", "Oiwai o noberu", "명절인사 건네", "Myeongjeol-insa geonne"
    ),
    item(
        "Share sweets", "مٹھائی بانٹو", "Mithaai baanto", "मिठाई बाँटो", "Mithaai baanto",
        "وزع حلويات", "Wazzi' halawayat", "Reparte dulces", "Reh-PAR-teh DOOL-sehs",
        "Partage douceurs", "Pahr-tahzh doo-suhr", "Teil Leckereien", "TYLE LEK-keh-rye-en",
        "Distribuisci dolci", "Dees-tree-BWEE-shee DOHL-chee", "Distribua docinhos", "Dees-tree-BOO-ah doh-SEEN-yoos",
        "Угощай сладостями", "Oo-gahsh-CHY SLAH-dahst-yah-mee", "Tatlı ikram et", "Taht-luh eek-rahm et",
        "Bagi-bagi kue", "Bah-gee bah-gee koo-eh", "分 糖果", "Fēn tángguǒ",
        "お菓子を 分け合う", "Okashi o wakeau", "다과 함께 나눠", "Dagwa hamkke nanwo"
    ),
    item(
        "Light lamp", "چراغ جلاؤ", "Chiraagh jalao", "दीपक जलाओ", "Deepak jalaao",
        "أشعل قنديلاً", "Ash'il qandilan", "Enciende lamparita", "Ehn-SYEHN-deh lahm-pah-REE-tah",
        "Allume lanterne", "Ah-loom lahn-tehrn", "Zünde Lichter an", "TSOON-deh LIKH-ter ahn",
        "Accendi lanterna", "Ahk-CHEHN-dee lahn-TEHR-nah", "Acenda luzinha", "Ah-SEHN-dah loo-ZEEN-yah",
        "Зажги фонарик", "Zahzh-GEE fah-NAH-reek", "Kandili yak", "Kahn-dee-lee yahk",
        "Nyalakan pelita", "Nyah-lah-kahn peh-lee-tah", "点 华灯", "Diǎn huádēng",
        "灯りを 灯す", "Akari o tomosu", "등불 밝혀줘", "Deungbul balkhyeojwo"
    )
]

# 60. packing-bags
w1["packing-bags"] = [
    item(
        "Clean socks", "صاف موزے", "Saaf mozay", "साफ़ मोज़े", "Saaf moze",
        "جوارب نظيفة", "Jawarib nadhifa", "Calcetines limpios", "Kahl-seh-TEE-nehs LEEM-pyohs",
        "Chaussettes propres", "Shoh-seht proh-pruh", "Saubere Socken", "ZOW-beh-reh ZOK-ken",
        "Calze pulite", "KAHL-tseh poo-LEE-teh", "Meias limpas", "MAY-ahs LEEM-pahs",
        "Чистые носочки", "CHEES-ty-yeh nah-SOHCH-kee", "Temiz çoraplar", "Teh-meez choh-rahp-lahr",
        "Kaus kaki bersih", "Kowss kah-kee behr-seeh", "净 袜子", "Jìng wàzi",
        "清潔な 靴下", "Seiketsuna kutsushita", "깨끗한 양말", "Kkaekkeut-han yangmal"
    ),
    item(
        "Warm jacket", "گرم جیکٹ", "Garam jacket", "गर्म जैकेट", "Garm jacket",
        "سترة دافئة", "Sutra dafi'a", "Chaqueta abrigadora", "Chah-KEH-tah ah-bree-gah-DOH-rah",
        "Veste chaude", "Vehst shod", "Warme Jacke", "VAHR-meh YAHK-keh",
        "Giacca calda", "JAHK-kah KAHL-dah", "Jaqueta quentinha", "Zhah-KAY-tah ken-CHEEN-yah",
        "Тёплая куртка", "TYOHP-lah-yah KOORT-kah", "Sıcak mont", "Suh-dzhak mohnt",
        "Jaket hangat", "Jah-keht hahng-aht", "暖 外套", "Nuǎn wàitào",
        "暖かい ジャケット", "Atatakai jaketto", "따뜻한 점퍼", "Ttatteut-han jeompeo"
    ),
    item(
        "Favorite toy", "پسندیدہ کھلونا", "Pasandeeda khilona", "मनपसंद खिलौना", "Manpasand khilauna",
        "لعبة مفضلة", "Lu'ba mufaddala", "Juguete preferido", "Hoo-GEH-teh preh-feh-REE-doh",
        "Jouet préféré", "Zhoo-ay pray-fay-ray", "Lieblingsspielzeug", "LEEP-lings-shpeel-tsoyk",
        "Giocattolo preferito", "Joh-KAHT-toh-loh preh-feh-REE-toh", "Brinquedo favorito", "Breen-KAY-doo fah-voh-REE-too",
        "Любимая игрушка", "Lyoo-BEE-mah-yah eeg-ROOSH-kah", "En sevilen oyuncak", "En seh-vee-len oh-yoon-jahk",
        "Mainan kesayangan", "Mye-nahn keh-sah-yahng-ahn", "爱 玩具", "Ài wánjù",
        "大好きな おもちゃ", "Daisukina omocha", "제일 아끼는 장난감", "Jeil akkineun jangnamgam"
    )
]

w2["packing-bags"] = [
    item(
        "Fold clothes", "کپڑے تہہ کرو", "Kapray teh karo", "कपड़े मोड़ो", "Kapde modo",
        "اطو الملابس", "Itwi al-malabis", "Dobla ropa", "DOH-blah ROH-pah",
        "Plie vêtements", "Plee veht-mahn", "Falte Kleidung", "FAHL-teh KLY-doong",
        "Piega vestiti", "PYEH-gah vehs-TEE-tee", "Dobre roupas", "DAW-bree HOH-pahs",
        "Сложи одежду", "Slah-ZHY ah-DYEHZH-doo", "Giysileri katla", "Geey-see-leh-ree kaht-lah",
        "Lipat baju", "Lee-paht bah-joo", "叠 衣服", "Dié yīfu",
        "服を たたむ", "Fuku o tatamu", "옷을 개어", "Oseul gaeo"
    ),
    item(
        "Zip bag", "چین بند کرو", "Chain band karo", "ज़िप लगाओ", "Zip lagaao",
        "أغلق السحاب", "Aghliq as-sahhab", "Cierra cremallera", "SYEH-rrah kreh-mah-YEH-rah",
        "Ferme fermeture", "Fehrm fehr-muh-toor", "Zieh Reißverschluss", "TSEE RYS-fehr-shloos",
        "Chiudi cerniera", "KYOO-dee chehr-NYEH-rah", "Feche o zíper", "FEH-shee oo ZEE-pehr",
        "Застегни молнию", "Zahs-styehg-NEE MOHL-nee-yoo", "Fermuarı çek", "Fehr-moo-ahr-uh chek",
        "Tutup ritsleting", "Too-toop reet-sleh-teeng", "拉好 拉链", "Lāhǎo lāliàn",
        "チャックを 閉める", "Chakku o shimeru", "지퍼 올려", "Jipeo ollyeo"
    ),
    item(
        "Lift luggage", "بیگ اٹھاؤ", "Bag uthao", "बैग उठाओ", "Bag uthaao",
        "احمل الحقيبة", "Ihmil al-haqiba", "Levanta maleta", "Leh-VAHN-tah mah-LEH-tah",
        "Porte sac", "Pohrt sahk", "Heb Tasche", "HAYP TAH-sheh",
        "Solleva borsa", "Sohl-LEH-vah BOHR-sah", "Levante bolsa", "Leh-VAHN-chee BOWL-sah",
        "Подними сумку", "Pahd-nee-MEE SOOM-koo", "Çantayı kaldır", "Chahn-tah-yuh kahl-duhr",
        "Angkat koper", "Ahng-kaht koh-pehr", "提好 箱包", "Tíhǎo xiāngbāo",
        "荷物を 持ち上げる", "Nimotsu o mochiageru", "가방 들어올려", "Gabang deureoollyeo"
    )
]

# 61. happy-new-year
w1["happy-new-year"] = [
    item(
        "Bright sparks", "روشن پٹاخے", "Roshan pataakhay", "चमकती फुलझड़ी", "Chamaktee phuljhadi",
        "ألعاب نارية", "Al'ab nariyya", "Chispas brillantes", "CHEES-pahs bree-YAHN-tehs",
        "Étincelles festives", "Ay-tan-sehl fehs-teev", "Funkelnde Wunderkerzen", "FOON-keln-deh VOON-der-kehr-tsen",
        "Scintille festose", "Sheen-TEEL-leh fehs-TOH-zeh", "Fogos brilhantes", "FAW-goos breel-YAHN-chees",
        "Яркие фейерверки", "YAHR-kee-yeh fey-yer-VYEHR-kee", "Rengarenk havai fişekler", "Ren-gah-renk hah-vye fee-shek-lehr",
        "Kembang api cerah", "Kehm-bahng ah-pee cheh-rah", "绚 烟火", "Xuàn yānhuǒ",
        "きらめく 花火", "Kirameku hanabi", "화려한 불꽃놀이", "Hwaryeohan bulkkochnori"
    ),
    item(
        "Fresh start", "نیا آغاز", "Naya aaghaaz", "नई शुरुआत", "Nayi shuruwaat",
        "بداية مشرقة", "Bidaya mushriqa", "Comienzo feliz", "Koh-MYEHN-soh feh-LEES",
        "Nouveau départ", "Noo-voh day-pahr", "Froher Neuanfang", "FROH-er NOY-ahn-fahng",
        "Inizio sereno", "Ee-NEE-tsyoh seh-REH-noh", "Recomeço alegre", "Heh-koh-MEH-soo ah-LEH-gree",
        "Новый рубеж", "NOH-vyy roo-BYEZH", "Umut dolu başlangıç", "Oo-moot doh-loo bahsh-lahn-guhch",
        "Awal baru ceria", "Ah-wahl bah-roo cheh-ree-ah", "美 愿景", "Měi yuànjǐng",
        "清々しい 新年", "Kiyogiyoshii shinnen", "새로운 출발", "Saeroun chulbal"
    ),
    item(
        "Happy crowd", "خوش باش لوگ", "Khush baash log", "हँसता-खेलता परिवार", "Hansta-khelta parivaar",
        "جمع مبتهج", "Jam' mubtahij", "Familia alegre", "Fah-MEE-lyah ah-LEH-greh",
        "Foule joyeuse", "Fool zhwah-yuhz", "Fröhliche Runde", "FRER-likh-eh ROON-deh",
        "Festa gioiosa", "FEHS-tah joh-YOH-zah", "Comemoração animada", "Koh-meh-moh-rah-SOWN ah-nee-MAH-dah",
        "Весёлая компания", "Vyeh-SYOH-lah-yah kahm-PAH-nee-yah", "Coşkulu kutlama", "Johsh-koo-loo koot-lah-mah",
        "Suasana riang", "Swah-sah-nah ree-ahng", "喜 盛宴", "Xǐ shèngyàn",
        "賑やかな 祝祭", "Nigiyakana shukusai", "기쁨 넘치는 모임", "Gippeum neomchineun moim"
    )
]

w2["happy-new-year"] = [
    item(
        "Cheer loud", "خوشی سے نعرے", "Khushi se naaray", "ज़ोर से जयकार", "Zor se jaikaar",
        "اهتف بفرح", "Ihtif bi-farah", "Grita de alegría", "GREE-tah deh ah-leh-GREE-ah",
        "Crie de joie", "Kree duh zhwah", "Juble laut", "YOO-bleh lowt",
        "Esulta felice", "Eh-ZOOL-tah feh-LEE-cheh", "Comemore alto", "Koh-meh-MAW-ree AHL-too",
        "Радостно кричи", "RAH-dahst-nah kree-CHEE", "Neşeyle tezahürat yap", "Neh-shay-leh teh-zah-hew-raht yahp",
        "Bersorak gembira", "Behr-soh-rahk gehm-bee-rah", "齐 欢呼", "Qí huānhū",
        "歓声を 上げる", "Kansei o ageru", "다함께 환호해", "Dahamkke hwanhohae"
    ),
    item(
        "Count countdown", "الٹی گنتی گنو", "Ulti ginti gino", "उलटी गिनती गिनो", "Ulti ginti gino",
        "ابدأ العد التنازلي", "Ibda' al-'add at-tanazuliy", "Haz la cuenta", "AHS lah KWEHN-tah",
        "Compte à rebours", "Kohnt ah ruh-boor", "Zähl Countdown", "TSAYL KOWNT-down",
        "Fai conto alla rovescia", "FYE KOHN-toh AHL-lah roh-VEH-shah", "Faça contagem regressiva", "FAH-sah kohn-TAH-zheng heh-greh-SEE-vah",
        "Считай секунды", "Schee-TYE seh-KOON-dy", "Geri sayım yap", "Geh-ree sah-yuhm yahp",
        "Hitung mundur", "Hee-toong moon-door", "倒 计时", "Dào jìshí",
        "カウントダウン 数える", "Kauntodaun kazoeru", "카운트다운 세어봐", "Kaunteudaun seeobwa"
    ),
    item(
        "Wish joy", "خوشیاں مانگو", "Khushiyan maango", "शुभकामनाएँ दो", "Shubhkaamnayein do",
        "تمن الخير للجميع", "Tamanna al-khayr lil-jami'", "Desea felicidades", "Deh-SEH-ah feh-lee-see-DAH-dehs",
        "Souhaite bonheur", "Soo-eht boh-nuhr", "Wünsch Glück", "VOONSH glook",
        "Augura gioia", "Ow-GOO-rah JOH-yah", "Deseje felicidades", "Deh-ZEH-zhee feh-lee-see-DAH-jees",
        "Пожелай счастья", "Pah-zheh-LYE SCHAHST-yah", "Mutluluklar dile", "Moot-loo-look-lahr dee-leh",
        "Doakan sukacita", "Doh-ah-kahn soo-kah-chee-tah", "祝 幸福", "Zhù xìngfú",
        "幸せを 祈る", "Shiawase o inoru", "행복을 빌어줘", "Haengbogeul bireojwo"
    )
]

# 62. birthday-gifts
w1["birthday-gifts"] = [
    item(
        "Big box", "بڑا ڈبہ", "Bara dabba", "बड़ा डिब्बा", "Bada dibba",
        "علبة كبيرة", "'Ulba kabira", "Caja grande", "KAH-hah GRAHN-deh",
        "Boîte cadeau", "Bwaht kah-doh", "Große Überraschungskiste", "GROHS-seh oo-ber-RAHSH-oongs-kis-teh",
        "Scatola regalo", "SKAH-toh-lah reh-GAH-loh", "Caixa de presente", "KYE-shah jee preh-ZEHN-chee",
        "Большая коробка", "Bahl-SHAH-yah kah-ROHP-kah", "Kocaman hediye paketi", "Koh-jah-mahn heh-dee-yeh pah-keh-tee",
        "Kotak kado besar", "Koh-tahk kah-doh beh-sahr", "大 礼盒", "Dà lǐhé",
        "大きな プレゼント箱", "Ōkina purezentobako", "커다란 선물상자", "Keodaran seonmulsangja"
    ),
    item(
        "Red ribbon", "لال ربن", "Laal ribbon", "लाल रिबन", "Laal ribbon",
        "شريط أحمر", "Sharit ahmar", "Cinta roja", "SEEN-tah ROH-hah",
        "Ruban rouge", "Roo-bahn roozh", "Rote Schleife", "ROH-teh SHLY-feh",
        "Nastro rosso", "NAHS-troh ROHS-soh", "Fita vermelha", "FEE-tah vehr-MEHL-yah",
        "Красный бантик", "KRAHS-nyy BAHN-teek", "Kırmızı kurdele", "Kuhr-muh-zuh koor-deh-leh",
        "Pita merah", "Pee-tah meh-rah", "红 丝带", "Hóng sīdài",
        "赤い リボン", "Akai ribon", "빨간 리본", "Ppalgan ribon"
    ),
    item(
        "Nice surprise", "خوشگوار سرپرائز", "Khushgawar surprise", "प्यारा सरप्राइज़", "Pyaara surprise",
        "مفاجأة سارة", "Mufaja'a sarra", "Linda sorpresa", "LEEN-dah sohr-PREH-sah",
        "Belle surprise", "Bel soor-preez", "Tolle Überraschung", "TOL-leh oo-ber-RAHSH-oong",
        "Splendida sorpresa", "SPLEHN-dee-dah sohr-PREH-zah", "Bela surpresa", "BEH-lah soor-PRAY-zah",
        "Чудесный сюрприз", "Choo-DYEHS-nyy syoor-PREEZ", "Tatlı sürpriz", "Taht-luh sewr-preez",
        "Kejutan manis", "Keh-joo-tahn mah-nees", "惊 礼物", "Jīng lǐwù",
        "素敵な サプライズ", "Sutekina sapuraizu", "놀라운 깜짝선물", "Nollaun kkamjjakseonmul"
    )
]

w2["birthday-gifts"] = [
    item(
        "Untie ribbon", "ربن کھولو", "Ribbon kholo", "रिबन खोलो", "Ribbon kholo",
        "فك الشريط", "Fukk ash-sharit", "Desata moño", "Dehs-AH-tah MOH-nyoh",
        "Défais ruban", "Day-feh roo-bahn", "Löse Schleife", "LER-zeh SHLY-feh",
        "Sciogli nastro", "SHOH-lyee NAHS-troh", "Desate laço", "Deh-ZAH-chee LAH-soo",
        "Развяжи бантик", "Rahz-vyah-ZHY BAHN-teek", "Kurdeleyi çöz", "Koor-deh-leh-yee cherz",
        "Buka pita", "Boo-kah pee-tah", "解开 丝带", "Jiěkāi sīdài",
        "リボン ほどく", "Ribon hodoku", "리본을 풀어", "Riboneul pureo"
    ),
    item(
        "Tear paper", "ریپر ہٹاؤ", "Wrapper hatao", "रैपर हटाओ", "Wrapper hataao",
        "انزع الغلاف", "Inza' al-ghilaf", "Abre papel", "AH-breh pah-PEHL",
        "Déchire papier", "Day-sheer pah-pyay", "Reiß Papier", "RYSS pah-PEER",
        "Strappa carta", "STRAHP-pah KAHR-tah", "Rasgue embrulho", "HAHS-gee ehm-BROOL-yoo",
        "Сними обёртку", "Snee-MEE ah-BYOHRT-koo", "Paket kağıdını yırt", "Pah-ket kah-uh-duh-nuh yuhrt",
        "Sobek bungkus", "Soh-behk boong-koos", "撕 包装", "Sī bāozhuāng",
        "包装紙 破く", "Hōsōshi yabuku", "포장지 뜯어", "Pojangji tteudeo"
    ),
    item(
        "See present", "تحفہ دیکھو", "Tohfa dekho", "उपहार देखो", "Upahaar dekho",
        "انظر للهدايا", "Undhur lil-hadaya", "Mira regalo", "MEE-rah reh-GAH-loh",
        "Découvre cadeau", "Day-koo-vruh kah-doh", "Bestaune Geschenk", "Beh-SHTOW-neh geh-SHENK",
        "Guarda regalo", "GWAHR-dah reh-GAH-loh", "Veja presente", "VAY-zhah preh-ZEHN-chee",
        "Посмотри подарок", "Pah-smah-TREE pah-DAH-rahk", "Hediyeni gör", "Heh-dee-yeh-nee ger",
        "Lihat hadiah", "Lee-haht hah-dee-ah", "看 礼物", "Kàn lǐwù",
        "プレゼント 見る", "Purezento miru", "선물을 확인해", "Seonmureul hwaginhae"
    )
]

output_path = os.path.join(os.path.dirname(__file__), "..", "src", "data", "multilingual", "cat4_tech_weather_holidays.ts")
export_ts_module(output_path, "CAT4_W1", "CAT4_W2", w1, w2)
