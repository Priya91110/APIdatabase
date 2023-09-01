# connections
import mysql.connector
import csv
data = mysql.connector.connect(host="localhost", user="root", password="12345", database="priyadb1")
mycursor = data.cursor()

# mucursor = mycursor.execute("show databases")
# for db in mycursor:
#     print(db)

# mycursor.execute('show tables')
# for tb in mycursor:
#     print(tb)
# 
# create new table and its coloumns to add these csv data in our mysql table
# mycursor.execute("create table sample_table(moive_name varchar(255),director_name varchar(255), numbers int, moive_type varchar(255))")
# mycursor.execute('''select * from priyadb1.sample_table''')
# result=mycursor.fetchall()
# print(result)

# showing data of csv file
with open("sample1.csv", mode="r") as file:
    csv_data=csv.reader(file)
    for new_data in csv_data:
        # print(new_data)
        query='''insert into priyadb1.sample_table(moive_name, director_name, numbers, moive_type) values(%s,%s,%s,%s);'''
        mycursor.execute(query,new_data)
        data.commit()
        
mycursor.execute('''select * from priyadb1.sample_table''')
result=mycursor.fetchall()
print(result)

