from db import movies

def find_avg_from_category(category: str) -> str:
    count_of_movies_with_this_category = 0
    all_imdb_scores_with_this_category = 0

    for movie in movies:
        if movie['category'].lower() == category.lower():
            count_of_movies_with_this_category += 1
            all_imdb_scores_with_this_category += movie['imdb']
    
    if count_of_movies_with_this_category == 0: return None
    return f'avg score for your category: {all_imdb_scores_with_this_category / count_of_movies_with_this_category}'

print(find_avg_from_category("Acion"))