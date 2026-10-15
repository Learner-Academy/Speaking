# Category 5: Sports & Games (5), Clothes & Style (5), Chores & Helping (5) = 15 topics
import os
import sys
sys.path.append(os.path.dirname(__file__))
from helper import item, export_ts_module

w1 = {}
w2 = {}

# 63. playing-soccer
w1["playing-soccer"] = [
    item(
        "Round ball", "گول فٹ بال", "Gol football", "गोल फ़ुटबॉल", "Gol football",
        "كرة مستديرة", "Kura mustadira", "Balón redondo", "Bah-LOHN reh-DOHN-doh",
        "Ballon rond", "Bah-lohn rohn", "Runder Fußball", "ROON-der FOOS-bahl",
        "Pallone rotondo", "Pahl-LOH-neh roh-TOHN-doh", "Bola redonda", "BOH-lah heh-DOHN-dah",
        "Круглый мяч", "KROOG-lyy myahch", "Yuvarlak futbol topu", "Yoo-vahr-lahk foot-bohl toh-poo",
        "Bola bulat", "Boh-lah boo-laht", "圆 足球", "Yuán zúqiú",
        "丸い サッカーボール", "Marui sakkābōru", "둥근 축구공", "Dunggeun chukgugong"
    ),
    item(
        "Green field", "سبز میدان", "Sabz maidaan", "हरा मैदान", "Hara maidaan",
        "ملعب أخضر", "Mal'ab akhdar", "Cancha verde", "KAHN-chah VEHR-deh",
        "Terrain vert", "Teh-ran vehr", "Grünes Spielfeld", "GREW-nes SHPEEL-felt",
        "Campo verde", "KAHM-poh VEHR-deh", "Campo verde", "KAHM-poo VEHR-jee",
        "Зелёное поле", "Zyeh-LYOH-nah-yeh POH-lyeh", "Yeşil saha", "Yeh-sheel sah-hah",
        "Lapangan hijau", "Lah-pahng-ahn hee-jow", "绿 球场", "Lǜ qiúchǎng",
        "緑の グラウンド", "Midori no guraundo", "초록 운동장", "Chorok undongjang"
    ),
    item(
        "Big goal", "بڑا گول", "Bara goal", "बड़ा गोल", "Bada goal",
        "هدف رائع", "Hadaf ra'i'", "Gran gol", "GRAHN gohl",
        "Beau but", "Boh boo", "Tolles Tor", "TOL-les tohr",
        "Bel gol", "BEHL gohl", "Golaço lindo", "Goh-LAH-soo LEEN-doo",
        "Меткий гол", "MYEHT-kiy gohl", "Harika gol", "Hah-ree-kah gohl",
        "Gol indah", "Gohl een-dah", "大 球门", "Dà qiúmén",
        "大きな ゴール", "Ōkina gōru", "멋진 골대", "Meotjin goldae"
    )
]

w2["playing-soccer"] = [
    item(
        "Kick ball", "گیند مارو", "Gend maaro", "गेंद मारो", "Gend maaro",
        "سدد الكرة", "Saddid al-kura", "Patea balón", "Pah-TEH-ah bah-LOHN",
        "Tire ballon", "Teer bah-lohn", "Schieß Ball", "SHEESS bahl",
        "Calcia palla", "KAHL-chah PAHL-lah", "Chute bola", "SHOO-chee BOH-lah",
        "Бей по мячу", "BEY pah myah-CHOO", "Topa vur", "Toh-pah voor",
        "Tendang bola", "Tehn-dahng boh-lah", "踢 足球", "Tī zúqiú",
        "ボールを 蹴る", "Bōru o keru", "공을 차봐", "Gongeul chabwa"
    ),
    item(
        "Pass friend", "دوست کو پاس دو", "Dost ko pass do", "दोस्त को पास दो", "Dost ko pass do",
        "مرر لصديقك", "Marrir li-sadiqik", "Pasa amigo", "PAH-sah ah-MEE-goh",
        "Passe ami", "Pahs ah-mee", "Pass Kumpel", "PAHS KOOM-pel",
        "Passa palla", "PAHS-sah PAHL-lah", "Toque amigo", "TAW-kee ah-MEE-goo",
        "Дай пас другу", "DYE pahs DROO-goo", "Arkadaşına pas ver", "Ahr-kah-dah-shuh-nah pahs vehr",
        "Oper ke teman", "Oh-pehr keh teh-mahn", "传 队友", "Chuán duìyǒu",
        "パスを 出す", "Pasu o dasu", "친구에게 패스해", "Chinguege paeseuhae"
    ),
    item(
        "Score goal", "گول کرو", "Goal karo", "गोल करो", "Goal karo",
        "سجل هدفاً", "Sajjil hadafan", "Anota gol", "Ah-NOH-tah gohl",
        "Marque but", "Mahrk boo", "Triff Tor", "TRIF tohr",
        "Fai gol", "FYE gohl", "Marque gol", "MAHR-kee gohl",
        "Забей гол", "Zah-BEY gohl", "Gol at", "Gohl aht",
        "Cetak gol", "Cheh-tahk gohl", "射 进门", "Shè jìnmén",
        "シュート 決める", "Shūto kimeru", "골인 성공해", "Gorin seonggonghae"
    )
]

# 64. swimming-talk
w1["swimming-talk"] = [
    item(
        "Clear pool", "صاف سوئمنگ پول", "Saaf swimming pool", "साफ़ तरणताल", "Saaf tarantaal",
        "مسبح نظيف", "Masbah nadhif", "Alberca limpia", "Ahl-BEHR-kah LEEM-pyah",
        "Bassin clair", "Bah-san klehr", "Sauberes Schwimmbecken", "ZOW-beh-res SHVIM-bek-ken",
        "Piscina pulita", "Pee-SHEE-nah poo-LEE-tah", "Piscina limpa", "Pee-SEE-nah LEEM-pah",
        "Чистый бассейн", "CHEES-tyy bahs-SYEYN", "Tertemiz havuz", "Tehr-teh-meez hah-vooz",
        "Kolam jernih", "Koh-lahm jehr-neeh", "清 泳池", "Qīng yǒngchí",
        "きれいな プール", "Kireina pūru", "깨끗한 수영장", "Kkaekkeut-han suyeongjang"
    ),
    item(
        "Blue goggles", "نیلے چشمے", "Neele chashmay", "नीला चश्मा", "Neela chashma",
        "نظارات سباحة", "Nazzarat sibaha", "Gafas azules", "GAH-fahs ah-SOO-lehs",
        "Lunettes bleues", "Loo-neht bluh", "Blaue Schwimmbrille", "BLOW-eh SHVIM-bril-leh",
        "Occhialini blu", "Ohk-kyah-LEE-nee bloo", "Óculos azuis", "AW-koo-loos ah-ZOO-ees",
        "Синие очки", "SEE-nyee-yeh ahch-KEE", "Mavi deniz gözlüğü", "Mah-vee deh-neez gerz-lew-ew",
        "Kacamata renang biru", "Kah-chah-mah-tah reh-nahng bee-roo", "蓝 泳镜", "Lán yǒngjìng",
        "青い ゴーグル", "Aoi gōguru", "파란 물안경", "Paran murangyeong"
    ),
    item(
        "Soft towel", "نرم تولیہ", "Naram toliya", "नरम तौलिया", "Naram tauliya",
        "منشفة ناعمة", "Minshafa na'ima", "Toalla suave", "Toh-AH-yah SWAH-veh",
        "Serviette douce", "Sehr-vyet doos", "Kuscheliges Badetuch", "KOOSH-eh-lee-ges BAH-deh-tookh",
        "Telo morbido", "TEH-loh MOHR-bee-doh", "Toalha fofa", "Toh-AHL-yah FAW-fah",
        "Пушистое полотенце", "Poo-SHEES-tah-yeh pah-lah-TYEHN-tseh", "Yumuşacık havlu", "Yoo-moo-shah-juhk hahv-loo",
        "Handuk lembut", "Hahn-dook lehm-boot", "软 浴巾", "Ruǎn yùjīn",
        "ふわふわの バスタオル", "Fuwafuwano basutaoru", "부드러운 타월", "Budeureo-un tawol"
    )
]

w2["swimming-talk"] = [
    item(
        "Kick water", "پانی میں پاؤں مارو", "Paani mein paaon maaro", "पानी में छपछपाओ", "Paani mein chhapchhapaao",
        "اضرب الماء", "Idrib al-ma'", "Mueve piernas", "MWEH-veh PYEHR-nahs",
        "Bats pieds", "Bah pyay", "Paddel Wasser", "PAHD-del VAHS-ser",
        "Sgambetta forte", "Zgahm-BEHT-tah FOHR-teh", "Bata pernas", "BAH-tah PEHR-nahs",
        "Болтай ножками", "Bahl-TYE NOHZH-kah-mee", "Ayak çırp", "Ah-yahk chuhrp",
        "Kecipak kaki", "Keh-chee-pahk kah-kee", "打 水花", "Dǎ shuǐhuā",
        "バタ足 する", "Bataashi suru", "발차기 힘차게해", "Balchagi himchagehae"
    ),
    item(
        "Blow bubbles", "بلبلے بناؤ", "Bulbulay banao", "बुलबुले बनाओ", "Bulbule banaao",
        "انفخ فقاعات", "Infukh fuqa'at", "Haz burbujas", "AHS boor-BOO-hahs",
        "Fais bulles", "Feh bool", "Puste Blasen", "POOS-teh BLAH-zen",
        "Fai bolle", "FYE BOHL-leh", "Faça bolinhas", "FAH-sah boh-LEEN-yahs",
        "Пускай пузыри", "Poos-KYE poo-zy-REE", "Baloncuk çıkar", "Bah-lohn-jook chuh-kahr",
        "Bikin gelembung", "Bee-keen geh-lehm-boong", "吹 气泡", "Chuī qìpào",
        "ブクブク 泡を出す", "Bukubuku awa o dasu", "보글보글 물방울", "Bogeulbogeul mulbang-ul"
    ),
    item(
        "Dry body", "جسم خشک کرو", "Jism khushk karo", "शरीर पोंछो", "Shareer poncho",
        "جفف نفسك", "Jaffif nafsak", "Sécate bien", "SEH-kah-teh byan",
        "Essuie-toi bien", "Eh-swee twah byan", "Trockne ab", "TROK-neh ahp",
        "Asciugati bene", "Ah-SHOO-gah-tee BEH-neh", "Seque o corpo", "SEH-kee oo KOHR-poo",
        "Вытрись насухо", "VY-trees NAH-soo-khah", "İyice kurulan", "Ee-yee-jeh koo-roo-lahn",
        "Keringkan badan", "Keh-reeng-kahn bah-dahn", "擦 干身体", "Cā gānshēntǐ",
        "しっかり 拭く", "Shikkari fuku", "물기 닦아내", "Mulgi dakka-nae"
    )
]

