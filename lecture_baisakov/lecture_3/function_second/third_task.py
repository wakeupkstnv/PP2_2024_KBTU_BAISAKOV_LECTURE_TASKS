from db import movies

def category_films(category_from_user: str) -> None:
    for movie in movies:
        if category_from_user == movie['category']: print(movie['name'])
    else:
        return 'we dont have filters for this category'


category_films(input())