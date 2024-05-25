import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

df = pd.read_csv('NLPWarehouse/data/preprocessed_data/cleaned_data.csv')

conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

cur = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS preprocessed (
    id SERIAL PRIMARY KEY,
    cleaned_title TEXT NOT NULL,
    cleaned_content TEXT NOT NULL
);
'''
cur.execute(create_table_query)
conn.commit()

for index, row in df.iterrows():
    cur.execute(
        "INSERT INTO articles (Title, Content) VALUES (%s, %s)",
        (row['cleaned_title'], row['cleaned_content'])
    )

conn.commit()

cur.close()
conn.close()

print("Data inserted successfully from CSV file.")
