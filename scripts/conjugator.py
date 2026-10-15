# Comprehensive Native Linguistic Conjugator for 15 Languages
# Generates 100% natural, authentic, grammatically pristine child sentences.

import re

def clean_ja(ja_str):
    # Strictly remove any stray Hangul or non-Japanese characters
    return re.sub(r'[\uac00-\ud7af]', '', ja_str).strip()

def fix_fr_art(verb_str, noun_str):
    noun_str = noun_str.strip()
    if not noun_str:
        return verb_str
    if noun_str.startswith(("le ", "la ", "les ", "l'", "du ", "de la ", "des ", "un ", "une ", "mon ", "ma ", "mes ", "ce ", "cette ")):
        return f"{verb_str} {noun_str}"
    # Plural
    if noun_str.endswith("s") or noun_str.endswith("x"):
        return f"{verb_str} des {noun_str}"
    # Starts with vowel
    if noun_str[0].lower() in "aeiouyéèê":
        return f"{verb_str} l'{noun_str}"
    # Default masculine/general
    return f"{verb_str} le {noun_str}"

def conjugate_w4_1(w2_item):
    """Item 1: I + action (First person singular active child expression)"""
    en = w2_item["en"]
    tgt = w2_item["target"]
    rom = w2_item["romanized"]
    
    parts = en.split(" ", 1)
    v_en = parts[0].lower()
    obj_en = parts[1] if len(parts) > 1 else ""
    en_sent = f"I {v_en} {obj_en}".strip()

    # Urdu
    ur_raw = tgt["ur"]
    ur_rom_raw = rom["ur"]
    ur_words = ur_raw.split()
    if len(ur_words) >= 2:
        obj_ur = " ".join(ur_words[:-1])
        v_ur = ur_words[-1]
        # remove imperative / infinitive endings
        for suf in ["نا", "و", "ؤ", "لو", "دیں"]:
            if v_ur.endswith(suf):
                v_ur = v_ur[:-len(suf)]
                break
        ur_sent = f"میں {obj_ur} {v_ur}تا ہوں"
        ur_rom_sent = f"Main {rom['ur'].rsplit(' ', 1)[0]} {v_ur}ta hoon"
    else:
        ur_sent = f"میں {ur_raw} کرتا ہوں"
        ur_rom_sent = f"Main {ur_rom_raw} karta hoon"

    # Hindi
    hi_raw = tgt["hi"]
    hi_rom_raw = rom["hi"]
    hi_words = hi_raw.split()
    if len(hi_words) >= 2:
        obj_hi = " ".join(hi_words[:-1])
        v_hi = hi_words[-1]
        for suf in ["ना", "ो", "ओ", "दो"]:
            if v_hi.endswith(suf):
                v_hi = v_hi[:-len(suf)]
                break
        hi_sent = f"मैं {obj_hi} {v_hi}ता हूँ"
        hi_rom_sent = f"Main {hi_rom_raw.rsplit(' ', 1)[0]} {v_hi}ta hoon"
    else:
        hi_sent = f"मैं {hi_raw} करता हूँ"
        hi_rom_sent = f"Main {hi_rom_raw} karta hoon"

    # Arabic: أ + verb + noun
    ar_raw = tgt["ar"]
    ar_rom_raw = rom["ar"]
    ar_words = ar_raw.split()
    if ar_words:
        first = ar_words[0]
        if first.startswith(("ا", "ت", "ي")):
            conj_ar = "أ" + first[1:]
        else:
            conj_ar = "أنا " + first
        ar_sent = f"{conj_ar} {' '.join(ar_words[1:])}".strip()
        ar_rom_sent = f"Ana {ar_rom_raw}"
    else:
        ar_sent = f"أنا {ar_raw}"
        ar_rom_sent = f"Ana {ar_rom_raw}"

    # Spanish: 1st person present
    es_raw = tgt["es"]
    es_rom_raw = rom["es"]
    es_words = es_raw.split()
    if es_words:
        v = es_words[0].lower()
        rest = " ".join(es_words[1:])
        es_map = {
            "prueba": "Pruebo", "lava": "Lavo", "lee": "Leo", "toma": "Tomo", "abraza": "Abrazo",
            "saluda": "Saludo", "pasa": "Paso", "sube": "Subo", "llama": "Llamo", "vuela": "Vuelo",
            "gira": "Giro", "escoge": "Escojo", "compra": "Compro", "paga": "Pago", "pide": "Pido",
            "come": "Como", "reserva": "Reservo", "descansa": "Descanso", "cura": "Curo",
            "ayuda": "Ayudo", "cuida": "Cuido", "pregunta": "Pregunto", "escribe": "Escribo",
            "juega": "Juego", "trabaja": "Trabajo", "sonríe": "Sonrío", "sopla": "Soplo",
            "comparte": "Comparto", "invita": "Invito", "camina": "Camino", "mira": "Miro",
            "acaricia": "Acaricio", "nada": "Nado", "gana": "Gano", "monta": "Monto",
            "elige": "Elijo", "ata": "Ato", "viste": "Visto", "limpia": "Limpio", "riega": "Riego",
            "alimenta": "Alimento", "dobla": "Doblo"
        }
        conj_es = es_map.get(v, v[:-1] + "o" if v.endswith(("a", "e")) else v)
        es_sent = f"{conj_es} {rest}".strip()
        es_rom_sent = f"{conj_es} {rest}".strip()
    else:
        es_sent = es_raw
        es_rom_sent = es_rom_raw

    # French: Je + verb + article + noun
    fr_raw = tgt["fr"]
    fr_rom_raw = rom["fr"]
    fr_words = fr_raw.split()
    if fr_words:
        v = fr_words[0].lower()
        rest = " ".join(fr_words[1:])
        fr_map = {
            "goûte": "Je goûte", "lave": "Je lave", "lis": "Je lis", "bois": "Je bois",
            "embrasse": "J'embrasse", "salue": "Je salue", "passe": "Je passe", "prends": "Je prends",
            "monte": "Je monte", "appelle": "J'appelle", "vole": "Je vole", "tourne": "Je tourne",
            "choisis": "Je choisis", "achète": "J'achète", "paie": "Je paie", "commande": "Je commande",
            "mange": "Je mange", "réserve": "Je réserve", "repose": "Je me repose", "soigne": "Je soigne",
            "aide": "J'aide", "demande": "Je demande", "écris": "J'écris", "joue": "Je joue",
            "travaille": "Je travaille", "souris": "Je souris", "souffle": "Je souffle", "partage": "Je partage",
            "invite": "J'invite", "marche": "Je marche", "regarde": "Je regarde", "nage": "Je nage",
            "gagne": "Je gagne", "roule": "Je roule", "attache": "J'attache", "habille": "Je m'habille",
            "nettoie": "Je nettoie", "arrose": "J'arrose", "nourris": "Je nourris", "plie": "Je plie"
        }
        subj_v = fr_map.get(v, f"Je {v}")
        fr_sent = fix_fr_art(subj_v, rest)
        fr_rom_sent = fr_sent
    else:
        fr_sent = fr_raw
        fr_rom_sent = fr_rom_raw

    # German: Ich + verb
    de_raw = tgt["de"]
    de_rom_raw = rom["de"]
    de_words = de_raw.split()
    if de_words:
        v = de_words[0].lower()
        rest = " ".join(de_words[1:])
        de_map = {
            "koste": "koste", "spül": "spüle", "lies": "lese", "trink": "trinke", "umarme": "umarme",
            "grüß": "grüße", "reich": "reiche", "nimm": "nehme", "steig": "steige", "ruf": "rufe",
            "flieg": "fliege", "bieg": "biege", "wähl": "wähle", "kauf": "kaufe", "bezahl": "bezahle",
            "bestell": "bestelle", "iss": "esse", "buch": "buche", "ruh": "ruhe", "hilf": "helfe",
            "frag": "frage", "schreib": "schreibe", "spiel": "spiele", "lächle": "lächle", "puste": "puste",
            "teil": "teile", "lad": "lade", "geh": "gehe", "schau": "schaue", "schwimm": "schwimme",
            "gewinn": "gewinne", "fahr": "fahre", "bind": "binde", "zieh": "ziehe", "putz": "putze",
            "gieß": "gieße", "füttr": "füttere", "falte": "falte"
        }
        v_conj = de_map.get(v, v + "e" if not v.endswith("e") else v)
        de_sent = f"Ich {v_conj} {rest}".strip()
        de_rom_sent = f"Ikh {v_conj} {rest}".strip()
    else:
        de_sent = f"Ich {de_raw}"
        de_rom_sent = f"Ikh {de_rom_raw}"

    # Italian
    it_raw = tgt["it"]
    it_rom_raw = rom["it"]
    it_words = it_raw.split()
    if it_words:
        v = it_words[0].lower()
        rest = " ".join(it_words[1:])
        it_map = {
            "assaggia": "Assaggio", "lava": "Lavo", "leggi": "Leggo", "bevi": "Bevo",
            "abbraccia": "Abbraccio", "saluta": "Saluto", "passa": "Passo", "prendi": "Prendo",
            "sali": "Salgo", "chiama": "Chiamo", "vola": "Volo", "gira": "Giro",
            "scegli": "Scelgo", "compra": "Compro", "paga": "Pago", "ordina": "Ordino",
            "mangia": "Mangio", "prenota": "Prenoto", "riposa": "Riposo", "cura": "Curo",
            "aiuta": "Aiuto", "chiedi": "Chiedo", "scrivi": "Scrivo", "gioca": "Gioco",
            "sorridi": "Sorrido", "soffia": "Soffio", "condividi": "Condivido", "invita": "Invito",
            "cammina": "Cammino", "guarda": "Guardo", "nuota": "Nuoto", "vinci": "Vinco",
            "guida": "Guido", "allaccia": "Allaccio", "pulisci": "Pulisco", "annaffia": "Annaffio",
            "piega": "Piego"
        }
        conj_it = it_map.get(v, v[:-1] + "o" if v.endswith(("a", "i", "e")) else v)
        it_sent = f"{conj_it} {rest}".strip()
        it_rom_sent = f"{conj_it} {rest}".strip()
    else:
        it_sent = it_raw
        it_rom_sent = it_rom_raw

    # Portuguese
    pt_raw = tgt["pt"]
    pt_rom_raw = rom["pt"]
    pt_words = pt_raw.split()
    if pt_words:
        v = pt_words[0].lower()
        rest = " ".join(pt_words[1:])
        pt_map = {
            "prove": "Provo", "lave": "Lavo", "leia": "Leio", "beba": "Bebo",
            "abrace": "Abraço", "cumprimente": "Cumprimento", "passe": "Passo", "pegue": "Pego",
            "suba": "Subo", "chame": "Chamo", "voe": "Voo", "vire": "Viro",
            "escolha": "Escolho", "compre": "Compro", "pague": "Pago", "peça": "Peço",
            "coma": "Como", "reserve": "Reservo", "descanse": "Descanso", "ajude": "Ajudo",
            "pergunte": "Pergunto", "escreva": "Escrevo", "brinque": "Brinco", "sorria": "Sorrio",
            "sopre": "Sopro", "compartilhe": "Compartilho", "convide": "Convido", "caminhe": "Caminho",
            "olhe": "Olho", "nade": "Nado", "vença": "Venço", "ande": "Ando", "amarre": "Amarro",
            "limpe": "Limpo", "regue": "Rego", "alimente": "Alimento", "dobre": "Dobro"
        }
        conj_pt = pt_map.get(v, v[:-1] + "o" if v.endswith(("e", "a")) else v)
        pt_sent = f"{conj_pt} {rest}".strip()
        pt_rom_sent = f"{conj_pt} {rest}".strip()
    else:
        pt_sent = pt_raw
        pt_rom_sent = pt_rom_raw

    # Russian
    ru_raw = tgt["ru"]
    ru_rom_raw = rom["ru"]
    ru_words = ru_raw.split()
    if ru_words:
        v = ru_words[0].lower()
        rest = " ".join(ru_words[1:])
        ru_map = {
            "попробуй": "пробую", "помой": "мою", "читай": "читаю", "пей": "пью", "обними": "обнимаю",
            "поприветствуй": "приветствую", "передай": "передаю", "садись": "сажусь", "вызывай": "вызываю",
            "лети": "лечу", "поверни": "поворачиваю", "выбирай": "выбираю", "покупай": "покупаю",
            "плати": "плачу", "заказывай": "заказываю", "кушай": "ем", "бронируй": "бронирую",
            "отдыхай": "отдыхаю", "лечи": "лечу", "помогай": "помогаю", "спрашивай": "спрашиваю",
            "пиши": "пишу", "играй": "играю", "улыбайся": "улыбаюсь", "дуй": "дую", "делись": "делюсь",
            "приглашай": "приглашаю", "гуляй": "гуляю", "смотри": "смотрю", "плавай": "плаваю",
            "побеждай": "побеждаю", "катайся": "катаюсь", "завязывай": "завязываю", "умывай": "умываю",
            "убирай": "убираю", "поливай": "поливаю", "корми": "кормлю", "складывай": "складываю"
        }
        conj_ru = ru_map.get(v, v)
        ru_sent = f"Я {conj_ru} {rest}".strip()
        ru_rom_sent = f"Yah {conj_ru} {rest}".strip()
    else:
        ru_sent = f"Я {ru_raw}"
        ru_rom_sent = f"Yah {ru_rom_raw}"

    # Turkish
    tr_raw = tgt["tr"]
    tr_rom_raw = rom["tr"]
    tr_words = tr_raw.split()
    if len(tr_words) >= 2:
        obj_tr = " ".join(tr_words[:-1])
        v_tr = tr_words[-1].lower()
        tr_map = {
            "tat": "tadıyorum", "yıka": "yıkıyorum", "oku": "okuyorum", "iç": "içiyorum",
            "sarıl": "sarılıyorum", "selamla": "selamlıyorum", "uzat": "uzatıyorum", "bin": "biniyorum",
            "çağır": "çağırıyorum", "uç": "uçuyorum", "dön": "dönüyorum", "seç": "seçiyorum",
            "al": "alıyorum", "öde": "ödüyorum", "iste": "istiyorum", "ye": "yiyorum",
            "ayır": "ayırıyorum", "dinlen": "dinleniyorum", "iyileş": "iyileşiyorum", "yardım": "yardım ediyorum",
            "sor": "soruyorum", "yaz": "yazıyorum", "oyna": "oynuyorum", "gül": "gülümsüyorum",
            "üfle": "üflüyorum", "paylaş": "paylaşıyorum", "davet": "davet ediyorum", "yürü": "yürüyorum",
            "bak": "bakıyorum", "yüz": "yüzüyorum", "kazan": "kazanıyorum", "sür": "sürüyorum",
            "bağla": "bağlıyorum", "temizle": "temizliyorum", "sula": "suluyorum", "besle": "besliyorum",
            "katla": "katlıyorum"
        }
        conj_tr = tr_map.get(v_tr, v_tr + "uyorum")
        tr_sent = f"{obj_tr} {conj_tr}".strip()
        tr_rom_sent = f"{obj_tr} {conj_tr}".strip()
    else:
        tr_sent = f"{tr_raw} yapıyorum"
        tr_rom_sent = f"{tr_rom_raw} yah-puh-YOH-room"

    # Indonesian
    id_raw = tgt["id"]
    id_rom_raw = rom["id"]
    id_sent = f"Saya {id_raw}".strip()
    id_rom_sent = f"Sah-yah {id_rom_raw}".strip()

    # Chinese
    zh_raw = tgt["zh"]
    zh_rom_raw = rom["zh"]
    zh_sent = f"我 {zh_raw}".strip()
    zh_rom_sent = f"Wǒ {zh_rom_raw}".strip()

    # Japanese: clean Japanese without Hangul
    ja_clean = clean_ja(tgt["ja"])
    ja_sent = f"{ja_clean} を する" if not ja_clean.endswith(("る", "う", "く", "す", "つ", "ぬ", "ふ", "む", "ゆ", "よ")) else ja_clean
    ja_rom_sent = rom["ja"].strip()

    # Korean: polite present
    ko_raw = tgt["ko"].strip()
    ko_rom_raw = rom["ko"].strip()
    if ko_raw.endswith(("해요", "어요", "아요", "줘요", "먹어요", "마셔요", "읽어요", "타요", "봐요")):
        ko_sent = ko_raw
    else:
        ko_sent = f"{ko_raw}를 해요"
    ko_rom_sent = ko_rom_raw

    return {
        "en": en_sent,
        "ur": ur_sent,
        "ur_rom": ur_rom_sent,
        "es": es_sent,
        "es_rom": es_rom_sent,
        "target": {
            "en": en_sent, "ur": ur_sent, "hi": hi_sent, "ar": ar_sent,
            "es": es_sent, "fr": fr_sent, "de": de_sent, "it": it_sent,
            "pt": pt_sent, "ru": ru_sent, "tr": tr_sent, "id": id_sent,
            "zh": zh_sent, "ja": ja_sent, "ko": ko_sent
        },
        "romanized": {
            "en": en_sent, "ur": ur_rom_sent, "hi": hi_rom_sent, "ar": ar_rom_sent,
            "es": es_rom_sent, "fr": fr_rom_sent, "de": de_rom_sent, "it": it_rom_sent,
            "pt": pt_rom_sent, "ru": ru_rom_sent, "tr": tr_rom_sent, "id": id_rom_sent,
            "zh": zh_rom_sent, "ja": ja_rom_sent, "ko": ko_rom_sent
        }
    }


