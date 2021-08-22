for _ in range(4):
    x1,y1,p1,q1, x2,y2,p2,q2 = map(int, input().split())
    
    if p2<x1 or p1<x2 or q1<y2 or q2<y1:
        print('d')
    elif (p2==x1 or p1==x2) and (q1==y2 or q2==y1):
        print('c')
    elif (p2==x1 or p1==x2) or (q1==y2 or q2==y1):
        print('b')
    else:
        print('a')

    # lft1, lft2 = min(x1,x2), max(x1,x2)
    # rgt1, rgt2 = min(y1,y2), max(y1,y2)
    # lwr1, lwr2 = min(p1,p2), max(p1,p2)
    # upr1, upr2 = min(q1,q2), max(q1,p2)
    
    # if rgt2<lft1 or rgt1<lft2 or upr1<lwr2 or upr2<lwr1:
    #     print('d')
    # elif (rgt2==lft1 or rgt1==lft2) and (upr1==lwr2 or upr2==lwr1):
    #     print('c')
    # elif (rgt2==lft1 or rgt1==lft2) or (upr1==lwr2 or upr2==lwr1):
    #     print('b')
    # else:
    #     print('a')
        
"""

3 10 50 60 100 100 200 300
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600

"""