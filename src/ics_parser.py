from icalendar import Calendar


def parse_ics(filename):

    with open(filename, "rb") as f:
        cal = Calendar.from_ical(f.read())

    events = []

    for component in cal.walk():

        if component.name != "VEVENT":
            continue

        event = {
            "summary": str(component.get("SUMMARY")),
            "start": component.get("DTSTART").dt,
            "end": component.get("DTEND").dt
            if component.get("DTEND")
            else None,
            "description": str(component.get("DESCRIPTION", "")),
            "location": str(component.get("LOCATION", "")),
        }

        events.append(event)

    return events