# 65. team-games
w1["team-games"] = [
    item(
        "Strong team", "مضبوط ٹیم", "Mazboot team", "मज़बूत टीम", "Mazboot team",
        "فريق متحد", "Fariq muttahid", "Equipo unido", "Eh-KEE-poh oo-NEE-doh",
        "Belle équipe", "Bel ay-keep", "Starkes Team", "SHTAHR-kes teem",
        "Squadra forte", "SKWAH-drah FOHR-teh", "Equipe unida", "Eh-KEE-pee oo-NEE-dah",
        "Дружная команда", "DROOZH-nah-yah kah-MAHN-dah", "Güçlü takım", "Gewch-lew tah-kuhm",
        "Tim kompak", "Teem kohm-pahk", "强 队伍", "Qiáng duìwu",
        "強い チーム", "Tsuyoi chīmu", "튼튼한 팀워크", "Teunteun-han timwokeu"
    ),
    item(
        "Red jersey", "سرخ جرسی", "Surkh jersey", "लाल जर्सी", "Laal jersey",
        "قميص أحمر", "Qamis ahmar", "Camiseta roja", "Kah-mee-SEH-tah ROH-hah",
        "Maillot rouge", "Mah-yoh roozh", "Rotes Trikot", "ROH-tes tree-KOH",
        "Maglia rossa", "MAH-lyah ROHS-sah", "Camisa vermelha", "Kah-MEE-zah vehr-MEHL-yah",
        "Красная форма", "KRAHS-nah-yah FOHR-mah", "Kırmızı forma", "Kuhr-muh-zuh fohr-mah",
        "Kaos merah", "Kah-ohs meh-rah", "红 球衣", "Hóng qiúyī",
        "赤い ユニフォーム", "Akai yunifōmu", "빨간 유니폼", "Ppalgan yunipom"
    ),
    item(
        "Loud cheer", "زوردار نعرہ", "Zordaar naara", "ज़ोरदार उत्साह", "Zordaar utsaah",
        "هتاف عال", "Hutaf 'alin", "Porra alegre", "POH-rrah ah-LEH-greh",
        "Clameur joyeuse", "Klah-muhr zhwah-yuhz", "Lauter Jubel", "LOW-ter YOO-bel",
        "Coro entusiasta", "KOH-roh ehn-too-ZYAH-stah", "Grito de torcida", "GREE-too jee tohr-SEE-dah",
        "Громкая поддержка", "GROHM-kah-yah pahd-DYEHRZH-kah", "Coşkulu tezahürat", "Johsh-koo-loo teh-zah-hew-raht",
        "Sorak semangat", "Soh-rahk seh-mahng-aht", "齐 助威", "Qí zhùwēi",
        "熱い 応援", "Atsui ōen", "우렁찬 응원", "Ureongchan eung-won"
    )
]

w2["team-games"] = [
    item(
        "Pass baton", "رلے بڑھاؤ", "Relay barhao", "डंडा आगे बढ़ाओ", "Danda aage badhaao",
        "سلم الراية", "Sallim ar-raya", "Pasa relevo", "PAH-sah reh-LEH-voh",
        "Passe témoin", "Pahs tay-mwan", "Reich Stab", "RYE-kh shtahp",
        "Passa testimone", "PAHS-sah tehs-tee-MOH-neh", "Passe bastão", "PAH-see bahs-TOWN",
        "Передай эстафету", "Pyeh-ryeh-DAY ehs-tah-FYEH-too", "Bayrağı uzat", "By-rah-uh oo-zaht",
        "Oper tongkat", "Oh-pehr tohng-kaht", "接力 交棒", "Jièlì jiāobàng",
        "バトン 渡す", "Baton watasu", "바통을 건네줘", "Batongeul geonnejwo"
    ),
    item(
        "Cheer loud", "حوصلہ بڑھاؤ", "Housla barhao", "उत्साह बढ़ाओ", "Utsaah badhaao",
        "شجع رفاقك", "Shajji' rifaqak", "Anima fuerte", "Ah-NEE-mah FWEHR-teh",
        "Encourage amis", "Ahn-koo-rahzh ah-mee", "Feu're an", "FOY-reh ahn",
        "Tifa con grinta", "TEE-fah kohn GREEN-tah", "Torça muito", "TOHR-sah MOON-too",
        "Поддержи друзей", "Pahd-dyehr-ZHY droo-ZYEY", "Takımını destekle", "Tah-kuh-muh-nuh dehs-tek-leh",
        "Beri semangat", "Beh-ree seh-mahng-aht", "大声 加油", "Dàshēng jiāyóu",
        "大きな声で 応援する", "Ōkina koe de ōen-suru", "힘차게 응원해", "Himchage eung-wonhae"
    ),
    item(
        "Celebrate together", "جشن مناؤ", "Jashan manao", "साथ जश्न मनाओ", "Saath jashn manaao",
        "احتفلوا معاً", "Ihtafile ma'an", "Celebren juntos", "Seh-LEH-brehn HOON-tohs",
        "Fêtez ensemble", "Feh-tay ahn-sahn-bluh", "Feiert zusammen", "FY-ert tsoo-ZAHM-men",
        "Festeggia insieme", "Fehs-TEHD-jah een-SYEH-meh", "Comemore juntos", "Koh-meh-MAW-ree ZHOON-toos",
        "Празднуйте вместе", "PRAHZD-nooy-tyeh VMYEHS-tyeh", "Birlikte sevinin", "Beer-leek-teh seh-vee-neen",
        "Rayakan bersama", "Rah-yah-kahn behr-sah-mah", "共同 庆祝", "Gòngtóng qìngzhù",
        "みんなで 喜ぶ", "Minna de yorokobu", "다함께 축하해", "Dahamkke chukhahae"
    )
]

# 66. winning-and-losing
w1["winning-and-losing"] = [
    item(
        "Bright medal", "چمکتا تمغہ", "Chamakta tamgha", "चमकता पदक", "Chamakta padak",
        "ميدالية ذهبية", "Midaliya dhahabiyya", "Medalla brillante", "Meh-DAH-yah bree-YAHN-teh",
        "Médaille d'or", "May-die dohr", "Glänzende Medaille", "GLEN-tsen-deh meh-DAHL-lyeh",
        "Medaglia lucente", "Meh-DAH-lyah loo-CHEHN-teh", "Medalha dourada", "Meh-DAHL-yah doh-RAH-dah",
        "Золотая медаль", "Zah-lah-TAH-yah myeh-DAHL", "Parlak madalya", "Pahr-lahk mah-dahl-yah",
        "Medali emas", "Meh-dah-lee eh-mahs", "闪 奖牌", "Shǎn jiǎngpái",
        "輝く メダル", "Kagayaku medaru", "반짝이는 메달", "Banjjagineun medal"
    ),
    item(
        "Good sport", "اچھا کھلاڑی", "Achha khilaari", "सच्चा खिलाड़ी", "Sachha khilaadi",
        "روح رياضية", "Ruh riyadiyya", "Deportista noble", "Deh-pohr-TEES-tah NOH-bleh",
        "Esprit sportif", "Ehs-pree spohr-teef", "Faires Spiel", "FY-res shpeel",
        "Spirito sportivo", "SPEE-ree-toh spohr-TEE-voh", "Espírito esportivo", "Ehs-PEE-ree-too ehs-pohr-CHEE-voo",
        "Честная игра", "CHYEHST-nah-yah eeg-RAH", "Centilmen duruş", "Jen-teel-men doo-roosh",
        "Jiwa sportif", "Jee-wah spohr-teef", "好 风范", "Hǎo fēngfàn",
        "フェアプレー 精神", "Feapurē seishin", "멋진 스포츠맨십", "Meotjin seupocheumaensip"
    ),
    item(
        "Warm handshake", "دوستانہ مصافحہ", "Dostana musafaha", "सद्भावना हाथ मिलाना", "Sadbhaawana haath milaana",
        "مصافحة ودية", "Musafaha widdiyya", "Apretón cordial", "Ah-preh-TOHN kohr-DYAHL",
        "Poignée chaleureuse", "Pwah-nyay shah-luh-ruhz", "Herzlicher Händedruck", "HEHRTS-likh-er HEN-deh-drook",
        "Stretta amichevole", "STREHT-tah ah-mee-KEH-voh-leh", "Aperto de mão", "Ah-PEHR-too jee mown",
        "Дружеское рукопожатие", "DROO-zheh-skah-yeh roo-kah-pah-ZHAH-tyee-yeh", "Dostça tokalaşma", "Dohst-chah toh-kah-lahsh-mah",
        "Jabat tangan hangat", "Jah-baht tahng-ahn hahng-aht", "握 手言和", "Wò shǒuyánhé",
        "温かい 握手", "Atatakai akushu", "따뜻한 악수", "Ttatteut-han aksu"
    )
]

w2["winning-and-losing"] = [
    item(
        "Say good game", "اچھا کھیلے", "Achha khelay", "अच्छा खेले", "Achha khele",
        "قل لعبنا جيداً", "Qul la'ibna jayyidan", "Di bien jugado", "DEE byan hoo-GAH-doh",
        "Dis beau match", "Dee boh mahtsh", "Sag Gut gespielt", "ZAHK goot geh-SHPEELT",
        "Dì bella partita", "DEE BEHL-lah pahr-TEE-tah", "Diga bom jogo", "JEE-gah bohn ZHOH-goo",
        "Скажи отличная игра", "Skah-ZHY aht-LEECH-nah-yah eeg-RAH", "Tebrik et", "Tehb-reek et",
        "Ucap main bagus", "Oo-chahp my-een bah-goos", "互 道精彩", "Hù dàojīngcǎi",
        "「いい試合だった」と称える", "Ii shiai datta to tataeru", "멋진 경기였다고 칭찬해", "Meotjin gyeong-giyeottago chingchanhae"
    ),
    item(
        "Shake hands", "ہاتھ ملاؤ", "Haath milao", "हाथ मिलाओ", "Haath milaao",
        "صافح منافسك", "Safih munafisak", "Estrecha manos", "Ehs-TREH-chah MAH-nohs",
        "Serre la main", "Sehr lah man", "Gib Hand", "GIP hahnt",
        "Stringi la mano", "STREEN-jee lah MAH-noh", "Aperte as mãos", "Ah-PEHR-chee ahs mowns",
        "Пожми руку сопернику", "Pahzh-MEE ROO-koo sah-PYEHR-nee-koo", "El sıkış", "Ehl suh-kuhsh",
        "Bersalaman sportif", "Behr-sah-lah-mahn spohr-teef", "双方 握手", "Shuāngfāng wòshǒu",
        "握手を 交わす", "Akushu o kawasu", "서로 손잡아", "Seoro sonjaba"
    ),
    item(
        "Try again", "دوبارہ کوشش کرو", "Dobara koshish karo", "फिर कोशिश करो", "Phir koshish karo",
        "حاول مجدداً", "Hawil mujaddadan", "Intenta de nuevo", "Een-TEHN-tah deh NWEH-voh",
        "Recommence avec le sourire", "Ruh-koh-mahns ah-vehk luh soo-reer", "Versuch's noch mal", "Fehr-ZOOKHS nokh mahl",
        "Riprova con grinta", "Ree-PROH-vah kohn GREEN-tah", "Tente outra vez", "TEHN-chee OH-trah vez",
        "Попробуй снова", "Pah-PROH-buy SNOH-vah", "Tekrar dene", "Tek-rahr deh-neh",
        "Coba lagi nanti", "Choh-bah lah-gee nahn-tee", "再 接再厉", "Zài jiēzàilì",
        "また 挑戦する", "Mata chōsen-suru", "다시 도전해", "Dasi dojeonhae"
    )
]

