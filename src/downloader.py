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




































# """
# Calendar Downloader
# -------------------
# Responsible ONLY for downloading pages and files.
# No parsing logic belongs here.
# """

# import requests


# class CalendarDownloader:

#     def __init__(self):

#         self.session = requests.Session()

#         self.session.headers.update({

#             "User-Agent": "CalendarDownloader/1.0"

#         })

#         print("HTTP Session Created")

#     def test_connection(self, url):

#         print(f"Connecting to {url}")

#         response = self.session.get(url, timeout=30)

#         print("Status Code :", response.status_code)

#         return response.status_code == 200