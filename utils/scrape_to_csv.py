import csv
from newspaper import Article
import os

input_csv_path = 'NLPWarehouse/utils/tuko_urls.csv'
print(os.path.isfile(input_csv_path))
output_csv_path = 'tuko_articles.csv'

urls = []
with open(input_csv_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        urls.append(row[0])

with open(output_csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(['Title', 'Content'])

    for url in urls:
        article = Article(url)
        article.download()
        article.parse()
        writer.writerow([article.title, article.text])

print(f'Articles have been saved to {output_csv_path}')
