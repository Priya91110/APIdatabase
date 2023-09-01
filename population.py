
from sqlalchemy import create_engine
import pandas as pd
import json
import requests
def get_conn():
    try:
        engine = create_engine('postgresql://postgres:12345@localhost:5432/postgres')
        return  engine
    except:
        print("connection failed")
    return None
def insert_data():
    url="https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    response = requests.get(url)
    data1 = response.json()["data"]
    if response.status_code == 200:
        conn = get_conn()
        df = pd.DataFrame(data1)
        df.rename(
            columns={
            "ID Nation": "idnation",
            "Nation": "nation",
            "ID Year": "idyear",
            "Year": "year",
            "Population": "population",
            "Slug Nation": "slugnation",},inplace=True)
        # df.to_sql("table",con=your connection,"schema",if_exists="append",index=False)
        df.to_sql('population_tb', con=conn, schema='apis', if_exists='append', index=False)
    else:
        print("error")
insert_data()