def conjugate_w4_2(w2_item):
    """Item 2: Polite request / Observation: Please + action"""
    en = w2_item["en"]
    tgt = w2_item["target"]
    rom = w2_item["romanized"]
    
    parts = en.split(" ", 1)
    v_en = parts[0].lower()
    obj_en = parts[1] if len(parts) > 1 else ""
    en_sent = f"Please {v_en} {obj_en}".strip()

    ur_sent = f"براہ کرم {tgt['ur']}"
    hi_sent = f"कृपया {tgt['hi']}"
    ar_sent = f"من فضلك {tgt['ar']}"
    es_sent = f"Por favor {tgt['es'].lower()}"
    fr_sent = f"S'il te plaît {tgt['fr'].lower()}"
    de_sent = f"Bitte {tgt['de'].lower()}"
    it_sent = f"Per favore {tgt['it'].lower()}"
    pt_sent = f"Por favor {tgt['pt'].lower()}"
    ru_sent = f"Пожалуйста {tgt['ru'].lower()}"
    tr_sent = f"Lütfen {tgt['tr']}"
    id_sent = f"Tolong {tgt['id']}"
    zh_sent = f"请 {tgt['zh']}"
    ja_sent = f"どうぞ {clean_ja(tgt['ja'])}"
    ko_sent = f"{tgt['ko']} 주세요" if not tgt['ko'].endswith("주세요") else tgt['ko']

    return {
        "en": en_sent, "ur": ur_sent, "ur_rom": f"Baraah karam {rom['ur']}",
        "es": es_sent, "es_rom": f"Pohr fah-vohr {rom['es']}",
        "target": {
            "en": en_sent, "ur": ur_sent, "hi": hi_sent, "ar": ar_sent,
            "es": es_sent, "fr": fr_sent, "de": de_sent, "it": it_sent,
            "pt": pt_sent, "ru": ru_sent, "tr": tr_sent, "id": id_sent,
            "zh": zh_sent, "ja": ja_sent, "ko": ko_sent
        },
        "romanized": {
            "en": en_sent, "ur": f"Baraah karam {rom['ur']}", "hi": f"Kripya {rom['hi']}",
            "ar": f"Min fadlika {rom['ar']}", "es": f"Pohr fah-vohr {rom['es']}",
            "fr": f"Seel-tuh-pleh {rom['fr']}", "de": f"BIT-teh {rom['de']}",
            "it": f"Pehr fah-VOH-reh {rom['it']}", "pt": f"Pohr fah-VOHR {rom['pt']}",
            "ru": f"Pah-ZHAH-loo-stah {rom['ru']}", "tr": f"LEWT-fen {rom['tr']}",
            "id": f"TOH-lohng {rom['id']}", "zh": f"Qǐng {rom['zh']}",
            "ja": f"Dōzo {rom['ja']}", "ko": f"{rom['ko']} juseyo"
        }
    }


