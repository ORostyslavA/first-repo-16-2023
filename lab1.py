import requests

url = "https://www.google.com/"
response = requests.get(url)
print(response.text)

city = "Lviv"

is_voter = False
is_citizen = True
is_raining = True
is_snowing = False

print(city)
print(is_voter, is_citizen)
print(is_raining is not is_snowing)
