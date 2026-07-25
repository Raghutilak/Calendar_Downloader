import config

from downloader import CalendarDownloader
from parser import extract_cities
from ics_parser import parse_ics
from festival_builder import build_festivals
from export_daywise import export_daywise_json
from manifest_builder import build_manifest


def main():

    downloader = CalendarDownloader()

    total_success = 0
    total_failed = 0

    # ---------------------------------
    # Build Every Year
    # ---------------------------------

    for year in config.YEARS:

        print()
        print("=" * 50)
        print(f"Building ALL Cities ({year})")
        print("=" * 50)

        # -----------------------------
        # Download Year Index
        # -----------------------------

        cache_file = (
            f"{config.CACHE_DIR}/ics_{year}.html"
        )

        if not downloader.download_year_index(
            year,
            cache_file
        ):
            continue

        # -----------------------------
        # Extract Cities
        # -----------------------------

        cities = extract_cities(
            cache_file,
            year
        )

        print(f"Cities Found : {len(cities)}")
        print()

        success = 0
        failed = 0

        # -----------------------------
        # Build Every City
        # -----------------------------

        for city in cities:

            print("-" * 50)
            print(city.name)

            try:

                # ---------------------
                # Download ICS
                # ---------------------

                ics_file = (
                    f"{config.ICS_CACHE_DIR}/"
                    f"{city.name}_{year}.ics"
                )

                downloader.download_file(
                    city.ics_url,
                    ics_file
                )

                # ---------------------
                # Parse ICS
                # ---------------------

                events = parse_ics(
                    ics_file
                )

                # ---------------------
                # Build Festivals
                # ---------------------

                festivals = build_festivals(
                    events
                )

                # ---------------------
                # Export Daywise JSON
                # ---------------------

                json_file = (
                    f"{config.DATA_DIR}/"
                    f"{year}/"
                    f"{city.name}.json"
                )



                export_daywise_json(
                    festivals,
                    json_file,
                    city.name,
                    year
                )

                success += 1

            except Exception as e:

                failed += 1

                print()
                print(f"ERROR : {city.name}")
                print(e)
                print()

        print()
        print(f"{year} Completed")
        print(f"Successful : {success}")
        print(f"Failed     : {failed}")

        total_success += success
        total_failed += failed

    # ---------------------------------
    # Build Manifest
    # ---------------------------------

    manifest_file = (
        f"{config.DATA_DIR}/manifest.json"
    )

    build_manifest(manifest_file)

    # ---------------------------------
    # Final Summary
    # ---------------------------------

    print()
    print("=" * 50)
    print("ALL YEARS COMPLETED")
    print("=" * 50)
    print(f"Successful : {total_success}")
    print(f"Failed     : {total_failed}")
    print("=" * 50)


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
# from manifest_builder import build_manifest


# def main():

#     # ---------------------------------
#     # Command Line
#     # ---------------------------------

#     parser = argparse.ArgumentParser(
#         description="Build calendar JSON for all cities."
#     )

#     parser.add_argument(
#         "--year",
#         type=int,
#         default=config.YEAR,
#         help="Calendar year"
#     )

#     args = parser.parse_args()

#     # year = args.year
#     years = config.YEARS

#     # ---------------------------------
#     # Header
#     # ---------------------------------

#     print("=" * 50)
#     print(f"Building ALL Cities ({years})")
#     print("=" * 50)

#     downloader = CalendarDownloader()

#     # ---------------------------------
#     # Download Year Index
#     # ---------------------------------

#     cache_file = (
#         f"{config.CACHE_DIR}/ics_{years}.html"
#     )

#     if not downloader.download_year_index(
#         years,
#         cache_file
#     ):
#         return

#     # ---------------------------------
#     # Extract Cities
#     # ---------------------------------

#     cities = extract_cities(
#         cache_file,
#         years
#     )

#     print(f"Cities Found : {len(cities)}")
#     print()

#     success = 0
#     failed = 0

#     successful_cities = []

#     # ---------------------------------
#     # Build Every City
#     # ---------------------------------

#     for city in cities:

#         print("-" * 50)
#         print(city.name)

#         try:

#             # -------------------------
#             # Download ICS
#             # -------------------------

#             ics_file = (
#                 f"{config.ICS_CACHE_DIR}/"
#                 f"{city.name}_{years}.ics"
#             )

#             downloader.download_file(
#                 city.ics_url,
#                 ics_file
#             )

#             # -------------------------
#             # Parse ICS
#             # -------------------------

#             events = parse_ics(
#                 ics_file
#             )

#             # -------------------------
#             # Build Festivals
#             # -------------------------

#             festivals = build_festivals(
#                 events
#             )

#             # -------------------------
#             # Export JSON
#             # -------------------------

            
#             # Export only Day-wise JSON

#             json_file = (
#                 f"{config.DATA_DIR}/"
#                 f"{years}/"
#                 f"{city.name}.json"
#             )

#             export_daywise_json(
#                 festivals,
#                 json_file,
#                 city.name,
#                 years
#             )


#             successful_cities.append(
#                 city.name
#             )

#             success += 1

#         except Exception as e:

#             failed += 1

#             print()
#             print(f"ERROR : {city.name}")
#             print(e)
#             print()

#     # ---------------------------------
#     # Build Manifest
#     # ---------------------------------

#     manifest_file = (
#         f"{config.DATA_DIR}/manifest.json"
#     )
 
#     build_manifest(manifest_file)

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





























