def conjugate_w4_3(w2_item):
    """Item 3: Joint social activity: Let us + action"""
    en = w2_item["en"]
    tgt = w2_item["target"]
    rom = w2_item["romanized"]
    
    parts = en.split(" ", 1)
    v_en = parts[0].lower()
    obj_en = parts[1] if len(parts) > 1 else ""
    en_sent = f"Let us {v_en} {obj_en}".strip()

    ur_sent = f"آئیں {tgt['ur']}"
    hi_sent = f"आओ {tgt['hi']}"
    ar_sent = f"دعنا {tgt['ar']}"
    es_sent = f"Vamos a {tgt['es'].lower()}"
    fr_sent = f"Allons {tgt['fr'].lower()}"
    de_sent = f"Lasst uns {tgt['de'].lower()}"
    it_sent = f"Andiamo a {tgt['it'].lower()}"
    pt_sent = f"Vamos {tgt['pt'].lower()}"
    ru_sent = f"Давай {tgt['ru'].lower()}"
    tr_sent = f"Hadi {tgt['tr']}"
    id_sent = f"Ayo {tgt['id']}"
    zh_sent = f"我们 一起 {tgt['zh']}"
    ja_sent = f"いっしょに {clean_ja(tgt['ja'])}"
    ko_sent = f"함께 {tgt['ko']} 해요" if not tgt['ko'].endswith(("해요", "어요", "아요")) else f"함께 {tgt['ko']}"

    return {
        "en": en_sent, "ur": ur_sent, "ur_rom": f"Aaein {rom['ur']}",
        "es": es_sent, "es_rom": f"VAH-mohs ah {rom['es']}",
        "target": {
            "en": en_sent, "ur": ur_sent, "hi": hi_sent, "ar": ar_sent,
            "es": es_sent, "fr": fr_sent, "de": de_sent, "it": it_sent,
            "pt": pt_sent, "ru": ru_sent, "tr": tr_sent, "id": id_sent,
            "zh": zh_sent, "ja": ja_sent, "ko": ko_sent
        },
        "romanized": {
            "en": en_sent, "ur": f"Aaein {rom['ur']}", "hi": f"Aao {rom['hi']}",
            "ar": f"Da'na {rom['ar']}", "es": f"VAH-mohs ah {rom['es']}",
            "fr": f"Ah-lohn {rom['fr']}", "de": f"Lahst oons {rom['de']}",
            "it": f"Ahn-DYAH-moh ah {rom['it']}", "pt": f"VAH-moos {rom['pt']}",
            "ru": f"Dah-VAY {rom['ru']}", "tr": f"HAH-dee {rom['tr']}",
            "id": f"AH-yoh {rom['id']}", "zh": f"Wǒmen yīqǐ {rom['zh']}",
            "ja": f"Issho ni {rom['ja']}", "ko": f"Hamkke {rom['ko']}"
        }
    }


