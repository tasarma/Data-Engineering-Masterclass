import mysql.connector as mc
import csv
import time

start = time.time()

db = mc.connect( host = "localhost",
                        user = "root",
                        password = "sifre",
                        db = "proje")

cur = db.cursor()

insert1 = "INSERT INTO ratings (tconst, averageRating, numVotes) VALUES (%s, %s, %s)"
insert2 = "INSERT INTO akas (titleId, ordering, title, region, language, types, attributes, isOriginalTitle) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
insert3 = "INSERT INTO crew (tconst, directors, writers) VALUES (%s, %s, %s)"
insert4 = "INSERT INTO episode (tconst, parentTconst, seasonNumber, episodeNumber) VALUES (%s, %s, %s, %s)"
insert5 = "INSERT INTO namebasics (nconst, primaryName, birthYear, deathYear, primaryProfession, knownForTitles) VALUES (%s, %s, %s, %s, %s, %s)"
insert6 = "INSERT INTO principals (tconst, ordering, nconst, category, job, characters) VALUES (%s, %s, %s, %s, %s, %s)"
insert7 = "INSERT INTO hadi (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s"


my_data = []
with open('ratings.tsv', newline='') as csvfile:
    csv_data = csv.reader(csvfile)
    for row in csv_data:
        for i in row:
            my_data.append(tuple(i.split('\t')))

cursor.executemany(insert, my_data)

cursor.close()
