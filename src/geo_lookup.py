import json
import time
from pathlib import Path

from geopy.geocoders import Nominatim
from geopy.exc import (
    GeocoderRateLimited,
    GeocoderUnavailable,
    GeocoderTimedOut,
    GeocoderServiceError,
)

from timezonefinder import TimezoneFinder


CACHE_FILE = Path("../cache/city_coordinates.json")

geolocator = Nominatim(
    user_agent="gcal_builder"
)

tf = TimezoneFinder()


def load_cache():

    if CACHE_FILE.exists():

        with open(
            CACHE_FILE,
            encoding="utf-8"
        ) as f:

            return json.load(f)

    return {}


def save_cache(cache):

    CACHE_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        CACHE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            cache,
            f,
            indent=2,
            ensure_ascii=False,
            sort_keys=True
        )


def get_city_info(city, country):

    cache = load_cache()

    key = f"{city},{country}"

    # -------------------------------
    # Already cached
    # -------------------------------

    if key in cache:

        print(f"Using cache : {key}")

        return cache[key]

    print(f"Looking up : {key}")

    location = None

    # -------------------------------
    # Retry lookup
    # -------------------------------

    for attempt in range(5):

        try:

            location = geolocator.geocode(
                key,
                exactly_one=True,
                timeout=30
            )

            break

        except (
            GeocoderRateLimited,
            GeocoderUnavailable,
            GeocoderTimedOut,
            GeocoderServiceError,
        ) as e:

            wait = (attempt + 1) * 5

            print(
                f"Retry {attempt + 1}/5 "
                f"after {wait}s "
                f"({e})"
            )

            time.sleep(wait)

    # Respect Nominatim usage policy
    time.sleep(1)

    # -------------------------------
    # Not found
    # -------------------------------

    if location is None:

        print(f"Not found : {key}")

        info = {

            "lat": None,

            "lon": None,

            "timezone": None

        }

    else:

        timezone = tf.timezone_at(
            lat=location.latitude,
            lng=location.longitude
        )

        info = {

            "lat": round(location.latitude, 6),

            "lon": round(location.longitude, 6),

            "timezone": timezone

        }

        print(
            f"OK : "
            f"{info['lat']}, "
            f"{info['lon']} "
            f"{timezone}"
        )

    # -------------------------------
    # Save immediately
    # -------------------------------

    cache[key] = info

    save_cache(cache)

    return info