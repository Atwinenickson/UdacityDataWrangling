import pandas as pd
import json

total_objects = []
total_dict = []
with open("tweet-json.txt") as file:
    for item in file:
        item = item.strip()
        total_objects.append(item)

for item in total_objects:
    list_items = json.loads(item)
    created_at = list_items['created_at']
    retweet_count = list_items['retweet_count']
    id = list_items['id']
    favorite_count = list_items['favorite_count']

    my_dict = {"TWEETID": [id], "RETWEETCOUNT":[retweet_count], "FAVOURITECOUNT": [favorite_count], "DATECREATED": [created_at]}
    total_dict.append(my_dict)


df = pd.DataFrame.from_dict(total_dict)

print(df)
