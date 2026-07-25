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

Output:

```
data/
    2027/
        Bombay.json
```

## Future

- Multi-year generation
- Multi-city generation
- Day-wise JSON
- Flutter integration
