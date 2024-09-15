# menu_scraper.py
HTTP_ERROR_MSG = "Error: URL must be HTTP, not HTTPS."
INVALID_URL_MSG = "Error: Invalid URL. Please enter a valid HTTP URL."

def menu_scraper():
    print(r"""

▄• ▄▌• ▌ ▄ ·. ▄▄▄▄· ▄▄▄   ▄▄▄· 
█▪██▌·██ ▐███▪▐█ ▀█▪▀▄ █·▐█ ▀█ 
█▌▐█▌▐█ ▌▐▌▐█·▐█▀▀█▄▐▀▀▄ ▄█▀▀█ 
▐█▄█▌██ ██▌▐█▌██▄▪▐█▐█•█▌▐█ ▪▐▌
 ▀▀▀ ▀▀  █▪▀▀▀·▀▀▀▀ .▀  ▀ ▀  ▀ 

""")
    print("Welcome to the scraper menu!")
    print("Enter the URL you want to scrape (HTTP only):")

    url = input("> ")

    try:
        from urllib.parse import urlparse
        result = urlparse(url)
        if not result.scheme or not result.netloc:
            print(INVALID_URL_MSG)
            return None
        if result.scheme == "https":
            print(HTTP_ERROR_MSG)
            return None
    except ValueError:
        print(INVALID_URL_MSG)
        return None

    return url

def show_options():
    print("\nScraping options:")
    print("1. Extract all titles (h3)")
    print("2. Extract all links")
    print("3. Quit")

def get_option():
    option = input("> ")
    return option
