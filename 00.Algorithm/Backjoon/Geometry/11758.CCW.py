x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())

# 벡터활용 내외적 구분
vec12 = [x2-x1, y2-y1]
vec23 = [x3-x2, y3-y2]
outcal = vec12[0]*vec23[1]-vec12[1]*vec23[0]
if outcal==0:
    print(0)
elif outcal>0:
    print(1)
else:
    print(-1)









# if x1==x2:
#     if x3 < x2:
#         print(-1)
#     else:
#         print(1)
# else:
#     y_bord = y1 + (y1-y2)*(x3-x1)/(x1-x2)
#     deg = (y1-y2)/(x1-x2)
#     if y3 == y_bord:
#         print(0)
#     else:
#         if deg > 0:
#             if y3 < y_bord:
#                 print(-1)
#             else:
#                 print(1)
#         if deg < 0:
#             if y3 < y_bord:
#                 print(1)
#             else:
#                 print(-1)