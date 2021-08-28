days = [31,28,31,30,31,30,31,31,30,31,30,31]
totmdays = [0]+[sum(days[:i+1]) for i in range(12)]
wkdays = ['MON','TUE','WED','THU','FRI','SAT','SUN']
x,y = map(int, input().split())
totdays = totmdays[x-1] + y-1
print(wkdays[totdays%7])