from DictofMovies import movies
def Average(cat):
    avg = 0
    cnt = 0
    for i in movies:
        if i["category"] == cat:
            avg += i["imdb"]
            cnt += 1
    print(avg/cnt)
Average("Romance")
