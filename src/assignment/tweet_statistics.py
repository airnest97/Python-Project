from functools import reduce
from statistics import mean

users = [
    {"username": "airnest", "age": 24, "tweets": ["I like food", "I love sleep", "I'm bored"], "verified": True},
    {"username": "walexi", "age": 22, "tweets": [], "verified": False},
    {"username": "funkezi", "age": 26, "tweets": ["on God", "We the best", "Life is good", "Life tough", "Life hard"],
     "verified": True},
    {"username": "sola", "age": 16, "tweets": [], "verified": False},
    {"username": "aura", "age": 21, "tweets": ["Omooooo", "We move", "E choke"], "verified": True},
    {"username": "west", "age": 44, "tweets": ["Thank you"], "verified": True},
    {"username": "kim", "age": 12, "tweets": ["I'm single", "I'm searching"], "verified": False},
    {"username": "willy", "age": 14, "tweets": ["Greatness", "Be yourself", "Be cheerful", "Be gentle"],
     "verified": True},
    {"username": "bisidi", "age": 27, "tweets": [], "verified": False},
    {"username": "shantelli", "age": 29, "tweets": ["I like food", "I love sleep", "Silver"], "verified": False},
]

# USERS WITH VERIFIED USERNAME
print("USERS WITH VERIFIED USERNAME: ", [user["username"] for user in users if user["verified"] is True])

verified_usernames = list(map(lambda x: x["username"] if x["verified"] is True else None, users))
print("USERS WITH VERIFIED USERNAME: ", verified_usernames)

verified_usernames_ = map(lambda y: y['username'], filter(lambda x: x['verified'], users))
print("USERS WITH VERIFIED USERNAME: ", list(verified_usernames_))

verified_usernames_1 = filter(lambda x: x, map(lambda x: x['username'] if x['verified'] else False, users))
print("USERS WITH VERIFIED USERNAME: ", list(verified_usernames_1))


print()
print()


# NAMES OF ACTIVE USERS
print("NAMES OF ACTIVE USERS: ", [user["username"] for user in users if user["tweets"] != []])
active_users = list(map(lambda x: x["username"] if x["tweets"] != [] else None, users))
print("NAMES OF ACTIVE USERS: ", active_users)


print()
print()


# NAMES OF USER BELOW 25 AND VERIFIED
print("NAMES OF USER BELOW 25 AND VERIFIED: ", [user["username"] for user in users if user["age"] < 25 and user["verified"] is True])

verified_below_twenty_five = list(
    map(lambda x: x["username"] if x["age"] < 25 and x["verified"] is True else None, users))
print("NAMES OF USER BELOW 25 AND VERIFIED: ", verified_below_twenty_five)


print()
print()


# MAXIMUM AGE
print("MAXIMUM AGE: ", max(user["age"] for user in users))

maximum_age = reduce(lambda x, y: x if x["age"] > y["age"] else y, users)
print("MAXIMUM AGE: ", maximum_age["age"])


print()
print()


# MINIMUM AGE
print("MINIMUM AGE: ", min(user["age"] for user in users))

minimum_age = reduce(lambda x, y: x if x["age"] < y["age"] else y, users)
print("MINIMUM AGE: ", minimum_age["age"])


print()
print()


# AVERAGE AGE
print("AVERAGE AGE: ", (sum(user["age"] for user in users) / len(users)))

average_age = reduce(lambda x, y: x + y, (user['age'] for user in users)) / len(users)
print("AVERAGE AGE: ", average_age)

print("MEAN AGE: ", mean(user["age"] for user in users))


print()
print()


# ASCENDING ORDER OF NAMES
print("ASCENDING ORDER OF NAMES: ", sorted(users, key=lambda x: x["username"]))


print()
print()


# DESCENDING ORDER OF NAMES
print("DESCENDING ORDER OF NAMES: ", sorted(users, key=lambda x: x["username"], reverse=True))


print()
print()


# ARRANGE USERS IN ASCENDING ORDER USING AGE
print("ARRANGE USERS IN ASCENDING ORDER USING AGE: ", sorted(users, key=lambda x: x["age"]))


print()
print()


# ARRANGE USERS IN DESCENDING ORDER USING AGE
print("ARRANGE USERS IN DESCENDING ORDER USING AGE: ", sorted(users, key=lambda x: x["age"], reverse=True))


print()
print()


# USER WITH LONGEST NAME
longest_name_ = max(users, key=lambda x: len(x["username"]))
print("USER WITH LONGEST NAME: ", longest_name_["username"])

longest_name = reduce(lambda x, y: x if len(x["username"]) > len(y["username"]) else y, users)
print("USER WITH LONGEST NAME: ", longest_name["username"])


print()
print()


# USER WITH THE MOST TWEET
most_tweet_ = max(users, key=lambda x: len(x["tweets"]))
print("USER WITH THE MOST TWEET: ", most_tweet_["username"])
print(most_tweet_["tweets"])

most_tweet = reduce(lambda x, y: x if len(x["tweets"]) > len(y["tweets"]) else y, users)
print("USER WITH THE MOST TWEET: ", most_tweet["username"])
print(most_tweet["tweets"])
