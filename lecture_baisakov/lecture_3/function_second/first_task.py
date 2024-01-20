from db import movies

def is_good_film(name_user: list) -> bool:
    for Dictionary in movies:
        if name_user.lower() == Dictionary['name'].lower(): return True if Dictionary['imdb'] > 5.5 else False
    else:
        return 'We dont have a this film in db'
    
print(is_good_film(input()))