"""
Calendar Downloader
"""

from pathlib import Path
import requests


class CalendarDownloader:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent": "CalendarDownloader/1.0"
        })

        print("HTTP Session Created")

    def test_connection(self, url):

        print(f"Connecting to {url}")

        response = self.session.get(url, timeout=30)

        print("Status Code :", response.status_code)

        return response.status_code == 200

    def download_page(self, url, filename):

        print(f"Downloading: {url}")

        response = self.session.get(url, timeout=30)

        response.raise_for_status()

        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Saved: {filename}")


    def download_file(self, url, filename):

        print(f"Downloading file:\n{url}")

        response = self.session.get(url, timeout=60)
        response.raise_for_status()

        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        with open(filename, "wb") as f:
            f.write(response.content)

        print(f"Saved: {filename}")


    def download_year_index(self, year, cache_file):
        """
        Download the ICS index page for the specified year.
        Returns True if successful, otherwise False.
        """

        url = f"https://www.vaisnavacalendar.info/calendar-file-downloads/ics-ical-calendar-files-{year}"

        try:

            self.download_page(
                url,
                cache_file
            )

            return True

        except requests.HTTPError as e:

            if e.response.status_code == 404:

                print()
                print("=" * 50)
                print(f"ERROR : Calendar for year {year} is not available.")
                print("The official Vaisnava Calendar has not published this year yet.")
                print("=" * 50)

                return False

            raise


































