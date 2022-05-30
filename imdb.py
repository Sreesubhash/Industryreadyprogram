import csv

# csv fileused id Geeks.csv
filename = "imdb.csv"

# opening the file using "with"
# statement
with open(filename, 'r') as data:
    for line in csv.reader(data):
        print(line)

import csv
data = []
with open('imdb.csv', newline='\n') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for d in reader:
        d['Actors'] = [name.strip() for name in d['Actors'].split(",")]
        d['Genre'] = [genre.strip() for genre in d['Genre'].split(",")]
        data.append(d)

counts = {}
for d in data:
    if d['Director'] not in counts:
        counts[d['Director']] = 1
    else:
        counts[d['Director']] += 1

name, count = max(counts.items(), key=lambda x: x[1])
print(f"Director {name} has done maximum number of movies: {count}")

director_actor_count = {}
for d in data:
    for actor in d["Actors"]:
        combo = (d["Director"], actor)
        if combo not in director_actor_count:
            director_actor_count[combo] = 1
        else:
            director_actor_count[combo] += 1

(director, actor), count = max(director_actor_count.items(), key=lambda x: x[1])
print(f"Combo '{director} - {actor}' has done maximum number of movies count :{count}")

