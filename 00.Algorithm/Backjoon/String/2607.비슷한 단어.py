from collections import Counter
def sim(a, b):
    word_cnt1, word_cnt2 = Counter(a), Counter(b)
    word_cnt1.subtract(word_cnt2)
    cnt, val_cnt = 0, 0
    for key, val in word_cnt1.items():
        if abs(val) >= 1:
            cnt += 1
            val_cnt += val
        if val > 1 or (cnt > 1 and abs(val_cnt) >= 1):
            return False
    return True
    # summ = sum(map(lambda x: abs(x), word_cnt1.values()))
    # if summ <= 1:
    #     return True
    # return False

if __name__ == "__main__":
    n = int(input())
    word = input()
    ans = 0
    for _ in range(n-1):
        if sim(word, input()):
            ans += 1
    print(ans)

"""
2
dog
doll
"""