def drink_me(param):
    msg = "drinking " + param + " glass"
    print(msg)
    param = "empty" ##これなんで必要？
    print(param)

glass = "full"
drink_me(glass)
print("the glass is", glass)