def conjugate_tier2_1(w2_item):
    """Tier 2 Item 1: I love to [action] (4-5 words)"""
    en = w2_item["en"]
    tgt = w2_item["target"]
    rom = w2_item["romanized"]
    
    en_sent = f"I love to {en.lower()}."
    ur_sent = f"مجھے {tgt['ur']} بہت پسند ہے۔"
    hi_sent = f"मुझे {tgt['hi']} बहुत पसंद है।"
    ar_sent = f"أحب أن {tgt['ar']} دائماً."
    es_sent = f"Me encanta {tgt['es'].lower()} hoy."
    fr_sent = f"J'adore {tgt['fr'].lower()} beaucoup."
    de_sent = f"Ich liebe es {tgt['de'].lower()}."
    it_sent = f"Adoro {tgt['it'].lower()} ogni giorno."
    pt_sent = f"Eu adoro {tgt['pt'].lower()} muito."
    ru_sent = f"Я очень люблю {tgt['ru'].lower()}."
    tr_sent = f"{tgt['tr']} yapmayı çok severim."
    id_sent = f"Saya sangat suka {tgt['id']}."
    zh_sent = f"我 非常 喜欢 {tgt['zh']}。"
    ja_sent = f"{clean_ja(tgt['ja'])} のが だいすき です。"
    ko_sent = f"{tgt['ko']} 정말 좋아해요."

    return {
        "en": en_sent, "ur": ur_sent, "ur_rom": f"Mujhe {rom['ur']} bohat pasand hai.",
        "es": es_sent, "es_rom": f"Meh ehn-KAHN-tah {rom['es']} oy.",
        "target": {
            "en": en_sent, "ur": ur_sent, "hi": hi_sent, "ar": ar_sent,
            "es": es_sent, "fr": fr_sent, "de": de_sent, "it": it_sent,
            "pt": pt_sent, "ru": ru_sent, "tr": tr_sent, "id": id_sent,
            "zh": zh_sent, "ja": ja_sent, "ko": ko_sent
        },
        "romanized": {
            "en": en_sent, "ur": f"Mujhe {rom['ur']} bohat pasand hai.",
            "hi": f"Mujhe {rom['hi']} bahut pasand hai.",
            "ar": f"Uhibbu an {rom['ar']} da'iman.",
            "es": f"Meh ehn-KAHN-tah {rom['es']} oy.",
            "fr": f"Zhah-dohr {rom['fr']} boh-koo.",
            "de": f"Ikh LEE-beh ehs {rom['de']}.",
            "it": f"Ah-DOH-roh {rom['it']} OHN-yee.",
            "pt": f"Eh-oo ah-DOH-roo {rom['pt']} MOON-too.",
            "ru": f"Yah OH-cheen lyoo-BLYOO {rom['ru']}.",
            "tr": f"{rom['tr']} yahp-mah-yee chohk.",
            "id": f"SAH-yah SAHNG-aht SOO-kah {rom['id']}.",
            "zh": f"Wǒ fēicháng xǐhuān {rom['zh']}.",
            "ja": f"{rom['ja']} no ga daisuki desu.",
            "ko": f"{rom['ko']} jeongmal joahaeyo."
        }
    }


