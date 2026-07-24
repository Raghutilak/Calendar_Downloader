"""
festival_builder.py

Convert parsed ICS events into Festival objects.
"""

import re

from models import Festival


# ----------------------------------------------------
# Category
# ----------------------------------------------------

def get_category(title: str) -> str:
    """Determine the festival category."""

    t = title.lower()

    if "mahadvadasi" in t:
        return "Mahadvadasi"

    if "ekadasi" in t:
        return "Ekadasi"

    if "break fast" in t:
        return "BreakFast"
    
    if "disappearance" in t:
        return "Disappearance"

    if "appearance" in t:
        return "Appearance"

    return "Festival"







# ----------------------------------------------------
# Priority
# ----------------------------------------------------

def get_priority(category: str) -> int:
    """Assign notification/display priority."""

    priorities = {
        "Ekadasi": 5,
        "Mahadvadasi": 5,
        "Appearance": 4,
        "Disappearance": 4,
        "Festival": 3,
        "BreakFast": 2,
    }

    return priorities.get(category, 1)


# ----------------------------------------------------
# Fasting
# ----------------------------------------------------

def is_fasting(title: str) -> bool:
    """Return True if the festival involves fasting."""

    return "fasting" in title.lower()


# ----------------------------------------------------
# Break Fast
# ----------------------------------------------------

def parse_break_fast(title: str):
    """
    Extract break-fast time.

    Example:

    Break fast 07:12 (sunrise) - 10:53

    returns

    ("07:12", "10:53")
    """

    match = re.search(r"(\d{2}:\d{2}).*?(\d{2}:\d{2})", title)

    if match:
        return match.group(1), match.group(2)

    return "", ""


# ----------------------------------------------------
# Clean Title
# ----------------------------------------------------

def clean_title(title: str) -> str:
    """
    Clean unnecessary spaces.

    More rules can be added later.
    """

    return " ".join(title.split())


# ----------------------------------------------------
# Build Festival
# ----------------------------------------------------

def build_festival(event: dict) -> Festival:
    """
    Convert one parsed ICS event into a Festival object.
    """

    title = clean_title(event["summary"])

    category = get_category(title)

    festival = Festival(
        title=title,
        date=event["start"],
        category=category,
        fasting=is_fasting(title),
        priority=get_priority(category),
        reminder=True,
        description=event.get("description", "")
    )

    if category == "BreakFast":

        start, end = parse_break_fast(title)

        festival.break_fast_start = start
        festival.break_fast_end = end

        festival.title = "Break Fast"

    return festival


# ----------------------------------------------------
# Build List
# ----------------------------------------------------

def build_festivals(events):
    """
    Convert a list of parsed events into Festival objects.
    """

    festivals = []

    for event in events:
        festivals.append(build_festival(event))

    festivals.sort(
        key=lambda f: (f.date, -f.priority)
    )

    return festivals


































































# from festival import Festival


# def classify(summary):
#     s = summary.lower()

#     if "ekadasi" in s:
#         return "Ekadasi", True

#     if "mahadvadasi" in s:
#         return "Mahadvadasi", True

#     if "break fast" in s:
#         return "BreakFast", False

#     if "disappearance" in s:
#         return "Disappearance", False

#     if "appearance" in s:
#         return "Appearance", False

#     if "fasting" in s:
#         return "Fasting", True

#     return "Festival", False




# def build_festivals(events):

#     festivals = []

#     for e in events:

#         category, fasting = classify(e["summary"])

#         festivals.append(
#             Festival(
#                 date=e["start"],
#                 title=e["summary"],
#                 category=category,
#                 fasting=fasting
#             )
#         )

#     return festivals




