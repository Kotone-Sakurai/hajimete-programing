#再帰させると、どんどん問題が小さくなっていく
#7文字の回分→5文字→3文字…みたいに

def is_palindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]: #最初の文字と最後の文字
           return is_palindrome(word[1:-1])
        else:
            return False

words = ['tacocat', 'radar', 'yak', 'rader', 'kayjak']
for word in words:
    print(word, is_palindrome(word))