# 67. riding-a-bike
w1["riding-a-bike"] = [
    item(
        "Red bicycle", "سرخ سائیکل", "Surkh bicycle", "लाल साइकिल", "Laal cycle",
        "دراجة حمراء", "Darraja hamra'", "Bici roja", "BEE-see ROH-hah",
        "Vélo rouge", "Vay-loh roozh", "Rotes Fahrrad", "ROH-tes FAHR-raht",
        "Bici rossa", "BEE-chee ROHS-sah", "Bicicleta vermelha", "Bee-see-KLAY-tah vehr-MEHL-yah",
        "Красный велосипед", "KRAHS-nyy vye-lah-see-PYEHT", "Kırmızı bisiklet", "Kuhr-muh-zuh bee-seek-let",
        "Sepeda merah", "Seh-peh-dah meh-rah", "红 自行车", "Hóng zìxíngchē",
        "赤い 自転車", "Akai jitensha", "빨간 자전거", "Ppalgan jajeon-geo"
    ),
    item(
        "Safe helmet", "حفاظتی ہیلمٹ", "Hifaazati helmet", "सुरक्षा हेलमेट", "Suraksha helmet",
        "خوذة واقية", "Khudha waqiya", "Casco seguro", "KAHS-koh seh-GOO-roh",
        "Casque solide", "Kahsk soh-leed", "Sicherer Helm", "ZIKH-er-er helm",
        "Casco protettivo", "KAHS-koh proh-teht-TEE-voh", "Capacete seguro", "Kah-pah-SAY-chee seh-GOO-roo",
        "Надёжный шлем", "Nah-DYOHZH-nyy shlyem", "Koruyucu kask", "Koh-roo-yoo-joo kahsk",
        "Helm pengaman", "Hehlm peh-ngah-mahn", "牢 头盔", "Láo tóukuī",
        "安全な ヘルメット", "Anzenna herumetto", "안전 헬멧", "Anjeon helmet"
    ),
    item(
        "Smooth road", "ہموار سڑک", "Hamwaar sarak", "साफ़ सड़क", "Saaf sadak",
        "طريق ممهد", "Tariq mumahhad", "Camino plano", "Kah-MEE-noh PLAH-noh",
        "Piste lisse", "Peest lees", "Ebener Radweg", "AY-beh-ner RAHT-vayk",
        "Pista ciclabile", "PEES-tah chee-KLAH-bee-leh", "Pista plana", "PEES-tah PLAH-nah",
        "Ровная дорожка", "ROHV-nah-yah dah-ROHZH-kah", "Düzgün bisiklet yolu", "Dewz-gewn bee-seek-let yoh-loo",
        "Jalanan mulus", "Jah-lahn-ahn moo-loos", "平 道路", "Píng dàolù",
        "走りやすい 道", "Hashiriyasui michi", "매끄러운 길", "Maekkeureoun gil"
    )
]

w2["riding-a-bike"] = [
    item(
        "Wear helmet", "ہیلمٹ پہنو", "Helmet pehno", "हेलमेट पहनो", "Helmet pehno",
        "ارتد الخوذة", "Irtadi al-khudha", "Ponte casco", "POHN-teh KAHS-koh",
        "Mets casque", "Meh kahsk", "Setz Helm auf", "ZEHTS helm owf",
        "Allaccia casco", "Ahl-LAHT-chah KAHS-koh", "Coloque capacete", "Koh-LAW-kee kah-pah-SAY-chee",
        "Надень шлем", "Nah-DYEHN shlyem", "Kaskını tak", "Kahs-kuh-nuh tahk",
        "Pakai helm", "Pah-kye hehlm", "戴好 头盔", "Dàihǎo tóukuī",
        "ヘルメット かぶる", "Herumetto kaburu", "헬멧을 착용해", "Helmeseul chagyonghae"
    ),
    item(
        "Pedal fast", "پیڈل مارو", "Pedal maaro", "पैडल मारो", "Pedal maaro",
        "اضغط الدواسات", "Idghat ad-dawwasat", "Pedalea alegre", "Peh-dah-LEH-ah ah-LEH-greh",
        "Pédale bien", "Pay-dahl byan", "Tritt Pedale", "TRIT peh-DAH-leh",
        "Pedala forte", "Peh-DAH-lah FOHR-teh", "Pedale com ritmo", "Peh-DAH-lee kohn HEET-moo",
        "Крути педали", "Kroo-TEE pyeh-DAH-lee", "Pedalları çevir", "Peh-dahl-lah-ruh cheh-veer",
        "Kayuh sepeda", "Kah-yooh seh-peh-dah", "蹬 脚踏板", "Dēng jiǎotàbǎn",
        "ペダルを こぐ", "Pedaru o kogu", "페달을 밟아", "Pedareul balba"
    ),
    item(
        "Ring bell", "گھنٹی بجاؤ", "Ghanti bajao", "घंटी बजाओ", "Ghanti bajaao",
        "دق الجرس", "Duqq al-jaras", "Toca timbre", "TOH-kah TEEM-breh",
        "Sonne sonnette", "Sohn soh-neht", "Klingle laut", "KLING-leh lowt",
        "Suona campanello", "SWAW-nah kahm-pah-NEHL-loh", "Toque campainha", "TAW-kee kahm-pah-EEN-yah",
        "Звони в звоночек", "Zvah-NEE v zvah-NOH-cheek", "Zili çal", "Zee-lee chahl",
        "Bunyikan bel", "Boo-nyee-kahn behl", "按 车铃", "Àn chēlíng",
        "ベルを 鳴らす", "Beru o narasu", "따릉이 울려", "Ttareung-i ulryeo"
    )
]

# 68. choosing-clothes
w1["choosing-clothes"] = [
    item(
        "Bright shirt", "چمکیلی قمیض", "Chamkeeli qameez", "चमकीली क़मीज़", "Chamkeeli qameez",
        "قميص زاه", "Qamis zahin", "Camisa bonita", "Kah-MEE-sah boh-NEE-tah",
        "T-shirt coloré", "Tee-shuhrt koh-loh-ray", "Buntes Hemd", "BOON-tes hemt",
        "Maglietta colorata", "Mah-LYEHT-tah koh-loh-RAH-tah", "Camisa alegre", "Kah-MEE-zah ah-LEH-gree",
        "Яркая рубашка", "YAHR-kah-yah roo-BAHSH-kah", "Renkli gömlek", "Renk-lee germ-lek",
        "Kemeja cerah", "Keh-meh-jah cheh-rah", "亮 衬衫", "Liàng chènshān",
        "明るい シャツ", "Akarui shatsu", "화사한 셔츠", "Hwasahan syeocheu"
    ),
    item(
        "Blue pants", "نیلی پتلون", "Neeli patloon", "नीली पैंट", "Neeli pant",
        "بنطال أزرق", "Bintal azraq", "Pantalones azules", "Pahn-tah-LOH-nehs ah-SOO-lehs",
        "Pantalon bleu", "Pahn-tah-lohn bluh", "Blaue Hose", "BLOW-eh HOH-zeh",
        "Pantaloni blu", "Pahn-tah-LOH-nee bloo", "Calça azul", "KAHL-sah ah-ZOOL",
        "Синие брючки", "SEE-nyee-yeh BRYOOTSH-kee", "Mavi pantolon", "Mah-vee pahn-toh-lohn",
        "Celana biru", "Cheh-lah-nah bee-roo", "蓝 裤子", "Lán kùzi",
        "青い ズボン", "Aoi zubon", "파란 바지", "Paran baji"
    ),
    item(
        "Warm sweater", "گرم سویٹر", "Garam sweater", "गर्म स्वेटर", "Garm sweater",
        "كنزة صوفية", "Kanza sufiyya", "Suéter calientito", "SWEH-tehr kah-lyen-TEE-toh",
        "Pull chaud", "Pool sho", "Kuscheliger Pullover", "KOOSH-eh-lee-ger pool-LOH-ver",
        "Maglione caldo", "Mah-LYOH-neh KAHL-doh", "Suéter quentinho", "SWAY-tehr ken-CHEEN-yoo",
        "Тёплый свитер", "TYOHP-lyy SVYEE-tyer", "Sıcak kazak", "Suh-dzhak kah-zahk",
        "Sweter hangat", "Sweh-tehr hahng-aht", "暖 毛衣", "Nuǎn máoyī",
        "暖かい セーター", "Atatakai sētā", "따뜻한 스웨터", "Ttatteut-han seuweteo"
    )
]

w2["choosing-clothes"] = [
    item(
        "Pick shirt", "قمیض چنو", "Qameez chuno", "क़मीज़ चुनो", "Qameez chuno",
        "اختر قميصاً", "Ikhtar qamisan", "Elige camisa", "Eh-LEE-heh kah-MEE-sah",
        "Choisis t-shirt", "Shwah-zee tee-shuhrt", "Wähl T-Shirt", "VAYL TEE-shirt",
        "Scegli maglia", "SHEH-lyee MAH-lyah", "Escolha camisa", "Ehs-KOHL-yah kah-MEE-zah",
        "Выбери кофту", "VY-bye-ree KOHF-too", "Gömleğini seç", "Germ-leh-ee-nee sech",
        "Pilih kemeja", "Pee-leeh keh-meh-jah", "选 衬衫", "Xuǎn chènshān",
        "シャツを 選ぶ", "Shatsu o erabu", "셔츠를 골라", "Syeocheureul golla"
    ),
    item(
        "Match colors", "رنگ ملاؤ", "Rang milao", "रंग मिलाओ", "Rang milaao",
        "نسق الألوان", "Nassiq al-alwan", "Combina ropa", "Kohm-BEE-nah ROH-pah",
        "Assortis couleurs", "Ah-sohr-tee koo-luhr", "Stimm Farben ab", "SHTIM FAHR-ben ahp",
        "Abbina colori", "Ahb-BEE-nah koh-LOH-ree", "Combine cores", "Kohm-BEE-nee KAW-rees",
        "Подбери цвета", "Pahd-bye-REE tsvyeh-TAH", "Renkleri uydur", "Renk-leh-ree oo-y-door",
        "Padukan warna", "Pah-doo-kahn wahr-nah", "配 颜色", "Pèi yánsè",
        "色を 合わせる", "Iro o awaseru", "색상을 맞춰봐", "Saeksang-eul matchwobwa"
    ),
    item(
        "Wear dress", "لباس پہنو", "Libaas pehno", "पोशाक पहनो", "Poshaak pehno",
        "البس فستانك", "Ilbas fustanak", "Ponte vestido", "POHN-teh vehs-TEE-doh",
        "Enfile tenue", "Ahn-feel tuh-noo", "Zieh Kleid an", "TSEE klyte ahn",
        "Metti vestito", "MEHT-tee vehs-TEE-toh", "Vista vestido", "VEES-tah vehs-CHEE-doo",
        "Надень наряд", "Nah-DYEHN nah-RYAHT", "Elbiseni giy", "Ehl-bee-seh-nee geey",
        "Kenakan gaun", "Keh-nah-kahn gah-oon", "穿 新衣", "Chuān xīnyī",
        "服を 着る", "Fuku o kiru", "옷을 입어", "Oseul ibeo"
    )
]

