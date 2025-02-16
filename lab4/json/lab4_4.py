import json
with open("sample-data.json", 'r') as file:
    data = json.load(file)
interf = data["imdata"]
print("Interface Status ", end= "")
print("="*50)
print("DN", " "*40, "Description", " "*10, "Speed", " "*5, "MTU" )