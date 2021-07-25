import requests
import pandas as pd
from datetime import datetime

SEASON = 29
today = datetime.today().strftime('%m/%d/%y')
rank_file = '/home/robert/PycharmProjects/overwatch_sr/sr.csv'

try:
    rank_log = pd.read_csv('/home/robert/PycharmProjects/overwatch_sr/sr.csv')
except FileNotFoundError:
    rank_log = pd.DataFrame(columns=['date', 'season', 'tank', 'damage', 'support'])


response = requests.get('https://ow-api.com/v1/stats/pc/us/SKCwillie-1534/profile')
data = response.json()

try:
    past_tank_sr = rank_log['tank'].iloc[-1]
    past_damage_sr = rank_log['damage'].iloc[-1]
    past_support_sr = rank_log['support'].iloc[-1]
except IndexError:
    past_tank_sr = 0
    past_damage_sr = 0
    past_support_sr = 0

current_tank_sr = data['ratings'][0]['level']
current_damage_sr = data['ratings'][1]['level']
current_support_sr = data['ratings'][2]['level']

if current_tank_sr != past_tank_sr or current_support_sr != past_support_sr or current_damage_sr != past_damage_sr:
    try:
        rank_log.loc[len(rank_log.index)] = [today, SEASON, current_tank_sr, current_damage_sr, current_support_sr]
    except ValueError:
        rank_log.loc[0] = [today, SEASON, current_tank_sr, current_damage_sr, current_support_sr]
rank_log.to_csv(rank_file, index=False)
