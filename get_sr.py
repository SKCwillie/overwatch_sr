import requests
import json

user_1 = 'SKCwillie-1534'
user_2 = 'Mcree-11646'
system = 'pc'
country = 'us'


def get_ranks(battletag, platform, region):
    headers = {}
    payload = {}
    url = f'https://ow-api.com/v1/stats/{platform}/{region}/{battletag}/profile'
    response = requests.request('GET', url=url, headers=headers, data=payload)
    response_dict = json.loads(response.text)
    qp_sr = response_dict['rating']
    if qp_sr > 0:
        comp_sr = {'qp': qp_sr}
    try:
        for i in response_dict['ratings']:
            comp_sr[i['role']] = i['level']
        return comp_sr
    except TypeError:
        return 'NaN'


rank = get_ranks(user_1, system, country)
print(rank)
