import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

from models import CalendarCity


def extract_cities(filename, year):

    with open(filename, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    cities = []

    pattern = re.compile(r"(.+?) \[(.+?)\]-a\d+-ICS")

    for a in soup.find_all("a", href=True):

        text = a.get_text(strip=True)

        href = a["href"]

        match = pattern.match(text)

        if not match:
            continue

        city = match.group(1)

        country = match.group(2)

        BASE = "https://www.vaisnavacalendar.info/"

        href = urljoin(BASE, href)

        cities.append(
            CalendarCity(
                city,
                country,
                year,
                href
            )
        )

    return cities
























