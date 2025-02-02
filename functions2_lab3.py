from DictofMovies import movies
def Check(name):
    for i in movies:
        if i["name"] == name:
            if i["imdb"] > 5.5:
                print("True")
            else: print("False")
Check("Exam")
Check("We Two")
Check("Detective")