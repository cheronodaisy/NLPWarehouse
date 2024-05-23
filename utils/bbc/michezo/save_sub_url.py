import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
def read_existing_urls(output_file):
    """Read existing URLs from the CSV file and return them as a set."""
    existing_urls = set()
    try:
        with open(output_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                if row:
                    existing_urls.add(row[0])
    except FileNotFoundError:
        # File does not exist, so no existing URLs
        pass
    return existing_urls

def fetch_sub_urls_with_scroll(main_url_template, start_page, end_page, output_file):
    """Fetch all sub-URLs from pages with infinite scrolling and pagination, then save them to a CSV file."""
    # Setup WebDriver (assuming chromedriver)
    #maximize the chrome
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/chromium-browser"  # Path to Chromium binary
    options.add_argument('--headless')  # Run Chromium in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Manually specify the path to the Chromedriver
    driver = webdriver.Chrome(
        service=Service("/usr/lib/chromium-browser/chromedriver"), 
        options=options
    )
    # driver = webdriver.Chrome()  # or specify the path if not in PATH webdriver.Chrome(executable_path='/path/to/chromedriver')
    sub_urls = []

    try:
        for page_num in range(start_page, end_page + 1):
            # Construct the URL for the current page
            url = main_url_template.format(page=page_num)
            driver.get(url)
            
            # Perform infinite scrolling
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                # Scroll down to the bottom of the page
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # Wait for new page segment to load
                time.sleep(3)
                # Calculate new scroll height and compare with last scroll height
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            # Process the page content after scrolling
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            post_titles = soup.find_all('h2', class_='bbc-110w6ng e47bds20')
            for title in post_titles:
                link = title.find('a', href=True)
                if link:
                    sub_urls.append(link['href'])

    finally:
        driver.quit()  # Make sure to close the browser

    # Read existing URLs from the CSV file
    existing_urls = read_existing_urls(output_file)

    # Append new sub URLs to CSV file
    with open(output_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for url in sub_urls:
            if url not in existing_urls:
                writer.writerow([url])

# Template URL for the category page with pagination
main_url_template = "https://www.bbc.com/swahili/topics/ckdxndddjkxt?page={page}"
start_page = 1  # Starting page number
end_page = 39    # Ending page number
output_file = "sub_urls.csv"  # Output CSV file

fetch_sub_urls_with_scroll(main_url_template, start_page, end_page, output_file)
print(f"Sub URLs appended to {output_file}")




