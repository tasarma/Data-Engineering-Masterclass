import csv
import mysql.connector
import time

start = time.time()

db = mysql.connector.connect(   host = "localhost",
                        user = "root",
                        password = "psswrd",
                        db = "project1")

cursor = db.cursor()

query = "select count(*) from (select tconst, count('category') as f from principals where category='actress' group by tconst having f>=4) as sum;"

cursor.execute(query)

myresult = cursor.fetchall()
for x in myresult:
    print(x)

cursor.close()

end = time.time()
print(f'sogu çalışma zamanı : {end-start}')
