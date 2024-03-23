# import json
#
# import requests
#
# request_url = "https://swapi.dev/api/people"
# header = 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
# r = requests.get(request_url, request_url, headers={"User-Agent": header})
#
# results = r.json()['results']
# print(results)
#
# with open('api_output.json', 'w') as ouput:
#     json.dump(results, ouput, indent=4)
#
# for eye in results:
#     print(eye)

import json

import requests

base_api = "https://swapi.dev/api/people"
user_agent = 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
try:

    r = requests.get(f"{base_api}/people", headers={"User-Agent": user_agent})

    results = r.json()['results']
    print(results)

with open('api_output.json', 'w') as ouput:
    json.dump(results, ouput, indent=4)

exept Exception as e:
    print(e)
        results = {}

with open('api_output.json', 'w') as ouput:
    json.dump(results, ouput, indent=4)

for eye in results:
    print(eye)