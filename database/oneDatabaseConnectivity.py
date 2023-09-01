# connections
import mysql.connector
import csv
data = mysql.connector.connect(host="localhost", user="root", password="12345", database="onedatabase")
mycursor = data.cursor()
with open("sample2.csv", mode="r") as file:
    csv_data=csv.reader(file)
    for new_data in csv_data:
        # print(new_data)

        query='''insert into onedatabase.table1(Name,Team,Position,Height,age)values(%s,%s,%s,%s,%s);'''
        mycursor.execute(query, new_data)
        data.commit()
        
        
mycursor.execute('''select * from onedatabase.table1''')
result = mycursor.fetchall()
print(result)