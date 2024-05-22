import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

def fetch_sub_urls_with_scroll(main_url, num_pages, output_file):
    """Fetch all sub-URLs from a page with infinite scrolling and pagination, then save them to a CSV file."""
    # Setup WebDriver (assuming chromedriver)
    driver = webdriver.Chrome()  # or specify the path if not in PATH webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.get(main_url)
    sub_urls = []

    try:
        for _ in range(num_pages):
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
            post_titles = soup.find_all('h', class_='bbc-110w6ng e47bds20')
            for title in post_titles:
                link = title.find('a', href=True)
                if link:
                    sub_urls.append(link['href'])
            
            # Find and click the next page link
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.bbc-8n7wgv > a:not([aria-current="page"])'))
                )
                next_button.click()
                time.sleep(3)  # Wait for the next page to load
            except Exception as e:
                print(f"No more pages or error: {e}")
                break

    finally:
        driver.quit()  # make sure to close the browser

    # Write sub URLs to CSV file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Sub URL"])
        for url in sub_urls:
            writer.writerow([url])

# Main URL for the category page
main_url = "https://www.bbc.com/swahili/topics/c6z8lg838klt"
num_pages = 2  # Number of pages you want to scrape
output_file = "sub_urls.csv"  # Output CSV file

fetch_sub_urls_with_scroll(main_url, num_pages, output_file)
print(f"Sub URLs saved to {output_file}")

