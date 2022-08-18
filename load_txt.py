import pandas as pd
import json

total_objects = []
total_dict = []
with open("tweet-json.txt") as file:
    for item in file:
        item = item.strip()
        total_objects.append(item)

for item in total_objects:
    pp = json.loads(item)
    r = pp['created_at']
    pr = pp['retweet_count']
    id = pp['id']
    rp = pp['favorite_count']

    my_dict = {"S.No.": [id], "Item":[pr], "Quantity": [rp], "Price": [r]}
    total_dict.append(my_dict)


df = pd.DataFrame.from_dict(total_dict)

print(df)