# 69. tying-shoes
w1["tying-shoes"] = [
    item(
        "Long shoelace", "لمبا تسمہ", "Lamba tasma", "लंबा फ़ीता", "Lamba feeta",
        "رباط طويل", "Ribat tawil", "Cordón largo", "Kohr-DOHN LAHR-goh",
        "Lacet souple", "Lah-seh soopl", "Langer Schnürsenkel", "LAHN-ger SHNOOR-zeng-kel",
        "Laccio lungo", "LAHT-choh LOON-goh", "Cadarço comprido", "Kah-DAHR-soo kohm-PREE-doo",
        "Длинный шнурок", "DLEEN-nyy shnoo-ROHK", "Uzun ayakkabı bağcığı", "Oo-zoon ah-yahk-kah-buh bah-juh-uh",
        "Tali sepatu panjang", "Tah-lee seh-pah-too pahn-jahng", "长 鞋带", "Cháng xiédài",
        "長い 靴ひも", "Nagai kutsuhimo", "긴 신발끈", "Gin sinbalkkeun"
    ),
    item(
        "Clean sneaker", "صاف جوتا", "Saaf joota", "साफ़ जूता", "Saaf joota",
        "حذاء رياضي", "Hitha' riyadiy", "Zapatilla limpia", "Sah-pah-TEE-yah LEEM-pyah",
        "Basket propre", "Bahs-keht proh-pruh", "Sauberer Turnschuh", "ZOW-ber-er TOORN-shoo",
        "Scarpa pulita", "SKAHR-pah poo-LEE-tah", "Tênis limpinho", "TAY-nees leem-PEEN-yoo",
        "Чистый кроссовок", "CHEES-tyy krahs-SOH-vahk", "Temiz spor ayakkabı", "Teh-meez spohr ah-yahk-kah-buh",
        "Sepatu kets rapi", "Seh-pah-too kehts rah-pee", "净 运动鞋", "Jìng yùndòngxié",
        "清潔な スニーカー", "Seiketsuna sunīkā", "깔끔한 운동화", "Kkalkkeum-han undonghwa"
    ),
    item(
        "Tight knot", "مضبوط گرہ", "Mazboot girah", "पक्की गाँठ", "Pakki gaanth",
        "عقدة محكمة", "'Uqda muhkama", "Nudo firme", "NOO-doh FEER-meh",
        "Nœud solide", "Nuh soh-leed", "Fester Knoten", "FEHS-ter KNOH-ten",
        "Nodo stretto", "NOH-doh STREHT-toh", "Nó firme", "NAW FEER-mee",
        "Крепкий узелок", "KRYEHP-kiy oo-zye-LOHK", "Sıkı düğüm", "Suh-kuh dew-yewm",
        "Simpul erat", "Seem-pool eh-raht", "紧 绳结", "Jǐn shéngjié",
        "しっかりした 結び目", "Shikkarishita musubime", "단단한 매듭", "Dandan-han maedeup"
    )
]

w2["tying-shoes"] = [
    item(
        "Cross laces", "تسمے آر پار کرو", "Tasmay aar paar karo", "फ़ीते क्रास करो", "Feete cross karo",
        "قاطع الرباطين", "Qati' ar-ribatayn", "Cruza cordones", "KROO-sah kohr-DOH-nehs",
        "Croise lacets", "Krwahz lah-seh", "Überkreuz Schnürsenkel", "OO-ber-kroyts SHNOOR-zeng-kel",
        "Incrocia lacci", "Een-KROH-chah LAHT-chee", "Cruze cadarços", "KROO-zee kah-DAHR-soos",
        "Скрести шнурочки", "Skryes-TEE shnoo-ROHCH-kee", "Bağcıkları çaprazla", "Bah-juhk-lah-ruh chahp-rahz-lah",
        "Silangkan tali", "See-lahng-kahn tah-lee", "交叉 鞋带", "Jiāochā xiédài",
        "ひもを 交差させる", "Himo o kōsasaseru", "끈을 교차시켜", "Kkeuneul gyochasikyeo"
    ),
    item(
        "Make loop", "کنڈی بناؤ", "Kundi banao", "लूप बनाओ", "Loop banaao",
        "اصنع حلقة", "Isna' halaqa", "Haz orejita", "AHS oh-reh-HEE-tah",
        "Forme boucle", "Fohrm bookl", "Mach Schleife", "MAHKH SHLY-feh",
        "Fai asola", "FYE ah-ZOH-lah", "Faça laço", "FAH-sah LAH-soo",
        "Сделай петельку", "SDYEH-lye pyeh-TYEHL-koo", "Halka yap", "Hahl-kah yahp",
        "Bentuk lingkaran tali", "Behn-took leeng-kah-rahn tah-lee", "捏出 圈圈", "Niēchū quānquān",
        "輪っかを 作る", "Wakka o tsukuru", "고리를 만들어", "Gorireul mandeureo"
    ),
    item(
        "Pull tight", "زور سے کھینچو", "Zor se kheecho", "कसकर खींचो", "Kaskar kheecho",
        "شد بإحكام", "Shudd bi-ihkam", "Jala fuerte", "HAH-lah FWEHR-teh",
        "Tire fort", "Teer fohr", "Zieh fest", "TSEE fehst",
        "Tira bene", "TEE-rah BEH-neh", "Puxe firme", "POO-shee FEER-mee",
        "Затяни крепко", "Zah-tyah-NEE KRYEHP-kah", "İyice sık", "Ee-yee-jeh suhk",
        "Tarik kencang", "Tah-reek kehn-chahng", "拉紧 蝴蝶结", "Lājǐn húdiéjié",
        "ぎゅっと 引っ張る", "Gyutto hipparu", "꼭 잡아당겨", "Kkok jabadanggyeo"
    )
]

# 70. washing-face
w1["washing-face"] = [
    item(
        "Cool water", "ٹھنڈا پانی", "Thanda paani", "ठंडा पानी", "Thanda paani",
        "ماء منعش", "Ma' mun'ish", "Agua fresca", "AH-gwah FREHS-kah",
        "Eau fraîche", "Oh frehsh", "Kühles Wasser", "KOO-les VAHS-ser",
        "Acqua fresca", "AHK-wah FREHS-kah", "Água fresquinha", "AH-gwah frehs-KEEN-yah",
        "Прохладная вода", "Prahkh-LAHD-nah-yah vah-DAH", "Serin su", "Seh-reen soo",
        "Air segar", "Ah-yeer seh-gahr", "清 凉水", "Qīng liángshuǐ",
        "冷たい お水", "Tsumetai omizu", "시원한 물", "Siwon-han mul"
    ),
    item(
        "White foam", "سفید جھاگ", "Safaid jhaag", "सफ़ेद झाग", "Safed jhaag",
        "رغوة صابون", "Raghwat sabun", "Espuma suave", "Ehs-POO-mah SWAH-veh",
        "Mousse douce", "Moos doos", "Weicher Seifenschaum", "VY-kher ZY-fen-showm",
        "Schiuma soffice", "SKYW-mah SOHF-fee-cheh", "Espuma cremosa", "Ehs-POO-mah kreh-MOH-zah",
        "Белая пенка", "BYEH-lah-yah PYEHN-kah", "Köpüklü sabun", "Ker-pewk-lew sah-boon",
        "Busa lembut", "Boo-sah lehm-boot", "白 泡沫", "Bái pàomò",
        "モコモコの 泡", "Mokomoko no awa", "풍성한 거품", "Pungseong-han geopum"
    ),
    item(
        "Dry towel", "خشک تولیہ", "Khushk toliya", "सूखा तौलिया", "Sookha tauliya",
        "منشفة نظيفة", "Minshafa nadhifa", "Toalla limpia", "Toh-AH-yah LEEM-pyah",
        "Serviette douce", "Sehr-vyet doos", "Trockenes Handtuch", "TROK-neh-nes HAHNT-tookh",
        "Asciugamano morbido", "Ah-shoo-gah-MAH-noh MOHR-bee-doh", "Toalha sequinha", "Toh-AHL-yah seh-KEEN-yah",
        "Сухое полотенчико", "Soo-KHOY-eh pah-lah-TYEHN-chee-kah", "Yumuşak kuru havlu", "Yoo-moo-shahk koo-roo hahv-loo",
        "Handuk kering rapi", "Hahn-dook keh-reeng rah-pee", "干 毛巾", "Gān máojīn",
        "乾いた タオル", "Kawaita taoru", "뽀송한 수건", "Pposong-han sugeon"
    )
]

