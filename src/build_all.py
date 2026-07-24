import argparse

import config
from downloader import CalendarDownloader
from parser import extract_cities
from ics_parser import parse_ics
from festival_builder import build_festivals
from exporter import export_json
from export_daywise import export_daywise_json
from manifest_builder import build_manifest


def main():

    # ---------------------------------
    # Command Line
    # ---------------------------------

    parser = argparse.ArgumentParser(
        description="Build calendar JSON for all cities."
    )

    parser.add_argument(
        "--year",
        type=int,
        default=config.YEAR,
        help="Calendar year"
    )

    args = parser.parse_args()

    year = args.year

    # ---------------------------------
    # Header
    # ---------------------------------

    print("=" * 50)
    print(f"Building ALL Cities ({year})")
    print("=" * 50)

    downloader = CalendarDownloader()

    # ---------------------------------
    # Download Year Index
    # ---------------------------------

    cache_file = (
        f"{config.CACHE_DIR}/ics_{year}.html"
    )

    if not downloader.download_year_index(
        year,
        cache_file
    ):
        return

    # ---------------------------------
    # Extract Cities
    # ---------------------------------

    cities = extract_cities(
        cache_file,
        year
    )

    print(f"Cities Found : {len(cities)}")
    print()

    success = 0
    failed = 0

    successful_cities = []

    # ---------------------------------
    # Build Every City
    # ---------------------------------

    for city in cities:

        print("-" * 50)
        print(city.name)

        try:

            # -------------------------
            # Download ICS
            # -------------------------

            ics_file = (
                f"{config.ICS_CACHE_DIR}/"
                f"{city.name}_{year}.ics"
            )

            downloader.download_file(
                city.ics_url,
                ics_file
            )

            # -------------------------
            # Parse ICS
            # -------------------------

            events = parse_ics(
                ics_file
            )

            # -------------------------
            # Build Festivals
            # -------------------------

            festivals = build_festivals(
                events
            )

            # -------------------------
            # Export Flat JSON
            # -------------------------

            json_file = (
                f"{config.DATA_DIR}/"
                f"{year}/"
                f"{city.name}.json"
            )

            export_json(
                festivals,
                json_file
            )

            # -------------------------
            # Export Day-wise JSON
            # -------------------------

            daywise_file = (
                f"{config.DATA_DIR}/"
                f"{year}/"
                f"{city.name}_daywise.json"
            )

            export_daywise_json(
                festivals,
                daywise_file,
                city.name,
                year
            )

            successful_cities.append(
                city.name
            )

            success += 1

        except Exception as e:

            failed += 1

            print()
            print(f"ERROR : {city.name}")
            print(e)
            print()

    # ---------------------------------
    # Build Manifest
    # ---------------------------------

    manifest_file = (
        f"{config.DATA_DIR}/manifest.json"
    )

    build_manifest(
        year,
        successful_cities,
        manifest_file
    )

    # ---------------------------------
    # Summary
    # ---------------------------------

    print()
    print("=" * 50)
    print("Completed")
    print("=" * 50)
    print(f"Successful : {success}")
    print(f"Failed     : {failed}")
    print(f"Total      : {len(cities)}")
    print("=" * 50)


if __name__ == "__main__":
    main()






























































# import requests

# import config
# from downloader import CalendarDownloader
# from parser import extract_cities
# from ics_parser import parse_ics
# from festival_builder import build_festivals
# from exporter import export_json
# from export_daywise import export_daywise_json
# from manifest_builder import build_manifest


# def main():

#     print("=" * 50)
#     print(f"Building ALL Cities ({config.YEAR})")
#     print("=" * 50)

#     downloader = CalendarDownloader()

#     # ---------------------------------
#     # Download city index page
#     # ---------------------------------

#     if not downloader.download_year_index(
#         config.YEAR,
#         f"{config.CACHE_DIR}/ics_{config.YEAR}.html"
#     ):
#         return

#     # ---------------------------------
#     # Extract cities
#     # ---------------------------------

#     cities = extract_cities(
#         f"{config.CACHE_DIR}/ics_{config.YEAR}.html",
#         config.YEAR
#     )

#     print(f"Cities Found : {len(cities)}")
#     print()

#     success = 0
#     failed = 0

#     # ---------------------------------
#     # Process every city
#     # ---------------------------------

#     for city in cities:

#         print("-" * 50)
#         print(city.name)

#         try:

#             # Download ICS

#             ics_file = (
#                 f"{config.ICS_CACHE_DIR}/"
#                 f"{city.name}_{config.YEAR}.ics"
#             )

#             downloader.download_file(
#                 city.ics_url,
#                 ics_file
#             )

#             # Parse ICS

