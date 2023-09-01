
import requests
import psycopg2
import os
import pandas as pd


def create_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="12345",
            host="localhost",
            port="5432"
        )
        print("Connection to database successful!")
        #  Perform database operations here
        # conn.close()
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to database")
        print(e)
        
        
def create_table():
    table_query = """
    CREATE TABLE if not exist apis.api_entriess (
    id INT PRIMARY KEY,
    api VARCHAR(255),
    description TEXT,
    auth VARCHAR(255),
    https BOOLEAN,
    cors VARCHAR(255),
    link VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL
    );"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(table_query)
    cursor.execute('''select * from apis.api_entries;''')
    print(cursor.fetchall())
    import pdb; pdb.set_trace()
    

def get_data(url):
    response =  requests.get(url)
    data = response.json()
    return data

def processing_dataframe():
    url = "https://api.publicapis.org/entries"
    raw_data = get_data(url)
    data = raw_data['entries']
    df = pd.DataFrame(data)
    import pdb; pdb.set_trace()
    df.to_csv('api_data.csv', sep=',', index=False)
    df['timestamp_now_str'] = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    with open('api_data.csv', 'r') as csv_file:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.copy_expert("COPY api_test.api_entries (api, description, auth, https, cors, link, category)FROM STDIN WITH CSV HEADER DELIMITER ','", csv_file)
        conn.commit()

def main():
    # create_table()
    processing_dataframe()
    
if __name__ == "__main__":
    main()
   