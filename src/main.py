import argparse

import config
from downloader import CalendarDownloader
from parser import extract_cities
from ics_parser import parse_ics
from festival_builder import build_festivals
from exporter import export_json


def find_city(cities, city_name):
    """Find a city by name (case-insensitive)."""

    for city in cities:
        if city.name.lower() == city_name.lower():
            return city

    return None


def main():

    # ---------------------------------
    # Command-line arguments
    # ---------------------------------

    parser = argparse.ArgumentParser(
        description="GCAL Builder"
    )

    parser.add_argument(
        "--city",
        default=config.CITY,
        help="City name"
    )

    parser.add_argument(
        "--year",
        type=int,
        default=config.YEAR,
        help="Calendar year"
    )

    args = parser.parse_args()

    city_name = args.city
    year = args.year

    # ---------------------------------
    # Header
    # ---------------------------------

    print("=" * 50)
    print("GCAL Builder")
    print("=" * 50)
    print(f"City : {city_name}")
    print(f"Year : {year}")
    print()

    downloader = CalendarDownloader()

    # ---------------------------------
    # Download year index
    # ---------------------------------

    cache_file = f"{config.CACHE_DIR}/ics_{year}.html"

    if not downloader.download_year_index(
        year,
        cache_file
    ):
        return

    # ---------------------------------
    # Extract cities
    # ---------------------------------

    cities = extract_cities(
        cache_file,
        year
    )

    print(f"Cities Found : {len(cities)}")

    # ---------------------------------
    # Find requested city
    # ---------------------------------

    selected_city = find_city(
        cities,
        city_name
    )

    if selected_city is None:

        print()
        print(f"ERROR : City '{city_name}' not found.")
        print()
        print("Available cities:\n")

        for city in cities:
            print(city.name)

        return

    print(f"Selected City : {selected_city.name}")
    print()

    # ---------------------------------
    # Download ICS
    # ---------------------------------

    ics_file = (
        f"{config.ICS_CACHE_DIR}/"
        f"{selected_city.name}_{year}.ics"
    )

    downloader.download_file(
        selected_city.ics_url,
        ics_file
    )

    # ---------------------------------
    # Parse ICS
    # ---------------------------------

    events = parse_ics(ics_file)

    print(f"Events Parsed : {len(events)}")

    # ---------------------------------
    # Build festivals
    # ---------------------------------

    festivals = build_festivals(events)

    print(f"Festivals Built : {len(festivals)}")

    # ---------------------------------
    # Export JSON
    # ---------------------------------

    json_file = (
        f"{config.DATA_DIR}/"
        f"{year}/"
        f"{selected_city.name}.json"
    )

    export_json(
        festivals,
        json_file
    )

    # ---------------------------------
    # Summary
    # ---------------------------------

    print()
    print("=" * 50)
    print("Completed Successfully")
    print("=" * 50)
    print(f"JSON : {json_file}")


if __name__ == "__main__":
    main()



































































# import sys

# import config
# import requests
# from downloader import CalendarDownloader
# from parser import extract_cities
# from ics_parser import parse_ics
# from festival_builder import build_festivals
# from exporter import export_json


# def find_city(cities, city_name):
#     """Find a city by name (case-insensitive)."""
#     for city in cities:
#         if city.name.lower() == city_name.lower():
#             return city
#     return None


# def main():

#     print("=" * 50)
#     print("GCAL Builder")
#     print("=" * 50)

#     # ---------------------------------
#     # Determine city
#     # ---------------------------------

#     city_name = config.CITY

#     if len(sys.argv) > 1:
#         city_name = " ".join(sys.argv[1:])

#     print(f"City : {city_name}")
#     print(f"Year : {config.YEAR}")
#     print()

#     downloader = CalendarDownloader()

    
#     # ---------------------------------
#     # Download ICS index page
#     # -----------------------------

#     index_url = config.get_ics_year_url(config.YEAR)

#     try:

#         downloader.download_page(
#             index_url,
#             f"{config.CACHE_DIR}/ics_{config.YEAR}.html"
#         )

