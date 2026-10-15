import re
import json

def fix_topic_single_word_items():
    filepath = 'src/data/multilingual/topicSingleWordItems.ts'
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Fix big-feelings item 2: Mind -> Heart
    old_big_feelings_mind = '''    {
      "en": "Mind",
      "target": {
        "en": "Mind",
        "ur": "دل",
        "hi": "मन",
        "ar": "قلب",
        "es": "Mente",
        "fr": "Esprit",
        "de": "Geist",
        "it": "Mente",
        "pt": "Mente",
        "ru": "сердце",
        "tr": "gönül",
        "id": "Hati",
        "zh": "心态",
        "ja": "心",
        "ko": "마음"
      },
      "romanized": {
        "en": "mind",
        "ur": "dil",
        "hi": "mann",
        "ar": "Qalb",
        "es": "MEHN-teh",
        "fr": "Ehs-pree",
        "de": "gyste",
        "it": "MEHN-teh",
        "pt": "MEHN-chee",
        "ru": "SYEHRD-tseh",
        "tr": "ger-newl",
        "id": "Hah-tee",
        "zh": "xīntài",
        "ja": "kokoro",
        "ko": "maeum"
      }
    }'''

    new_big_feelings_heart = '''    {
      "en": "Heart",
      "target": {
        "en": "Heart",
        "ur": "دل",
        "hi": "दिल",
        "ar": "قلب",
        "es": "Corazón",
        "fr": "Cœur",
        "de": "Herz",
        "it": "Cuore",
        "pt": "Coração",
        "ru": "Сердце",
        "tr": "Kalp",
        "id": "Hati",
        "zh": "爱心",
        "ja": "心",
        "ko": "마음"
      },
      "romanized": {
        "en": "heart",
        "ur": "dil",
        "hi": "dil",
        "ar": "Qalb",
        "es": "Koh-rah-SOHN",
        "fr": "Kuhr",
        "de": "HERTS",
        "it": "KWOH-reh",
        "pt": "Koh-rah-SOWN",
        "ru": "SYEHRD-tseh",
        "tr": "Kahlp",
        "id": "Hah-tee",
        "zh": "àixīn",
        "ja": "kokoro",
        "ko": "maeum"
      }
    }'''

    if old_big_feelings_mind in text:
        text = text.replace(old_big_feelings_mind, new_big_feelings_heart)
        print("Replaced big-feelings Mind -> Heart")
    else:
        print("Warning: old_big_feelings_mind pattern not matched directly, using regex")
        # Try regex replacement for big-feelings
        pattern = r'\{\s*"en":\s*"Mind",\s*"target":\s*\{\s*"en":\s*"Mind",\s*"ur":\s*"دل",[\s\S]*?"ko":\s*"maeum"\s*\}\s*\}'
        m = re.search(pattern, text)
        if m:
            text = text[:m.start()] + new_big_feelings_heart.strip() + text[m.end():]
            print("Regex replaced big-feelings Mind -> Heart")

    # 2. Fix lost-in-public item 3: Mind -> Help
    old_lost_in_public_mind = '''    {
      "en": "Mind",
      "target": {
        "en": "Mind",
        "ur": "دل",
        "hi": "मन",
        "ar": "قلب",
        "es": "Ánimo",
        "fr": "Cœur",
        "de": "Mut",
        "it": "Mente",
        "pt": "Mente",
        "ru": "мысли",
        "tr": "duruş",
        "id": "Kepala",
        "zh": "心神",
        "ja": "気持ち",
        "ko": "마음"
      },
      "romanized": {
        "en": "mind",
        "ur": "dil",
        "hi": "mann",
        "ar": "Qalb",
        "es": "AH-nee-moh",
        "fr": "Kuhr",
        "de": "moot",
        "it": "MEHN-teh",
        "pt": "MEHN-chee",
        "ru": "MYS-lee",
        "tr": "doo-roosh",
        "id": "Keh-pah-lah",
        "zh": "xīnshén",
        "ja": "kimochi",
        "ko": "maeum"
      }
    }'''

    new_lost_in_public_help = '''    {
      "en": "Help",
      "target": {
        "en": "Help",
        "ur": "مدد",
        "hi": "मदद",
        "ar": "مساعدة",
        "es": "Ayuda",
        "fr": "Aide",
        "de": "Hilfe",
        "it": "Aiuto",
        "pt": "Ajuda",
        "ru": "Помощь",
        "tr": "Yardım",
        "id": "Bantuan",
        "zh": "帮助",
        "ja": "たすけ",
        "ko": "도움"
      },
      "romanized": {
        "en": "help",
        "ur": "madad",
        "hi": "madad",
        "ar": "Musa'ada",
        "es": "Ah-YOO-dah",
        "fr": "Ehd",
        "de": "HIL-feh",
        "it": "Ah-YOO-toh",
        "pt": "Ah-ZHOO-dah",
        "ru": "POH-moshch",
        "tr": "Yahr-duhm",
        "id": "Bahn-too-ahn",
        "zh": "bāngzhù",
        "ja": "tasuke",
        "ko": "doum"
      }
    }'''

    if old_lost_in_public_mind in text:
        text = text.replace(old_lost_in_public_mind, new_lost_in_public_help)
        print("Replaced lost-in-public Mind -> Help")
    else:
        print("Warning: old_lost_in_public_mind pattern not matched directly, using regex")
        pattern2 = r'\{\s*"en":\s*"Mind",\s*"target":\s*\{\s*"en":\s*"Mind",\s*"ur":\s*"دل",[\s\S]*?"ja":\s*"kimochi",\s*"ko":\s*"maeum"\s*\}\s*\}'
        m2 = re.search(pattern2, text)
        if m2:
            text = text[:m2.start()] + new_lost_in_public_help.strip() + text[m2.end():]
            print("Regex replaced lost-in-public Mind -> Help")

    # 3. Fix describing-pain item 1: Tummy -> پیٹ (pet) / पेट (pet)
    old_describing_pain_tummy = '''    {
      "en": "Tummy",
      "target": {
        "en": "Tummy",
        "ur": "درد",
        "hi": "दर्द",
        "ar": "بطن",
        "es": "Pancita",
        "fr": "Ventre",
        "de": "spürbar",
        "it": "Pancino",
        "pt": "Barriguinha",
        "ru": "животик",
        "tr": "karın",
        "id": "Perut",
        "zh": "隐隐痛",
        "ja": "お腹",
        "ko": "배"
      },
      "romanized": {
        "en": "tummy",
        "ur": "dard",
        "hi": "dard",
        "ar": "Batn",
        "es": "Pahn-SEE-tah",
        "fr": "Vahnt-ruh",
        "de": "shpoor-bahr",
        "it": "Pahn-CHEE-noh",
        "pt": "Bah-hee-GEEN-yah",
        "ru": "zhy-VOH-teek",
        "tr": "kah-ruhn",
        "id": "Peh-root",
        "zh": "yǐnyǐntòng",
        "ja": "onaka",
        "ko": "bae"
      }
    }'''

    new_describing_pain_tummy = '''    {
      "en": "Tummy",
      "target": {
        "en": "Tummy",
        "ur": "پیٹ",
        "hi": "पेट",
        "ar": "بطن",
        "es": "Pancita",
        "fr": "Ventre",
        "de": "Bauch",
        "it": "Pancino",
        "pt": "Barriguinha",
        "ru": "Животик",
        "tr": "Karın",
        "id": "Perut",
        "zh": "肚子",
        "ja": "おなか",
        "ko": "배"
      },
      "romanized": {
        "en": "tummy",
        "ur": "pait",
        "hi": "pet",
        "ar": "Batn",
        "es": "Pahn-SEE-tah",
        "fr": "Vahntr",
        "de": "Bowkh",
        "it": "Pahn-CHEE-noh",
        "pt": "Bah-hee-GEEN-yah",
        "ru": "zhy-VOH-teek",
        "tr": "kah-ruhn",
        "id": "Peh-root",
        "zh": "dùzi",
        "ja": "onaka",
        "ko": "bae"
      }
    }'''

    if old_describing_pain_tummy in text:
        text = text.replace(old_describing_pain_tummy, new_describing_pain_tummy)
        print("Replaced describing-pain Tummy")
    else:
        pattern3 = r'\{\s*"en":\s*"Tummy",\s*"target":\s*\{\s*"en":\s*"Tummy",\s*"ur":\s*"درد",[\s\S]*?"ja":\s*"onaka",\s*"ko":\s*"bae"\s*\}\s*\}'
        m3 = re.search(pattern3, text)
        if m3:
            text = text[:m3.start()] + new_describing_pain_tummy.strip() + text[m3.end():]
            print("Regex replaced describing-pain Tummy")

    # 4. Fix at-the-clinic: Smile in French -> Sourire (not Courageux)
    text = re.sub(
        r'("at-the-clinic"[\s\S]*?"en":\s*"Smile"[\s\S]*?"fr":\s*)"Courageux"',
        r'\1"Sourire"',
        text
    )
    text = re.sub(
        r'("at-the-clinic"[\s\S]*?"en":\s*"Smile"[\s\S]*?"romanized":\s*\{[\s\S]*?"fr":\s*)"Koo-rah-zhuh"',
        r'\1"Soo-reer"',
        text
    )

    # 5. Fix making-friends: Friend in French -> Ami (not Nouvel)
    text = re.sub(
        r'("making-friends"[\s\S]*?"en":\s*"Friend"[\s\S]*?"fr":\s*)"Nouvel"',
        r'\1"Ami"',
        text
    )
    text = re.sub(
        r'("making-friends"[\s\S]*?"en":\s*"Friend"[\s\S]*?"romanized":\s*\{[\s\S]*?"fr":\s*)"Noo-vehl"',
        r'\1"Ah-mee"',
        text
    )

    # 6. Fix saying-sorry: Mistake in French -> Erreur (not Simple)
    text = re.sub(
        r'("saying-sorry"[\s\S]*?"en":\s*"Mistake"[\s\S]*?"fr":\s*)"Simple"',
        r'\1"Erreur"',
        text
    )
    text = re.sub(
        r'("saying-sorry"[\s\S]*?"en":\s*"Mistake"[\s\S]*?"romanized":\s*\{[\s\S]*?"fr":\s*)"San-pluh"',
        r'\1"Ehr-ruhr"',
        text
    )

    # 7. Fix shopping-for-shoes: Size in French -> Pointure (not Bonne)
    text = re.sub(
        r'("shopping-for-shoes"[\s\S]*?"en":\s*"Size"[\s\S]*?"fr":\s*)"Bonne"',
        r'\1"Pointure"',
        text
    )

    # 8. Fix video-games: Score in French -> Score (not Meilleur)
    text = re.sub(
        r'("video-games"[\s\S]*?"en":\s*"Score"[\s\S]*?"fr":\s*)"Meilleur"',
        r'\1"Score"',
        text
    )

    # 9. Fix festival-greetings: Sweets in Spanish -> Dulces (not ricos)
    text = re.sub(
        r'("festival-greetings"[\s\S]*?"en":\s*"Sweets"[\s\S]*?"es":\s*)"ricos"',
        r'\1"Dulces"',
        text
    )

    # 10. Fix festival-greetings: Hugs in Arabic -> أحضان / عناق, Hindi -> झप्पी
    text = re.sub(
        r'("festival-greetings"[\s\S]*?"en":\s*"Hugs"[\s\S]*?"ar":\s*)"تهان"',
        r'\1"أحضان"',
        text
    )
    text = re.sub(
        r'("festival-greetings"[\s\S]*?"en":\s*"Hugs"[\s\S]*?"hi":\s*)"मिलना"',
        r'\1"झप्पी"',
        text
    )

    # 11. Fix happy-new-year: Crowd in Hindi -> भीड़, Spanish -> Gente, Arabic -> حشود
    text = re.sub(
        r'("happy-new-year"[\s\S]*?"en":\s*"Crowd"[\s\S]*?"hi":\s*)"परिवार"',
        r'\1"भीड़"',
        text
    )
    text = re.sub(
        r'("happy-new-year"[\s\S]*?"en":\s*"Crowd"[\s\S]*?"es":\s*)"Familia"',
        r'\1"Gente"',
        text
    )
    text = re.sub(
        r'("happy-new-year"[\s\S]*?"en":\s*"Crowd"[\s\S]*?"ar":\s*)"جمع"',
        r'\1"حشود"',
        text
    )

    # 12. Fix winning-and-losing: Sport in Urdu -> کھیل, Hindi -> खेल, Arabic -> رياضة, Spanish -> Deporte, French -> Sport
    text = re.sub(
        r'("winning-and-losing"[\s\S]*?"en":\s*"Sport"[\s\S]*?"ur":\s*)"کھلاڑی"',
        r'\1"کھیل"',
        text
    )
    text = re.sub(
        r'("winning-and-losing"[\s\S]*?"en":\s*"Sport"[\s\S]*?"hi":\s*)"खिलाड़ी"',
        r'\1"खेल"',
        text
    )
    text = re.sub(
        r'("winning-and-losing"[\s\S]*?"en":\s*"Sport"[\s\S]*?"ar":\s*)"روح"',
        r'\1"رياضة"',
        text
    )
    text = re.sub(
        r'("winning-and-losing"[\s\S]*?"en":\s*"Sport"[\s\S]*?"es":\s*)"Deportista"',
        r'\1"Deporte"',
        text
    )
    text = re.sub(
        r'("winning-and-losing"[\s\S]*?"en":\s*"Sport"[\s\S]*?"fr":\s*)"Esprit"',
        r'\1"Sport"',
        text
    )

    # 13. Fix winning-and-losing: Handshake in Hindi -> हाथ मिलाना, Urdu -> ہاتھ ملانا
    text = re.sub(
        r'("winning-and-losing"[\s\S]*?"en":\s*"Handshake"[\s\S]*?"hi":\s*)"मिलाना"',
        r'\1"हाथ मिलाना"',
        text
    )

    # 14. Fix holiday-plans: Suitcase in Urdu -> سوٹس کیس
    text = re.sub(
        r'("holiday-plans"[\s\S]*?"en":\s*"Suitcase"[\s\S]*?"ur":\s*)"کیس"',
        r'\1"سوٹس کیس"',
        text
    )

    # 15. Fix cleaning-the-room: Basket in Russian -> Корзина, Turkish -> Sepet
    text = re.sub(
        r'("cleaning-the-room"[\s\S]*?"en":\s*"Basket"[\s\S]*?"ru":\s*)"игрушек"',
        r'\1"Корзина"',
        text
    )
    text = re.sub(
        r'("cleaning-the-room"[\s\S]*?"en":\s*"Basket"[\s\S]*?"tr":\s*)"sepeti"',
        r'\1"Sepet"',
        text
    )

    # 16. Fix washing-dishes: Bubbles in Turkish -> Köpük, Sponge in Urdu -> سپنج
    text = re.sub(
        r'("washing-dishes"[\s\S]*?"en":\s*"Bubbles"[\s\S]*?"tr":\s*)"su"',
        r'\1"Köpük"',
        text
    )
    text = re.sub(
        r'("washing-dishes"[\s\S]*?"en":\s*"Sponge"[\s\S]*?"ur":\s*)"فوم"',
        r'\1"سپنج"',
        text
    )

    # 17. Fix feeding-pets: Kibble in Urdu -> خوراک, Hindi -> खाना
    text = re.sub(
        r'("feeding-pets"[\s\S]*?"en":\s*"Kibble"[\s\S]*?"ur":\s*)"دلیہ"',
        r'\1"خوراک"',
        text
    )
    text = re.sub(
        r'("feeding-pets"[\s\S]*?"en":\s*"Kibble"[\s\S]*?"hi":\s*)"भोजन"',
        r'\1"खाना"',
        text
    )

    # 18. Fix folding-clothes: Pile in Russian -> Стопка, Turkish -> Yığın
    text = re.sub(
        r'("folding-clothes"[\s\S]*?"en":\s*"Pile"[\s\S]*?"ru":\s*)"одежды"',
        r'\1"Стопка"',
        text
    )
    text = re.sub(
        r'("folding-clothes"[\s\S]*?"en":\s*"Pile"[\s\S]*?"tr":\s*)"yığını"',
        r'\1"Yığın"',
        text
    )

    # 19. Fix phone-calls: Voice in Urdu -> آواز, Spanish -> Voz, News in Spanish -> Noticias, French -> Nouvelles
    text = re.sub(
        r'("phone-calls"[\s\S]*?"en":\s*"Voice"[\s\S]*?"ur":\s*)"انداز"',
        r'\1"آواز"',
        text
    )
    text = re.sub(
        r'("phone-calls"[\s\S]*?"en":\s*"Voice"[\s\S]*?"es":\s*)"Tono"',
        r'\1"Voz"',
        text
    )
    text = re.sub(
        r'("phone-calls"[\s\S]*?"en":\s*"News"[\s\S]*?"es":\s*)"Buenas"',
        r'\1"Noticias"',
        text
    )
    text = re.sub(
        r'("phone-calls"[\s\S]*?"en":\s*"News"[\s\S]*?"fr":\s*)"Bonne"',
        r'\1"Nouvelles"',
        text
    )

    # 20. Fix video-chats: Picture in Hindi -> तस्वीर, French -> Image
    text = re.sub(
        r'("video-chats"[\s\S]*?"en":\s*"Picture"[\s\S]*?"hi":\s*)"वीडियो"',
        r'\1"तस्वीर"',
        text
    )
    text = re.sub(
        r'("video-chats"[\s\S]*?"en":\s*"Picture"[\s\S]*?"fr":\s*)"Vidéo"',
        r'\1"Image"',
        text
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Saved updated topicSingleWordItems.ts")

if __name__ == '__main__':
    fix_topic_single_word_items()
