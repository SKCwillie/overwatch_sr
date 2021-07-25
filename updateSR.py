import requests
import pandas as pd
import time
from datetime import datetime


def update_sr():

    SEASON = 29
    COLUMNS = ['date', 'season', 'tank', 'damage', 'support', 'quickplay']
    today = datetime.today().strftime('%m/%d/%y')
    rank_file = '/home/robert/PycharmProjects/overwatch_sr/sr.csv'

    try:
        rank_log = pd.read_csv('/home/robert/PycharmProjects/overwatch_sr/sr.csv')
    except FileNotFoundError:
        rank_log = pd.DataFrame(columns=COLUMNS)

    response = requests.get('https://ow-api.com/v1/stats/pc/us/SKCwillie-1534/profile')
    data = response.json()

    try:
        past_tank_sr = rank_log['tank'].iloc[-1]
        past_damage_sr = rank_log['damage'].iloc[-1]
        past_support_sr = rank_log['support'].iloc[-1]
        past_qp_sr = rank_log['quickplay'].iloc[-1]
    except IndexError:
        past_tank_sr = 0
        past_damage_sr = 0
        past_support_sr = 0
        past_qp_sr = 0
    except KeyError:
        return

    current_tank_sr = data['ratings'][0]['level']
    current_damage_sr = data['ratings'][1]['level']
    current_support_sr = data['ratings'][2]['level']
    current_qp_sr = data['rating']

    if (current_tank_sr != past_tank_sr or
            current_support_sr != past_support_sr or
            current_damage_sr != past_damage_sr or
            current_qp_sr != past_qp_sr):
        try:
            rank_log.loc[len(rank_log.index)] = ([today, SEASON,
                                                  current_tank_sr, current_damage_sr,
                                                  current_support_sr, current_qp_sr])
            print('Updated SR!')
        except ValueError:
            rank_log.loc[0] = [today, SEASON, current_tank_sr, current_damage_sr, current_support_sr, current_qp_sr]
    rank_log.to_csv(rank_file, index=False)


if __name__ == '__main__':
    REPEAT = 5  #every 5 mins
    while True:
        update_sr()
        time.sleep(REPEAT * 60)
