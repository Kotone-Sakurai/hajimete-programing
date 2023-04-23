#再帰させる

marbles = [10, 13, 39, 14, 41, 9, 3] 

def recursive_compute_sum(lists):
    #基本ケース
    if len(lists) == 0:
        return 0
    #再帰ケース
    else:
        first = lists[0] #1つめ
        rest = lists[1:] #それ以外
        sums = first + recursive_compute_sum(rest)
        return sums

sums = recursive_compute_sum(marbles)
print('The total is', sums)
