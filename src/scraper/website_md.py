import os
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import html2text
from urllib.parse import urlparse, quote

def load_config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

config = load_config()

def init_driver(download_path):
    """Initialize Selenium WebDriver with specified download directory."""
    options = Options()
    if config['scraper']['headless']:
        options.headless = True
    prefs = {"download.default_directory": os.getcwd() + '/' + download_path}
    options.add_experimental_option("prefs", prefs)
    service = Service(executable_path=config['scraper']['chromedriver_path'])
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def fetch_page_content(driver, url):
    """Fetches and converts a webpage to markdown format using Selenium."""
    driver.get(url)
    title = driver.title
    html_content = driver.page_source
    text_maker = html2text.HTML2Text()
    text_maker.ignore_links = True
    markdown = text_maker.handle(html_content)
    return markdown, title

def fetch_urls(driver, main_url):
    elements = driver.find_elements(By.TAG_NAME, 'a')
    urls = []
    for element in elements:
        href = element.get_attribute('href')
        if href and href != 'javascript:void(0)' and href != 'None':
            if urlparse(href).netloc == urlparse(main_url).netloc:
                urls.append(href)
    return urls

def safe_write(data, path):
    """Safely writes data to a file."""
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred when writing to {path}: {e}")

def generate_filename(url):
    """Generates a filename from a URL by using its path and query."""
    base_name = url.replace("/", "_").replace("=", "_").replace("&", "_")
    safe_name = quote(base_name, safe="")
    return f"{safe_name}.md"

def scrape_site(base_url, fol_name):
    driver = init_driver(fol_name)
    visited = set()
    urls_to_visit = {base_url}

    while urls_to_visit:
        current_url = urls_to_visit.pop()
        print(f"{current_url}")
        if current_url not in visited:
            visited.add(current_url)
            markdown, page_title = fetch_page_content(driver, current_url)

            markdown = f"# {page_title}\n## PageLink: {current_url}\n## PageData:\n{markdown}"
            if markdown:
                filename = generate_filename(current_url)
                file_path = os.path.join(fol_name, filename)
                safe_write(markdown, file_path)

            new_urls = fetch_urls(driver, current_url)
            urls_to_visit.update(new_urls)
    driver.quit()
