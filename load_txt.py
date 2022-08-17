import pandas as pd

cols = ['TweetID', 'RetweetCount', 'FavoriteCount']

df = pd.read_fwf('tweet-json.txt', 
                 header=None,widths=[6,5,7,4],
                 names=cols)
print(df)