import requests
import datetime

SHEET_ENDPOINT = "https://api.sheety.co/20272124109ec9d57ad70fc8eb07bbd3/workoutTracking/workouts"
TRACKAPI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
HEADERS = {
    "Authorization": os.environ.get("AUTHORIZATION")
}


def get_calorie_info():
    app_id = "e80a52e5"
    api_key = os.environ.get("API_KEY")

    query = input("Tell me which exercise you did: ")
    json = {
        "query": query,
        "gender": "M",
        "weight_kg":70,
        "height_cm": 180,
        "age": 25
    }

    headers = {
        "x-app-id": app_id,
        "x-app-key": api_key,
    }

    response = requests.post(url=TRACKAPI_ENDPOINT, json=json, headers=headers)
    response.raise_for_status()
    # print(response.json())
    return response.json()['exercises']


now = datetime.datetime.now()
date = now.strftime("%d/%m/%Y")
time = f"{now.hour}:{now.minute}"

row = {}
calorie_info = get_calorie_info()
for item in calorie_info:

    row = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": item['name'],
            "duration": str(item['duration_min']),
            "calories": item['nf_calories']
        }
    }
    print(row)
    sheet_response = requests.post(url=SHEET_ENDPOINT, json=row, headers=HEADERS)
    print(sheet_response.text)

