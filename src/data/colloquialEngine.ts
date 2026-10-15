import { AgeGroup, GeneratedSentence, LanguageCode } from '../types';

interface LexicalChunkFrame {
  openings: Partial<Record<LanguageCode, string[]>>;
  openingsPhonetic: Partial<Record<LanguageCode, string[]>>;
  needs: Partial<Record<LanguageCode, string[]>>;
  needsPhonetic: Partial<Record<LanguageCode, string[]>>;
  polites: Partial<Record<LanguageCode, string[]>>;
  politesPhonetic: Partial<Record<LanguageCode, string[]>>;
  englishMeanings: {
    opening: string;
    need: string;
    polite: string;
  }[];
}

// Domain vocabulary slots per scenario group
const SCENARIO_THEMES: Record<string, { objects: Partial<Record<LanguageCode, string[]>>; objectsPhonetic: Partial<Record<LanguageCode, string[]>> }> = {
  'hd-breakfast': {
    objects: {
      es: ['el jugo de naranja frío', 'el pan tostado caliente', 'la leche con miel', 'la fruta picada', 'las galletas de avena', 'el cereal crujiente', 'un vaso de agua', 'la mermelada de fresa', 'los huevos revueltos', 'una servilleta limpia'],
      en: ['the cold orange juice', 'the warm toasted bread', 'milk with sweet honey', 'the fresh sliced fruit', 'crunchy oatmeal cookies', 'the bowl of cereal', 'a fresh glass of water', 'sweet strawberry jam', 'fluffy scrambled eggs', 'a clean paper napkin'],
      ar: ['عصير البرتقال البارد', 'الخبز المحمص الدافئ', 'الحليب مع العسل', 'قطع الفاكهة الطازجة', 'بسكويت الشوفان', 'وعاء رقائق الحبوب', 'كوب ماء نقي', 'مربى الفراولة اللذيذ', 'البيض المخفوق', 'منديلاً نظيفاً'],
      ur: ['ٹھنڈا مالٹے کا جوس', 'گرم ٹوسٹ روٹی', 'شہد ملا دودھ', 'کٹے ہوئے تازہ پھل', 'اوٹ میل بسکٹ', 'اناج کا پیالہ', 'تازہ پانی کا گلاس', 'اسٹرابیری جیم', 'تلے ہوئے انڈے', 'صاف نیپکن'],
      hi: ['ठंडा संतरे का जूस', 'गरम टोस्टेड ब्रेड', 'शहद वाला ताजा दूध', 'कटे हुए ताजे फल', 'ओट्स वाले बिस्कुट', 'सीरियल का कटोरा', 'ताजे पानी का गिलास', 'स्ट्रॉबेरी का मीठा जैम', 'भुर्जी वाले अंडे', 'एक साफ नैपकिन'],
      fr: ['le jus d\'orange bien frais', 'le pain grillé chaud', 'du lait au miel doux', 'les fruits frais coupés', 'des biscuits croustillants', 'le bol de céréales', 'un grand verre d\'eau', 'la confiture de fraises', 'les œufs brouillés moelleux', 'une serviette propre'],
    },
    objectsPhonetic: {
      es: ['ehl KHOO-goh deh nah-RAHN-khah FREE-oh', 'ehl PAHN tohs-TAH-doh kah-LYEHN-teh', 'lah LEH-cheh kohn MYEHL', 'lah FROO-tah pee-KAH-dah', 'lahs gah-YEH-tahs deh ah-VEH-nah', 'ehl seh-reh-AHL kroo-KHYEHN-teh', 'oon VAH-soh deh AH-gwah', 'lah mehr-meh-LAH-dah', 'lohs WEH-vohs reh-VWEHL-tohs', 'OO-nah sehr-vee-YEH-tah'],
      en: ['thuh kohld oh-rinj joos', 'thuh wahrm tohst-ed bred', 'milk with sweet huh-nee', 'thuh fresh slyst froot', 'kruhn-chee oht-meel cook-eez', 'thuh bohl ov seer-ee-ul', 'a fresh glass ov wah-ter', 'sweet straw-behr-ee jam', 'fluhf-fee skram-bld egz', 'a kleen nap-kin'],
      ar: ['a-seer al-bur-tu-qaal al-baa-rid', 'al-khubz al-mu-ham-mas', 'al-ha-leeb ma-al a-sal', 'qi-ta al-faa-ki-hah', 'bis-ka-weet ash-shoo-faan', 'wa-aa ar-ra-qaa-iq', 'koob maa na-qiyy', 'mu-rab-baa al-fa-raw-lah', 'al-bayd al-makh-fooq', 'man-dee-lan na-zee-fan'],
      ur: ['thanda maltay ka juice', 'garam toast roti', 'shehad mila doodh', 'katay huay phall', 'oatmeal biscuit', 'anaaj ka pyaala', 'taaza paani ka glass', 'strawberry jam', 'talay huay anday', 'saaf napkin'],
      hi: ['thanda santre ka juice', 'garam toasted bread', 'shehad wala taaza doodh', 'katey taazey phal', 'oats waley biscuit', 'cereal ka katora', 'taaze paani ka glass', 'strawberry jam', 'ande ki bhurji', 'ek saaf napkin'],
      fr: ['luh zhoo doh-rahnzh fray', 'luh pan gree-yay shoh', 'dew lay oh myel', 'lay frwee fress koo-pay', 'day bees-kwee kroos-tee-yahn', 'luh bohl duh say-ray-ahl', 'un grahn vehr doh', 'lah kohn-fee-tewr duh frehz', 'lay z-uh broo-yay', 'oon sehr-vee-yet proh-pruh'],
    },
  },
};

