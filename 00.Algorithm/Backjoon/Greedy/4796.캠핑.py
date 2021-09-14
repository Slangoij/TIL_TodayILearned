import sys
input = sys.stdin.readline

i = 1
L,P,V = map(int, input().split())
while L!=0 or P!=0 or V!=0:
    print(f"Case {i}: {(V // P) * L + min((V % P), L)}")
    i += 1
    L,P,V = map(int, input().split())