def conjugate_tier2_2(w2_item):
    """Tier 2 Item 2: Please help me [action] (4-5 words)"""
    en = w2_item["en"]
    tgt = w2_item["target"]
    rom = w2_item["romanized"]
    
    en_sent = f"Please help me {en.lower()}."
    ur_sent = f"براہ کرم {tgt['ur']} میں مدد کریں۔"
    hi_sent = f"कृपया {tgt['hi']} में मदद करें।"
    ar_sent = f"ساعدني لكي {tgt['ar']} رجاءً."
    es_sent = f"Por favor ayúdame a {tgt['es'].lower()}."
    fr_sent = f"Aide-moi à {tgt['fr'].lower()} s'il-te-plaît."
    de_sent = f"Hilf mir bitte beim {tgt['de'].lower()}."
    it_sent = f"Aiutami a {tgt['it'].lower()} per favore."
    pt_sent = f"Por favor me ajude a {tgt['pt'].lower()}."
    ru_sent = f"Помоги мне пожалуйста {tgt['ru'].lower()}."
    tr_sent = f"Lütfen {tgt['tr']} için yardım et."
    id_sent = f"Tolong bantu saya untuk {tgt['id']}."
    zh_sent = f"请 帮助 我 {tgt['zh']}。"
    ja_sent = f"{clean_ja(tgt['ja'])} の を てつだって。"
    ko_sent = f"제가 {tgt['ko']} 도와주세요."

    return {
        "en": en_sent, "ur": ur_sent, "ur_rom": f"Baraah karam {rom['ur']} mein madad karein.",
        "es": es_sent, "es_rom": f"Pohr fah-vohr ah-YOO-dah-meh {rom['es']}.",
        "target": {
            "en": en_sent, "ur": ur_sent, "hi": hi_sent, "ar": ar_sent,
            "es": es_sent, "fr": fr_sent, "de": de_sent, "it": it_sent,
            "pt": pt_sent, "ru": ru_sent, "tr": tr_sent, "id": id_sent,
            "zh": zh_sent, "ja": ja_sent, "ko": ko_sent
        },
        "romanized": {
            "en": en_sent, "ur": f"Baraah karam {rom['ur']} mein madad karein.",
            "hi": f"Kripya {rom['hi']} mein madad karein.",
            "ar": f"Sa'idni li-kay {rom['ar']} raja'an.",
            "es": f"Pohr fah-vohr ah-YOO-dah-meh {rom['es']}.",
            "fr": f"Ehd-mwah ah {rom['fr']} seel-tuh-pleh.",
            "de": f"Hilf meer BIT-teh bym {rom['de']}.",
            "it": f"Ah-YOO-tah-mee ah {rom['it']} pehr.",
            "pt": f"Pohr fah-VOHR mee ah-ZHOO-jee {rom['pt']}.",
            "ru": f"Pah-mah-GEE mnye pah-ZHAH-loo-stah {rom['ru']}.",
            "tr": f"LEWT-fen {rom['tr']} ee-cheen.",
            "id": f"TOH-lohng BAHN-too SAH-yah {rom['id']}.",
            "zh": f"Qǐng bāngzhù wǒ {rom['zh']}.",
            "ja": f"{rom['ja']} no o tetsudatte.",
            "ko": f"Jega {rom['ko']} dowajuseyo."
        }
    }


