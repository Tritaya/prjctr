from random import randint
from faker import Faker
from collections import defaultdict
from pprint import pprint
import csv

nm=''
names = [nm:=Faker().name().split()[0] if not nm in ('Mr.', 'Dr.') 
            else 'Robert' for i in range(5) ]
print(names)

# just a 5 elements list
games_result_ls = names[:]

games = 100
for game in range(games): 
    for i, n in enumerate(names):
        if game == 0:
            d = defaultdict(int)
            d['Player name'] = n 
            d['Score'] += randint(1,10)
            games_result_ls[i] = d
        else:
            games_result_ls[i]['Score'] += randint(1,10)

pprint(games_result_ls)
print(len(games_result_ls))

# for record in games_result_ls:
with open('games.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Player name', 'Score'])
    writer.writeheader()
    writer.writerows(games_result_ls)


# Part 2 - reading from csv, sorting and saving to another csv

with open('games.csv') as f:
    reader = csv.DictReader(f)
    games_read_from_csv = list(reader)

pprint(games_read_from_csv)

# sorting
games_sorted = sorted(games_read_from_csv, key=lambda x: x['Score'], reverse=True)

# renaming
for d in games_sorted:
    d['Highest score'] = d.pop('Score')

pprint(games_sorted)

with open ('high_scores.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Player name', 'Highest score'])
    writer.writeheader()
    writer.writerows(games_sorted)
