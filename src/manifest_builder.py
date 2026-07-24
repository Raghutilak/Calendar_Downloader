import json
from pathlib import Path
from datetime import datetime


def build_manifest(year, cities, filename):
    """
    Create manifest.json for Flutter app.
    """

    Path(filename).parent.mkdir(parents=True, exist_ok=True)

    data = {
        "version": "1.0.0",
        "latestYear": year,
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cities": []
    }

    for city in sorted(cities):

        data["cities"].append({
            "name": city,
            "file": f"{year}/{city}_daywise.json"
        })

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False
        )

    print(f"Manifest created : {filename}")