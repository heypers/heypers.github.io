from core.api import DataManager

def get_localized_string(lang, key):
    return DataManager.get_lines(lang, key)
