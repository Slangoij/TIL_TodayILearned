import sys
import copy
input = sys.stdin.readline

def chkpal(strr, leng):
    if strr[:leng//2] == list(reversed(strr[-(leng//2):])):
        return True
    return False

def chksimpal(strr, leng):
    stt, end, chk = 0, leng-1, False
    while stt<end:
        if strr[stt] != strr[end]:
            if not chk:
                if strr[stt] == strr[end-1] and chkpal(strr[stt:end], leng):
                    end -= 1
                    chk = True
                elif strr[stt+1] == strr[end] and chkpal(strr[stt+1:end+1], leng):
                    stt += 1
                    chk = True
                else:
                    return False
            else:
                return False
        stt += 1
        end -= 1
    return True

for _ in range(int(input())):
    strr = list(input().strip())
    leng = len(strr)
    if chkpal(strr, leng):
        print(0)
    elif chksimpal(strr, leng):
        print(1)
    else:
        print(2)



# # 첫번째 시도: N^2의 복잡도에 100,000길이의 문자열 조회하려니 실패
# def chksimpal(strr, leng):
#     stt,end = 0,leng-1
#     front, back = '',''
#     for skip in range(len(strr)):
#         for i in range(leng//2):
#             if stt == skip:
#                 stt += 1
#             elif end == skip:
#                 end -= 1
#             front += strr[stt]
#             back += strr[end]
#             if front != back:
#                 break
#             stt += 1
#             end -= 1
#         if front == back:
#             return True
#         stt,end = 0,leng-1
#         front, back = '', ''
#     return False