// Generic lexical replacement chunks for all other 9 categories
const UNIVERSAL_CHUNK_SETS: LexicalChunkFrame = {
  openings: {
    es: [
      '¿Me pasas',
      'Oye, quiero',
      '¿Dónde guardaron',
      'Por favor, muéstrame',
      'Me encanta',
      '¿Podemos llevar',
      'Mira con cuidado',
      'Tengo muchas ganas de',
      'Ayúdame con',
      '¿A qué hora sale',
    ],
    en: [
      'Could you pass me',
      'Hey, I would like',
      'Where did we keep',
      'Please show me',
      'I really love',
      'Can we take along',
      'Look closely at',
      'I am super excited for',
      'Please help me with',
      'What time does',
    ],
    ar: [
      'ناولني لو سمحت',
      'يا هلا، أود تجربة',
      'أين وضعتم',
      'أرني من فضلك',
      'يعجبني جداً',
      'هل يمكننا أخذ',
      'انظر جيداً إلى',
      'أنا متحمس جداً لـ',
      'ساعدني في ترتيب',
      'في أي وقت يتحرك',
    ],
    ur: [
      'کیا آپ مجھے پکڑا سکتے ہیں',
      'سنیں، مجھے چاہیے',
      'آپ نے کہاں رکھا ہے',
      'مہربانی کر کے مجھے دکھائیں',
      'مجھے بہت پسند ہے',
      'کیا ہم ساتھ لے سکتے ہیں',
      'دھیان سے دیکھیں',
      'مجھے بہت شوق ہے',
      'میری مدد کریں',
      'کس وقت روانہ ہوگا',
    ],
    hi: [
      'जरा पास करना',
      'सुनिए, मुझे चाहिए',
      'आपने कहाँ रखा है',
      'कृपया मुझे दिखाइए',
      'मुझे बहुत पसंद है',
      'क्या हम साथ ले सकते हैं',
      'ध्यान से देखिए',
      'मुझे बहुत उत्साह है',
      'मेरी मदद कीजिए',
      'यह किस समय निकलेगा',
    ],
    fr: [
      'Tu me passes',
      'Dis, j\'aimerais bien',
      'Où avez-vous rangé',
      'Montre-moi, s\'il te plaît,',
      'J\'adore vraiment',
      'Est-ce qu\'on peut emporter',
      'Regarde bien',
      'J\'ai tellement hâte pour',
      'Aide-moi avec',
      'À quelle heure part',
    ],
  },
  openingsPhonetic: {
    es: [
      'Meh PAH-sahs',
      'OH-yeh, KYEH-roh',
      'DOHN-deh gwahr-DAH-rohn',
      'POHR fah-VOHR, MWEHS-trah-meh',
      'Meh ehn-KAHN-tah',
      'Poh-DEH-mohs yeh-VAHR',
      'MEE-rah kohn kwee-DAH-doh',
      'TEHN-goh MOO-chahs GAH-nahs deh',
      'Ah-YOO-dah-meh kohn',
      'Ah keh OH-rah SAH-leh',
    ],
    en: [
      'Kood yoo pass mee',
      'Hey, eye wood lyk',
      'Wehr did wee keep',
      'Pleez show mee',
      'Eye reel-ee luhv',
      'Kan wee tayk uh-long',
      'Look klohs-lee at',
      'Eye am soo-per ek-sy-ted for',
      'Pleez help mee with',
      'Wut tym duhz',
    ],
    ar: [
      'Naa-wil-nee low sa-maht',
      'Yaa ha-laa, u-wadd',
      'Ay-na wa-da-tum',
      'A-ri-nee min fad-lak',
      'Yu-ji-bu-nee jid-dan',
      'Hal yum-ki-nu-naa akhz',
      'Un-zur jay-yi-dan i-laa',
      'A-naa mu-ta-ham-mis jid-dan',
      'Saa-id-nee fee',
      'Fee ayy waqt ya-ta-har-rak',
    ],
    ur: [
      'Kya aap mujhay pakra saktay hain',
      'Sunain, mujhay chahiye',
      'Aap nay kahan rakha hai',
      'Meherbani kar kay dikhayen',
      'Mujhay bohat pasand hai',
      'Kya hum saath lay saktay hain',
      'Dhiyan say dekhein',
      'Mujhay bohat shoq hai',
      'Meri madad karein',
      'Kis waqt rawana hoga',
    ],
    hi: [
      'Zara paas karna',
      'Suniye, mujhe chahiye',
      'Aapne kahan rakha hai',
      'Kripya mujhe dikhaiye',
      'Mujhe bahut pasand hai',
      'Kya hum saath le sakte hain',
      'Dhyan se dekhiye',
      'Mujhe bahut utsaah hai',
      'Meri madad kijiye',
      'Yeh kis samay niklega',
    ],
    fr: [
      'Too muh pahs',
      'Dee, zhem-ray byan',
      'Oo ah-vay voo rahn-zhay',
      'Mohn-truh mwah, seel tuh play',
      'Zhah-dohr vray-mahn',
      'Ehs kohn puh tahm-pohr-tay',
      'Ruh-gahrd byan',
      'Zhay tel-mahn aht poor',
      'Ehd mwah ah-vek',
      'Ah kel uhr pahr',
    ],
  },
  needs: {
    es: [
      'la mochila escolar azul',
      'el billete de transporte rápido',
      'el juguete favorito de bloques',
      'la manzana dulce y roja',
      'el termómetro de la clínica',
      'el balón de fútbol nuevo',
      'el paraguas amarillo brillante',
      'el dibujo con lápices de colores',
      'el consejo para esta tarea',
      'la medicina para el dolor',
    ],
    en: [
      'the blue school backpack',
      'the express transit ticket',
      'the favorite building block toy',
      'the sweet crisp red apple',
      'the clinic digital thermometer',
      'the brand-new soccer ball',
      'the bright yellow umbrella',
      'the drawing with color pencils',
      'the helpful advice on homework',
      'the soothing pain medicine',
    ],
    ar: [
      'حقيبة المدرسة الزرقاء',
      'تذكرة السفر السريع',
      'لعبة المكعبات المفضلة',
      'التفاحة الحمراء الحلوة',
      'مقياس حرارة العيادة',
      'كرة القدم الجديدة',
      'المظلة الصفراء الزاهية',
      'الرسمة بالألوان الخشبية',
      'نصيحة لحل الواجب المدرسي',
      'الدواء المسكن للألم',
    ],
    ur: [
      'نیلا اسکول کا بستہ',
      'تیز رفتار سفر کا ٹکٹ',
      'پسندیدہ بلاکس کا کھلونا',
      'میٹھا اور سرخ سیب',
      'کلینک کا تھرمامیٹر',
      'فٹ بال کی نئی گیند',
      'چمکیلی پیلی چھتری',
      'رنگین پنسلوں کی تصویر',
      'ہوم ورک کے لیے مشورہ',
      'درد دور کرنے والی دوا',
    ],
    hi: [
      'नीला स्कूल का बस्ता',
      'एक्सप्रेस यात्रा का टिकट',
      'पसंदीदा ब्लॉक्स का खिलौना',
      'मीठा और लाल सेब',
      'क्लिनिक का थर्मामीटर',
      'फुटबॉल की नई गेंद',
      'चमकीली पीली छतरी',
      'रंग-बिरंगी पेंसिल का चित्र',
      'होमवर्क के लिए सलाह',
      'दर्द कम करने वाली दवा',
    ],
    fr: [
      'le sac d\'école bleu ciel',
      'le ticket de transport rapide',
      'le jeu de construction préféré',
      'la pomme rouge bien croquante',
      'le thermomètre de la clinique',
      'le tout nouveau ballon de foot',
      'le parapluie jaune vif',
      'le dessin aux crayons de couleur',
      'le bon conseil pour les devoirs',
      'le médicament apaisant',
    ],
  },
  needsPhonetic: {
    es: [
      'lah moh-CHEE-lah ehs-koh-LAHR ah-ZOOL',
      'ehl bee-YEH-teh deh trahns-POHR-teh',
      'ehl khoo-GEH-teh fah-voh-REE-toh',
      'lah mahn-SAH-nah DOOL-seh ee ROH-khah',
      'ehl tehr-MOH-meh-troh',
      'ehl bah-LOHN deh FOOT-bohl NWEH-voh',
      'ehl pah-RAH-gwahs ah-mah-REE-yoh',
      'ehl dee-BOO-khoh kohn LAH-pee-sehs',
      'ehl kohn-SEH-khoh PAH-rah ehs-tah tah-REH-ah',
      'lah meh-dee-SEE-nah PAH-rah ehl doh-LOHR',
    ],
    en: [
      'thuh bloo skool bak-pak',
      'thuh ex-pres tran-zit tik-it',
      'thuh fayv-rit bil-ding blok toy',
      'thuh sweet krisp red ap-ul',
      'thuh klin-ik dij-i-tul ther-mom-uh-ter',
      'thuh brand-new sok-er bawl',
      'thuh bryt yel-loh uhm-brel-luh',
      'thuh draw-ing with kuh-ler pen-sulz',
      'thuh help-ful ad-vys on hohm-werk',
      'thuh sooth-ing payn med-i-sun',
    ],
    ar: [
      'ha-qee-bat al-mad-ra-sah az-zar-qaa',
      'taz-ka-rat as-sa-far as-sa-ree',
      'lubat al-mu-kab-baat al-mu-fad-da-lah',
      'at-tuf-faa-hah al-ham-raa',
      'miq-yaas ha-raa-rat al-i-yaa-dah',
      'ku-rat al-qa-dam al-ja-dee-dah',
      'al-mi-zal-lah as-saf-raa',
      'ar-ras-mah bil-al-waan',
      'na-see-hah li-hal al-waa-jib',
      'ad-da-waa al-mu-sak-kin',
    ],
    ur: [
      'neela school bag',
      'tez raftaar ticket',
      'pasandeeda khilona',
      'meetha laal saib',
      'clinic ka thermometer',
      'football ki nayi ball',
      'chamkeeli peeli chatri',
      'rangeen pencils ki drawing',
      'homework ke liye mashwara',
      'dard door karnay wali dawa',
    ],
    hi: [
      'neela school bag',
      'express yatra ticket',
      'pasandeeda khilauna',
      'meetha laal seb',
      'clinic thermometer',
      'football ki nayi ball',
      'chamkeeli peeli chhatri',
      'rangeen pencil drawing',
      'homework ke liye salah',
      'dard ki dava',
    ],
    fr: [
      'luh sahk day-kohl bluh',
      'luh tee-kay duh trahns-pohr rah-peed',
      'luh zhoo duh kohn-strewk-syohn pray-fay-ray',
      'lah pohm roozh kroh-kahnt',
      'luh tehr-moh-mehtr',
      'luh bah-lohn duh foot nuh-voh',
      'luh pah-rah-plwee zhohn veef',
      'luh deh-san oh kray-yohn',
      'luh bohn kohn-say poor lay duh-vwahr',
      'luh may-dee-kah-mahn ah-peh-zahn',
    ],
  },
  polites: {
    es: [
      '¿porfa?',
      'muchas gracias.',
      'si eres tan amable.',
      'te lo agradezco un montón.',
      'cuando puedas.',
      'con mucho gusto.',
      'un segundito.',
      '¡qué alegría!',
      'de verdad.',
      'para hoy mismo.',
    ],
    en: [
      'pretty please?',
      'thank you so much.',
      'if you would be so kind.',
      'I appreciate it a ton.',
      'whenever you have a moment.',
      'with great pleasure.',
      'just for a second.',
      'how wonderful!',
      'really and truly.',
      'right away today.',
    ],
    ar: [
      'لو تكرمت؟',
      'شكراً جزيلاً لك.',
      'إن كنت لطيفاً.',
      'ممتن لك جداً.',
      'في أقرب وقت.',
      'بكل سرور.',
      'للحظة واحدة.',
      'يا لها من فرحة!',
      'حبيبي والله.',
      'اليوم بالتحديد.',
    ],
    ur: [
      'پلیز؟',
      'آپ کا بہت شکریہ۔',
      'مہربانی فرما کر۔',
      'دل سے شکر گزار ہوں۔',
      'جب بھی وقت ملے۔',
      'بہت خوشی سے۔',
      'صرف ایک لمحے کے لیے۔',
      'کتنی زبردست بات ہے!',
      'سچ مچ۔',
      'آج ہی کے دن۔',
    ],
    hi: [
      'प्लीज़?',
      'आपका बहुत धन्यवाद।',
      'कृपया करके।',
      'दिल से आभारी हूँ।',
      'जब भी समय मिले।',
      'बड़ी खुशी से।',
      'बस एक पल के लिए।',
      'कितनी बढ़िया बात है!',
      'सचमुच।',
      'आज ही के दिन।',
    ],
    fr: [
      's\'il te plaît, dis ?',
      'merci infiniment.',
      'si tu es bien aimable.',
      'je te remercie tellement.',
      'dès que tu as une seconde.',
      'avec grand plaisir.',
      'juste un instant.',
      'quel bonheur !',
      'vraiment super.',
      'dès aujourd\'hui.',
    ],
  },
  politesPhonetic: {
    es: [
      'POHR-fah',
      'MOO-chahs GRAH-syahs',
      'SEE EH-rehs TAHN ah-MAH-bleh',
      'Teh loh ah-grah-DEHS-koh oon mohn-TOHN',
      'KWAHN-doh PWEH-dahs',
      'Kohn MOO-choh GOOS-toh',
      'Oon seh-goon-DEE-toh',
      'Keh ah-leh-GREE-ah',
      'Deh vehr-DAHD',
      'PAH-rah OY MEES-moh',
    ],
    en: [
      'prit-tee pleez',
      'thank yoo soh much',
      'if yoo wood bee soh kynd',
      'eye uh-pree-shee-ayt it',
      'wen-ev-er yoo hav a moh-ment',
      'with grayt plezh-er',
      'juhst for a sek-und',
      'how wuhn-der-ful',
      'reel-ee and troo-lee',
      'ryt uh-way to-day',
    ],
    ar: [
      'Low ta-kar-ramt',
      'Shook-ran ja-zee-lan lak',
      'In koon-ta la-tee-fan',
      'Moom-tann la-ka jid-dan',
      'Fee aq-rab waqt',
      'Bi-kull su-roor',
      'Li-lah-zah waa-hi-dah',
      'Yaa la-haa min far-hah',
      'Ha-bee-bee wal-lah',
      'Al-yawm bit-tah-deed',
    ],
    ur: [
      'Please',
      'Aap ka bohat shukriya',
      'Meherbani farma kar',
      'Dill say shukr guzaar hoon',
      'Jub bhi waqt milay',
      'Bohat khushi say',
      'Sirf ek lamhay kay liye',
      'Kitni zabardast baat hai',
      'Such much',
      'Aaj he kay din',
    ],
    hi: [
      'Please',
      'Aapka bahut dhanyavaad',
      'Kripya karke',
      'Dil se aabhari hoon',
      'Jab bhi samay mile',
      'Badi khushi se',
      'Bas ek pal ke liye',
      'Kitni badhiya baat hai',
      'Sach-much',
      'Aaj hi ke din',
    ],
    fr: [
      'Seel tuh play dee',
      'Mehr-see an-fee-nee-mahn',
      'See too ay byan em-ahbl',
      'Zhuh tuh ruh-mehr-see tel-mahn',
      'Day kuh too ah oon suh-gohnd',
      'Ah-vek grahn pleh-zeer',
      'Zhoost un an-stahn',
      'Kel boh-nuhr',
      'Vray-mahn soo-pehr',
      'Day oh-zhoor-dwee',
    ],
  },
  englishMeanings: [
    { opening: 'Pass me', need: 'the blue school backpack', polite: 'please?' },
    { opening: 'Hey, I would like', need: 'the express transit ticket', polite: 'thank you so much.' },
    { opening: 'Where did we keep', need: 'the favorite building block toy', polite: 'if you would be so kind.' },
    { opening: 'Please show me', need: 'the sweet crisp red apple', polite: 'I appreciate it a ton.' },
    { opening: 'I really love', need: 'the clinic digital thermometer', polite: 'whenever you have a moment.' },
    { opening: 'Can we take along', need: 'the brand-new soccer ball', polite: 'with great pleasure.' },
    { opening: 'Look closely at', need: 'the bright yellow umbrella', polite: 'just for a second.' },
    { opening: 'I am super excited for', need: 'the drawing with color pencils', polite: 'how wonderful!' },
    { opening: 'Please help me with', need: 'the helpful advice on homework', polite: 'really and truly.' },
    { opening: 'What time does', need: 'the soothing pain medicine', polite: 'arrive today?' },
  ],
};

