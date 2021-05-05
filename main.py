import imdb
import csv

moviesDB = imdb.IMDb()


print("Enter an actor's name: ")
person = moviesDB.search_person(input())
actor_id = person[0].personID

actor_results = moviesDB.get_person_filmography(actor_id)
if 'actor' in actor_results['data']['filmography']:
    filmography = actor_results['data']['filmography']['actor'] 
else:
    filmography = actor_results['data']['filmography']['actress']

rows = []
# loop through the filmography and retrieve attributes
for i in range(len(filmography)):
    print(i)
    film_id = filmography[i].getID()
    movie = moviesDB.get_movie(film_id)

    title = movie['title']
    if movie.has_key('year'):
        year = movie['year']
    else:
        year = '0'
    if movie.has_key('rating'):
        rating = movie['rating']
    else:
        rating = '0'
    if movie.has_key('directors'):
        directors = movie['directors']
        directors = ' '.join(map(str, directors))
    else:
        directors = "Unknown"
    if movie.has_key('genres'):
        genre = movie['genres']
        genre = ', '.join(map(str, genre))
    else:
        genre = "Unknown"
    if movie.has_key('production companies'):
        studio = movie['production companies']
        studio = ', '.join(map(str, studio))
    else:
        studio = "Unknown"

    row = []

    row.append(title)
    row.append(year)
    row.append(directors)
    row.append(studio)
    row.append(genre)
    row.append(rating)

    rows.append(row)


# id,title,japan release date,rating,length,genre,director,studio
fields = ['title', 'release date', 'director', 'studio', 'genre', 'rating']
with open(f"{person[0]}_filmography.csv", "w", newline='') as file1:
    csvwriter = csv.writer(file1)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
    # truncate the last two bytes to not have a newline at the end of .csv file
    # this is required for a proper functioning of PapaParse JS library
    size = file1.tell()
    file1.truncate(size - 2)
