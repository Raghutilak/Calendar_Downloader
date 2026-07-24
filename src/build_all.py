import requests

import config
from downloader import CalendarDownloader
from parser import extract_cities
from ics_parser import parse_ics
from festival_builder import build_festivals
from exporter import export_json


def main():

    print("=" * 50)
    print(f"Building ALL Cities ({config.YEAR})")
    print("=" * 50)

    downloader = CalendarDownloader()

    # ---------------------------------
    # Download city index page
    # ---------------------------------

    # index_url = config.get_ics_year_url(config.YEAR)

    # try:

    #     downloader.download_page(
    #         index_url,
    #         f"{config.CACHE_DIR}/ics_{config.YEAR}.html"
    #     )

    # except requests.HTTPError as e:

    #     if e.response.status_code == 404:

    #         print()
    #         print("=" * 50)
    #         print(f"ERROR : Calendar for year {config.YEAR} is not available.")
    #         print("The official Vaisnava Calendar has not published this year yet.")
    #         print("=" * 50)
    #         return

    #     raise
    






    if not downloader.download_year_index(
        config.YEAR,
        f"{config.CACHE_DIR}/ics_{config.YEAR}.html"
    ):
        return

    # ---------------------------------
    # Extract cities
    # ---------------------------------

    cities = extract_cities(
        f"{config.CACHE_DIR}/ics_{config.YEAR}.html",
        config.YEAR
    )

    print(f"Cities Found : {len(cities)}")
    print()

    success = 0
    failed = 0

    # ---------------------------------
    # Process every city
    # ---------------------------------

    for city in cities:

        print("-" * 50)
        print(city.name)

        try:

            # Download ICS

            ics_file = (
                f"{config.ICS_CACHE_DIR}/"
                f"{city.name}_{config.YEAR}.ics"
            )

            downloader.download_file(
                city.ics_url,
                ics_file
            )

            # Parse ICS

            events = parse_ics(ics_file)

            # Build festivals

            festivals = build_festivals(events)

            # Export JSON

            json_file = (
                f"{config.DATA_DIR}/"
                f"{config.YEAR}/"
                f"{city.name}.json"
            )

            export_json(
                festivals,
                json_file
            )

            success += 1

        except Exception as e:

            failed += 1

            print()
            print(f"ERROR : {city.name}")
            print(e)
            print()

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