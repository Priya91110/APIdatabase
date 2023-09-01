# import requests
# import json
# import pandas as pd
# url = 'https://api.publicapis.org/entries'

# response = requests.get(url)
# print(response.status_code)
# print(response.json())
# print(response.json()['entries'])
# print(pd.DataFrame(response.json()['entries']).head(50)[['API','Description','HTTPS','Cors','Link','Category']])
# print(pd.DataFrame(response.json()['entries']).head(50)[['API','Description','Category']])
# print(pd.DataFrame(response.json()['entries'])[['API','Description','Category']])
# df=pd.DataFrame(response.json()['entries'])[['API','Description','HTTPS','Cors','Link','Category']]
# print(df.head())
# nedf=pd.DataFrame()
# for i in range(1425):
    # nedf.append((pd.DataFrame(response.json()['entries']).head(i))[['API','Description','HTTPS','Cors','Link','Category']])
    

# Create a sample DataFrame

# Convert the DataFrame to CSV
# df1=pd.DataFrame(df, columns=['API','Description','HTTPS','Cors','Link','Category'])
# df1.to_csv('F:/backend/Database/mydata.csv')  
import mysql.connector
import csv
mydata=mysql.connector.connect(host="localhost", user="root", password="12345", database="api_data")
mycursor=mydata.cursor()
mycursor.execute("select * from api_data.api_table")
result = mycursor.fetchall()
print(result)

mycursor=mydata.cursor()
with open('mydata.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for row in csvFile:
        mycursor.execute('''insert into api_data.api_table(API,Description,HTTPS,Cors,Link,Category) values(%s, %s, %s, %s,%s,%s),(row[0],row[1],row[2],row[3],row[4],row[5],row[6])''')
    mydata.commit()
mycursor.execute('''select * from api_data.api_table;''')
result = mycursor.fetchall()
print(result)