#             events = parse_ics(ics_file)

#             # Build festivals

#             festivals = build_festivals(events)

#             # Export JSON

#             json_file = (
#                 f"{config.DATA_DIR}/"
#                 f"{config.YEAR}/"
#                 f"{city.name}.json"
#             )

#             export_json(
#                 festivals,
#                 json_file
#             )

#             daywise_file = (
#                 f"{config.DATA_DIR}/"
#                 f"{config.YEAR}/"
#                 f"{city.name}_daywise.json"
#             )

#             export_daywise_json(
#                 festivals,
#                 daywise_file
#             )

#             success += 1

#         except Exception as e:

#             failed += 1

        

#             print()
#             print(f"ERROR : {city.name}")
#             print(e)
#             print()

#     city_names = [city.name for city in cities]

#     build_manifest(
#         config.YEAR,
#         city_names,
#         f"{config.DATA_DIR}/manifest.json"
#     )



#     # ---------------------------------
#     # Summary
#     # ---------------------------------

#     print()
#     print("=" * 50)
#     print("Completed")
#     print("=" * 50)
#     print(f"Successful : {success}")
#     print(f"Failed     : {failed}")
#     print(f"Total      : {len(cities)}")
#     print("=" * 50)


# if __name__ == "__main__":
#     main()




























































# import config
# import requests

# from downloader import CalendarDownloader
# from parser import extract_cities
# from ics_parser import parse_ics
# from festival_builder import build_festivals
# from exporter import export_json


# def main():

#     print("=" * 50)
#     print(f"Building ALL Cities ({config.YEAR})")
#     print("=" * 50)

#     downloader = CalendarDownloader()

#     # Download city index
#     index_url = config.get_ics_year_url(config.YEAR)

#     downloader.download_page(
#         index_url,
#         f"{config.CACHE_DIR}/ics_{config.YEAR}.html"
#     )

#     # Get all cities
#     cities = extract_cities(
#         f"{config.CACHE_DIR}/ics_{config.YEAR}.html",
#         config.YEAR
#     )

#     print(f"Cities Found : {len(cities)}")
#     print()

#     success = 0

#     for city in cities:

#         print("-" * 50)
#         print(city.name)

#         try:

#             ics_file = (
#                 f"{config.ICS_CACHE_DIR}/"
#                 f"{city.name}_{config.YEAR}.ics"
#             )

#             downloader.download_file(
#                 city.ics_url,
#                 ics_file
#             )

            


#             events = parse_ics(ics_file)

#             festivals = build_festivals(events)

#             json_file = (
#                 f"{config.DATA_DIR}/"
#                 f"{config.YEAR}/"
#                 f"{city.name}.json"
#             )

#             export_json(
#                 festivals,
#                 json_file
#             )

#             success += 1

#         except Exception as e:

#             print(f"ERROR : {city.name}")
#             print(e)

#     print()
#     print("=" * 50)
#     print(f"Completed : {success}/{len(cities)} cities")
#     print("=" * 50)


# if __name__ == "__main__":
#     main()


























# import config

# from utils import safe_filename
# from downloader import CalendarDownloader
# from parser import extract_cities
# from ics_parser import parse_ics
# from festival_builder import build_festivals
# from exporter import export_json


# def main():

#     print("=" * 60)
#     print("Building ALL ISKCON Calendars")
#     print("=" * 60)

#     downloader = CalendarDownloader()

#     html_file = f"{config.CACHE_DIR}/ics_{config.YEAR}.html"

#     downloader.download_page(
#         config.get_ics_year_url(config.YEAR),
#         html_file
#     )

#     cities = extract_cities(
#         html_file,
#         config.YEAR
#     )

#     print(f"\nCities found : {len(cities)}\n")

#     success = 0

#     for city in cities:

#         try:

#             print(f"[{success+1}/{len(cities)}] {city.city}")

#             ics_file = (
#                 f"{config.ICS_CACHE_DIR}/"
#                 f"{safe_filename(city.city)}_{config.YEAR}.ics"
#             )

#             downloader.download_file(
#                 city.ics_url,
#                 ics_file
#             )

#             events = parse_ics(ics_file)

#             festivals = build_festivals(events)

#             json_file = (
#                 f"{config.DATA_DIR}/"
#                 f"{config.YEAR}/"
#                 f"{safe_filename(city.city)}.json"
#             )

#             export_json(
#                 festivals,
#                 json_file
#             )

#             success += 1

#         except Exception as e:

#             print("FAILED:", city.city)
#             print(e)

#     print()
#     print("=" * 60)
#     print(f"Finished : {success}/{len(cities)}")
#     print("=" * 60)


# if __name__ == "__main__":
#     main()