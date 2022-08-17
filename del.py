with open('tweet_json.txt', 'w') as f:
    for i in vars(item).values():
        f.write(f"{i.created_at}\n")