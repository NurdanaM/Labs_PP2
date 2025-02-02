def func(movie):
    return movie["imdb"] > 5.5

m = {
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
}

print(func(m))