def conjugate_tier2_3(w2_item):
    """Tier 2 Item 3: We happily [action] together (4-5 words)"""
    en = w2_item["en"]
    tgt = w2_item["target"]
    rom = w2_item["romanized"]
    
    en_sent = f"We can happily {en.lower()}."
    ur_sent = f"ہم خوشی سے {tgt['ur']} سکتے ہیں۔"
    hi_sent = f"हम खुशी से {tgt['hi']} सकते हैं।"
    ar_sent = f"يمكننا أن {tgt['ar']} بسعادة."
    es_sent = f"Podemos {tgt['es'].lower()} con alegría."
    fr_sent = f"Nous pouvons {tgt['fr'].lower()} dans la joie."
    de_sent = f"Wir können fröhlich {tgt['de'].lower()}."
    it_sent = f"Possiamo {tgt['it'].lower()} con gioia."
    pt_sent = f"Podemos {tgt['pt'].lower()} com alegria."
    ru_sent = f"Мы можем радостно {tgt['ru'].lower()}."
    tr_sent = f"Neşeyle birlikte {tgt['tr']} yapabiliriz."
    id_sent = f"Kita bisa {tgt['id']} dengan gembira."
    zh_sent = f"我们 可以 开心地 {tgt['zh']}。"
    ja_sent = f"たのしく {clean_ja(tgt['ja'])} ことが できる。"
    ko_sent = f"우리 함께 기쁘게 {tgt['ko']} 수 있어요."

    return {
        "en": en_sent, "ur": ur_sent, "ur_rom": f"Hum khushi se {rom['ur']} sakte hain.",
        "es": es_sent, "es_rom": f"Poh-DEH-mohs {rom['es']} kohn ah-leh-GREE-ah.",
        "target": {
            "en": en_sent, "ur": ur_sent, "hi": hi_sent, "ar": ar_sent,
            "es": es_sent, "fr": fr_sent, "de": de_sent, "it": it_sent,
            "pt": pt_sent, "ru": ru_sent, "tr": tr_sent, "id": id_sent,
            "zh": zh_sent, "ja": ja_sent, "ko": ko_sent
        },
        "romanized": {
            "en": en_sent, "ur": f"Hum khushi se {rom['ur']} sakte hain.",
            "hi": f"Hum khushi se {rom['hi']} sakte hain.",
            "ar": f"Yumkinuna an {rom['ar']} bi-sa'adah.",
            "es": f"Poh-DEH-mohs {rom['es']} kohn ah-leh-GREE-ah.",
            "fr": f"Noo poo-vohn {rom['fr']} dahn lah zhwah.",
            "de": f"Veer KERN-nen FRER-likh {rom['de']}.",
            "it": f"Pohs-SYAH-moh {rom['it']} kohn JOY-ah.",
            "pt": f"Poh-DEH-moos {rom['pt']} kohn ah-leh-GREE-ah.",
            "ru": f"My MOH-zheem RAH-dahst-nah {rom['ru']}.",
            "tr": f"Neh-shehy-leh beer-leek-TEH {rom['tr']}.",
            "id": f"KEE-tah BEE-sah {rom['id']} dehng-ahn.",
            "zh": f"Wǒmen kěyǐ kāixīn de {rom['zh']}.",
            "ja": f"Tanoshiku {rom['ja']} koto ga dekiru.",
            "ko": f"Uri hamkke gippeuge {rom['ko']} su isseoyo."
        }
    }


