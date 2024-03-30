from constants import API
import requests

def get_info(id, api_key):
    url = f'https://api.clashofclans.com/v1/players/%23{id}'
    headers = {'Authorization': f'Bearer {api_key}',
               'cache-control': 'public max-age=600',
               'content-type': 'application/json'}
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        data = res.json()
        return data
    else:
        print(f"Error Status Code: {res.status_code}")
        return None
    
# data = get_info('LP8J2CCC2', API)

# if data:
#     for key, value in data.items():
#         print(f"{key}: {value}")
