import csv
import newspaper

news = newspaper.build('https://kiswahili.tuko.co.ke/tags/citizen-tv-kenya/')

csv_file_path = 'tuko_urls.csv'

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['URL'])

    for article in news.articles:
        writer.writerow([article.url])

print(f'Article URLs have been saved to {csv_file_path}')
