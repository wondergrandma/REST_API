import requests

#Definovanie Flask serveru
BASE ="http://127.0.0.1:5000/"

#Zdroj dát
response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

'''data = [{"userId": 1,"id": 2, "title": "Pozdrav", "body": 'Ahoj Ahoj Ahoj'},
        {"userId": 2,"id": 4, "title": "Pijem", "body": "Mineralka je dobrá"}, 
        {"userId": 2,"id": 6, "title": "Oslavujeme", "body": "50-te narodeniny"},
        {"userId": 2,"id": 8, "title": "Skúšam auto", "body": "Mam nove auto"}, 
        {"userId": 5,"id": 10, "title": "Deravá guma", "body": "Opravujem bicykel"}, 
        {"userId": 6,"id": 12, "title": "Pomoc", "body": "Ako opraviť auto"}]'''

#Požiadavky na server (BASE + " ") - definuje URL
for i in range(len(data)):
    response = requests.put(BASE + "status/" + str(i), data[i])
    print(response.json())

input()

response = requests.get(BASE + "status/4")
print(response.json())

input()

response = requests.delete(BASE + "status/3")
print(str(response.json()) + " Was deleted!")

input()

response = requests.get(BASE + "status/3")
print(response.json())

#response = requests.patch(BASE + "status/2", {"title": "IDEM IDEM", "body": "nejdem nejdem"})
#print(response.json())