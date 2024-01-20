from db import movies

def good_film_list(movies = movies) -> None:
    for movie in movies:
        if movie['imdb'] > 5.5:
            print(movie['name'])

good_film_list()