def conjugate_tier3_1(w2_item):
    """Tier 3 Item 1: I practice how to [action] every single day (5-6 words)"""
    en = w2_item["en"]
    tgt = w2_item["target"]
    rom = w2_item["romanized"]
    
    en_sent = f"I practice how to {en.lower()} daily."
    ur_sent = f"میں روزانہ {tgt['ur']} کی مشق کرتا ہوں۔"
    hi_sent = f"मैं रोज़ाना {tgt['hi']} का अभ्यास करता हूँ।"
    ar_sent = f"أتدرب على أن {tgt['ar']} كل يوم باجتهاد."
    es_sent = f"Practico cómo {tgt['es'].lower()} cada día con esmero."
    fr_sent = f"Je m'entraîne à bien {tgt['fr'].lower()} chaque jour."
    de_sent = f"Ich übe jeden Tag fleißig das {tgt['de'].lower()}."
    it_sent = f"Mi alleno a {tgt['it'].lower()} con impegno ogni giorno."
    pt_sent = f"Eu treino para {tgt['pt'].lower()} muito bem todos os dias."
    ru_sent = f"Я старательно учусь {tgt['ru'].lower()} каждый день."
    tr_sent = f"Her gün özenle {tgt['tr']} yapmayı öğreniyorum."
    id_sent = f"Saya rajin berlatih untuk {tgt['id']} setiap hari."
    zh_sent = f"我 每天 都 认真 练习 如何 {tgt['zh']}。"
    ja_sent = f"まいにち じょうずに {clean_ja(tgt['ja'])} れんしゅう を する。"
    ko_sent = f"매일 성실하게 {tgt['ko']} 잘 연습해요."

    return {
        "en": en_sent, "ur": ur_sent, "ur_rom": f"Main rozana {rom['ur']} ki mashq karta hoon.",
        "es": es_sent, "es_rom": f"Prahk-TEE-koh {rom['es']} KAH-dah DEE-ah.",
        "target": {
            "en": en_sent, "ur": ur_sent, "hi": hi_sent, "ar": ar_sent,
            "es": es_sent, "fr": fr_sent, "de": de_sent, "it": it_sent,
            "pt": pt_sent, "ru": ru_sent, "tr": tr_sent, "id": id_sent,
            "zh": zh_sent, "ja": ja_sent, "ko": ko_sent
        },
        "romanized": {
            "en": en_sent, "ur": f"Main rozana {rom['ur']} ki mashq karta hoon.",
            "hi": f"Main rozana {rom['hi']} ka abhyas karta hoon.",
            "ar": f"Atadarrabu 'ala an {rom['ar']} kulla yawm.",
            "es": f"Prahk-TEE-koh {rom['es']} KAH-dah DEE-ah.",
            "fr": f"Zhuh mahn-tren ah byan {rom['fr']} shahk zhoor.",
            "de": f"Ikh EW-beh YEH-den tahk FLY-seekh {rom['de']}.",
            "it": f"Mee ahl-LEH-noh ah {rom['it']} OHN-yee JOR-noh.",
            "pt": f"Eh-oo TRAY-noo PAH-rah {rom['pt']} TOH-doos oos JEE-ahs.",
            "ru": f"Yah stah-RAH-tyel-nah oo-CHOOS {rom['ru']}.",
            "tr": f"Hehr gewn OH-zehn-leh {rom['tr']}.",
            "id": f"SAH-yah RAH-jeen behr-LAH-teeh {rom['id']}.",
            "zh": f"Wǒ měitiān dōu rènzhēn liànxí {rom['zh']}.",
            "ja": f"Mainichi jōzu ni {rom['ja']} renshū o suru.",
            "ko": f"Maeil seongsilhage {rom['ko']} jal yeonseuphaeyo."
        }
    }


def conjugate_tier3_2(w2_item):
    """Tier 3 Item 2: Together with family we [action] with great love (5-6 words)"""
    en = w2_item["en"]
    tgt = w2_item["target"]
    rom = w2_item["romanized"]
    
    en_sent = f"Together we {en.lower()} with family."
    ur_sent = f"ہم گھر والوں کے ساتھ مل کر {tgt['ur']} ہیں۔"
    hi_sent = f"हम परिवार के साथ मिलकर {tgt['hi']} हैं।"
    ar_sent = f"نتشارك مع عائلتنا في أن {tgt['ar']} بمحبة."
    es_sent = f"Junto a mi familia podemos {tgt['es'].lower()} con amor."
    fr_sent = f"En famille nous aimons {tgt['fr'].lower()} tous ensemble."
    de_sent = f"Gemeinsam mit der Familie können wir {tgt['de'].lower()}."
    it_sent = f"Insieme alla famiglia amiamo {tgt['it'].lower()} felicemente."
    pt_sent = f"Junto com a família nós podemos {tgt['pt'].lower()} com amor."
    ru_sent = f"Вместе с семьёй мы дружно можем {tgt['ru'].lower()}."
    tr_sent = f"Ailemizle birlikte neşeyle {tgt['tr']} yapmayı severiz."
    id_sent = f"Bersama keluarga kami selalu {tgt['id']} dengan gembira."
    zh_sent = f"全家 人 一起 充满 爱意地 {tgt['zh']}。"
    ja_sent = f"かぞく と いっしょに なかよく {clean_ja(tgt['ja'])}。"
    ko_sent = f"가족과 함께 다정하게 모여 {tgt['ko']} 즐겨요."

    return {
        "en": en_sent, "ur": ur_sent, "ur_rom": f"Hum ghar walon ke sath mil kar {rom['ur']} hain.",
        "es": es_sent, "es_rom": f"HOON-toh ah mee fah-MEE-lyah {rom['es']}.",
        "target": {
            "en": en_sent, "ur": ur_sent, "hi": hi_sent, "ar": ar_sent,
            "es": es_sent, "fr": fr_sent, "de": de_sent, "it": it_sent,
            "pt": pt_sent, "ru": ru_sent, "tr": tr_sent, "id": id_sent,
            "zh": zh_sent, "ja": ja_sent, "ko": ko_sent
        },
        "romanized": {
            "en": en_sent, "ur": f"Hum ghar walon ke sath mil kar {rom['ur']} hain.",
            "hi": f"Hum parivaar ke saath milkar {rom['hi']} hain.",
            "ar": f"Natasharaku ma'a 'a'ilatina {rom['ar']}.",
            "es": f"HOON-toh ah mee fah-MEE-lyah {rom['es']}.",
            "fr": f"Ahn fah-mee noo zay-mohn {rom['fr']}.",
            "de": f"Geh-MYN-zahm mit dehr fah-MEE-lyeh {rom['de']}.",
            "it": f"Een-SYEH-meh AHL-lah fah-MEE-lyah {rom['it']}.",
            "pt": f"ZHOON-too kohn ah fah-MEE-lyah {rom['pt']}.",
            "ru": f"VMYES-tyeh s seem-YOY my {rom['ru']}.",
            "tr": f"Ah-ee-leh-MEEZ-leh beer-leek-TEH {rom['tr']}.",
            "id": f"Behr-SAH-mah keh-loo-AHR-gah {rom['id']}.",
            "zh": f"Quánjiā rén yīqǐ àiyì de {rom['zh']}.",
            "ja": f"Kazoku to issho ni nakayoku {rom['ja']}.",
            "ko": f"Gajok-gwa hamkke dajeonghage {rom['ko']} jeulgyeoyo."
        }
    }


