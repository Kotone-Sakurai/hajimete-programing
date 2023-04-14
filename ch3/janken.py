import random

#これあってもなくても動く
winner = ""


#コンピューター側
#random_choice = random.randint(0, 2)
#if random_choice == 0:
#    computer_choice = "ぐう"
#elif random_choice == 1:
#    computer_choice = "ちょき"
#else:
#    computer_choice = "ぱあ"
#print("the computer choice is ", computer_choice)

#下記のほうが短く書ける   
choices = ['ぐう', 'ちょき', 'ぱあ']
computer_choice = random.choice(choices)
#print("こっちは", computer_choice)

user_choice = ""
while (user_choice != "ぐう" and
       user_choice != "ちょき" and
       user_choice != "ぱあ"):
    user_choice = input("じゃーんけーん？ ")

if computer_choice == user_choice:
    winner = "あいこだね"
elif computer_choice == "ぐう" and user_choice == "ちょき":
    winner = "おれの勝ち。出直してきてください。"
elif computer_choice == "ちょき" and user_choice == "ぱあ":
    winner = "おれの勝ち。出直してきてください。"
elif computer_choice == "ぱあ" and user_choice == "ぐう":
    winner = "おれの勝ち。出直してきてください。"
else:
    winner = "おまえの勝ちかも。"

print(winner)

