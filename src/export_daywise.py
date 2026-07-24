import json
from pathlib import Path
from dataclasses import asdict


def export_daywise_json(festivals, filename, city="", year=0):
    """
    Export festivals grouped by calendar date.
    """

    Path(filename).parent.mkdir(parents=True, exist_ok=True)

    data = {
        "version": "1.0.0",
        "city": city,
        "year": year,
        "dates": {}
    }

    for festival in festivals:

        date = festival.date.isoformat()

        if date not in data["dates"]:

            data["dates"][date] = {
                "day": festival.date.strftime("%A"),
                "festivals": []
            }

        item = asdict(festival)

        item["date"] = date

        data["dates"][date]["festivals"].append(item)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False
        )

    print(
        f"Exported {len(data['dates'])} dates to {filename}"
    )









































































# import json
# from pathlib import Path
# from dataclasses import asdict


# def export_daywise_json(festivals, filename):
#     """
#     Export festivals grouped by date.
#     """

#     Path(filename).parent.mkdir(parents=True, exist_ok=True)

#     daywise = {}

#     # -----------------------------
#     # Group festivals by date
#     # -----------------------------

#     for festival in festivals:

#         date = festival.date.isoformat()

#         if date not in daywise:
#             daywise[date] = []

#         item = asdict(festival)

#         item["date"] = date

#         daywise[date].append(item)

#     # -----------------------------
#     # Write JSON
#     # -----------------------------

#     with open(filename, "w", encoding="utf-8") as f:
#         json.dump(
#             daywise,
#             f,
#             indent=2,
#             ensure_ascii=False
#         )

#     print(
#         f"Exported {len(daywise)} days to {filename}"
#     )