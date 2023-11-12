import re
from countries import countries
from collections import defaultdict
from datetime import datetime
import time
import pytz

continents = defaultdict(list)
midnight = defaultdict(list)

# dodowanie do slownika continents, gdzie klucze==kontynenty, values==informacja o krajach w tych kontynentach podana w coutries.py
for country_data in countries:
    continents[list(country_data.values()).__getitem__(2)].append(country_data)

for key in continents.keys():
    print(key)
    lists = continents[key]
    for l in lists:
        for timeZone in list(l.values()).__getitem__(0):
            time = datetime.now(pytz.timezone(timeZone))
            cur_time = str(time).split(' ')[1]
            country = list(l.values()).__getitem__(3)
            s = f'Time in {country} in time zone {timeZone} is {cur_time}'
            print(s)
            midnight[cur_time.split('.')[0]].append(s) # dodawanie do nowego slownika, gdzie klucze==czas, values==info o krajach, ktore aktualnie maja ten czas

sorted_dict = dict(sorted(midnight.items())) # sortowanie odnosnie czasu(od polnocy)

print(' ')
print('POSORTOWANE KRAJE ODNOSNIE POLNOCY')
print(' ')

for key in sorted_dict.keys():
    print(key)
    lists = sorted_dict[key]
    for l in lists:
        print(l)