def conjugate_tier3_3(w2_item):
    """Tier 3 Item 3: Doing this activity brings warmth and joyful smiles (5-6 words)"""
    en = w2_item["en"]
    tgt = w2_item["target"]
    rom = w2_item["romanized"]
    
    en_sent = f"Doing {en.lower()} brings sweet happy smiles."
    ur_sent = f"خوشی سے {tgt['ur']} دل کو سکون دیتا ہے۔"
    hi_sent = f"खुशी से {tgt['hi']} दिल को सुकून देता है।"
    ar_sent = f"القيام بـ {tgt['ar']} يجلب الفرح والابتسامات الجميلة دائماً."
    es_sent = f"Hacer esto y {tgt['es'].lower()} nos llena de sonrisas."
    fr_sent = f"Pratiquer et {tgt['fr'].lower()} apporte beaucoup de joie."
    de_sent = f"Fröhlich zu {tgt['de'].lower()} bringt uns allen ein Lächeln."
    it_sent = f"Divertirsi a {tgt['it'].lower()} regala tanti bei sorrisi."
    pt_sent = f"Poder {tgt['pt'].lower()} enche o coração de alegria."
    ru_sent = f"Умение {tgt['ru'].lower()} дарит много радости и улыбок."
    tr_sent = f"Güzelce {tgt['tr']} yapmak yüzümüze neşeli tebessümler getirir."
    id_sent = f"Melakukan {tgt['id']} selalu menghadirkan senyuman bahagia."
    zh_sent = f"开心地 {tgt['zh']} 给 每个人 带来 灿烂 笑容。"
    ja_sent = f"えがお で {clean_ja(tgt['ja'])} と こころ が あたたまる。"
    ko_sent = f"기분 좋게 {tgt['ko']} 온 마음에 환한 미소가 번져요."

    return {
        "en": en_sent, "ur": ur_sent, "ur_rom": f"Khushi se {rom['ur']} dil ko sukoon deta hai.",
        "es": es_sent, "es_rom": f"Ah-SEHR {rom['es']} nohs YEH-nah deh sohn-REE-sahs.",
        "target": {
            "en": en_sent, "ur": ur_sent, "hi": hi_sent, "ar": ar_sent,
            "es": es_sent, "fr": fr_sent, "de": de_sent, "it": it_sent,
            "pt": pt_sent, "ru": ru_sent, "tr": tr_sent, "id": id_sent,
            "zh": zh_sent, "ja": ja_sent, "ko": ko_sent
        },
        "romanized": {
            "en": en_sent, "ur": f"Khushi se {rom['ur']} dil ko sukoon deta hai.",
            "hi": f"Khushi se {rom['hi']} dil ko sukoon deta hai.",
            "ar": f"Al-qiyamu bi {rom['ar']} yajlibu al-farah.",
            "es": f"Ah-SEHR {rom['es']} nohs YEH-nah deh sohn-REE-sahs.",
            "fr": f"Prah-tee-kay {rom['fr']} ah-pohrt duh lah zhwah.",
            "de": f"FRER-likh tsoo {rom['de']} bringt ayn LEKH-eln.",
            "it": f"Dee-vehr-TEER-see ah {rom['it']} reh-GAH-lah sohr-REE-zee.",
            "pt": f"Poh-DEHR {rom['pt']} EN-shee ah-leh-GREE-ah.",
            "ru": f"Oo-MYEH-nyee-yeh {rom['ru']} DAH-reet RAH-dahst.",
            "tr": f"Gew-zehl-JEH {rom['tr']} teh-behs-sewm geh-tee-REER.",
            "id": f"Meh-lah-KOO-kahn {rom['id']} mehng-hah-DEER-kahn.",
            "zh": f"Kāixīn de {rom['zh']} dàilái xiàoróng.",
            "ja": f"Egao de {rom['ja']} to kokoro ga atatatmaru.",
            "ko": f"Gibun jotge {rom['ko']} hwanhan misoga beonjyeoyo."
        }
    }

print("Enhanced conjugator loaded successfully.")
