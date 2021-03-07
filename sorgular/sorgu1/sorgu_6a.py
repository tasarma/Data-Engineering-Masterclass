import csv
import mysql.connector
import time

start = time.time()

db = mysql.connector.connect(   host = "localhost",
                        user = "root",
                        password = "psswrd",
                        db = "project1")

cursor = db.cursor()

query = "select t.originalTitle, e.seasonNumber, e.episodeNumber, r.averageRating from episode e inner join titlebasics t on e.parentTconst = t.tconst inner join ratings r on e.tconst = r.tconst where t.originalTitle = 'Game of Thrones' order by r.averageRating desc limit 5;"
  
cursor.execute(query)

myresult = cursor.fetchall()
for x in myresult:
    print(x)

cursor.close()

end = time.time()
print(f'sogu çalışma zamanı : {end-start}')
