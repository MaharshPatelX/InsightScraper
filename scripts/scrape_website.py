import os
from urllib.parse import urlparse
from src.scraper.website_md import scrape_site

def main():
    base_url = input("Enter the base URL of the website: ")
    fol_name = str(urlparse(base_url).netloc).replace("/", "_").replace("=", "_").replace("&", "_")
    os.makedirs(fol_name, exist_ok=True)
    scrape_site(base_url, fol_name)

if __name__ == "__main__":
    main()
