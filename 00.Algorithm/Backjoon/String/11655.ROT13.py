def tmplamb(x):
    if ord(x) in range(65, 91):
        return (ord(x) - 52) % 26 + 65
    elif ord(x) in range(97, 123):
        return (ord(x) - 84) % 26 + 97
    return ord(x)


print("".join(map(chr, map(tmplamb, list(input())))))
