from bs4 import BeautifulSoup


def find_ics_links(filename):

    with open(filename, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    print("\n===== ICS LINKS =====\n")

    for a in soup.find_all("a", href=True):

        text = a.get_text(" ", strip=True)

        href = a["href"]

        if "ICS" in text.upper():

            print(text)
            print(href)
            print()













































# from bs4 import BeautifulSoup


# def inspect_homepage(filename):

#     with open(filename, encoding="utf-8") as f:
#         html = f.read()

#     soup = BeautifulSoup(html, "html.parser")

#     print("\n====== LINKS FOUND ======\n")

#     links = soup.find_all("a")

#     for link in links:

#         text = link.get_text(strip=True)

#         href = link.get("href")

#         if href:
#             print(f"{text:40} -> {href}")