import json
with open("c:/Users/Зухра/Desktop/PP2/lab1/lab4/json/sample-data.json", "r") as file:
    data = json.load(file)
interf = data["imdata"]
print("Interface Status ")
print("="*70)
print("DN", " "*43, "Description", " "*5, "Speed", " "*3, "MTU" )
print("-"*43, " ", "-"*15, " ", "-"*7, " ", "-"*5)
for dat in interf:
    for i in dat:
        for j in dat[i]:
            print(dat[i][j]["dn"], "\t", "\t", "\t", dat[i][j]["speed"]," ", dat[i][j]["mtu"])