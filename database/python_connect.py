#!/usr/bin/python
import psycopg2

try:
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host="localhost",
        database="new_db",
        port="5432",
        user="postgres",
        password="12345"
    )
    # create a cursor
    cur = conn.cursor()
    
    # execute a statement
    print('PostgreSQL database version:')
    # cur.execute('SELECT version()')
    query = '''insert into countries.india(state, pincode) values(%s ,%s)'''
    data = ('himachal', 456789)
    cur.execute(query, data)
    # cur.execute("""select * from countries.india;""")
    
    # display the PostgreSQL database server version
    # db_version = cur.fetchall()
    # print(db_version)
    
# close the communication with the PostgreSQL
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
