import re

def get_category(title):

    t = title.lower()

    if "ekadasi" in t:
        return "Ekadasi"

    if "mahadvadasi" in t:
        return "Mahadvadasi"

    if "appearance" in t:
        return "Appearance"

    if "disappearance" in t:
        return "Disappearance"

    if "break fast" in t:
        return "BreakFast"

    return "Festival"


