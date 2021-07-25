import requests
import pandas as pd

rank_file = '/home/robert/PycharmProjects/overwatch_sr/sr.csv'
rank_log = pd.read_csv('/home/robert/PycharmProjects/overwatch_sr/sr.csv')

response = requests.get('https://ow-api.com/v1/stats/pc/us/SKCwillie-1534/profile')
data = response.json()

past_tank_sr = rank_log['tank'].iloc[-1]
past_damage_sr = rank_log['damage'].iloc[-1]
past_support_sr = rank_log['support'].iloc[-1]

current_tank_sr = data['ratings'][0]['level']
current_damage_sr = data['ratings'][1]['level']
current_support_sr = data['ratings'][2]['level']

if current_tank_sr != past_tank_sr or current_support_sr != past_support_sr or current_damage_sr != past_damage_sr:
    rank_log.loc[len(rank_log.index)] = [current_tank_sr, current_damage_sr, current_support_sr]

rank_log.to_csv(rank_file, index=False)
