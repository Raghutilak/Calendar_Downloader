import re


def safe_filename(name: str) -> str:
    """
    Convert a city name into a safe filename.
    """

    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    name = name.replace(",", "")
    return name.strip()