/**
 * Dynamic 90-Day Sentence Engine
 * Generates at least 10 structured sentences per scenario seeded by (dayIndex % 30)
 */
export function generateScenarioSentences(
  scenarioId: string,
  targetLang: LanguageCode,
  motherTongue: LanguageCode,
  dayIndex: number,
  ageGroup: AgeGroup
): GeneratedSentence[] {
  const seed = (dayIndex - 1) % 30;
  const sentences: GeneratedSentence[] = [];

  const themeData = SCENARIO_THEMES[scenarioId];

  for (let i = 0; i < 10; i++) {
    const shift = (seed + i) % 10;
    const needShift = (seed * 2 + i) % 10;
    const politeShift = (seed * 3 + i) % 10;

    const opening = UNIVERSAL_CHUNK_SETS.openings[targetLang][shift];
    const openingPhonetic = UNIVERSAL_CHUNK_SETS.openingsPhonetic[targetLang][shift];

    // Use scenario specific theme objects if available, else generic needs
    const object = themeData?.objects[targetLang]
      ? themeData.objects[targetLang][needShift]
      : UNIVERSAL_CHUNK_SETS.needs[targetLang][needShift];

    const objectPhonetic = themeData?.objectsPhonetic[targetLang]
      ? themeData.objectsPhonetic[targetLang][needShift]
      : UNIVERSAL_CHUNK_SETS.needsPhonetic[targetLang][needShift];

    const polite = UNIVERSAL_CHUNK_SETS.polites[targetLang][politeShift];
    const politePhonetic = UNIVERSAL_CHUNK_SETS.politesPhonetic[targetLang][politeShift];

    // Build authentic native colloquial target string:
    // [Opening Chunk] + [Object/Need] + [Polite Marker]
    let colloquialTarget = `${opening} ${object}, ${polite}`;
    if (targetLang === 'ar' || targetLang === 'ur') {
      colloquialTarget = `${opening} ${object}، ${polite}`;
    }

    const phoneticTransliteration = `${openingPhonetic} — ${objectPhonetic} — ${politePhonetic}`;

    // Build Mother Tongue translation string
    const mtOpening = UNIVERSAL_CHUNK_SETS.openings[motherTongue][shift];
    const mtObject = themeData?.objects[motherTongue]
      ? themeData.objects[motherTongue][needShift]
      : UNIVERSAL_CHUNK_SETS.needs[motherTongue][needShift];
    const mtPolite = UNIVERSAL_CHUNK_SETS.polites[motherTongue][politeShift];

    let motherTongueTranslation = `${mtOpening} ${mtObject}, ${mtPolite}`;
    if (motherTongue === 'ar' || motherTongue === 'ur') {
      motherTongueTranslation = `${mtOpening} ${mtObject}، ${mtPolite}`;
    }

    sentences.push({
      id: `${scenarioId}-d${dayIndex}-s${i + 1}`,
      speaker: i % 2 === 0 ? 'Junior' : 'Native Friend',
      colloquialTarget,
      motherTongueTranslation,
      phoneticTransliteration,
      openingChunk: opening,
      objectNeed: object,
      politeMarker: polite,
      tip: `Day ${dayIndex} pattern drill · Frame substitution formula: [${opening}] + [${object}]`,
    });
  }

  return sentences;
}