w2["washing-face"] = [
    item(
        "Splash water", "چھینٹے مارو", "Chheentay maaro", "छींटे मारो", "Chheente maaro",
        "رش الماء", "Rushsh al-ma'", "Salpica agua", "Sahl-PEE-kah AH-gwah",
        "Éclabousse eau", "Ay-klah-boos oh", "Spritz Wasser", "SHPRITS VAHS-ser",
        "Sciacqua viso", "SHAHK-kwah VEE-zoh", "Jogue água", "ZHOH-gee AH-gwah",
        "Ополосни личико", "Ah-pah-lahs-NEE LEE-cheek-kah", "Su serp", "Soo sehrp",
        "Percikkan air", "Pehr-cheek-kahn ah-yeer", "泼 清水", "Pō qīngshuǐ",
        "水で バシャバシャ洗う", "Mizu de bashabasha arau", "물을 찰방찰방 묻혀", "Mureul chalbangchalbang muthyeo"
    ),
    item(
        "Rub cheeks", "گال ملو", "Gaal malo", "गाल मलो", "Gaal malo",
        "افرك وجنتيك", "Ufruk wajnatayk", "Frota mejillas", "FROH-tah meh-HEE-yahs",
        "Frotte joues", "Froht zhoo", "Reib Wangen", "RYEP VAHNG-en",
        "Strofina guance", "Stroh-FEE-nah GWAHN-cheh", "Esfregue bochechas", "Ehs-FRAY-gee boh-SHAY-kahs",
        "Потри щёчки", "Pah-TREE SHCHYOHCH-kee", "Yanakları ov", "Yah-nahk-lah-ruh ohv",
        "Usap pipi", "Oo-sahp pee-pee", "搓 脸颊", "Cuō liǎnjiá",
        "ほっぺた こする", "Hoppeta kosuru", "볼을 문질러", "Boreul munjilleo"
    ),
    item(
        "Pat dry", "تولیے سے خشک کرو", "Toliye se khushk karo", "थपकी देकर पोंछो", "Thapki dekar poncho",
        "جفف بلطف", "Jaffif bi-lutf", "Seca suave", "SEH-kah SWAH-veh",
        "Tamponne doucement", "Tahm-pohn doos-mahn", "Tupf trocken", "TOOPF TROK-ken",
        "Tampona piano", "Tahm-POH-nah PYAH-noh", "Seque delicadamente", "SEH-kee deh-lee-kah-dah-MEHN-chee",
        "Промокни полотенцем", "Prah-mahk-NEE pah-lah-TYEHN-tsem", "Havluyla kurula", "Hahv-looy-lah koo-roo-lah",
        "Tepuk perlahan hingga kering", "Teh-pook pehr-lah-hahn heeng-gah keh-reeng", "轻 擦干", "Qīng cāgān",
        "タオルで 押さえる", "Taoru de osaeru", "수건으로 톡톡닦아", "Sugeoneuro toktokdakka"
    )
]

# 71. getting-dressed
w1["getting-dressed"] = [
    item(
        "Neat outfit", "صاف لباس", "Saaf libaas", "साफ़ पोशाक", "Saaf poshaak",
        "ملابس مرتبة", "Malabis murattaba", "Ropa ordenada", "ROH-pah ohr-deh-NAH-dah",
        "Tenue propre", "Tuh-noo proh-pruh", "Ordentliche Kleidung", "OHR-dent-likh-eh KLY-doong",
        "Vestiti ordinati", "Vehs-TEE-tee ohr-dee-NAH-tee", "Roupa limpinha", "HOH-pah leem-PEEN-yah",
        "Аккуратная одежда", "Ahk-koo-RAHT-nah-yah ah-DYEHZH-dah", "Düzgün kıyafet", "Dewz-gewn kuh-yah-fet",
        "Pakaian rapi", "Pah-kye-ahn rah-pee", "整 衣服", "Zhěng yīfu",
        "きちんとした 服", "Kichintoshita fuku", "단정한 옷차림", "Danjeong-han otcharim"
    ),
    item(
        "Small button", "چھوٹا بٹن", "Chhota button", "छोटा बटन", "Chhota button",
        "زر صغير", "Zirr saghir", "Botón pequeño", "Boh-TOHN peh-KAY-nyoh",
        "Petit bouton", "Puh-tee boo-tohn", "Kleiner Knopf", "KLY-ner knohpf",
        "Bottone piccolo", "Boht-TOH-neh PEEK-koh-loh", "Botão pequeno", "Boh-TOWN peh-KAY-noo",
        "Маленькая пуговица", "MAH-lyen-kah-yah POO-gah-vee-tsah", "Küçük düğme", "Kew-chewk dew-meh",
        "Kancing kecil", "Kahn-cheeng keh-cheel", "小 纽扣", "Xiǎo niǔkòu",
        "小さな ボタン", "Chiisana botan", "작은 단추", "Jageun danchu"
    ),
    item(
        "Cozy coat", "آرام دہ کوٹ", "Aaram deh coat", "आरामदेह कोट", "Aaraamdeh coat",
        "معطف دافئ", "Mi'taf dafi'", "Abrigo cómodo", "Ah-BREE-goh KOH-moh-doh",
        "Manteau doux", "Mahn-toh doo", "Gemütliche Jacke", "Geh-MYOOT-likh-eh YAHK-keh",
        "Cappotto comodo", "Kahp-POHT-toh KOH-moh-doh", "Casaco aconchegante", "Kah-ZAH-koo ah-kohn-sheh-GAHN-chee",
        "Уютное пальто", "Oo-YOOT-nah-yeh pahl-TOH", "Rahat kaban", "Rah-haht kah-bahn",
        "Mantel nyaman", "Mahn-tehl nyah-mahn", "暖 外套", "Nuǎn wàitào",
        "着心地の 良いコート", "Kigokochi no yoi kōto", "포근한 코트", "Pogeun-han koteu"
    )
]

w2["getting-dressed"] = [
    item(
        "Pull shirt", "قمیض پہنو", "Qameez pehno", "क़मीज़ पहनो", "Qameez pehno",
        "ارتد قميصك", "Irtadi qamisak", "Ponte camisa", "POHN-teh kah-MEE-sah",
        "Enfile chandail", "Ahn-feel shahn-die", "Zieh Hemd an", "TSEE hemt ahn",
        "Infila maglietta", "Een-FEE-lah mah-LYEHT-tah", "Vista a camiseta", "VEES-tah ah kah-mee-ZEH-tah",
        "Натяни футболку", "Nah-tyah-NEE foot-BOHL-koo", "Tişörtünü geçir", "Tee-shohr-tew-new geh-cheer",
        "Kenakan kaus", "Keh-nah-kahn kah-oos", "套上 卫衣", "Tàoshàng wèiyī",
        "シャツを 着る", "Shatsu o kiru", "티셔츠 쑥입어", "Tisyeocheu ssuk-ibeo"
    ),
    item(
        "Button up", "بٹن بند کرو", "Button band karo", "बटन लगाओ", "Button lagaao",
        "أزرر القميص", "Azrir al-qamis", "Abotona todo", "Ah-boh-TOH-nah TOH-doh",
        "Boutonne bien", "Boo-tohn byan", "Knöpf zu", "KNERPF tsoo",
        "Abbottona bene", "Ahb-boh-TOH-nah BEH-neh", "Abotoe os botões", "Ah-boh-TOY-ee oos boh-TOWNS",
        "Застегни пуговички", "Zahs-styehg-NEE POO-gah-veech-kee", "Düğmeleri ilikle", "Dew-meh-leh-ree ee-leek-leh",
        "Kancingkan baju", "Kahn-cheeng-kahn bah-joo", "系好 扣子", "Jìhǎo kòuzi",
        "ボタンを 留める", "Botan o tomeru", "단추 꼼꼼히잠가", "Danchu kkomkkom-hijamga"
    ),
    item(
        "Check mirror", "شیشے میں دیکھو", "Sheeshay mein dekho", "शीशे में देखो", "Sheeshe mein dekho",
        "انظر للمرآة", "Undhur lil-mir'at", "Mírate al espejo", "MEE-rah-teh ahl ehs-PEH-hoh",
        "Regarde miroir", "Ruh-gahrd mee-rwahr", "Schau in Spiegel", "SHOW in SHPEE-gel",
        "Guardati allo specchio", "GWAHR-dah-tee AHL-loh SPEHK-kyoh", "Olhe no espelho", "AW-lyee noo ehs-PAY-lyoo",
        "Посмотри в зеркало", "Pah-smah-TREE v ZYEHR-kah-lah", "Aynaya bak", "Eye-nah-yah bahk",
        "Bercerminlah rapi", "Behr-chehr-meen-lah rah-pee", "照 镜子", "Zhào jìngzi",
        "鏡を 見る", "Kagami o miru", "거울을 비춰봐", "Geoureul bichwobwa"
    )
]

# 72. shopping-for-shoes
w1["shopping-for-shoes"] = [
    item(
        "Shiny shoes", "چمکتے جوتے", "Chamakte jootay", "चमकते जूते", "Chamakte joote",
        "حذاء لامع", "Hitha' lami'", "Zapatos lustrosos", "Sah-PAH-tohs loos-TROH-sohs",
        "Chaussures brillantes", "Shoh-soor bree-yahnt", "Glänzende Schuhe", "GLEN-tsen-deh SHOO-eh",
        "Scarpe lucide", "SKAHR-peh LOO-chee-deh", "Sapatos brilhantes", "Sah-PAH-toos breel-YAHN-chees",
        "Блестящие туфельки", "Blye-STYAH-shchyee-yeh TOO-fyel-kee", "Parlak ayakkabılar", "Pahr-lahk ah-yahk-kah-buh-lahr",
        "Sepatu mengkilap", "Seh-pah-too mehng-kee-lahp", "亮 皮鞋", "Liàng píxié",
        "ピカピカの 靴", "Pikapika no kutsu", "반짝이는 구두", "Banjjagineun gudu"
    ),
    item(
        "Right size", "صحیح ناپ", "Saheeh naap", "सही नाप", "Sahi naap",
        "مقاس مناسب", "Maqas munasib", "Talla perfecta", "TAH-yah pehr-FEHK-tah",
        "Bonne pointure", "Buhn pwan-toor", "Passende Schuhgröße", "PAHS-sen-deh SHOO-grer-seh",
        "Misura giusta", "Mee-ZOO-rah JOOS-tah", "Tamanho certo", "Tah-MAHN-yoo SEHR-too",
        "Подходящий размер", "Pahd-khah-DYAH-shchiy rahz-MYEHR", "Tam numara", "Tahm noo-mah-rah",
        "Ukuran pas", "Oo-koo-rahn pahs", "正 尺码", "Zhèng chǐmǎ",
        "ぴったりの サイズ", "Pittari no saizu", "딱 맞는 사이즈", "Ttak manneun saijeu"
    ),
    item(
        "Soft sole", "نرم تلوہ", "Naram talwa", "नरम सोल", "Naram sole",
        "نعل مريح", "Na'l murih", "Suela suave", "SWEH-lah SWAH-veh",
        "Semelle souple", "Suh-mehl soopl", "Weiche Sohle", "VY-kheh ZOH-leh",
        "Suola morbida", "SWAW-lah MOHR-bee-dah", "Sola macia", "SAW-lah mah-SEE-ah",
        "Мягкая подошва", "MYAHK-kah-yah pah-DOHSH-vah", "Yumuşak taban", "Yoo-moo-shahk tah-bahn",
        "Sol empuk", "Sohl ehm-pook", "软 鞋底", "Ruǎn xiédǐ",
        "クッション性のある 靴底", "Kusshonsei no aru kutsuzoko", "푹신한 신발밑창", "Puksin-han sinbalmitchang"
    )
]

