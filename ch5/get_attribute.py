def get_attribute(query, default):
    question = query + default + "? "
    answer = input(question)
    if answer == "":
        answer = default
    print("you choose", answer)
    return answer

hair = get_attribute("髪色は？", "茶色")
eye = get_attribute("目は？", "黒")
