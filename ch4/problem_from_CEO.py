scores = [1, 53, 43, 144, 65, 86, 72, 28, 9, 10]

#,じゃなくて+にすると連結部分にデフォでできちゃう空白を消せるが、同型にする必要がある
#length = len(scores)
#i = 0
#while i < length:
#    print("あと"+str(scores[i])+"回")
#    i = i + 1

#for score in scores:
#    print("あと"+str(score))

max_score = 0
for score in scores:
    if score > max_score:
        max_score = score
print(max_score)

menu = []
menu.append(1)
menu.append(3)
print(menu)

del menu[0]
print(menu)

menu.extend([3, 5, 6])
print(menu)
