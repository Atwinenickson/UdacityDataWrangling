import pandas as pd
import json

total_objects = []
with open("tweet-json.txt") as file:
    for item in file:
        item = item.strip()
        total_objects.append(item)

for item in total_objects:
    print(item)



    pp = json.loads(item)
    r = pp['created_at']
    pr = pp['retweet_count']
    id = pp['id']
    rp = pp['favorite_count']
    print(id)
    print('........id......')


    print(pr)
    print('........id......')

    print(rp)
    print('........id......')

    print(r)
    print('........id......')

    my_dict = {"S.No.": [id], "Item":[pr], "Quantity": [rp], "Price": [r]}

    df = pd.DataFrame.from_dict(my_dict)

    print(df)
