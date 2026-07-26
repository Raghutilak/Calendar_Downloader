# Calendar Downloader

Download the official ISKCON/Vaisnava Calendar ICS files and convert them into structured JSON for use in mobile and desktop applications.

## Features

- Download official calendar files
- Discover all available cities
- Download city-specific ICS files
- Parse festivals
- Detect Ekadasi
- Detect Mahadvadasi
- Detect Appearance festivals
- Detect Disappearance festivals
- Detect Break Fast timings
- Export clean JSON

## Project Structure

Calendar_Downloader/

    src/
        main.py
        downloader.py
        parser.py
        ics_parser.py
        festival_builder.py
        exporter.py
        models.py

    cache/
    data/
    logs/

## Requirements

- Python 3.11+
- requests
- beautifulsoup4
- icalendar

Install:

```bash
pip install -r requirements.txt
```

Run:

```bash
python src/main.py
```

# Calendar Downloader

Python tool to download Vaisnava calendar data, parse festival events,
and generate JSON files for use by the mobile alarm/calendar application.

## GitHub Repository

Repository:
https://github.com/Raghutilak/Calendar_Data

## Workflow

Calendar Downloader
|
v
Download ICS calendar data
|
v
Parse festival events
|
v
Generate Calendar_Data JSON
|
v
Flutter Alarm App reads JSON and creates reminders

## Output

Generated files are stored separately:

Calendar_Data/

├── manifest.json
├── 2026/
└── 2027/

The Flutter app uses manifest.json from github Repository to locate calendar files.

## City Selection Logic

The mobile app selects calendar data using:

GPS detected city
|
v
Exact city match?
|
Yes → Use city JSON
|
No
|
v
Alias match?
|
Yes → Use mapped city JSON
|
No
|
v
Find nearest available calendar city
|
v
Use nearest city's JSON

## Development

Create virtual environment:

python -m venv .venv

Activate:

.venv\Scripts\activate

Run downloader:

python src/main.py

## Version History

- Milestone 1 - Homepage downloader
- Version 1.1 - CLI support and all-city generator
- Calendar 2027 - Festival JSON generation

cmd
(.venv) C:\Calendar_Downloader>git remote -v
origin https://github.com/Raghutilak/Calendar_Data.git (fetch)
origin https://github.com/Raghutilak/Calendar_Data.git (push)

(.venv) C:\Calendar_Downloader>git push -u origin master
Enumerating objects: 41, done.

(.venv) C:\Calendar_Downloader>git status

git add .
git commit -m "describe changes"
git push

e.g...
git add README.md
git commit -m "Update README with project documentation"
git push

GitHub repo(normal sharing link from browser): https://github.com/Raghutilak/Calendar_Data

Local project: C:\Calendar_Downloader
