import requests
import json

response = requests.get('https://ow-api.com/v1/stats/pc/us/SKCwillie-1534/profile')
data = response.json()

for dict in data['ratings']:

	print(dict['role'], dict['level'])
