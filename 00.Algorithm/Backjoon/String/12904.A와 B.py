def sol(S, T):
    while len(S) < len(T):
        if T[-1] == 'A':
            T.pop()
        elif T[-1] == 'B':
            T.pop()
            T = T[::-1]
        else:
            return 0
    if T == S:
        return 1
    else:
        return 0

if __name__ == "__main__":
    S = list(input().strip())
    T = list(input().strip())
    print(sol(S, T))
