import pandas as pd
import re
from bs4 import BeautifulSoup
from langdetect import detect

# Read raw data from CSV
df = pd.read_csv('raw_data.csv')

# Define preprocessing functions
def normalize_text(text):
    return text.lower()

def remove_punctuation_and_normalize_whitespace(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_html_tags_and_special_characters(text):
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text()
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    return text

def is_swahili(text):
    try:
        return detect(text) == 'sw'
    except:
        return False

def preprocess_text(text):
    text = normalize_text(text)
    text = remove_punctuation_and_normalize_whitespace(text)
    text = remove_html_tags_and_special_characters(text)
    return text

# Preprocess text data
cleaned_titles = []
cleaned_contents = []

for title, content in zip(df['title'], df['content']):
    cleaned_title = preprocess_text(title)
    cleaned_content = preprocess_text(content)
    
    if is_swahili(cleaned_title) and is_swahili(cleaned_content):
        cleaned_titles.append(cleaned_title)
        cleaned_contents.append(cleaned_content)

# Store cleaned data in a new DataFrame and save to CSV
cleaned_df = pd.DataFrame({'cleaned_title': cleaned_titles, 'cleaned_content': cleaned_contents})
cleaned_df.to_csv('cleaned_data.csv', index=False)
