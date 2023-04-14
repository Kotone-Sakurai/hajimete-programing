##関数内でグローバル変数を使う時
greeting = "Greetings"
def greet_1(name, msg):
    global greeting
    greeting = "Hi"
    print(greeting, name + ".", msg)

greet_1("June", "See you soon!")
print(greeting)


##パラメータとデフォルト値
def greet_2(name, emotion, msg="Hello!"):
    print("Wow", name + ".", msg, emotion)

greet_2("kotone", "lol")


##キーワード引数
greet_2(msg = "How have you been?", name = "Jill", emotion = "thumbs up")
