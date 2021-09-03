import sys
input = sys.stdin.readline

tree,segtree = [], []

def init(stt,end,node):
    global tree, segtree
    if stt==end:
        segtree[node] = tree[stt]
        return segtree[node]
    mid = (stt+end)/2
    tree[node] = init(stt,mid,node*2) * init(mid+1,end,node*2)
    return tree[node]

def cng(b,c):
    pass
def getsum(b,c):
    pass

def main():
    global tree, segtree
    N,M,K = map(int, input().split())
    tree,segtree = [], [0]*(N+1)
    for _ in range(N):
        tree.append(int(input()))
    for _ in range(M+K):
        a,b,c = map(int,input().split())
        if a == 1:
            cng(b, c)
        elif a == 2:
            getsum(b,c)

main()