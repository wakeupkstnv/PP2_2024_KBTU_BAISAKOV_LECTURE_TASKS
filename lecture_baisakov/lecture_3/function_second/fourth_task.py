from db import movies

def get_movie_with_avg_imdb(movies_list: list) -> None:
    count_of_movie = len(movies_list)
    all_imdb_scores = 0
    movies_which_havent = '\n'

    for name_of_movie in movies_list:
        for movie in movies:
            if name_of_movie.lower() == movie['name'].lower():
                all_imdb_scores += movie['imdb']
                break
        else:
            movies_which_havent += f'we dont have film with name {name_of_movie} in db'
            count_of_movie -= 1

    return f'avarage imdb score is: {all_imdb_scores / count_of_movie}' if len(movies_which_havent) == 0 else f'avarage imdb score is: {all_imdb_scores / count_of_movie} {movies_which_havent}'


print(get_movie_with_avg_imdb(['dark knight', 'hitman']))