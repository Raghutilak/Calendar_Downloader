import config
from downloader import CalendarDownloader
# from parser import inspect_homepage
from parser import find_ics_links


def main():

    print("Calendar Downloader Started")

    downloader = CalendarDownloader()

    if downloader.test_connection(config.BASE_URL):

        downloader.download_page(
            config.BASE_URL,
            "../cache/homepage.html"
        )

        # inspect_homepage("../cache/homepage.html")
        find_ics_links("../cache/homepage.html")

    else:

        print("Connection failed.")


if __name__ == "__main__":
    main()




































# import config
# from downloader import CalendarDownloader


# def main():

#     print("Calendar Downloader Started")

#     downloader = CalendarDownloader()

#     if downloader.test_connection(config.BASE_URL):

#         downloader.download_page(
#             config.BASE_URL,
#             "../cache/homepage.html"
#         )

#         print("Homepage downloaded successfully.")

#     else:

#         print("Connection failed.")


# if __name__ == "__main__":
#     main()

















































# import config
# from downloader import CalendarDownloader


# def main():

#     print("Calendar Downloader Started")

#     downloader = CalendarDownloader()

#     success = downloader.test_connection(config.BASE_URL)

#     if success:
#         print("Website is reachable.")
#     else:
#         print("Connection failed.")


# if __name__ == "__main__":
#     main()




