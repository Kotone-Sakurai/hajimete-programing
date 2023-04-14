##スコアをソートする
def bubble_sort(scores):
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(0, len(scores)-1):
            if scores[i] > scores[i+1]:
                temp = scores[i]
                scores[i] = scores[i+1]
                scores[i+1] = temp
                swapped = True
    print(scores)

scores = [6, 2, 8, 5, 0, 1, 9, 4]
bubble_sort(scores)


