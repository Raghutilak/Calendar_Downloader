import config

from downloader import CalendarDownloader
from parser import extract_cities
from ics_parser import parse_ics
from festival_builder import build_festivals
from export_daywise import export_daywise_json
from manifest_builder import ManifestBuilder



def main():

    downloader = CalendarDownloader()
    manifest = ManifestBuilder(config.DATA_DIR)

    total_success = 0
    total_failed = 0

    # ---------------------------------
    # Build Every Year
    # ---------------------------------

    for year in config.YEARS:
        manifest.add_year(year)

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

                manifest.add_city(
                    city.name,
                    city.country
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

    manifest.save()

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








