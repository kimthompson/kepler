import json
from pprint import pprint
json_data=open('kepler_objects.json')
data=json.load(json_data)

def star_list():
    stars = []
    for i in range(1, 429):
        if (i != 72) or (i != 73) or (i != 150):
            stars.append(i)
    return stars

stars = star_list();

def star_buckets(star):
    star_bucket = []
    for i in range(0, len(data)):
        if data[i]['Star'] == star:
            star_bucket.append(data[i])
    return star_bucket

all_stars = dict()

for star in stars:
    all_stars[star] = star_buckets(star)

with open('star_buckets.txt', 'w') as outfile:
    json.dump(all_stars, outfile)

# To grab, say, all Kepler-11 objects, type data['11']
# To access the first of those objects, type data['11'][0]
# You get the drift
