# web_scraper.py
import requests
from bs4 import BeautifulSoup
from menu_scraper import menu_scraper, show_options, get_option
from constants import TITLE_PATTERN, LINK_PATTERN

def get_url():
    url = menu_scraper()
    if url is None:
        return None
    return url

def parse_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    return BeautifulSoup(response.content, 'html.parser')

def scrape_titles(soup):
    titles = soup.find_all(TITLE_PATTERN)
    print("\nTitles found:")
    for title in titles:
        print(title.text.strip())

def scrape_links(soup):
    links = soup.find_all(LINK_PATTERN)
    print("\nLinks found:")
    for link in links:
        print(link.text.strip())

def display_results(soup, option):
    if option == "1":
        scrape_titles(soup)
    elif option == "2":
        scrape_links(soup)
    elif option == "3":
        print("Goodbye!")
        return False
    else:
        print("Invalid option. Try again.")
    return True

def main():
    url = get_url()
    if url is None:
        return

    soup = parse_page(url)
    if soup is None:
        return

    while True:
        show_options()
        option = get_option()
        if not display_results(soup, option):
            break

if __name__ == "__main__":
    main()
