import requests
import os
from datetime import datetime

nutrinionix_domain = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_DOMAIN = os.environ["sheety_domain"]

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


def get_exercise_data():

    exercise_text = input("Tell me which exercises you did: ")

    headers = {
        "x-app-id": os.environ["APP_ID"],
        "x-app-key": os.environ["API_KEY"],
        "Authorization": os.environ["AUTH"]

    }
    print(headers)

    parameters = {
        "query": exercise_text
    }

    response = requests.post(url=nutrinionix_domain, headers=headers, json=parameters)
    result = response.json()
    exersice_data = [{'duration_min': item['duration_min'], 'name': item['name'], 'calories': item['nf_calories']} for item in result["exercises"]]

    print(exersice_data)
    return exersice_data


def get_sheet_data():

    header = {
        "Authorization": os.environ["AUTH"]
    }

    response = requests.get(url=SHEETY_DOMAIN, headers=header)
    sheet_result = response.json()

    print(sheet_result)


def post_data_sheet():
    data = get_exercise_data()

    header = {
        "Authorization": os.environ["AUTH"]
    }

    for exe in data:

        body = {
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": exe["name"].title(),
                "duration": exe["duration_min"],
                "calories": exe["calories"]

            }
        }

        response = requests.post(url=SHEETY_DOMAIN, json=body, headers=header)
        post_result = response.json()

        print(post_result)


#get_exercise_data()
#get_sheet_data()

post_data_sheet()
