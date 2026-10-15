// Node script to build the complete 77-topic 2-word dataset
const fs = require('fs');

const DATA = {
  // 1. Home & Daily Life
  "breakfast-chat": [
    { en: "Warm toast", ur: "گرم ٹوسٹ", ur_rom: "Garam toast", es: "Tostada caliente", es_rom: "Tohs-TAH-dah kah-LYEHN-teh" },
    { en: "Drink milk", ur: "دودھ پیو", ur_rom: "Doodh peeyo", es: "Bebe leche", es_rom: "BEH-beh LEH-cheh" },
    { en: "Fresh juice", ur: "تازہ جوس", ur_rom: "Taaza juice", es: "Jugo fresco", es_rom: "HOO-goh FREHS-koh" }
  ],
  "lunch-dinner": [
    { en: "Eat food", ur: "کھانا کھاؤ", ur_rom: "Khaana khao", es: "Come comida", es_rom: "KOH-meh koh-MEE-dah" },
    { en: "Hot soup", ur: "گرم سوپ", ur_rom: "Garam soup", es: "Sopa caliente", es_rom: "SOH-pah kah-LYEHN-teh" },
    { en: "Yummy rice", ur: "مزیدار چاول", ur_rom: "Mazedar chawal", es: "Arroz rico", es_rom: "ah-RROHS REE-koh" }
  ],
  "kitchen-help": [
    { en: "Wash plate", ur: "پلیٹ دھوئیں", ur_rom: "Plate dho-ein", es: "Lava plato", es_rom: "LAH-vah PLAH-toh" },
    { en: "Clean table", ur: "میز صاف", ur_rom: "Mez saaf", es: "Limpia mesa", es_rom: "LEEM-pyah MEH-sah" },
    { en: "Pass spoon", ur: "چمچ دیں", ur_rom: "Chamach dein", es: "Pasa cuchara", es_rom: "PAH-sah koo-CHAH-rah" }
  ],
  "bedtime-stories": [
    { en: "Read book", ur: "کتاب پڑھیں", ur_rom: "Kitaab parhein", es: "Lee libro", es_rom: "LEH-eh LEE-broh" },
    { en: "Sweet dreams", ur: "اچھے خواب", ur_rom: "Achhe khwab", es: "Dulces sueños", es_rom: "DOOL-sehs SWEH-nyohs" },
    { en: "Sleep well", ur: "آرام کرو", ur_rom: "Aaram karo", es: "Duerme bien", es_rom: "DWEHR-meh BYEHN" }
  ],
  "morning-talk": [
    { en: "Wake up", ur: "جاگ جاؤ", ur_rom: "Jaag jao", es: "Despierta ya", es_rom: "dehs-PYEHR-tah yah" },
    { en: "Good morning", ur: "صبح بخیر", ur_rom: "Subah bakhair", es: "Buenos días", es_rom: "BWEH-nohs DEE-ahs" },
    { en: "Rise early", ur: "جلدی اٹھیں", ur_rom: "Jaldi uthein", es: "Levántate pronto", es_rom: "leh-VAHN-tah-teh PROHN-toh" }
  ],
  "evening-tea": [
    { en: "Warm tea", ur: "گرم چائے", ur_rom: "Garam chai", es: "Té caliente", es_rom: "TEH kah-LYEHN-teh" },
    { en: "Sweet biscuit", ur: "میٹھا بسکٹ", ur_rom: "Meetha biscuit", es: "Galleta dulce", es_rom: "gah-YEH-tah DOOL-seh" },
    { en: "Sip slow", ur: "آہستہ پیئیں", ur_rom: "Aahista peeyein", es: "Bebe despacio", es_rom: "BEH-beh dehs-PAH-syoh" }
  ],

  // 2. Family & Relatives
  "mom-and-dad": [
    { en: "Love mom", ur: "امی پیاری", ur_rom: "Ammi pyaari", es: "Ama mamá", es_rom: "AH-mah mah-MAH" },
    { en: "Hug dad", ur: "ابو پیارے", ur_rom: "Abbu pyaare", es: "Abraza papá", es_rom: "ah-BRAH-zah pah-PAH" },
    { en: "Kind parents", ur: "مہربان والدین", ur_rom: "Meherbaan walidain", es: "Padres amables", es_rom: "PAH-drehs ah-MAH-blehs" }
  ],
  "grandparents-chat": [
    { en: "Tell story", ur: "کہانی سنائیں", ur_rom: "Kahani sunayein", es: "Cuenta cuento", es_rom: "KWEHN-tah KWEHN-toh" },
    { en: "Gentle grandma", ur: "شفیق دادی", ur_rom: "Shafeeq dadi", es: "Abuela cariñosa", es_rom: "ah-BWEH-lah kah-ree-NYOH-sah" },
    { en: "Happy grandpa", ur: "مسکراتے دادا", ur_rom: "Muskuraate dada", es: "Abuelo alegre", es_rom: "ah-BWEH-loh ah-LEH-greh" }
  ],
  "morning-with-aunt": [
    { en: "Greet aunt", ur: "خالہ سلام", ur_rom: "Khaala salaam", es: "Saluda tía", es_rom: "sah-LOO-dah TEE-ah" },
    { en: "Warm smile", ur: "پیاری مسکراہٹ", ur_rom: "Pyaari muskuraahat", es: "Cálida sonrisa", es_rom: "KAH-lee-dah sohn-REE-sah" },
    { en: "Help aunt", ur: "مدد کریں", ur_rom: "Madad karein", es: "Ayuda tía", es_rom: "ah-YOO-dah TEE-ah" }
  ],
  "dinner-with-uncle": [
    { en: "Welcome uncle", ur: "چچا خوش‌آمدید", ur_rom: "Chacha khush-aamdeed", es: "Bienvenido tío", es_rom: "byehn-veh-NEE-doh TEE-oh" },
    { en: "Tasty dinner", ur: "لذیذ کھانا", ur_rom: "Lazeez khaana", es: "Cena rica", es_rom: "SEH-nah REE-kah" },
    { en: "Share food", ur: "کھانا بانٹیں", ur_rom: "Khaana baantein", es: "Comparte comida", es_rom: "kohm-PAHR-teh koh-MEE-dah" }
  ],
  "big-feelings": [
    { en: "Feel happy", ur: "خوش رہو", ur_rom: "Khush raho", es: "Siente alegría", es_rom: "SYEHN-teh ah-leh-GREE-ah" },
    { en: "Stay calm", ur: "پرسکون رہیں", ur_rom: "Pursukoon rahein", es: "Mantén calma", es_rom: "mahn-TEHN KAHL-mah" },
    { en: "Be brave", ur: "بہادر بنو", ur_rom: "Bahadur bano", es: "Sé valiente", es_rom: "SEH vah-LYEHN-teh" }
  ],

  // 3. Travel & Transport
  "bus-station": [
    { en: "Catch bus", ur: "بس پکڑیں", ur_rom: "Bus pakrein", es: "Toma autobús", es_rom: "TOH-mah ow-toh-BOOS" },
    { en: "Bus stop", ur: "بس اسٹاپ", ur_rom: "Bus stop", es: "Parada autobús", es_rom: "pah-RAH-dah ow-toh-BOOS" },
    { en: "Buy ticket", ur: "ٹکٹ خریدیں", ur_rom: "Ticket khareedein", es: "Compra boleto", es_rom: "KOHM-prah boh-LEH-toh" }
  ],
  "train-tickets": [
    { en: "Fast train", ur: "تیز ٹرین", ur_rom: "Taiz train", es: "Tren rápido", es_rom: "TREHN RRAH-pee-doh" },
    { en: "Train ticket", ur: "ٹرین ٹکٹ", ur_rom: "Train ticket", es: "Boleto tren", es_rom: "boh-LEH-toh TREHN" },
    { en: "Board train", ur: "سوار ہوں", ur_rom: "Sawaar hon", es: "Sube tren", es_rom: "SOO-beh TREHN" }
  ],
  "in-a-taxi": [
    { en: "Hail taxi", ur: "ٹیکسی روکیں", ur_rom: "Taxi rokein", es: "Pide taxi", es_rom: "PEE-deh TAHK-see" },
    { en: "Sit inside", ur: "اندر بیٹھیں", ur_rom: "Andar baithein", es: "Siéntate dentro", es_rom: "SYEHN-tah-teh DEHN-troh" },
    { en: "Pay fare", ur: "کرایہ دیں", ur_rom: "Kiraaya dein", es: "Paga tarifa", es_rom: "PAH-gah tah-REE-fah" }
  ],
  "airplane-flight": [
    { en: "Fly high", ur: "اونچا اڑیں", ur_rom: "Ooncha urein", es: "Vuela alto", es_rom: "VWEH-lah AHL-toh" },
    { en: "Fast airplane", ur: "تیز جہاز", ur_rom: "Taiz jahaaz", es: "Avión rápido", es_rom: "ah-VYEOHN RRAH-pee-doh" },
    { en: "Window seat", ur: "کھڑکی سیٹ", ur_rom: "Khirki seat", es: "Asiento ventana", es_rom: "ah-SYEHN-toh vehn-TAH-nah" }
  ],
  "asking-directions": [
    { en: "Turn right", ur: "دائیں مڑیں", ur_rom: "Daayein murein", es: "Gira derecha", es_rom: "HEE-rah deh-REH-chah" },
    { en: "Turn left", ur: "بائیں مڑیں", ur_rom: "Baayein murein", es: "Gira izquierda", es_rom: "HEE-rah ees-KYEHR-dah" },
    { en: "Go straight", ur: "سیدھے جائیں", ur_rom: "Seedhe jaayein", es: "Sigue recto", es_rom: "SEE-geh RREHK-toh" }
  ],

  // 4. Shopping & Food
  "grocery-store": [
    { en: "Fresh fruit", ur: "تازہ پھل", ur_rom: "Taaza phal", es: "Fruta fresca", es_rom: "FROO-tah FREHS-kah" },
    { en: "Buy apples", ur: "سیب خریدیں", ur_rom: "Saib khareedein", es: "Compra manzanas", es_rom: "KOHM-prah mahn-SAH-nahs" },
    { en: "Grocery cart", ur: "خریداری ٹوکری", ur_rom: "Khareedaari tokri", es: "Carrito compras", es_rom: "kah-RREE-toh KOHM-prahs" }
  ],
  "buying-toys": [
    { en: "Pick toy", ur: "کھلونا چنیں", ur_rom: "Khilona chunein", es: "Elige juguete", es_rom: "eh-LEE-heh hoo-GEH-teh" },
    { en: "Fun puzzle", ur: "مزیدار پہیلی", ur_rom: "Mazedaar paheli", es: "Rompecabezas divertido", es_rom: "rrohm-peh-kah-BEH-sahs dee-vehr-TEE-doh" },
    { en: "Toy car", ur: "کھلونا گاڑی", ur_rom: "Khilona gaadi", es: "Coche juguete", es_rom: "KOH-cheh hoo-GEH-teh" }
  ],
  "paying-cashier": [
    { en: "Pay money", ur: "پیسے دیں", ur_rom: "Paise dein", es: "Paga dinero", es_rom: "PAH-gah dee-NEH-roh" },
    { en: "Cash counter", ur: "کیش کاؤنٹر", ur_rom: "Cash counter", es: "Caja pago", es_rom: "KAH-hah PAH-goh" },
    { en: "Take receipt", ur: "رسید لیں", ur_rom: "Raseed lein", es: "Toma recibo", es_rom: "TOH-mah rreh-SEE-boh" }
  ],
  "ordering-snacks": [
    { en: "Want snack", ur: "اسنیک چاہیے", ur_rom: "Snack chahiye", es: "Quiero merienda", es_rom: "KYEH-roh meh-RYEHN-dah" },
    { en: "Crispy chips", ur: "خستہ چپس", ur_rom: "Khasta chips", es: "Papas crujientes", es_rom: "PAH-pahs kroo-HYEHN-tehs" },
    { en: "Sweet treat", ur: "میٹھی دعوت", ur_rom: "Meethi daawat", es: "Dulce regalo", es_rom: "DOOL-seh rreh-GAH-loh" }
  ],
  "street-food": [
    { en: "Hot snack", ur: "گرم سموسہ", ur_rom: "Garam samosa", es: "Bocadillo caliente", es_rom: "boh-kah-DEE-yoh kah-LYEHN-teh" },
    { en: "Spicy food", ur: "چٹپٹا کھانا", ur_rom: "Chatpata khaana", es: "Comida sabrosa", es_rom: "koh-MEE-dah sah-BROH-sah" },
    { en: "Sweet drink", ur: "میٹھا شربت", ur_rom: "Meetha sharbat", es: "Bebida dulce", es_rom: "beh-BEE-dah DOOL-seh" }
  ],
  "table-booking": [
    { en: "Book table", ur: "میز بک", ur_rom: "Mez book", es: "Reserva mesa", es_rom: "rreh-SEHR-vah MEH-sah" },
    { en: "Sit here", ur: "یہاں بیٹھیں", ur_rom: "Yahan baithein", es: "Siéntate aquí", es_rom: "SYEHN-tah-teh ah-KEE" },
    { en: "Dinner table", ur: "کھانے میز", ur_rom: "Khaane mez", es: "Mesa comedor", es_rom: "MEH-sah koh-meh-DOHR" }
  ],

  // 5. Health & Doctor
  "feeling-sick": [
    { en: "High fever", ur: "تیز بخار", ur_rom: "Taiz bukhaar", es: "Fiebre alta", es_rom: "FYEH-breh AHL-tah" },
    { en: "Rest now", ur: "آرام کریں", ur_rom: "Aaram karein", es: "Descansa ahora", es_rom: "dehs-KAHN-sah ah-OH-rah" },
    { en: "Drink water", ur: "پانی پیئیں", ur_rom: "Paani peeyein", es: "Bebe agua", es_rom: "BEH-beh AH-gwah" }
  ],
  "at-the-clinic": [
    { en: "See doctor", ur: "ڈاکٹر دیکھیں", ur_rom: "Doctor dekhein", es: "Visita médico", es_rom: "vee-SEE-tah MEH-dee-koh" },
    { en: "Feel better", ur: "بہتر ہوں", ur_rom: "Behtar hon", es: "Mejora pronto", es_rom: "meh-HOH-rah PROHN-toh" },
    { en: "Quiet clinic", ur: "پرسکون کلینک", ur_rom: "Pursukoon clinic", es: "Clínica tranquila", es_rom: "KLEE-nee-kah trahn-KEE-lah" }
  ],
  "pharmacy-visit": [
    { en: "Buy medicine", ur: "دوا خریدیں", ur_rom: "Dawa khareedein", es: "Compra medicina", es_rom: "KOHM-prah meh-dee-SEE-nah" },
    { en: "Take syrup", ur: "شربت پیئیں", ur_rom: "Sharbat peeyein", es: "Toma jarabe", es_rom: "TOH-mah hah-RAH-beh" },
    { en: "Medical store", ur: "میڈیکل اسٹور", ur_rom: "Medical store", es: "Tienda farmacia", es_rom: "TYEHN-dah fahr-MAH-syah" }
  ],
  "describing-pain": [
    { en: "Sore throat", ur: "گلا خراب", ur_rom: "Gala kharaab", es: "Garganta adolorida", es_rom: "gahr-GAHN-tah ah-doh-loh-REE-dah" },
    { en: "Tummy ache", ur: "پیٹ درد", ur_rom: "Pait dard", es: "Dolor barriga", es_rom: "doh-LOHR bah-RREE-gah" },
    { en: "Hurt finger", ur: "انگلی زخمی", ur_rom: "Ungli zakhmi", es: "Dedo lastimado", es_rom: "DEH-doh lahs-tee-MAH-doh" }
  ],
  "comforting-family": [
    { en: "Get well", ur: "جلد صحت", ur_rom: "Jald sehat", es: "Mejórate pronto", es_rom: "meh-HOH-rah-teh PROHN-toh" },
    { en: "Warm hug", ur: "پیارا گلے", ur_rom: "Pyaara galay", es: "Abrazo cálido", es_rom: "ah-BRAH-zoh KAH-lee-doh" },
    { en: "Feel safe", ur: "محفوظ رہیں", ur_rom: "Mehfooz rahein", es: "Siéntete seguro", es_rom: "SYEHN-teh-teh seh-GOO-roh" }
  ],

  // 6. School & Study
  "greeting-teachers": [
    { en: "Good morning", ur: "صبح بخیر", ur_rom: "Subah bakhair", es: "Buenos días", es_rom: "BWEH-nohs DEE-ahs" },
    { en: "Polite greeting", ur: "باادب سلام", ur_rom: "Ba-adab salaam", es: "Saludo respetuoso", es_rom: "sah-LOO-doh rrehs-peh-TWOH-soh" },
    { en: "Respect teacher", ur: "استاد احترام", ur_rom: "Ustaad ehtiraam", es: "Respeta maestro", es_rom: "rrehs-PEH-tah mah-EHS-troh" }
  ],
  "homework-help": [
    { en: "Open notebook", ur: "کاپی کھولیں", ur_rom: "Copy kholein", es: "Abre cuaderno", es_rom: "AH-breh kwah-DEHR-noh" },
    { en: "Write answer", ur: "جواب لکھیں", ur_rom: "Jawab likhein", es: "Escribe respuesta", es_rom: "ehs-KREE-beh rrehs-PWEHS-tah" },
    { en: "Finish homework", ur: "کام مکمل", ur_rom: "Kaam mukammal", es: "Termina tarea", es_rom: "tehr-MEE-nah tah-REH-ah" }
  ],
  "classroom-chat": [
    { en: "Quiet please", ur: "خاموش رہیں", ur_rom: "Khaamosh rahein", es: "Silencio porfavor", es_rom: "see-LEHN-syoh pohr-fah-VOHR" },
    { en: "Raise hand", ur: "ہاتھ اٹھائیں", ur_rom: "Haath uthaayein", es: "Levanta mano", es_rom: "leh-VAHN-tah MAH-noh" },
    { en: "Listen closely", ur: "غور سنیں", ur_rom: "Ghaur sunein", es: "Escucha bien", es_rom: "ehs-KOO-chah BYEHN" }
  ],
  "playground-bell": [
    { en: "Recess bell", ur: "تفریح گھنٹی", ur_rom: "Tafreeh ghanti", es: "Campana recreo", es_rom: "kahm-PAH-nah rreh-KREH-oh" },
    { en: "Run outside", ur: "باہر دوڑیں", ur_rom: "Baahar daurein", es: "Corre afuera", es_rom: "KOH-rreh ah-FWEH-rah" },
    { en: "Lunch break", ur: "کھانے وقفہ", ur_rom: "Khaane waqfa", es: "Pausa almuerzo", es_rom: "POW-sah ahl-MWEHR-zoh" }
  ],
  "group-projects": [
    { en: "Work together", ur: "ملکر کام", ur_rom: "Milkar kaam", es: "Trabajen juntos", es_rom: "trah-BAH-hehn HOON-tohs" },
    { en: "Share ideas", ur: "مشورہ کریں", ur_rom: "Mashwara karein", es: "Comparte ideas", es_rom: "kohm-PAHR-teh ee-DEH-ahs" },
    { en: "Draw poster", ur: "پوسٹر بنائیں", ur_rom: "Poster banayein", es: "Dibuja póster", es_rom: "dee-BOO-hah POHS-tehr" }
  ],

  // 7. Friends & Play
  "making-friends": [
    { en: "Say hello", ur: "ہیلو کہیں", ur_rom: "Hello kahein", es: "Di hola", es_rom: "DEE OH-lah" },
    { en: "Be friends", ur: "دوست بنیں", ur_rom: "Dost banein", es: "Seamos amigos", es_rom: "seh-AH-mohs ah-MEE-gohs" },
    { en: "Play together", ur: "ساتھ کھیلیں", ur_rom: "Saath khelein", es: "Jueguen juntos", es_rom: "HWEH-gehn HOON-tohs" }
  ],
  "birthday-party": [
    { en: "Happy birthday", ur: "سالگرہ مبارک", ur_rom: "Saalgirah mubarak", es: "Feliz cumpleaños", es_rom: "feh-LEEZ koom-pleh-AH-nyohs" },
    { en: "Cut cake", ur: "کیک کاٹیں", ur_rom: "Cake kaatein", es: "Corta pastel", es_rom: "KOHR-tah pahs-TEHL" },
    { en: "Blow candles", ur: "مومبتی بجھائیں", ur_rom: "Mombatti bujhaayein", es: "Sopla velas", es_rom: "SOH-plah VEH-lahs" }
  ],
  "sharing-toys": [
    { en: "Share blocks", ur: "بلاکس بانٹیں", ur_rom: "Blocks baantein", es: "Comparte bloques", es_rom: "kohm-PAHR-teh BLOH-kehs" },
    { en: "Take turns", ur: "باری لیں", ur_rom: "Baari lein", es: "Toma turnos", es_rom: "TOH-mah TOOR-nohs" },
    { en: "Play fair", ur: "اچھا کھیلیں", ur_rom: "Achha khelein", es: "Juega limpio", es_rom: "HWEH-gah LEEM-pyoh" }
  ],
  "playground-games": [
    { en: "Kick ball", ur: "گیند ماریں", ur_rom: "Gaind maarein", es: "Patea pelota", es_rom: "pah-TEH-ah peh-LOH-tah" },
    { en: "High swing", ur: "اونچا جھولا", ur_rom: "Ooncha jhoola", es: "Columpio alto", es_rom: "koh-LOOM-pyoh AHL-toh" },
    { en: "Hide seek", ur: "آنکھ مچولی", ur_rom: "Aankh macholi", es: "Juega escondite", es_rom: "HWEH-gah ehs-kohn-DEE-teh" }
  ],
  "inviting-a-friend": [
    { en: "Come over", ur: "گھر آئیں", ur_rom: "Ghar aayein", es: "Ven aquí", es_rom: "VEHN ah-KEE" },
    { en: "Welcome friend", ur: "خوش آمدید", ur_rom: "Khush aamdeed", es: "Bienvenido amigo", es_rom: "byehn-veh-NEE-doh ah-MEE-goh" },
    { en: "Play games", ur: "کھیل کھیلیں", ur_rom: "Khel khelein", es: "Juega juegos", es_rom: "HWEH-gah HWEH-gohs" }
  ],

  // 8. Nature & Outdoors
  "park-walks": [
    { en: "Green grass", ur: "ہری گھاس", ur_rom: "Hari ghaas", es: "Pasto verde", es_rom: "PAHS-toh VEHR-deh" },
    { en: "Tall trees", ur: "اونچے درخت", ur_rom: "Oonche darakht", es: "Árboles altos", es_rom: "AHR-boh-lehs AHL-tohs" },
    { en: "Fresh air", ur: "تازہ ہوا", ur_rom: "Taaza hawa", es: "Aire fresco", es_rom: "EYE-reh FREHS-koh" }
  ],
  "rainy-days": [
    { en: "Rain drops", ur: "بارش قطرے", ur_rom: "Baarish qatre", es: "Gotas lluvia", es_rom: "GOH-tahs YOO-vyah" },
    { en: "Wet umbrella", ur: "گیلی چھتری", ur_rom: "Geeli chhatri", es: "Paraguas mojado", es_rom: "pah-RAH-gwahs moh-HAH-doh" },
    { en: "Water puddle", ur: "پانی گڑھا", ur_rom: "Paani gaddha", es: "Charco agua", es_rom: "CHAHR-koh AH-gwah" }
  ],
  "pet-animals": [
    { en: "Cute kitten", ur: "پیاری بلی", ur_rom: "Pyaari billi", es: "Lindo gatito", es_rom: "LEEN-doh gah-TEE-toh" },
    { en: "Loyal puppy", ur: "وفادار کتا", ur_rom: "Wafadaar kutta", es: "Cachorro leal", es_rom: "kah-CHOH-rroh leh-AHL" },
    { en: "Soft fur", ur: "نرم بال", ur_rom: "Narm baal", es: "Pelaje suave", es_rom: "peh-LAH-heh SWAH-veh" }
  ],
  "beach-fun": [
    { en: "Sea waves", ur: "سمندری لہریں", ur_rom: "Samandari lehrein", es: "Olas marinas", es_rom: "OH-lahs mah-REE-nahs" },
    { en: "Golden sand", ur: "سنہری ریت", ur_rom: "Sunehri rait", es: "Arena dorada", es_rom: "ah-REH-nah doh-RAH-dah" },
    { en: "Sand castle", ur: "ریت قلعہ", ur_rom: "Rait qila", es: "Castillo arena", es_rom: "kahs-TEE-yoh ah-REH-nah" }
  ],
  "camping-trip": [
    { en: "Pitch tent", ur: "خیمہ لگائیں", ur_rom: "Khaima lagaayein", es: "Arma tienda", es_rom: "AHR-mah TYEHN-dah" },
    { en: "Camp fire", ur: "کیمپ آگ", ur_rom: "Camp aag", es: "Fogata brillante", es_rom: "foh-GAH-tah bree-YAHN-teh" },
    { en: "Starlit night", ur: "تاروں رات", ur_rom: "Taaron raat", es: "Noche estrellada", es_rom: "NOH-cheh ehs-treh-YAH-dah" }
  ],

  // 9. Manners & Help
  "saying-thank-you": [
    { en: "Thank you", ur: "شکریہ ادا", ur_rom: "Shukriya ada", es: "Muchas gracias", es_rom: "MOO-chahs GRAH-syahs" },
    { en: "Much thanks", ur: "بہت شکریہ", ur_rom: "Bohat shukriya", es: "Mil gracias", es_rom: "MEEL GRAH-syahs" },
    { en: "You welcome", ur: "کوئی بات", ur_rom: "Koi baat", es: "De nada", es_rom: "deh NAH-dah" }
  ],
  "saying-sorry": [
    { en: "So sorry", ur: "معاف کیجیے", ur_rom: "Maaf keejiye", es: "Lo siento", es_rom: "loh SYEHN-toh" },
    { en: "My mistake", ur: "میری غلطی", ur_rom: "Meri ghalti", es: "Mi error", es_rom: "mee eh-RROHR" },
    { en: "Pardon me", ur: "معاف فرمائیں", ur_rom: "Maaf farmaayein", es: "Perdona me", es_rom: "pehr-DOH-nah meh" }
  ],
  "asking-for-help": [
    { en: "Need help", ur: "مدد چاہیے", ur_rom: "Madad chahiye", es: "Necesito ayuda", es_rom: "neh-seh-SEE-toh ah-YOO-dah" },
    { en: "Help me", ur: "مدد کریں", ur_rom: "Madad karein", es: "Ayúdame ahora", es_rom: "ah-YOO-dah-meh ah-OH-rah" },
    { en: "Guide me", ur: "رہنمائی کریں", ur_rom: "Rehnumai karein", es: "Guíame porfavor", es_rom: "GEE-ah-meh pohr-fah-VOHR" }
  ],
  "lost-in-public": [
    { en: "Stay safe", ur: "محفوظ رہیں", ur_rom: "Mehfooz rahein", es: "Mantente seguro", es_rom: "mahn-TEHN-teh seh-GOO-roh" },
    { en: "Find guard", ur: "گارڈ ڈھونڈیں", ur_rom: "Guard dhoondein", es: "Busca guardia", es_rom: "BOOS-kah GWAHR-dyah" },
    { en: "Call mom", ur: "امی بلائیں", ur_rom: "Ammi bulaayein", es: "Llama mamá", es_rom: "YAH-mah mah-MAH" }
  ],
  "polite-requests": [
    { en: "Please pass", ur: "براہ کرم", ur_rom: "Barahe karam", es: "Pasa porfavor", es_rom: "PAH-sah pohr-fah-VOHR" },
    { en: "May I", ur: "اجازت ہے", ur_rom: "Ijaazat hai", es: "Puedo entrar", es_rom: "PWEH-doh ehn-TRAHR" },
    { en: "Give please", ur: "برائے مہربانی", ur_rom: "Baraaye meherbani", es: "Dame porfavor", es_rom: "DAH-meh pohr-fah-VOHR" }
  ],

  // 10. Fun & Tech
  "video-games": [
    { en: "Play game", ur: "گیم کھیلیں", ur_rom: "Game khelein", es: "Juega videojuego", es_rom: "HWEH-gah vee-deh-oh-HWEH-goh" },
    { en: "High score", ur: "اعلیٰ اسکور", ur_rom: "Aala score", es: "Puntuación alta", es_rom: "poon-twah-SYOHN AHL-tah" },
    { en: "Press start", ur: "اسٹارٹ دبائیں", ur_rom: "Start dabaayein", es: "Presiona inicio", es_rom: "preh-SYOH-nah ee-NEE-syoh" }
  ],
  "cartoon-talk": [
    { en: "Funny cartoon", ur: "مزیدار کارٹون", ur_rom: "Mazedaar cartoon", es: "Dibujo divertido", es_rom: "dee-BOO-hoh dee-vehr-TEE-doh" },
    { en: "Watch show", ur: "شو دیکھیں", ur_rom: "Show dekhein", es: "Mira programa", es_rom: "MEE-rah proh-GRAH-mah" },
    { en: "Laugh loud", ur: "کھلکھلا کر", ur_rom: "Khilkhila kar", es: "Ríe fuerte", es_rom: "REE-eh FWEHR-teh" }
  ],
  "drawing-colors": [
    { en: "Color crayons", ur: "رنگین مومبتی", ur_rom: "Rangeen mombatti", es: "Crayones coloridos", es_rom: "krah-YOH-nehs koh-loh-REE-dohs" },
    { en: "Draw picture", ur: "تصویر بنائیں", ur_rom: "Tasveer banayein", es: "Dibuja cuadro", es_rom: "dee-BOO-hah KWAH-droh" },
    { en: "Bright red", ur: "تیز لال", ur_rom: "Taiz laal", es: "Rojo brillante", es_rom: "RROH-hoh bree-YAHN-teh" }
  ],
  "phone-calls": [
    { en: "Ring bell", ur: "گھنٹی بجی", ur_rom: "Ghanti baji", es: "Suena timbre", es_rom: "SWEH-nah TEEM-breh" },
    { en: "Answer phone", ur: "فون اٹھائیں", ur_rom: "Phone uthaayein", es: "Contesta teléfono", es_rom: "kohn-TEHS-tah teh-LEH-foh-noh" },
    { en: "Say hello", ur: "ہیلو بولیں", ur_rom: "Hello bolein", es: "Di hola", es_rom: "DEE OH-lah" }
  ],
  "video-chats": [
    { en: "Wave hand", ur: "ہاتھ ہلائیں", ur_rom: "Haath hilaayein", es: "Mueve mano", es_rom: "MWEH-veh MAH-noh" },
    { en: "Video call", ur: "ویڈیو کال", ur_rom: "Video call", es: "Videollamada activa", es_rom: "vee-deh-oh-yah-MAH-dah ahk-TEE-vah" },
    { en: "See face", ur: "چہرہ دیکھیں", ur_rom: "Chehra dekhein", es: "Mira cara", es_rom: "MEE-rah KAH-rah" }
  ],

  // 11. Time & Weather
  "telling-time": [
    { en: "Wall clock", ur: "دیوار گھڑی", ur_rom: "Deewaar ghari", es: "Reloj pared", es_rom: "rreh-LOH pah-REHD" },
    { en: "What time", ur: "کیا وقت", ur_rom: "Kya waqt", es: "Qué hora", es_rom: "KEH OH-rah" },
    { en: "Noon time", ur: "دوپہر وقت", ur_rom: "Dopehar waqt", es: "Hora mediodía", es_rom: "OH-rah meh-dyoh-DEE-ah" }
  ],
  "todays-weather": [
    { en: "Sunny day", ur: "دھوپ دن", ur_rom: "Dhoop din", es: "Día soleado", es_rom: "DEE-ah soh-leh-AH-doh" },
    { en: "Cloudy sky", ur: "ابر آلود", ur_rom: "Abr alood", es: "Cielo nublado", es_rom: "SYEH-loh noo-BLAH-doh" },
    { en: "Cool breeze", ur: "ٹھنڈی ہوا", ur_rom: "Thandi hawa", es: "Brisa fresca", es_rom: "BREE-sah FREHS-kah" }
  ],
  "hot-and-cold-days": [
    { en: "Very hot", ur: "بہت گرم", ur_rom: "Bohat garam", es: "Muy caliente", es_rom: "MWEE kah-LYEHN-teh" },
    { en: "Very cold", ur: "بہت ٹھنڈا", ur_rom: "Bohat thanda", es: "Mucho frío", es_rom: "MOO-choh FREE-oh" },
    { en: "Wear jacket", ur: "جیکٹ پہنیں", ur_rom: "Jacket pehnein", es: "Usa chaqueta", es_rom: "OO-sah chah-KEH-tah" }
  ],
  "morning-routine": [
    { en: "Wash face", ur: "چہرہ دھوئیں", ur_rom: "Chehra dho-ein", es: "Lava cara", es_rom: "LAH-vah KAH-rah" },
    { en: "Brush teeth", ur: "دانت صاف", ur_rom: "Daant saaf", es: "Cepilla dientes", es_rom: "seh-PEE-yah DYEHN-tehs" },
    { en: "Comb hair", ur: "بال بنائیں", ur_rom: "Baal banayein", es: "Peina cabello", es_rom: "PEY-nah kah-BEH-yoh" }
  ],
  "night-sky": [
    { en: "Bright moon", ur: "چمکتا چاند", ur_rom: "Chamakta chaand", es: "Luna brillante", es_rom: "LOO-nah bree-YAHN-teh" },
    { en: "Shining stars", ur: "چمکتے تارے", ur_rom: "Chamakte taare", es: "Estrellas brillantes", es_rom: "ehs-TREH-yahs bree-YAHN-tehs" },
    { en: "Dark night", ur: "اندھیری رات", ur_rom: "Andheri raat", es: "Noche oscura", es_rom: "NOH-cheh ohs-KOO-rah" }
  ],

  // 12. Holidays & Events
  "holiday-plans": [
    { en: "Summer trip", ur: "گرمائی سفر", ur_rom: "Garmaai safar", es: "Viaje verano", es_rom: "VYAH-heh veh-RAH-noh" },
    { en: "Fun picnic", ur: "پرلطف پکنک", ur_rom: "Purlutf picnic", es: "Picnic divertido", es_rom: "PEEK-neek dee-vehr-TEE-doh" },
    { en: "Pack bags", ur: "سامان باندھیں", ur_rom: "Saamaan baandhein", es: "Prepara maletas", es_rom: "preh-PAH-rah mah-LEH-tahs" }
  ],
  "festival-greetings": [
    { en: "Happy holiday", ur: "عید مبارک", ur_rom: "Eid mubarak", es: "Felices fiestas", es_rom: "feh-LEE-sehs FYEHS-tahs" },
    { en: "Holiday joy", ur: "چھٹی خوشی", ur_rom: "Chhutti khushi", es: "Alegría festiva", es_rom: "ah-leh-GREE-ah fehs-TEE-vah" },
    { en: "Sweet treats", ur: "میٹھی سوغات", ur_rom: "Meethi saugaat", es: "Dulces ricos", es_rom: "DOOL-sehs REE-kohs" }
  ],
  "packing-bags": [
    { en: "Big suitcase", ur: "بڑا بکس", ur_rom: "Bada box", es: "Maleta grande", es_rom: "mah-LEH-tah GRAHN-deh" },
    { en: "Pack clothes", ur: "کپڑے رکھیں", ur_rom: "Kapre rakhein", es: "Guarda ropa", es_rom: "GWAHR-dah RROH-pah" },
    { en: "Zip bag", ur: "بیگ بند", ur_rom: "Bag band", es: "Cierra bolso", es_rom: "SYEH-rrah BOHL-soh" }
  ],
  "happy-new-year": [
    { en: "New year", ur: "نیا سال", ur_rom: "Naya saal", es: "Año nuevo", es_rom: "AH-nyoh NWEH-voh" },
    { en: "Happy celebration", ur: "مبارک جشن", ur_rom: "Mubarak jashan", es: "Celebración alegre", es_rom: "seh-leh-brah-SYOHN ah-LEH-greh" },
    { en: "Bright fireworks", ur: "روشن آتشبازی", ur_rom: "Roshan aatishbaazi", es: "Fuegos brillantes", es_rom: "FWEH-gohs bree-YAHN-tehs" }
  ],
  "birthday-gifts": [
    { en: "Gift box", ur: "تحفہ ڈبہ", ur_rom: "Tohfa dabba", es: "Caja regalo", es_rom: "KAH-hah rreh-GAH-loh" },
    { en: "Open present", ur: "تحفہ کھولیں", ur_rom: "Tohfa kholein", es: "Abre regalo", es_rom: "AH-breh rreh-GAH-loh" },
    { en: "Big surprise", ur: "بڑا سرپرائز", ur_rom: "Bada surprise", es: "Gran sorpresa", es_rom: "GRAHN sohr-PREH-sah" }
  ],

  // 13. Sports & Games
  "playing-soccer": [
    { en: "Kick ball", ur: "گیند ماریں", ur_rom: "Gaind maarein", es: "Patea balón", es_rom: "pah-TEH-ah bah-LOHN" },
    { en: "Score goal", ur: "گول کریں", ur_rom: "Goal karein", es: "Marca gol", es_rom: "MAHR-kah GOHL" },
    { en: "Run fast", ur: "تیز دوڑیں", ur_rom: "Taiz daurein", es: "Corre rápido", es_rom: "KOH-rreh RRAH-pee-doh" }
  ],
  "swimming-talk": [
    { en: "Cool pool", ur: "ٹھنڈا تالاب", ur_rom: "Thanda taalaab", es: "Piscina fresca", es_rom: "pees-SEE-nah FREHS-kah" },
    { en: "Swim fast", ur: "تیز تیریں", ur_rom: "Taiz tairein", es: "Nada rápido", es_rom: "NAH-dah RRAH-pee-doh" },
    { en: "Blue water", ur: "نیلا پانی", ur_rom: "Neela paani", es: "Agua azul", es_rom: "AH-gwah ah-ZOOL" }
  ],
  "team-games": [
    { en: "Pass ball", ur: "گیند دیں", ur_rom: "Gaind dein", es: "Pasa pelota", es_rom: "PAH-sah peh-LOH-tah" },
    { en: "Great team", ur: "زبردست ٹیم", ur_rom: "Zabardast team", es: "Buen equipo", es_rom: "BWEHN eh-KEE-poh" },
    { en: "Play together", ur: "ملکر کھیلیں", ur_rom: "Milkar khelein", es: "Jueguen unidos", es_rom: "HWEH-gehn oo-NEE-dohs" }
  ],
  "winning-and-losing": [
    { en: "Good game", ur: "اچھا کھیل", ur_rom: "Achha khel", es: "Buen juego", es_rom: "BWEHN HWEH-goh" },
    { en: "Shake hands", ur: "ہاتھ ملائیں", ur_rom: "Haath milaayein", es: "Estrecha manos", es_rom: "ehs-TREH-chah MAH-nohs" },
    { en: "Try hard", ur: "محنت کریں", ur_rom: "Mehnat karein", es: "Esfuérzate siempre", es_rom: "ehs-FWEHR-zah-teh SYEHM-preh" }
  ],
  "riding-a-bike": [
    { en: "Wear helmet", ur: "ہیلمٹ پہنیں", ur_rom: "Helmet pehnein", es: "Usa casco", es_rom: "OO-sah KAHS-koh" },
    { en: "Pedal fast", ur: "پیڈل ماریں", ur_rom: "Pedal maarein", es: "Pedalea rápido", es_rom: "peh-dah-LEH-ah RRAH-pee-doh" },
    { en: "Ring bell", ur: "گھنٹی بجائیں", ur_rom: "Ghanti bajaayein", es: "Toca timbre", es_rom: "TOH-kah TEEM-breh" }
  ],

  // 14. Clothes & Style
  "choosing-clothes": [
    { en: "Red shirt", ur: "لال قمیض", ur_rom: "Laal qameez", es: "Camisa roja", es_rom: "kah-MEE-sah RROH-hah" },
    { en: "Warm sweater", ur: "گرم سویٹر", ur_rom: "Garam sweater", es: "Suéter abrigado", es_rom: "SWEH-tehr ah-bree-GAH-doh" },
    { en: "Blue pants", ur: "نیلی پتلون", ur_rom: "Neeli patloon", es: "Pantalón azul", es_rom: "pahn-tah-LOHN ah-ZOOL" }
  ],
  "tying-shoes": [
    { en: "Tie laces", ur: "تسمے باندھیں", ur_rom: "Tasme baandhein", es: "Ata cordones", es_rom: "AH-tah kohr-DOH-nehs" },
    { en: "Tight knot", ur: "مضبوط گرہ", ur_rom: "Mazboot girah", es: "Nudo firme", es_rom: "NOO-doh FEER-meh" },
    { en: "Good shoes", ur: "اچھے جوتے", ur_rom: "Achhe joote", es: "Zapatos cómodos", es_rom: "sah-PAH-tohs KOH-moh-dohs" }
  ],
  "washing-face": [
    { en: "Clean water", ur: "صاف پانی", ur_rom: "Saaf paani", es: "Agua limpia", es_rom: "AH-gwah LEEM-pyah" },
    { en: "Soft soap", ur: "نرم صابن", ur_rom: "Narm saabun", es: "Jabón suave", es_rom: "hah-BOHN SWAH-veh" },
    { en: "Dry towel", ur: "سوکھا تولیہ", ur_rom: "Sookha tauliya", es: "Toalla seca", es_rom: "twah-YAH SEH-kah" }
  ],
  "getting-dressed": [
    { en: "Wear clothes", ur: "کپڑے پہنیں", ur_rom: "Kapre pehnein", es: "Ponte ropa", es_rom: "POHN-teh RROH-pah" },
    { en: "Button up", ur: "بٹن لگائیں", ur_rom: "Button lagaayein", es: "Abotona camisa", es_rom: "ah-boh-TOH-nah kah-MEE-sah" },
    { en: "Look neat", ur: "صاف ستھرا", ur_rom: "Saaf suthra", es: "Luce ordenado", es_rom: "LOO-seh ohr-deh-NAH-doh" }
  ],
  "shopping-for-shoes": [
    { en: "Shoe store", ur: "جوتوں دکان", ur_rom: "Jooton dukaan", es: "Zapatería local", es_rom: "sah-pah-teh-REE-ah loh-KAHL" },
    { en: "Right size", ur: "صحیح ناپ", ur_rom: "Sahi naap", es: "Talla correcta", es_rom: "TAH-yah koh-RREHK-tah" },
    { en: "Comfy sneakers", ur: "آرامدہ جوتے", ur_rom: "Aaramdeh joote", es: "Zapatillas cómodas", es_rom: "sah-pah-TEE-yahs KOH-moh-dahs" }
  ],

  // 15. Chores & Helping
  "cleaning-the-room": [
    { en: "Tidy room", ur: "کمرہ صاف", ur_rom: "Kamra saaf", es: "Ordena cuarto", es_rom: "ohr-DEH-nah KWAHR-toh" },
    { en: "Pick toys", ur: "کھلونے سمیٹیں", ur_rom: "Khilone sametein", es: "Recoge juguetes", es_rom: "rreh-KOH-heh hoo-GEH-tehs" },
    { en: "Make bed", ur: "بستر لگائیں", ur_rom: "Bistar lagaayein", es: "Tiende cama", es_rom: "TYEHN-deh KAH-mah" }
  ],
  "washing-dishes": [
    { en: "Wash cup", ur: "کپ دھوئیں", ur_rom: "Cup dho-ein", es: "Lava taza", es_rom: "LAH-vah TAH-sah" },
    { en: "Clean bowl", ur: "پیالہ صاف", ur_rom: "Pyaala saaf", es: "Limpia tazón", es_rom: "LEEM-pyah tah-SOHN" },
    { en: "Rinse plate", ur: "پلیٹ کھنگالیں", ur_rom: "Plate khangaalein", es: "Enjuaga plato", es_rom: "ehn-HWAH-gah PLAH-toh" }
  ],
  "watering-plants": [
    { en: "Water flowers", ur: "پھول سینچیں", ur_rom: "Phool seinchein", es: "Riega flores", es_rom: "RYEH-gah FLOH-rehs" },
    { en: "Green plant", ur: "ہرا پودا", ur_rom: "Hara pauda", es: "Planta verde", es_rom: "PLAHN-tah VEHR-deh" },
    { en: "Water can", ur: "پانی برتن", ur_rom: "Paani bartan", es: "Regadera agua", es_rom: "rreh-gah-DEH-rah AH-gwah" }
  ],
  "feeding-pets": [
    { en: "Feed pet", ur: "کھانا ڈالیں", ur_rom: "Khaana daalein", es: "Alimenta mascota", es_rom: "ah-lee-MEHN-tah mahs-KOH-tah" },
    { en: "Pet food", ur: "پالتو کھانا", ur_rom: "Paaltu khaana", es: "Comida mascota", es_rom: "koh-MEE-dah mahs-KOH-tah" },
    { en: "Fill bowl", ur: "پیالہ بھریں", ur_rom: "Pyaala bharein", es: "Llena plato", es_rom: "YEH-nah PLAH-toh" }
  ],
  "folding-clothes": [
    { en: "Fold shirt", ur: "قمیض موڑیں", ur_rom: "Qameez morein", es: "Dobla camisa", es_rom: "DOH-blah kah-MEE-sah" },
    { en: "Neat stack", ur: "صاف ڈھیر", ur_rom: "Saaf dhair", es: "Pila ordenada", es_rom: "PEE-lah ohr-deh-NAH-dah" },
    { en: "Put away", ur: "الماری رکھیں", ur_rom: "Almaari rakhein", es: "Guarda ropa", es_rom: "GWAHR-dah RROH-pah" }
  ]
};

console.log("Total topics defined:", Object.keys(DATA).length);
fs.writeFileSync("/tmp/two_words_base.json", JSON.stringify(DATA, null, 2));
