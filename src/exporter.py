import json
from pathlib import Path
from dataclasses import asdict


def export_json(festivals, filename):
    """
    Export Festival objects to JSON.
    """

    Path(filename).parent.mkdir(parents=True, exist_ok=True)

    data = []

    for festival in festivals:

        item = asdict(festival)

        # Convert date object to ISO string
        if hasattr(item["date"], "isoformat"):
            item["date"] = item["date"].isoformat()

        data.append(item)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False
        )

    print(f"Exported {len(data)} festivals to {filename}")    