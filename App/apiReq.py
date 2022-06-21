import requests

#Definovanie Flask serveru
BASE ="http://127.0.0.1:5000/"

#Zdroj dát
response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

#Požiadavky na server (BASE + " ") - definuje URL
#Put request, ktorý berie dáta z externej API a vkladá ich na server, nasledne dáta su aj outputnute do príkazového riadku.
print("PUT REQUEST DÁTA Z EXTERNEJ API")
for i in range(len(data)):
    response = requests.put(BASE + "status/" + str(i), data[i])
    print(response.json())
input()

#GET request, ktorý získava dáta z môjho serveru a outputne ich do príkazového riadku.
print("GET REQUEST S ČÍSLOM ID 4")
response = requests.get(BASE + "status/4")
print(response.json())
input()

#PATCH request, ktorý vykoná update vybraného statusu a outputne ho do príkazového riadku.
print("PATCH REQUEST S ČÍSLOM ID 2")
response = requests.patch(BASE + "status/2", {"title": "IDEM IDEM", "body": "nejdem nejdem"})
print(response.json())
input()

#DELETE request, ktorý zmaže vybrané dáta, dáta ktoré budu zmazané sa outputnu do príkazového riadku.
print("DELETE REQUEST S ČÍSLOM ID 3")
response = requests.delete(BASE + "status/3")
print(str(response.json()) + " Was deleted!")
input()

#GET request na zmazané dáta, outputne sa ERROR hlásenie.
print("GET REQUEST S ČÍSLOM 3 - OVERENIE FUNKCIE DELETE REQUESTU")
response = requests.get(BASE + "status/3")
print(response.json())