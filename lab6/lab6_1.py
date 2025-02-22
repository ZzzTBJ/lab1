import os
#1
path = 'c:/Users/Зухра/Desktop/PP2/lab1'
print("Fold i docs:", os.listdir(path))
#2
print("Existence: ", os.access(path, os.F_OK))
print("Readability: ", os.access(path, os.R_OK))
print("Writability: ", os.access(path, os.W_OK))
print("Executability: ", os.access(path, os.X_OK))
#3
if (os.access(path, os.F_OK)) == True:
    print("Success!")
    print("File: ", os.path.basename(path))
    print("Dir: ", os.path.dirname(path))
else:
    print("No such path")
#4 
with open("c:/Users/Зухра/Desktop/PP2/lab1/lab6/file.txt", "r") as file:
    lines = file.readlines()
print("There are", len(lines), "lines")
#5
lst = ["easygg","1", "loh"]
with open("c:/Users/Зухра/Desktop/PP2/lab1/lab6/file1.txt", "a") as file1:
    file1.writelines(f"{item}\n" for item in lst)
#6
a = ord('A')
base = 'c:/Users/Зухра/Desktop/PP2/lab1/lab6/files\\{}.txt'
for i in range(a, a+26):
    f = open(base.format(chr(i)), "x")
#7
with open("c:/Users/Зухра/Desktop/PP2/lab1/lab6/file2.txt", "w") as f1:
    with open("c:/Users/Зухра/Desktop/PP2/lab1/lab6/file.txt", "r") as f2:
        f1.write(f2.read())
#8

path2 = "c:/Users/Зухра/Desktop/PP2/lab1/lab6/file3.txt"
print("Existence: ", os.access(path2, os.F_OK))
print("Access: ", os.access(path2, os.X_OK))
if os.access(path2, os.F_OK) == True:
    if os.access(path2, os.X_OK) == True:
        os.remove(path2)
        print("File has been removed")
    else:
        print("Cannot be removed")
else:
    print("No such file")