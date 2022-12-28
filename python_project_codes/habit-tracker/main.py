import requests
import datetime

USERNAME = "rammani"
TOKEN = os.environ.get("TOKEN")
API_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # create a user at pixe.la
# response = requests.post(url=API_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{API_ENDPOINT}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Book Graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu",
}

header = {
    "X-USER-TOKEN": TOKEN,
}
# # headers required to provide authentication but make it not appear on the url
# response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
# print(response.text)

today = datetime.datetime.now()
print(today.strftime("%Y%m%d"))

pixel_add_endpoint = f"{graph_endpoint}/graph1"
pixel_add_param = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? "),
}

# post a pixel
response = requests.post(url=pixel_add_endpoint, json=pixel_add_param, headers=header)


# # update pixel
# date = datetime.datetime(2022, 11, 2).strftime("%Y%m%d")
# pixel_update_endpoint = f"{pixel_add_endpoint}/{date}"
# pixel_update_params = {
#     "quantity": "10",
# }
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=header)

# # delete pixel
# delete_endpoint = pixel_update_endpoint
# response = requests.delete(url=pixel_update_endpoint, headers=header)

print(response.text)
