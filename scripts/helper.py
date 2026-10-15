import json

def item(en, ur, ur_rom, hi, hi_rom, ar, ar_rom, es, es_rom, fr, fr_rom, de, de_rom, it, it_rom, pt, pt_rom, ru, ru_rom, tr, tr_rom, id_val, id_rom, zh, zh_rom, ja, ja_rom, ko, ko_rom=None):
    if ko_rom is None:
        ko_rom = ko
    return {
        "en": en,
        "ur": ur,
        "ur_rom": ur_rom,
        "es": es,
        "es_rom": es_rom,
        "target": {
            "en": en,
            "ur": ur,
            "hi": hi,
            "ar": ar,
            "es": es,
            "fr": fr,
            "de": de,
            "it": it,
            "pt": pt,
            "ru": ru,
            "tr": tr,
            "id": id_val,
            "zh": zh,
            "ja": ja,
            "ko": ko
        },
        "romanized": {
            "en": en,
            "ur": ur_rom,
            "hi": hi_rom,
            "ar": ar_rom,
            "es": es_rom,
            "fr": fr_rom,
            "de": de_rom,
            "it": it_rom,
            "pt": pt_rom,
            "ru": ru_rom,
            "tr": tr_rom,
            "id": id_rom,
            "zh": zh_rom,
            "ja": ja_rom,
            "ko": ko_rom
        }
    }

def export_ts_module(filename, w1_var, w2_var, w1_data, w2_data):
    w1_json = json.dumps(w1_data, ensure_ascii=False, indent=2)
    w2_json = json.dumps(w2_data, ensure_ascii=False, indent=2)
    
    content = f"""import {{ MultilingualTwoWordItem }} from './types';

export const {w1_var}: Record<string, [MultilingualTwoWordItem, MultilingualTwoWordItem, MultilingualTwoWordItem]> = {w1_json};

export const {w2_var}: Record<string, [MultilingualTwoWordItem, MultilingualTwoWordItem, MultilingualTwoWordItem]> = {w2_json};
"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully generated {filename}")
