import argparse

import config
from downloader import CalendarDownloader
from parser import extract_cities
from ics_parser import parse_ics
from festival_builder import build_festivals
from export_daywise import export_daywise_json
from manifest_builder import ManifestBuilder


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
        help="Default city (display only)"
    )

    args = parser.parse_args()

    city_name = args.city

    # ---------------------------------
    # Initialize
    # ---------------------------------

    downloader = CalendarDownloader()

    manifest = ManifestBuilder(
        config.DATA_DIR
    )

    # ---------------------------------
    # Process all years
    # ---------------------------------

    for year in config.YEARS:

        manifest.add_year(year)

        print("=" * 50)
        print("GCAL Builder")
        print("=" * 50)
        print(f"Year : {year}")
        print()

        # -----------------------------
        # Download year index
        # -----------------------------

        cache_file = (
            f"{config.CACHE_DIR}/ics_{year}.html"
        )

        if not downloader.download_year_index(
            year,
            cache_file
        ):
            print(f"Skipping year {year}")
            continue

        # -----------------------------
        # Extract cities
        # -----------------------------

        cities = extract_cities(
            cache_file,
            year
        )

        print(f"Cities Found : {len(cities)}")

        # -----------------------------
        # Process every city
        # -----------------------------

        for selected_city in cities:

            print()
            print(f"Processing : {selected_city.name}")

            ics_file = (
                f"{config.ICS_CACHE_DIR}/"
                f"{selected_city.name}_{year}.ics"
            )

            # Download ICS

            if not downloader.download_file(
                selected_city.ics_url,
                ics_file
            ):
                print(f"Skipped : {selected_city.name}")
                continue

            # Parse ICS

            events = parse_ics(
                ics_file
            )

            # Build festivals

            festivals = build_festivals(
                events
            )

            # Export DAYWISE JSON
            # This becomes City.json

            output_file = (
                f"{config.DATA_DIR}/"
                f"{year}/"
                f"{selected_city.name}.json"
            )

            export_daywise_json(
                festivals,
                output_file,
                selected_city.name,
                year
            )

            # Add city to manifest

            manifest.add_city(
                city=selected_city.name,
                country=selected_city.country
            )

            print(f"Completed : {selected_city.name}")

    # ---------------------------------
    # Save manifest
    # ---------------------------------

    manifest.save()

    # ---------------------------------
    # Summary
    # ---------------------------------

    print()
    print("=" * 50)
    print("All calendars generated successfully.")
    print("=" * 50)
    print(f"Years : {config.YEARS}")
    print(f"Output : {config.DATA_DIR}")


if __name__ == "__main__":
    main()




















































# import argparse

# import config
# from downloader import CalendarDownloader
# from parser import extract_cities
# from ics_parser import parse_ics
# from festival_builder import build_festivals
# from exporter import export_json
# from export_daywise import export_daywise_json
# from manifest_builder import ManifestBuilder




# def main():

#     # ---------------------------------
#     # Command-line arguments
#     # ---------------------------------

#     parser = argparse.ArgumentParser(
#         description="GCAL Builder"
#     )

#     parser.add_argument(
#         "--city",
#         default=config.CITY,
#         help="Default city (only used for display)"
#     )

#     args = parser.parse_args()

#     city_name = args.city

#     # ---------------------------------
#     # Initialize
#     # ---------------------------------

#     downloader = CalendarDownloader()

#     manifest = ManifestBuilder(
#         config.DATA_DIR
#     )

#     # ---------------------------------
#     # Process all years
#     # ---------------------------------

#     for year in config.YEARS:

#         manifest.add_year(year)

#         print("=" * 50)
#         print("GCAL Builder")
#         print("=" * 50)
#         print(f"City : {city_name}")
#         print(f"Year : {year}")
#         print()

#         # -----------------------------
#         # Download year index
#         # -----------------------------

#         cache_file = (
#             f"{config.CACHE_DIR}/ics_{year}.html"
#         )

#         if not downloader.download_year_index(
#             year,
#             cache_file
#         ):
#             print(f"Skipping year {year}")
#             continue

#         # -----------------------------
#         # Extract cities
#         # -----------------------------

#         cities = extract_cities(
#             cache_file,
#             year
#         )

#         print(f"Cities Found : {len(cities)}")

#         # -----------------------------
#         # Process every city
#         # -----------------------------

#         for selected_city in cities:

#             print()
#             print(f"Processing : {selected_city.name}")

#             ics_file = (
#                 f"{config.ICS_CACHE_DIR}/"
#                 f"{selected_city.name}_{year}.ics"
#             )

#             if not downloader.download_file(
#                 selected_city.ics_url,
#                 ics_file
#             ):
#                 print(f"Skipped : {selected_city.name}")
#                 continue

#             # -------------------------
#             # Parse ICS
#             # -------------------------

#             events = parse_ics(ics_file)

#             festivals = build_festivals(events)

#             # -------------------------
#             # Export festival JSON
#             # -------------------------

#             json_file = (
#                 f"{config.DATA_DIR}/"
#                 f"{year}/"
#                 f"{selected_city.name}.json"
#             )

#             export_json(
#                 festivals,
#                 json_file
#             )

#             # -------------------------
#             # Export daywise JSON
#             # -------------------------

#             daywise_file = (
#                 f"{config.DATA_DIR}/"
#                 f"{year}/"
#                 f"{selected_city.name}_daywise.json"
#             )

#             export_daywise_json(
#                 festivals,
#                 daywise_file,
#                 selected_city.name,
#                 year
#             )

#             # -------------------------
#             # Add city to manifest
#             # -------------------------

#             manifest.add_city(
#                 city=selected_city.name,
#                 country=selected_city.country
#             )

#             print(f"Completed : {selected_city.name}")

#     # ---------------------------------
#     # Save manifest
#     # ---------------------------------

#     manifest.save()

#     # ---------------------------------
#     # Summary
#     # ---------------------------------

#     print()
#     print("=" * 50)
#     print("All calendars generated successfully.")
#     print("=" * 50)
#     print(f"Years : {config.YEARS}")
#     print(f"Output : {config.DATA_DIR}")


# if __name__ == "__main__":
#     main()






























