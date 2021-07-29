
import json 

with open("movies.json") as file_object: 
    result = json.load(file_object)

movies = result["Search"] #movies will be an array of movies (dictionaries)

for movie in movies:
    print(movie["Title"])
    