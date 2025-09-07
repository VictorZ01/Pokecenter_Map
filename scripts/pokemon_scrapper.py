import os 
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException 
import csv
import argparse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

website = "https://support.pokemoncenter.com/hc/en-us/sections/13360842288916-Pok%C3%A9mon-Automated-Retail-Vending-Machines" 

class SeleniumImageScraper:
    def __init__(self):
        self.driver = None
        self.setup_driver()
        
    def setup_driver(self):
        chrome_options = Options()
        
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-features=VizDisplayCompositor")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        chrome_options.add_argument("--disable-automation")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--disable-features=TranslateUI")
        
        chrome_options.add_argument("--window-size=1920,1080")

        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            self.driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]})")
            self.driver.execute_script("Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']})")
            self.driver.execute_script("window.chrome = { runtime: {} }")
            
            self.driver.execute_script("""
                Object.defineProperty(navigator, 'permissions', {
                    get: () => ({
                        query: () => Promise.resolve({ state: 'granted' })
                    })
                });
            """)
            
            print("Starting scrapper with stealth mode")
        except Exception as e:
            print(f"IDK it died lol")
            raise
    
    def get_soup_selenium(self, url):
        try:
            self.driver.get(url)
            
            time.sleep(2)
            
            self.driver.execute_script("window.scrollTo(0, 100);")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, 0);")
             
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            time.sleep(3)

            page_source = self.driver.page_source
            return BeautifulSoup(page_source, 'html.parser')
            
        except TimeoutException:
            print(f"Timeout loading: {url}")
            return None
        except Exception as e:
            print(f"Error loading {url}: {e}")
            return None
    
    def close_driver(self):
        if self.driver:
            try:
                self.driver.quit()
                print("Driver closed")
            except Exception as e:
                print(f"Error closing driver: {e}")
            finally:
                self.driver = None

def get_list_states(url):
    scraper = SeleniumImageScraper()
    soup = scraper.get_soup_selenium(url)
    if soup:
        state_elements = soup.find_all("li", class_="article-list-item")
        scraper.close_driver()
        return state_elements

    return []

def get_link_page(page):
    links = {}
    if page:
        for item in page:
            element = item.find("a", class_="article-list-link")
            link = element["href"]
            name = element.get_text(strip=True)
            if link:
                links.update({name:"https://support.pokemoncenter.com"+link})
    return links

def get_addresses_page(urls):
    addresses = {}
    scraper = SeleniumImageScraper()
    for entry in urls[1:]:
        state = entry["State"]
        link = entry["Link"]
        soup = scraper.get_soup_selenium(link)
        if soup:
            table = soup.find("table")
            if table:
                rows = table.find("tbody").find_all("tr")
                for row in rows:
                    cells = [td.get_text(strip=True) for td in row.find_all("td")]
                    if state not in addresses:
                        addresses[state] = []
                    addresses[state].append(cells[2]+ ","+cells[3])
            else:
                print(f"No table found on {link}")
                break
    scraper.close_driver()
    return addresses

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some files.")
    parser.add_argument("states", help="Existing states file")
    args = parser.parse_args()
    
    csv_filename = "files/state_locations.csv"
    if not args.states:
        states = get_list_states(website)
        links = get_link_page(states)
        data_dicts = [
        {"State": row[0], "Link": row[1]}
        for row in links.items()
        ]

        with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
            json.dump(data_dicts, file, ensure_ascii=False, indent=2)
    
    with open(csv_filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    addresses = get_addresses_page(data)

    csv_writer = "files/addresses.csv"
    with open(csv_writer, mode='w', newline='', encoding='utf-8') as f:
            json.dump(addresses, f, ensure_ascii=False, indent=2)
 