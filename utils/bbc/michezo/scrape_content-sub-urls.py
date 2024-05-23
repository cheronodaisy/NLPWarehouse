import csv
from bs4 import BeautifulSoup
from requests import get
import time

def scrapper(url):
    """Main Scraper Function
    
    Keyword arguments:
    url -- the URL for the news article
    Return: a dictionary containing the content of the article
    """
    # Initialize the dictionary to hold the data
    article_details = {'Title': '', 'Content': ''}
    
    # Fetch the webpage content
    try:
        html_content = get(url).text
        parsed_content = BeautifulSoup(html_content, "html.parser")
        
        title_tag = parsed_content.find('title')
        if title_tag:
            title = title_tag.text.strip()
            article_details['Title'] = title.capitalize()  # Capitalize the first letter
        
        main_tag = parsed_content.find('main')
        if main_tag:
            content = ""
            paragraphs = main_tag.find_all('p')
            for p in paragraphs:
                content += p.text.strip() + "\n"
            article_details['Content'] = content.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return article_details

def write_to_csv(data, filename, mode='a'):
    """Write the scraped data to a CSV file in append mode.
    
    Keyword arguments:
    data -- dictionary containing scraped data
    filename -- the name of the output CSV file without extension
    mode -- file open mode ('a' for append)
    """
    if not data:
        print("No data to write.")
        return

    # CSV column headers (assuming they exist in the first call)
    fieldnames = ['Title', 'Content']

    # Open the CSV file for appending (or create if it doesn't exist)
    with open(f"{filename}.csv", mode=mode, newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Check file size to determine if it's empty
        file_size = file.tell()  # Get the current file position (should be 0 for empty file)

        # Write header only if file is empty (file size is 0)
        if file_size == 0:
            writer.writeheader()
        
        writer.writerow(data)

def process_urls_from_csv(input_file):
    """Read URLs from a CSV file and process each one."""
    with open(input_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for index, row in enumerate(reader, start=1):
            if row:  # Ensure the row is not empty
                url = row[0]
                print(f"Processing URL: {url}")
                scraped_data = scrapper(url)
                output_filename = "/home/dereje_senbatu/10x-project/NLPWarehouse/data/bbc/michezo/michezo"  # Use a single filename here
                write_to_csv(scraped_data, output_filename, mode='a')
                # Add a delay between requests to avoid overwhelming the server
                time.sleep(3)

# Path to the input CSV file containing the sub URLs
input_file = "/home/dereje_senbatu/10x-project/NLPWarehouse/utils/bbc/michezo/sub_urls.csv"
# Process each URL in the CSV file
process_urls_from_csv(input_file)

print("Processing completed.")