w2["shopping-for-shoes"] = [
    item(
        "Try shoe", "جوتا پہن کر دیکھو", "Joota pehan kar dekho", "जूता पहनकर देखो", "Joota pehankar dekho",
        "جرب الحذاء", "Jarrib al-hitha'", "Pruébate zapato", "PRAY-bah-teh sah-PAH-toh",
        "Essaye chaussure", "Eh-seh-yay shoh-soor", "Probier Schuh an", "Proh-BEER shoo ahn",
        "Prova scarpa", "PROH-vah SKAHR-pah", "Experimente sapato", "Ehs-peh-ree-MEHN-chee sah-PAH-too",
        "Примерь ботиночек", "Pree-MYEHR bah-TEE-nah-cheek", "Ayakkabıyı dene", "Ah-yahk-kah-buh-yuh deh-neh",
        "Coba sepatu", "Choh-bah seh-pah-too", "试 穿鞋", "Shì chuānxié",
        "靴を 履いてみる", "Kutsu o haitemiru", "신발을 신어봐", "Sinbareul sineobwa"
    ),
    item(
        "Walk around", "چل کر دیکھو", "Chal kar dekho", "चलकर देखो", "Chalkar dekho",
        "امش قليلاً", "Imshi qalilan", "Camina un poco", "Kah-MEE-nah oon POH-koh",
        "Marche un peu", "Mahrsh uhn puh", "Lauf Probe", "LOWF PROH-beh",
        "Cammina per prova", "Kahm-MEE-nah pehr PROH-vah", "Dê uns passos", "DAY oons PAH-soos",
        "Пройдись немного", "Prye-DEES nye-MNOH-gah", "Biraz yürü", "Bee-rahz yew-rew",
        "Coba berjalan santai", "Choh-bah behr-jah-lahn sahn-tye", "走 两步", "Zǒu liǎngbù",
        "少し 歩いてみる", "Sukoshi aruitemiru", "몇 걸음 걸어봐", "Myeot georeum georeobwa"
    ),
    item(
        "Wiggle toes", "انگلیاں ہلاؤ", "Ungliyan hilao", "उंगलियाँ हिलाओ", "Ungliyaan hilaao",
        "حرك أصابعك", "Harrik asabi'ak", "Mueve deditos", "MWEH-veh deh-DEE-tohs",
        "Bouge orteils", "Boozh ohr-tay", "Wackle mit Zehen", "VAHK-leh mit TSAY-en",
        "Muovi dita dei piedi", "MWOH-vee DEE-tah day PYEH-dee", "Mexa os dedinhos", "MAY-shah oos jee-JEEN-yoos",
        "Пошевели пальчиками", "Pah-sheh-vye-LEE PAHL-chee-kah-mee", "Parmaklarını oynat", "Pahr-mahk-lah-ruh-nuh oy-naht",
        "Goyangkan jari kaki", "Goh-yahng-kahn jah-ree kah-kee", "动 动脚趾", "Dòng dòngjiǎozhǐ",
        "つま先 動かす", "Tsumasaki ugokasu", "발가락 꼼지락", "Balgarak kkomjirak"
    )
]

# 73. cleaning-the-room
w1["cleaning-the-room"] = [
    item(
        "Neat room", "صاف ستھرا کمرہ", "Saaf suthra kamra", "साफ़-सुथरा कमरा", "Saaf-suthra kamra",
        "غرفة مرتبة", "Ghurfa murattaba", "Cuarto ordenado", "KWAHR-toh ohr-deh-NAH-doh",
        "Chambre rangée", "Shahmb-ruh rahn-zhay", "Aufgeräumtes Zimmer", "OWF-geh-roym-tes TSIM-mer",
        "Camera ordinata", "KAH-meh-rah ohr-dee-NAH-tah", "Quarto arrumado", "KWAHR-too ah-hoo-MAH-doo",
        "Убранная комната", "OOB-rahn-nah-yah KOHM-nah-tah", "Düzenli oda", "Dew-zen-lee oh-dah",
        "Kamar rapi", "Kah-mahr rah-pee", "整 房间", "Zhěng fángjiān",
        "片付いた 部屋", "Katadzuita heya", "정돈된 방", "Jeongdondoen bang"
    ),
    item(
        "Small broom", "چھوٹی جھاڑو", "Chhoti jhaaru", "छोटी झाड़ू", "Chhoti jhaadoo",
        "مكنسة صغيرة", "Miknasa saghira", "Escobita ligera", "Ehs-koh-BEE-tah lee-HEH-rah",
        "Petit balai", "Puh-tee bah-lay", "Handlicher Besen", "HAHNT-likh-er BAY-zen",
        "Scopa piccola", "SKOH-pah PEEK-koh-lah", "Vassourinha leve", "Vah-soo-REEN-yah LEH-vee",
        "Маленький веничек", "MAH-lyen-kiy VYEH-nee-cheek", "Küçük süpürge", "Kew-chewk sew-pewr-geh",
        "Sapu kecil", "Sah-poo keh-cheel", "巧 扫把", "Qiǎo sàobǎ",
        "使いやすい ほうき", "Tsukaiyasui hōki", "작고 가벼운 빗자루", "Jakgo gabyeoun bitjaru"
    ),
    item(
        "Toy basket", "کھلونوں کی ٹوکری", "Khilonon ki tokri", "खिलौनों की टोकरी", "Khilaunon ki tokri",
        "سلة ألعاب", "Sallat al'ab", "Cesto de juguetes", "SEHS-toh deh hoo-GEH-tehs",
        "Panier à jouets", "Pah-nyay ah zhoo-ay", "Bunte Spielzeugkiste", "BOON-teh SHPEEL-tsoyk-kis-teh",
        "Cesto dei giochi", "CHEHS-toh day JOH-kee", "Cesto de brinquedos", "SEHS-too jee breen-KAY-doos",
        "Коробка для игрушек", "Kah-ROHP-kah dlyah eeg-ROO-shehk", "Oyuncak sepeti", "Oh-yoon-jahk seh-peh-tee",
        "Keranjang mainan", "Keh-rahn-jahng my-nahn", "满 玩具筐", "Mǎn wánjùkuāng",
        "おもちゃの カゴ", "Omocha no kago", "장난감 바구니", "Jangnamgam baguni"
    )
]

w2["cleaning-the-room"] = [
    item(
        "Pick toys", "کھلونے سمیٹو", "Khilone sameto", "खिलौने समेटो", "Khilaune sameto",
        "اجمع ألعابك", "Ijma' al'abak", "Recoge juguetes", "Reh-KOH-heh hoo-GEH-tehs",
        "Range jouets", "Rahnzh zhoo-ay", "Räum Spielzeug auf", "ROYM SHPEEL-tsoyk owf",
        "Metti a posto i giochi", "MEHT-tee ah POHS-toh ee JOH-kee", "Guarde brinquedos", "GWAHR-jee breen-KAY-doos",
        "Собери игрушки", "Sah-bye-REE eeg-ROOSH-kee", "Oyuncakları topla", "Oh-yoon-jahk-lah-ruh toh-plah",
        "Kumpulkan mainan", "Koom-pool-kahn my-nahn", "收 玩具", "Shōu wánjù",
        "おもちゃを 片付ける", "Omocha o katadukeru", "장난감 정리해", "Jangnamgam jeongnihae"
    ),
    item(
        "Sweep dust", "مٹی جھاڑو", "Mitti jhaaru", "धूल साफ़ करो", "Dhool saaf karo",
        "اكنس الغبار", "Iknus al-ghubar", "Barre polvo", "BAH-rreh POHL-voh",
        "Balaie poussière", "Bah-lay poo-syehr", "Feg Staub weg", "FAYK SHTOWP vehk",
        "Spazza polvere", "SPAHT-tsah POHL-veh-reh", "Varra poeira", "VAH-hah poh-AY-rah",
        "Подмети соринки", "Pahd-mye-TEE sah-REEN-kee", "Tozları süpür", "Tohz-lah-ruh sew-pewr",
        "Sapu debu", "Sah-poo deh-boo", "扫 灰尘", "Sǎo huīchén",
        "ホコリを 掃く", "Hokori o haku", "먼지를 쓸어내", "Meonjireul sseureonae"
    ),
    item(
        "Make bed", "بستر ٹھیک کرو", "Bistar theek karo", "बिस्तर लगाओ", "Bistar lagaao",
        "رتب سريرك", "Rattib sarirak", "Tiende cama", "TYEHN-deh KAH-mah",
        "Fais lit", "Feh lee", "Mach Bett", "MAHKH bet",
        "Rifai letto", "Ree-FYE LEHT-toh", "Arrume cama", "Ah-HOO-mee KAH-mah",
        "Застели кроватку", "Zahs-tyeh-LEE krah-VAHT-koo", "Yatağını düzelt", "Yah-tah-uh-nuh dew-zelt",
        "Rapikan tempat tidur", "Rah-pee-kahn tehm-paht tee-door", "铺 被褥", "Pū bèirù",
        "ベッドを 整える", "Beddo o totonoeru", "침대 정리해", "Chimdae jeongnihae"
    )
]

# 74. washing-dishes
w1["washing-dishes"] = [
    item(
        "Warm bubbles", "گرم جھاگ", "Garam jhaag", "गर्म झाग", "Garm jhaag",
        "فقاعات صابون", "Fuqa'at sabun", "Burbujas tibias", "Boor-BOO-hahs TEE-byahs",
        "Bulles de savon", "Bool duh sah-vohn", "Warme Schaumblasen", "VAHR-meh SHOWN-blah-zen",
        "Bolle di sapone", "BOHL-leh dee sah-POH-neh", "Espuma morna", "Ehs-POO-mah MOHR-nah",
        "Тёплая мыльная пена", "TYOHP-lah-yah MYL-nah-yah PYEH-nah", "Köpüklü ılık su", "Ker-pewk-lew uh-luhk soo",
        "Busa sabun hangat", "Boo-sah sah-boon hahng-aht", "暖 肥皂泡", "Nuǎn féizàopào",
        "あたたかい 石けん泡", "Atatakai sekken'awa", "따뜻한 비눗방울", "Ttatteut-han binutbang-ul"
    ),
    item(
        "Yellow sponge", "پیلا فوم", "Peela foam", "पीला स्पंज", "Peela sponge",
        "إسفنجة صفراء", "Isfanja safra'", "Esponja amarilla", "Ehs-POHN-hah ah-mah-REE-yah",
        "Éponge jaune", "Ay-pohnzh zhohn", "Gelber Schwamm", "GEL-ber shvahm",
        "Spugna gialla", "SPOO-nyah JAHL-lah", "Esponja amarela", "Ehs-POHN-zhah ah-mah-REH-lah",
        "Жёлтая губка", "ZHOHL-tah-yah GOOB-kah", "Sarı bulaşık süngeri", "Sah-ruh boo-lah-shuhk sewn-geh-ree",
        "Spons kuning", "Spohns koo-neeng", "黄 海绵", "Huáng hǎimián",
        "黄色い スポンジ", "Kiiroi suponji", "노란 스펀지", "Noran seupeonji"
    ),
    item(
        "Clean glass", "صاف گلاس", "Saaf glass", "साफ़ गिलास", "Saaf gilaas",
        "كوب نظيف", "Kub nadhif", "Vaso reluciente", "VAH-soh reh-loo-SYEHN-teh",
        "Verre étincelant", "Vehr ay-tan-slahn", "Glänzendes Glas", "GLEN-tsen-des glahs",
        "Bicchiere splendente", "Beek-KYEH-reh splehn-DEHN-teh", "Copo brilhando", "KOH-poo breel-YAHN-doo",
        "Чистый стаканчик", "CHEES-tyy stah-KAHN-cheek", "Işıl ışıl bardak", "Uh-shuhl uh-shuhl bahr-dahk",
        "Gelas bening", "Geh-lahs beh-neeng", "净 玻璃杯", "Jìng bōlibēi",
        "ピカピカの コップ", "Pikapika no koppu", "반짝이는 유리컵", "Banjjagineun yuriken"
    )
]

