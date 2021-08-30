D, H, W = map(int, input().split())

sqrx = (D**2)*(H**2)/(H**2+W**2)
sqry = sqrx*(W**2)/H**2
print(int(sqrx**(1/2)), int(sqry**(1/2)))