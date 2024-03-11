import requests
import json
from datetime import *
year, month, day = input('Insert date(YYYY-MM-DD): ').split()
Date = date(int(year), int(month), int(day)).isoformat()
code = input('Insert currency code: ')
N = input('Insert number of last quotations(0 to 255): ')
if int(N) >= 255 or int(N) < 0:
    N = input('Insert number between 0 to 255')
#weekno = datetime.weekday()
#print(weekno)


exchangerate = requests.get("http://api.nbp.pl/api/exchangerates/rates/A/"+code+"/"+Date)
buyask_rate = requests.get("http://api.nbp.pl/api/exchangerates/rates/C/"+code+"/last/"+N)


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(exchangerate.json())
jprint(buyask_rate.json())
