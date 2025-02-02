from DictofMovies import movies
def Average(name):
    avg = 0
    for i in movies:
        if i["name"] in name:
            avg += i["imdb"]
    print(avg/len(name))
Average(["Exam", "We Two", "Detective"])
