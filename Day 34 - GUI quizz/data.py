import requests

parameters = {
    "amount": 15,
    "type": "boolean",
    "category": 14,
}

r = requests.get('https://opentdb.com/api.php', params=parameters)
r.raise_for_status()
data = r.json()
question_data = data["results"]
print(data)



