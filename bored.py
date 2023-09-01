import requests
import pandas as pd
import psycopg2 
import os

def test_con():
    try:
        con=psycopg2.connect(dbname="postgres",user="postgres", password="12345", host="localhost", port="5432")
        print("connection successfull")
        return con
    except psycopg2.Error as er:
        print("connection failed")
        
def create_table():
    t_query=""""
    CREATE TABLE if not exist apis.bored_api(
        id INT PRIMARY KEY,
        activity VARCHAR(225),
        type VARCHAR(225),
        participants INT,
        price DECIMAL,
        link VARCHAR(225),
        key VARCHAR(225),
        accessibility DECIMAL,
    );"""
    con = test_con()
    cursor = con.cursor()
    cursor.execute(t_query)
    cursor.execute('''select * from apis.bored_api;''')
    print(cursor.fetchall())
    
def get_data(url):
    response = requests.get(url)
    data = response.json()
    return data
    
def process():
    url="https://api.publicapis.org/entries"
    raw_data = get_data(url)
    import pdb; pdb.set_trace()
    data = raw_data['entries']
    df = pd.DataFrame(data)
    df.to_csv('new_file.csv', index=False)
    
def main():
    process()

if __name__ == "__main__":
    main()