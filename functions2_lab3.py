from DictofMovies import movies
def Sublist():
    for i in movies:
        if i["imdb"] > 5.5:
            print(i["name"], i["imdb"])
Sublist()