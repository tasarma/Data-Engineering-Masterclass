import csv
import mysql.connector
import time

start = time.time()

db = mysql.connector.connect(   host = "localhost",
                        user = "root",
                        password = "psswrd",
                        db = "project1")

cursor = db.cursor()

query = "select * from namebasics where birthYear > 2000 and primaryProfession like '%music_department%' and primaryProfession like '%actress%';"
  
cursor.execute(query)

myresult = cursor.fetchall()
for x in myresult:
    print(x)

cursor.close()

end = time.time()
print(f'sogu çalışma zamanı : {end-start}')
