import json
from pathlib import Path
from datetime import datetime

from geo_lookup import get_city_info


class ManifestBuilder:

    def __init__(self, output_folder):

        self.output_folder = Path(output_folder)

        self.manifest = {
            "version": "1.0.0",
            "generated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "latestYear": None,

            "years": [],

            "aliases": {
                "Mumbai": "Bombay",
                "Kolkata": "Calcutta",
                "Chennai": "Madras"
            },

            "cities": []
        }


    def add_year(self, year):

        if year not in self.manifest["years"]:
            self.manifest["years"].append(year)
        self.manifest["years"].sort()

        self.manifest["latestYear"] = max(self.manifest["years"])


    # def add_city(self, city, country):

    #     # Avoid duplicates
    #     for c in self.manifest["cities"]:
    #         if c["name"] == city and c["country"] == country:
    #             return

    #     info = get_city_info(city, country)

    #     self.manifest["cities"].append({
    #         "name": city,
    #         "country": country,
    #         "lat": info["lat"],
    #         "lon": info["lon"]
    #     })



    def add_city(self, city, country):

        for c in self.manifest["cities"]:

            if (
                c["name"] == city
                and
                c["country"] == country
            ):
                return

        info = get_city_info(
            city,
            country
        )

        self.manifest["cities"].append({

            "name": city,

            "country": country,

            "lat": info["lat"],

            "lon": info["lon"],

            "timezone": info["timezone"]

        })


    def save(self):

        output = self.output_folder / "manifest.json"

        with open(output, "w", encoding="utf-8") as f:
            json.dump(
                self.manifest,
                f,
                indent=2,
                ensure_ascii=False
            )

        print(f"Manifest saved : {output}")


    def add_year(self, year):

        if year not in self.manifest["years"]:
            self.manifest["years"].append(year)

        self.manifest["years"].sort()

        self.manifest["latestYear"] = max(
            self.manifest["years"]
        )


























