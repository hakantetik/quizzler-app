import requests

parameters = {
    "amount": 50,
    "category": 15,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
