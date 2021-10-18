def ucpc():
    strr = input()
    tofind = 'UCPC'
    tmpidx = 0
    for i in tofind:
        idx = strr.find(i, tmpidx)
        if idx < 0 or idx < tmpidx:
            return False
        tmpidx = idx
    return True

if __name__ == '__main__':
    if ucpc():
        print('I love UCPC')
    else:
        print('I hate UCPC')