w2["washing-dishes"] = [
    item(
        "Scrub pot", "دیگچی صاف کرو", "Deigchi saaf karo", "पतीला माँजो", "Pateela maanjo",
        "افرك القدر", "Ufruk al-qidr", "Frota cacerola", "FROH-tah kah-seh-ROH-lah",
        "Frotte casserole", "Froht kahs-rohl", "Schrubb Topf", "SHROOP topf",
        "Strofina pentola", "Stroh-FEE-nah pehn-TOH-lah", "Esfregue panela", "Ehs-FRAY-gee pah-NEH-lah",
        "Потри кастрюльку", "Pah-TREE kahs-TRYOOL-koo", "Tencereyi ovala", "Ten-jeh-reh-yee oh-vah-lah",
        "Gosok panci", "Goh-sohk pahn-chee", "刷 汤锅", "Shuā tāngguō",
        "お鍋を こする", "Onabe o kosuru", "냄비를 싹싹문질러", "Naembireul ssakssakmunjilleo"
    ),
    item(
        "Rinse soap", "جھاگ دھوؤ", "Jhaag dhoo", "साबुन धोओ", "Saabun dhoo",
        "اشطف بالماء", "Ishtuf bil-ma'", "Enjuaga espuma", "Ehn-HWAH-gah ehs-POO-mah",
        "Rince bien", "Rans byan", "Spül Seife ab", "SHPYOOL ZY-feh ahp",
        "Sciacqua bene", "SHAHK-kwah BEH-neh", "Enxágue louça", "Eng-SHAH-gee LOH-sah",
        "Смой всю пену", "SMOY fsyoo PYEH-noo", "Köpüğü durula", "Ker-pew-ew doo-roo-lah",
        "Bilas busa sabun", "Bee-lahs boo-sah sah-boon", "冲 洗泡沫", "Chōng xǐpàomò",
        "泡を 洗い流す", "Awa o arainagasu", "거품을 헹궈내", "Geopumeul heng-gwonae"
    ),
    item(
        "Dry cup", "کپ خشک کرو", "Cup khushk karo", "कप सुखाओ", "Cup sukhaao",
        "جفف الكوب", "Jaffif al-kub", "Seca taza", "SEH-kah TAH-sah",
        "Essuie tasse", "Eh-swee tahs", "Trockne Tasse ab", "TROK-neh TAHZ-zeh ahp",
        "Asciuga tazza", "Ah-SHOO-gah TAHT-tsah", "Seque xícara", "SEH-kee SHEE-kah-rah",
        "Вытри чашку полотенцем", "VY-tree CHAHSH-koo pah-lah-TYEHN-tsem", "Bardağı kurula", "Bahr-dah-uh koo-roo-lah",
        "Keringkan cangkir", "Keh-reeng-kahn chahng-keer", "擦 干杯子", "Cā gānbēizi",
        "コップを 拭く", "Koppu o fuku", "컵을 뽀득하게닦아", "Keobeul pmodeukhagedakka"
    )
]

# 75. watering-plants
w1["watering-plants"] = [
    item(
        "Green leaf", "سبز پتا", "Sabz patta", "हरी पत्ती", "Hari patti",
        "ورقة خضراء", "Waraqa khadra'", "Hoja verde", "OH-hah VEHR-deh",
        "Feuille verte", "Fuh-yuh vehrt", "Grünes Blatt", "GREW-nes blaht",
        "Foglia verde", "FOH-lyah VEHR-deh", "Folha verde", "FAWL-yah VEHR-jee",
        "Зелёный листочек", "Zyeh-LYOH-nyy lees-TOH-cheek", "Taptaze yeşil yaprak", "Tahp-tah-zeh yeh-sheel yahp-rahk",
        "Daun hijau", "Dow-oon hee-jow", "绿 叶片", "Lǜ yèpiàn",
        "みずみずしい 葉っぱ", "Mizumizushii happa", "파릇파릇한 잎", "Pareutpareut-han ip"
    ),
    item(
        "Pink flower", "گلابی پھول", "Gulaabi phool", "गुलाबी फूल", "Gulaabi phool",
        "زهرة وردية", "Zahra wardiyya", "Flor rosa", "FLOHR ROH-sah",
        "Fleur rose", "Fluhr rohz", "Rosa Blüte", "ROH-zah BLEW-teh",
        "Fiore rosa", "FYOH-reh ROH-zah", "Flor cor-de-rosa", "FLOHR kohr-jee-HOH-zah",
        "Нежно-розовый цветок", "NYEZH-nah ROH-zah-vyy tsvyeh-TOHK", "Pembe çiçek", "Pehm-beh chee-chek",
        "Bunga merah muda", "Boo-ngah meh-rah moo-dah", "粉 鲜花", "Fěn xiānhuā",
        "ピンクの お花", "Pinku no ohana", "분홍빛 꽃", "Bunhongbit kkot"
    ),
    item(
        "Wet soil", "نم مٹی", "Namm mitti", "गीली मिट्टी", "Geeli mitti",
        "تربة رطبة", "Turba ratba", "Tierra fresca", "TYEH-rrah FREHS-kah",
        "Terre humide", "Tehr oo-meed", "Feuchte Blumenerde", "FOYKH-teh BLOO-men-ehr-deh",
        "Terriccio umido", "Tehr-REET-choh OO-mee-doh", "Terra molhada", "TEH-hah mohl-YAH-dah",
        "Влажная земля", "VLAZH-nah-yah zyem-LYAH", "Nemli bereketli toprak", "Nehm-lee beh-reh-ket-lee toh-prahk",
        "Tanah subur gembur", "Tah-nah soo-boor gehm-boor", "润 泥土", "Rùn nítǔ",
        "湿った 土", "Shimetta tsuchi", "촉촉한 흙", "Chokchok-han heulk"
    )
]

w2["watering-plants"] = [
    item(
        "Pour water", "پانی ڈالو", "Paani daalo", "पानी डालो", "Paani daalo",
        "صب الماء", "Subb al-ma'", "Echa agua", "EH-chah AH-gwah",
        "Verse eau", "Vehrs oh", "Gieß Wasser", "GEESS VAHS-ser",
        "Versa acqua", "VEHR-sah AHK-wah", "Coloque água", "Koh-LAW-kee AH-gwah",
        "Налей водички", "Nah-LEY vah-DEECH-kee", "Bitkiye su ver", "Beet-kee-yeh soo vehr",
        "Tuang air", "Too-ahng ah-yeer", "倒 水浇花", "Dào shuǐjiāohuā",
        "お水を あげる", "Omizu o ageru", "물을 솔솔뿌려", "Mureul solsolppuryeo"
    ),
    item(
        "Fill can", "کین بھرو", "Can bharo", "झारी भरो", "Jhaari bharo",
        "املأ المرشة", "Imla' al-mirashsha", "Llena regadera", "YEH-nah reh-gah-DEH-rah",
        "Remplis arrosoir", "Rahn-plee ah-roh-zwahr", "Füll Kanne", "FEEL KAHN-neh",
        "Riempi annaffiatoio", "RYEHM-pee ahn-nahf-fyah-TOH-yoh", "Encha regador", "ENG-shah heh-gah-DOHR",
        "Наполни лейку", "Nah-POHL-nee LEY-koo", "Sulama kabını doldur", "Soo-lah-mah kah-buh-nuh dohl-dur",
        "Isi ceret siram", "Ee-see cheh-reht see-rahm", "装 水壶", "Zhuāng shuǐhú",
        "ジョウロに 水入れる", "Jōro ni mizu'ireru", "물뿌리개 채워", "Mulppurigae chaeweo"
    ),
    item(
        "Watch grow", "پودا بڑھتے دیکھو", "Pauda barhte dekho", "बढ़ते देखो", "Badhte dekho",
        "راقب النمو", "Raqib an-numuww", "Mira crecer", "MEE-rah kreh-SEHR",
        "Regarde grandir", "Ruh-gahrd grahn-deer", "Sieh Wachsen zu", "ZEE VAHK-sen tsoo",
        "Guarda crescere", "GWAHR-dah KREH-sheh-reh", "Veja crescer", "VAY-zhah kreh-SEHR",
        "Наблюдай за ростом", "Nahb-lyoo-DYE zah ROHS-tahm", "Büyümesini izle", "Bew-yew-meh-see-nee eez-leh",
        "Amati pertumbuhannya", "Ah-mah-tee pehr-toom-boo-hahn-nyah", "盼 长大", "Pàn zhǎngdà",
        "成長を 見守る", "Seichō o mimamoru", "자라는걸 지켜봐", "Jaranangeol jikyeobwa"
    )
]

