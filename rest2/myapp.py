import requests
import json

URL = "http://127.0.0.1:8000/student_create/"
data = {
    'name':'anu'
    ,'roll':105,
    'city':'pgdi'

}

json_data = json.dumps(data)
print(json_data)

r = requests.post(url = URL, data = json_data)
b=requests.post(url=URL,data=json_data)
print('lllllllllllllllllllll',b)
data = r.json()
print(data)



# import requests
# import json

# URL = "http://127.0.0.1:8000/student_create/"

# data = {
#     'name': 'anu',
#     'roll': 105,
#     'city': 'pgdi'
# }

# json_data = json.dumps(data)

# try:
#     r = requests.post(url=URL, data=json_data)
#     r.raise_for_status()  # Check for HTTP request errors
#     response_data = r.json()
#     print(response_data)
# except Exception as e:
#     print(f"An error occurred: {e}")
