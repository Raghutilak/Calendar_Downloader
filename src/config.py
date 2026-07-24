# ---------------------------------------
# Calendar Downloader Configuration
# ---------------------------------------

BASE_URL = "https://www.vaisnavacalendar.info"

YEAR = 2027

CITY = "Bombay"

CACHE_DIR = "../cache"

ICS_CACHE_DIR = "../cache/ics"

DATA_DIR = "../data"

LOG_DIR = "../logs"


def get_ics_year_url(year: int) -> str:
    return (
        "https://www.vaisnavacalendar.info/"
        f"calendar-file-downloads/ics-ical-calendar-files-{year}"
    )