#     except requests.HTTPError as e:

#         if e.response.status_code == 404:

#             print()
#             print("=" * 50)
#             print(f"ERROR : Calendar for year {config.YEAR} is not available.")
#             print("The official Vaisnava Calendar has not published this year yet.")
#             print("=" * 50)
#             return

#         raise




#     # if not downloader.download_year_index(
#     #     config.YEAR,
#     #     f"{config.CACHE_DIR}/ics_{config.YEAR}.html"
#     # ):
#     #     return






#     # ---------------------------------
#     # Extract all cities
#     # ---------------------------------

#     cities = extract_cities(
#         f"{config.CACHE_DIR}/ics_{config.YEAR}.html",
#         config.YEAR
#     )

#     print(f"Cities Found : {len(cities)}")

#     # ---------------------------------
#     # Find selected city
#     # ---------------------------------

#     selected_city = find_city(cities, city_name)

#     if selected_city is None:
#         print(f"\nERROR : City '{city_name}' not found.\n")

#         print("Available cities:\n")

#         for city in cities:
#             print(city.name)

#         return

#     print(f"Selected City : {selected_city.name}")
#     print()

#     # ---------------------------------
#     # Download city ICS
#     # ---------------------------------

#     ics_file = (
#         f"{config.ICS_CACHE_DIR}/"
#         f"{selected_city.name}_{config.YEAR}.ics"
#     )

#     # downloader.download_file(
#     #     selected_city.ics_url,
#     #     ics_file
#     # )


        

#     try:
#         downloader.download_page(
#             index_url,
#             f"{config.CACHE_DIR}/ics_{config.YEAR}.html"
#         )

#     except requests.HTTPError as e:

#         if e.response.status_code == 404:
#             print()
#             print(f"ERROR: Calendar for year {config.YEAR} is not available.")
#             print("Please choose another year.")
#             return

#         raise




#     # ---------------------------------
#     # Parse ICS
#     # ---------------------------------

#     events = parse_ics(ics_file)

#     print(f"Events Parsed : {len(events)}")

#     # ---------------------------------
#     # Build Festival objects
#     # ---------------------------------

#     festivals = build_festivals(events)

#     print(f"Festivals Built : {len(festivals)}")

    
#     # ---------------------------------
#     # Export JSON
#     # ---------------------------------

#     json_file = (
#         f"{config.DATA_DIR}/"
#         f"{config.YEAR}/"
#         f"{selected_city.name}.json"
#     )


#     export_json(
#         festivals,
#         json_file
#     )

#     print()
#     print("========================================")
#     print("Completed Successfully")
#     print("========================================")
#     print(f"JSON : {json_file}")


# if __name__ == "__main__":
#     main()






















































# import config
# from ics_parser import parse_ics
# from downloader import CalendarDownloader

# from parser import extract_cities
# from exporter import export_json


# def main():

#     downloader = CalendarDownloader()

#     url = config.get_ics_year_url(config.YEAR)

#     downloader.download_page(
#         url,
#         "../cache/ics_2027.html"
#     )

#     cities = extract_cities(
#         "../cache/ics_2027.html",
#         config.YEAR
#     )

#     bombay = next(
#         city for city in cities
#         if city.name == "Bombay"
#     )

#     print(bombay)

#     downloader.download_file(
#         bombay.ics_url,
#         "../cache/ics/Bombay_2027.ics"
#     )

#     events = parse_ics("../cache/ics/Bombay_2027.ics")

#     from festival_builder import build_festivals

#     festivals = build_festivals(events)


#     export_json(
#         festivals,
#         "../data/2027/Bombay.json"
#     )


#     print(f"\nFestivals: {len(festivals)}\n")

#     for f in festivals[:15]:
#         print(f)

#     print(f"\nEvents found: {len(events)}\n")

#     for e in events[:10]:

#         print(e)


#     print()

#     print(f"Cities found : {len(cities)}")

#     print()

#     for city in cities[:20]:

#         print(city)

       
# if __name__ == "__main__":
#     main()







