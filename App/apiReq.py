import requests

#Definovanie Flask serveru
BASE ="http://127.0.0.1:5000/"

#Zdroj dát
data = [{"userID": 10, "title": "TestTest", "body": "BodyBodyBodyyyyyy"},
        {"userID": 20, "title": "Ako variť", "body": "Uvar jedlo"},
        {"userID": 30, "title": "Ako piť", "body": "Pi vodu"}]

#Požiadavky na server (BASE + " ") - definuje URL
for i in range(len(data)):
    response = requests.put(BASE + "status/" + str(i), data[i])
    print(response.json())

#response = requests.put(BASE + "status/" + str(656454), data[0])
#print(response.json())


input()

response = requests.get(BASE + "status/4")
print(response.json())

input()

response = requests.patch(BASE + "status/2", {"title": "IDEM IDEM", "body": "nejdem nejdem"})
print(response.json())