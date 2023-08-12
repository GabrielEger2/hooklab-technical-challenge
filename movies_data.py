# movies_data.py
films = [
    {"title": "The Lord of the Rings", "year": 2001, "rating": 8.8},
    {"title": "Matrix", "year": 1999, "rating": 9.3},
    {"title": "Interstellar", "year": 2014, "rating": 8.6}
]

def get_average_rating():
    ratings = [film["rating"] for film in films]
    average_rating = sum(ratings) / len(ratings)
    return average_rating

def get_highest_rated_film():
    return max(films, key=lambda x: x["rating"])

def get_lowest_rated_film():
    return min(films, key=lambda x: x["rating"])

print(f"Average ratings of the films: {get_average_rating()}")
print(f"Film with the highest rating: {get_highest_rated_film()['title']}")
print(f"Year of release of the film with the lowest rating: {get_lowest_rated_film()['year']}")