import mysql.connector
import csv
mydata=mysql.connector.connect(host="localhost", user="root", password="12345", database="company")
mycursor=mydata.cursor()
# mycursor.execute("create table empdata(Area varchar(225), year int, geo_count int, ec_count int)")
# mycursor.execute('insert into company.empdata(Area, year, geo_count, ec_count)values("B012254",2015,176,5)')
# mycursor.execute("select * from company.empdata")
# result = mycursor.fetchall()
# print(result)

mycursor=mydata.cursor()
with open('order.csv', mode='r') as file:
    csvFile = csv.reader(file)
    # print(csvFile)
    # mycursor.execute('''insert into company.empdata(Area, year, geo_count, ec_count) values('A345800', 2022, 111, 62011)''')
    for data in csvFile:
        if 'Area' not in data:
            query = '''insert into company.empdata(Area, year, geo_count, ec_count) values(%s, %s, %s, %s);'''
            mycursor.execute(query, data)
            mydata.commit()

mycursor.execute('''select * from company.empdata;''')
result = mycursor.fetchall()
print(result)

# mylist=[("N014456",2016,125,101), ("S4501",2013,452)]
# for data in mylist:
#     myquery='''insert into company.empdata (Area, year, geo_count, ec_count)values(%s,%s,%s,%s);'''
#     mycursor.execute(myquery,data)
# mycursor.execute("select * from company.empdata")
# result = mycursor.fetchall()
# print(result)