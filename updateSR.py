import requests
import json
import pandas as pd


tank_file = '/home/robert/PycharmProjects/overwatch_sr/TankSR_21.csv'
damage_file = '/home/robert/PycharmProjects/overwatch_sr/DamageSR_21.csv'
support_file = '/home/robert/PycharmProjects/overwatch_sr/SupportSR_21.csv'

tank_csv = pd.read_csv(tank_file)
damage_csv = pd.read_csv(damage_file)
support_csv = pd.read_csv(support_file)

tank_sr = tank_csv['tank'].tolist()
damage_sr = damage_csv['damage'].tolist()
support_sr = support_csv['support'].tolist()


response = requests.get('https://ow-api.com/v1/stats/pc/us/SKCwillie-1534/profile')
data = response.json()

for i in data['ratings']:
    print(i['level'])
    if i['role'] == 'tank' and i['level'] != tank_sr[-1]:
        tank_sr.append(i['level'])
    elif i['role'] == 'damage' and i['level'] != damage_sr[-1]:
        damage_sr.append(i['level'])    
    elif i['role'] == 'support' and i['level'] != support_sr[-1]:
        support_sr.append(i['level'])  

print(tank_sr, damage_sr, support_sr)

tank_csv = pd.DataFrame({'tank': tank_sr})
damage_csv = pd.DataFrame({'damage': damage_sr})
support_csv = pd.DataFrame({'support': support_sr})

tank_csv.to_csv(tank_file, index=False)
damage_csv.to_csv(damage_file, index=False)
support_csv.to_csv(support_file, index=False)

print(data)
