import requests
import datetime

NUTRITION_API_KEY = "719db338e40c3b8efe94e12bb1ca0c1a"
NUTRITION_API_APPLICATION_ID = "b0fa724b"
GENDER = "male"
WEIGHT = 55
HEIGHT = 165
AGE = 15

nutrition_post_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

input_string = input("Tell me which exercise you did?: ")

headers = {
    "x-app-id": NUTRITION_API_APPLICATION_ID,
    "x-app-key": NUTRITION_API_KEY,
}

post_parameters = {
    "query": input_string,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

nutrition_response = requests.post(url=nutrition_post_endpoint, json=post_parameters, headers=headers)
nutrition_response.raise_for_status()

data = nutrition_response.json()

x = datetime.datetime.now()

date = x.strftime("%d/%m/%Y")
time = x.strftime("%H:%M:%S")

for exercise in data["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": data["exercises"][0]["name"].title(),
            "duration": round(data["exercises"][0]["duration_min"], 1),
            "calories": round(data["exercises"][0]["nf_calories"])
        }
    }
    sheety_endpoint = "https://api.sheety.co/akilesh/myWorkouts/workouts"
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_parameters)
    print(sheety_response.text)
