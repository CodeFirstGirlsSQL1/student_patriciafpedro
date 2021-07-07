import requests
import json


# POST REQUEST

# new_flight = {
#      "from_city": "Stockholm",
#      "to_city": "Oslo",
#      "days": [1, 7],
#      "captain": {'name': 'Ole',
#                  'surname': 'Johansson'},
#      "duration_min": 30,
#      "capacity": 50,
#      "booked": 20,
#      "available":  30,
#      "flight_id": 777
# }
#
# headers = {'content-type': 'application/json'}
# result = requests.post(
#     'http://127.0.0.1:5000/flights', headers=headers, data=json.dumps(new_flight)
# )
# print(result)


# # PUT REQUEST
#
# updated_flight = {
#      "new content": "test",
#      "flight_id": 555
# }
#
# fid = 555
#
# headers = {'content-type': 'application/json'}
# result = requests.put(
#     'http://127.0.0.1:5000/flights/{}'.format(fid), headers=headers, data=json.dumps(updated_flight)
# )
# print(result)


# DELETE REQUEST
# front end --> go to this url and delete the data correspondent to flight 555
# I already gave permission in the backend file for this to happen (in flight building_own_api.py)
# the data in the database in not touched
# The data is ony deleted in the browser(which is a front end just for us to
# be able to see the result. It's just a visualisation tool
fid = 555

headers = {'content-type': 'application/json'}
result = requests.delete(
    'http://127.0.0.1:5000/flights/{}'.format(fid), headers=headers
 )

print(result)