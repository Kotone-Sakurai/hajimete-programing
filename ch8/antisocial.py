#最も友達の少ない人を探す

#連想配列にユーザーデータを格納
users = {} 
users['Kim'] = {'email' : 'kim@oreilly.com','gender': 'f', 'age': 27, 'friends': ['John', 'Josh']}
users['John'] = {'email' : 'john@abc.com','gender': 'm', 'age': 24, 'friends': ['Kim', 'Josh']}
users['Josh'] = {'email' : 'josh@wickedlysmart.com','gender': 'm', 'age': 32, 'friends': ['Kim']}

max_value = 1000
for name in users:
   user = users[name]
   friends = user['friends']
   if len(friends) < max_value:
       most_anti_social = name
       max_value = len(friends)

print('The most anti-social is', most_anti_social)
