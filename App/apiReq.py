import requests

#Definovanie Flask serveru
BASE ="http://127.0.0.1:5000/"

#Zdroj dát
response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

#Požiadavky na server (BASE + " ") - definuje URL
#Put request, ktorý berie dáta z externej API a vkladá ich na server, nasledne dáta su aj outputnute do príkazového riadku.
for i in range(len(data)):
    response = requests.put(BASE + "status/" + str(i), data[i])
    print(response.json())
input()

#GET request, ktorý získava dáta z môjho serveru a outputne ich do príkazového riadku.
response = requests.get(BASE + "status/4")
print(response.json())
input()

#PATCH request, ktorý vykoná update vybraného statusu a outputne ho do príkazového riadku.
response = requests.patch(BASE + "status/2", {"title": "IDEM IDEM", "body": "nejdem nejdem"})
print(response.json())
input()

#DELETE request, ktorý zmaže vybrané dáta, dáta ktoré budu zmazané sa outputnu do príkazového riadku.
response = requests.delete(BASE + "status/3")
print(str(response.json()) + " Was deleted!")
input()

#GET request na zmazané dáta, outputne sa ERROR hlásenie.
response = requests.get(BASE + "status/3")
print(response.json())