from dataclasses import dataclass, field
from datetime import date
from typing import List


# ----------------------------------------
# Calendar City
# ----------------------------------------

@dataclass
class CalendarCity:
    name: str
    country: str
    year: int
    ics_url: str


# ----------------------------------------
# Festival
# ----------------------------------------

@dataclass
class Festival:

    title: str
    date: date

    category: str = "Festival"

    fasting: bool = False

    break_fast_start: str = ""
    break_fast_end: str = ""

    priority: int = 1

    reminder: bool = True

    description: str = ""


# ----------------------------------------
# Festival Day (Future Use)
# ----------------------------------------

@dataclass
class FestivalDay:

    date: date

    events: List[Festival] = field(default_factory=list)