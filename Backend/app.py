from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Database configuration
DATABASE = {
    'dbname': 'webscraping',
    'user': 'articles',
    'password': 'articles',
    'host': 'localhost',
    'port': '5432'
}

# Utility function to get a database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname=DATABASE['dbname'],
        user=DATABASE['user'],
        password=DATABASE['password'],
        host=DATABASE['host'],
        port=DATABASE['port']
    )
    return conn


@app.route('/')
def index():
    return 'Hello, World!'

#Retrieving data
@app.route('/texts', methods=['GET'])
def get_texts():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM articles;')
    texts = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(texts)
#Searching for data
@app.route('/texts/<int:id>', methods=['GET'])
def get_text_by_id(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM articles WHERE id = %s;', (id,))
    text = cur.fetchone()
    cur.close()
    conn.close()
    if text:
        return jsonify(text)
    return ('', 404)

# Search data
@app.route('/search', methods=['GET'])
def search_data():
    query = request.args.get('query')
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM articles WHERE column_name ILIKE %s;', ('%' + query + '%',))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

# Filter data
@app.route('/filter', methods=['GET'])
def filter_data():
    filters = request.args
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM articles WHERE column_name = %s;', (filters['filter'],))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)