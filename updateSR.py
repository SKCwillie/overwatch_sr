import requests
import json
import pandas as pd

tank_csv = pd.read_csv('/home/pi/Dev/workspace/TankSR_21.csv')
damage_csv = pd.read_csv('/home/pi/Dev/workspace/DamageSR_21.csv')
support_csv = pd.read_csv('/home/pi/Dev/workspace/SupportSR_21.csv')

tank_sr = tank_csv['tank'].tolist()
damage_sr = damage_csv['damage'].tolist()
support_sr = support_csv['support'].tolist()


response = requests.get('https://ow-api.com/v1/stats/pc/us/SKCwillie-1534/profile')
data = response.json()

for dict in data['ratings']:
    if dict['role'] == 'tank' and dict['level'] != tank_sr[-1]:
        tank_sr.append(dict['level'])
    elif dict['role'] == 'damage' and dict['level'] != damage_sr[-1]:
        damage_sr.append(dict['level'])    
    elif dict['role'] == 'support' and dict['level'] != support_sr[-1]:
        support_sr.append(dict['level'])  

print(tank_sr, damage_sr, support_sr)

tank_csv = pd.DataFrame({'tank': tank_sr})
damage_csv = pd.DataFrame({'damage': damage_sr})
support_csv = pd.DataFrame({'support': support_sr})

tank_csv.to_csv('/home/pi/Dev/workspace/TankSR_21.csv', index = False)
damage_csv.to_csv('/home/pi/Dev/workspace/DamageSR_21.csv', index = False)
support_csv.to_csv('/home/pi/Dev/workspace/SupportSR_21.csv', index = False)
