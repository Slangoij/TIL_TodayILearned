import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dnas = [{'A':0, 'C':0, 'G':0, 'T':0} for _ in range(m)]
for _ in range(n):
    dna = input().strip()
    for i in range(m):
        dnas[i][dna[i]] += 1
ans,ansdna = 0,''
for i in range(m):
    nowdna = sorted(list(dnas[i].items()), key=lambda x:(-x[1],x[0]))
    for j in range(1,4):
        ans += nowdna[j][1]
    ansdna += nowdna[0][0]
print(ansdna,ans,sep='\n')
