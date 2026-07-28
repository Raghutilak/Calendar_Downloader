
# ---------------------------------------
# Calendar Downloader Configuration
# ---------------------------------------

BASE_URL = "https://www.vaisnavacalendar.info"

YEARS = [2026, 2027]

CITY = "Bombay"

CACHE_DIR = "cache"

ICS_CACHE_DIR = "cache/ics"

DATA_DIR = "Calendar_Data"

LOG_DIR = "logs"



def get_ics_year_url(year: int) -> str:
    
    return (
        "https://www.vaisnavacalendar.info/"
        f"calendar-file-downloads/ics-ical-calendar-files-{year}"
    )


