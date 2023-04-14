##文章の読みやすさをスコア化する


##同じディレクトリ内にないとだめっぽい
import ch1text


##total_syllablesを数える
def count_syllables(words):
    count = 0
    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count
    return count


##音節数をヒューリスティックで求める
def count_syllables_in_word(word):
    count = 0

    ##末尾が記号の単語に考慮
    endings = ".,;?!:"
    last_char = word[-1]
    if last_char in endings:
        processed_word = word[0:-1] ##スライス：文字列の部分切り取り
    else:
        processed_word = word

    ##単語が3文字以下なら1音節
    if len(processed_word) <= 3:
        return 1

    ##末尾がeのものを排除
    ##これ一個上のifより前になきゃダメじゃね？
    if processed_word[-1] in "eE":
        processed_word = processed_word[0:-1]

    ##4文字以上なら母音の数を音節数としてカウント
    vowels = "aeiouAEIOU"
    prev_char_was_vowel = False
    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:
                count = count + 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False ##ここよくわからん

    ##末尾がyなら音節数を1追加
    if processed_word[-1] in "yY":
        count = count + 1

    return count


##total_sentencesを数える
def count_sentences(text):
    count = 0
    terminals = ".;?!"
    for char in text:
        ##inを使った方が簡潔
        ##if char == "." or char == ";" or char == "?" or char == "!":
        if char in terminals:     
            count = count + 1
    return count

##scoreをgradeに変換
def output_results(score):
    if score >= 90:
        print('Reading level of 5th Grade')
    elif score >= 80:
        print('Reading level of 6th Grade')
    elif score >= 70:
        print('Reading level of 7th Grade')
    elif score >= 60:
        print('Reading level of 8-9th Grade')
    elif score >= 50:
        print('Reading level of 10-12th Grade')
    elif score >= 30:
        print('Reading level of College Student')
    else:
        print('Reading level of College Graduate')


def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    ##total_wordsを数える
    words  = text.split()
    total_words = len(words)
    
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)

    ##scoreの計算式
    ##なんでこの公式なのかはoreilyにもわからないらしい
    score = (206.835
             - 1.015 * (total_words / total_sentences)
             - 84.6 * (total_syllables / total_words))
    
##    print(total_words, "words")
##    print(total_sentences, "sentences")
##    print(total_syllables, "syllables")
##    print(score, "reading ease score")
    output_results(score)

##実際の呼び出しはここだけ！
compute_readability(ch1text.text)
