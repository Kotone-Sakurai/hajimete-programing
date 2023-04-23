#エラーの際の例外処理をあらかじめ書く

try:
    num = input('数字は? ')
    result = 42 / int(num)
except ZeroDivisionError: #例外時
    print("割り切れないよ！")
except ValueError: #例外時
    print("数字を聞いてるんだよ")
else: #うまくいった時
    print('Your answer is', result)
finally:
    print('Thanks for stopping by.')
