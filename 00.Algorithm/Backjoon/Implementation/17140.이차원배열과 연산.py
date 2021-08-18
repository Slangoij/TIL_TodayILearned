# 4번째 시도: set변환은 크기순으로 정렬되지 않는다는것을 깨달음
R, C, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

def r_sort(arr):
    n_arr = [i for i in arr if i != 0]
    cntset = {key:0 for key in list(set(n_arr))}
    for i in n_arr:
        cntset[i] += 1
    cntset = sorted(cntset.items(), key=lambda x: (x[1], x[0]))
    cntlst = []
    for key, cnt in cntset:
        cntlst += [key,cnt]
    
    return cntlst[:100]

def opr():
    maxlen = 0
    for i in range(len(A)):
        A[i] = r_sort(A[i])
        maxlen = max(maxlen, len(A[i]))
    for i in range(len(A)):
        A[i] += [0] * (maxlen - len(A[i]))

def main():
    global A, R, C
    R, C = R-1, C-1
    for cnt in range(101):
    # for cnt in range(1000):
        row, col = len(A), len(A[0])
        if R<row and C<col and A[R][C] == K:
            return cnt
        if row >= col:
            opr()
        else:
            A = list(zip(*A))
            opr()
            A = list(zip(*A))
        # if cnt > 998:
        #     pass
    return -1

print(main())


"""

1 2 2
1 2 1
2 1 3
3 3 3

1 4 1
1 1 1
1 1 1
1 1 1

1 2 3
3 2 1
3 2 1
3 2 1

1 2 4
1 2 1
2 1 3
3 3 3

"""
# # 1번쨰 시도: 다른 사람들과의 풀이 차이를 모르겠다.
# def r_sort(arr):
#     arrset = set(arr)
#     cntset = {key:0 for key in arrset if key != 0}
#     for i in arr:
#         if i != 0:
#             cntset[i] += 1
#     cntset = sorted(cntset.items(), key=lambda x: x[1])
#     cntlst = []
#     for key, cnt in cntset:
#         cntlst.extend([key,cnt])
    
#     return cntlst[:100]

# def r_opr():
#     maxlen = 0
#     for i in range(len(A)):
#         A[i] = r_sort(A[i])
#         maxlen = max(maxlen, len(A[i]))
#     for i in range(len(A)):
#         leng = len(A[i])
#         if leng < maxlen:
#             A[i] += [0] * (maxlen - leng)

# def c_opr():
#     cols = [[] for _ in range(len(A[0]))]
#     for i in range(len(A)):
#         for j in range(len(A[i])):
#             cols[j].append(A[i][j])
#     maxlen = 0
#     for i in range(len(cols)):
#         cols[i] = r_sort(cols[i])
#         maxlen = max(maxlen, len(cols[i]))
#     for i in range(len(cols)):
#         leng = len(cols[i])
#         if leng < maxlen:
#             cols[i] += [0] * (maxlen - leng)

#     B = [[] for _ in range(maxlen)]
#     for j in range(len(cols)):
#         for i in range(maxlen):
#             B[i].append(cols[j][i])

#     return B

# cnt = 0
# while True:
#     row, col = len(A), len(A[0])
#     if R<=row and C<=col and A[R-1][C-1] == K:
#         break
#     if cnt > 100:
#         cnt = -1
#         break
#     if row >= col:
#         r_opr()
#     else:
#         A = c_opr()
#     cnt += 1

# print(cnt)




# # 3번째: 타 블로그 참고
# from collections import Counter
# def rc():
#     max_len = 0
#     len_s = len(s)
#     for j in range(len_s):
#         a = [i for i in s[j] if i != 0]
#         a = Counter(a).most_common()
#         a.sort(key = lambda x : (x[1], x[0]))
#         s[j] = []
#         for fi, se in a:
#             s[j].extend([fi,se])
#         max_len = max(len(a), max_len)
#     for j in range(len_s):
#         s[j] += [0] * (max_len - len(s[j]))
#         s[j] = s[j][:100]
# r, c, k = map(int, input().split())
# s = [list(map(int, input().split())) for i in range(3)]
# for i in range(101):
#     try:
#         if s[r - 1][c - 1] == k:
#             print(i)
#             break
#     except: pass
#     if len(s) < len(s[0]):
#         s = list(zip(*s))
#         rc()
#         s = list(zip(*s))
#     else:
#         rc()
# else:
#     print(-1)