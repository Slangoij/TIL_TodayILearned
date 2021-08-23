import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1,y1,x2,y2 = map(int,input().split())
    answer = 0
    n = int(input())
    for _ in range(n):
        cx,cy,r = map(int,input().split())
        in1 = (x1-cx)**2 + (y1-cy)**2 - r**2 > 0
        in2 = (x2-cx)**2 + (y2-cy)**2 - r**2 > 0
        if in1 != in2:
            answer += 1
    print(answer)