# 76. feeding-pets
w1["feeding-pets"] = [
    item(
        "Cute bowl", "پیارا پیالہ", "Pyaara pyala", "प्यारा कटोरा", "Pyaara katora",
        "وعاء جميل", "Wi'a' jamil", "Platito limpio", "Plah-TEE-toh LEEM-pyoh",
        "Jolie gamelle", "Zhoh-lee gah-mehl", "Bunter Futternapf", "BOON-ter FOOT-ter-nahpf",
        "Ciotola carina", "CHOH-toh-lah kah-REE-nah", "Tigela bonitinha", "Chee-ZHEH-lah boh-nee-CHEEN-yah",
        "Чистая мисочка", "CHEES-tah-yah MEE-sahch-kah", "Sevimli mama kabı", "Seh-veem-lee mah-mah kah-buh",
        "Mangkuk makan imut", "Mahng-kook mah-kahn ee-moot", "萌 宠物碗", "Méng chǒngwùwǎn",
        "可愛い フードボウル", "Kawaii fūdobōru", "귀여운 밥그릇", "Gwiyeoun bapgeureut"
    ),
    item(
        "Crisp kibble", "کرکرا دلیہ", "Kurkura daliya", "कुरकुरा भोजन", "Kurkura bhojan",
        "طعام مقرمش", "Ta'am muqarmash", "Croquetas ricas", "Kroh-KEH-tahs REE-kahs",
        "Croquettes croquantes", "Kroh-keht kroh-kahnt", "Knuspriges Futter", "KNOOS-pree-ges FOOT-ter",
        "Croccantini buoni", "Krohk-kahn-TEE-nee BWAW-nee", "Ração crocante", "Hah-SOWN kroh-KAHN-chee",
        "Хрустящий сухой корм", "Khroo-STYAH-shchiy soo-KHOY kohrm", "Çıtır mama taneleri", "Chuh-tuhr mah-mah tah-neh-leh-ree",
        "Biskuit hewan renyah", "Bees-koo-eet heh-wahn rehn-yah", "香 脆干粮", "Xiāng cuìgānliáng",
        "サクサク ドライフード", "Sakusaku doraifūdo", "바삭한 사료", "Basak-han saryo"
    ),
    item(
        "Fresh water", "تازہ پانی", "Taaza paani", "ताज़ा पानी", "Taaza paani",
        "ماء عذب", "Ma' 'adhb", "Agua fresca", "AH-gwah FREHS-kah",
        "Eau propre", "Oh proh-pruh", "Frisches Trinkwasser", "FRISH-es TRINK-vahs-ser",
        "Acqua fresca", "AHK-wah FREHS-kah", "Água limpinha", "AH-gwah leem-PEEN-yah",
        "Свежая чистая водичка", "SVYEH-zhah-yah CHEES-tah-yah vah-DEECH-kah", "Taze içme suyu", "Tah-zeh eech-meh soo-yoo",
        "Air minum bersih", "Ah-yeer mee-noom behr-seeh", "清 饮用水", "Qīng yǐnyòngshuǐ",
        "新鮮な お水", "Shinsen na omizu", "신선한 식수", "Sinseon-han siksu"
    )
]

w2["feeding-pets"] = [
    item(
        "Pour kibble", "خوراک ڈالو", "Khoraak daalo", "भोजन डालो", "Bhojan daalo",
        "صب الطعام", "Subb at-ta'am", "Sirve comida", "SEER-veh koh-MEE-dah",
        "Verse croquettes", "Vehrs kroh-keht", "Schütt Futter rein", "SHEET FOOT-ter ryne",
        "Versa croccantini", "VEHR-sah krohk-kahn-TEE-nee", "Coloque ração", "Koh-LAW-kee hah-SOWN",
        "Насыпь корма", "Nah-SYP KOHR-mah", "Mamayı dök", "Mah-mah-yuh derk",
        "Tuang pakan", "Too-ahng pah-kahn", "倒 宠粮", "Dào chǒngliáng",
        "ご飯を 入れる", "Gohan o ireru", "사료를 담아줘", "Saryoreul damajwo"
    ),
    item(
        "Change water", "پانی بدلو", "Paani badlo", "पानी बदलो", "Paani badlo",
        "جدد الماء", "Jaddid al-ma'", "Cambia agua", "KAHM-byah AH-gwah",
        "Change l'eau", "Shahnzh loh", "Wechsle Wasser", "VEKHS-leh VAHS-ser",
        "Cambia acqua", "KAHM-byah AHK-wah", "Troque água", "TRAW-kee AH-gwah",
        "Поменяй водичку", "Pah-mye-NYE vah-DEECH-koo", "Suyunu tazele", "Soo-yoo-noo tah-zeh-leh",
        "Ganti air minum", "Gahn-tee ah-yeer mee-noom", "换 清水", "Huàn qīngshuǐ",
        "お水を 取り替える", "Omizu o torikaeru", "물을 갈아줘", "Mureul garajwo"
    ),
    item(
        "Pet gently", "پیار کرو", "Pyaar karo", "प्यार से सहलाओ", "Pyaar se sahlaao",
        "داعب بحنان", "Da'ib bi-hanan", "Acaricia con amor", "Ah-kah-REE-syah kohn ah-MOHR",
        "Caresse gentiment", "Kah-rehs zhahn-tee-mahn", "Kuschel lieb", "KOOSH-el leep",
        "Accarezza teneramente", "Ahk-kah-REHT-tsah teh-neh-rah-MEHN-teh", "Faça carinho", "FAH-sah kah-REEN-yoo",
        "Погладь ласково", "Pah-GLYAHT LAHS-kah-vah", "Şefkatle sev", "Shehf-kaht-leh sehv",
        "Elus penuh kasih", "Eh-loos peh-nooh kah-seeh", "轻 摸头", "Qīng mōtóu",
        "頭を なでる", "Atama o naderu", "머리를 쓰다듬어", "Meorireul sseudadeumeo"
    )
]

# 77. folding-clothes
w1["folding-clothes"] = [
    item(
        "Warm blanket", "گرم کمبل", "Garam kambal", "गर्म कंबल", "Garm kambal",
        "غطاء دافئ", "Ghita' dafi'", "Manta abrigadora", "MAHN-tah ah-bree-gah-DOH-rah",
        "Plaid chaud", "Pled sho", "Kuscheldecke", "KOOSH-el-dek-keh",
        "Coperta calda", "Koh-PEHR-tah KAHL-dah", "Cobertor macio", "Koh-behr-TOHR mah-SEE-oo",
        "Тёплое одеяльце", "TYOHP-lah-yeh ah-dyeh-YAHL-tseh", "Sıcacık battaniye", "Suh-jah-juhk baht-tah-nee-yeh",
        "Selimut tebal nyaman", "Seh-lee-moot teh-bahl nyah-mahn", "暖 被单", "Nuǎn bèidān",
        "暖かい 毛布", "Atatakai mōfu", "포근한 이불", "Pogeun-han ibul"
    ),
    item(
        "Clean towel", "صاف تولیہ", "Saaf toliya", "साफ़ तौलिया", "Saaf tauliya",
        "منشفة نظيفة", "Minshafa nadhifa", "Toalla limpia", "Toh-AH-yah LEEM-pyah",
        "Serviette propre", "Sehr-vyet proh-pruh", "Frisches Handtuch", "FRISH-es HAHNT-tookh",
        "Asciugamano pulito", "Ah-shoo-gah-MAH-noh poo-LEE-toh", "Toalha cheirosa", "Toh-AHL-yah shay-RAW-zah",
        "Чистое полотенце", "CHEES-tah-yeh pah-lah-TYEHN-tseh", "Mis kokulu havlu", "Mees koh-koo-loo hahv-loo",
        "Handuk wangi bersih", "Hahn-dook wahng-gee behr-seeh", "净 毛巾", "Jìng máojīn",
        "清潔な タオル", "Seiketsuna taoru", "깨끗한 타월", "Kkaekkeut-han tawol"
    ),
    item(
        "Neat pile", "سلیقے کا ڈھیر", "Saleeqay ka dher", "सलीक़े का ढेर", "Saleeqe ka dher",
        "كومة مرتبة", "Kawma murattaba", "Pila ordenada", "PEE-lah ohr-deh-NAH-dah",
        "Pile bien rangée", "Peel byan rahn-zhay", "Sauberer Wäschestapel", "ZOW-ber-er VESH-eh-shtah-pel",
        "Pila ordinata", "PEE-lah ohr-dee-NAH-tah", "Pilha arrumada", "PEEL-yah ah-hoo-MAH-dah",
        "Ровная стопка одежды", "ROHV-nah-yah STOHP-kah ah-DYEHZH-dy", "Düzgün çamaşır yığını", "Dewz-gewn chah-mah-shuhr yuh-uh-nuh",
        "Tumpukan rapi", "Toom-poo-kahn rah-pee", "齐 衣堆", "Qí yīduī",
        "整然とした 山", "Seizentoshita yama", "가지런한 빨래더미", "Gajireon-han ppallaedeomi"
    )
]

w2["folding-clothes"] = [
    item(
        "Smooth cloth", "کپڑا سیدھا کرو", "Kapra seedha karo", "कपड़ा सीधा करो", "Kapda seedha karo",
        "ملس الثوب", "Mallis ath-thawb", "Alisa prenda", "Ah-LEE-sah PREHN-dah",
        "Lisse tissu", "Lees tee-soo", "Streich glatt", "SHTRYKH glaht",
        "Liscia stoffa", "LEE-shah STOHF-fah", "Alise o tecido", "Ah-LEE-zee oo teh-SEE-doo",
        "Разгладь складочки", "Rahz-GLYAHT SKLAH-dahch-kee", "Kırışıklıkları düzelt", "Kuh-ruh-shuhk-luhk-lah-ruh dew-zelt",
        "Ratakan kain halus", "Rah-tah-kahn kah-een hah-loos", "抚平 衣物", "Fǔpíng yīwù",
        "シワを 伸ばす", "Shiwa o nobasu", "옷감을 쫙펴", "Otgameul jjwakpyeo"
    ),
    item(
        "Fold square", "چوکور تہہ کرو", "Chaukor teh karo", "चौकोर मोड़ो", "Chaukor modo",
        "اطو بشكل مربع", "Itwi bi-shakl murabba'", "Dobla parejo", "DOH-blah pah-REH-hoh",
        "Plie carré", "Plee kah-ray", "Falte viereckig", "FAHL-teh FEER-ek-kikh",
        "Piega quadrato", "PYEH-gah kwah-DRAH-toh", "Dobre certinho", "DAW-bree sehr-CHEEN-yoo",
        "Сложи ровным квадратом", "Slah-ZHY ROHV-nym kvah-DRAH-tahm", "Kare şeklinde katla", "Kah-reh shehk-leen-deh kaht-lah",
        "Lipat persegi rapi", "Lee-paht pehr-seh-gee rah-pee", "折 方正", "Zhé fāngzhèng",
        "四角く たたむ", "Shikakuku tatamu", "네모나게 개어", "Nemonage gaeo"
    ),
    item(
        "Stack high", "اوپر رکھو", "Oopar rakho", "ऊपर रखो", "Oopar rakho",
        "رتب في الخزانة", "Rattib fil-khizana", "Apila ordenado", "Ah-PEE-lah ohr-deh-NAH-doh",
        "Empile sagement", "Ahn-peel sahzh-mahn", "Staple sauber", "SHTAH-pel ZOW-ber",
        "Impila nell'armadio", "Eem-PEE-lah nehl-lahr-MAH-dyoh", "Empilhe na gaveta", "Ehm-PEEL-yee nah gah-VAY-tah",
        "Сложи аккуратно в стопку", "Slah-ZHY ahk-koo-RAHT-nah v STOHP-koo", "Üst üste diz", "Ewst ews-teh deez",
        "Tumpuk rapi di lemari", "Toom-pook rah-pee dee leh-mah-ree", "叠好 摞起", "Diéhǎo luòqǐ",
        "重ねて 置く", "Kasanete oku", "차곡차곡 쌓아둬", "Chagokchagok ssahadwo"
    )
]

output_path = os.path.join(os.path.dirname(__file__), "..", "src", "data", "multilingual", "cat5_sports_clothes_chores.ts")
export_ts_module(output_path, "CAT5_W1", "CAT5_W2", w1, w2)
