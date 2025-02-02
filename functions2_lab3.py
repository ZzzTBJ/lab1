from DictofMovies import movies
def Category(cat):
    for i in movies:
        if i["category"] == cat:
            print(i["name"])
Category("Romance")