from collections import Counter
hansoo = input().strip()
cnts = Counter(hansoo)
chk = False
oddlet, ans = '', ''
for letter in cnts:
    if cnts[letter] % 2 == 1:
        if not oddlet:
            oddlet = letter
        else:
            print( "I'm Sorry Hansoo")
            chk = True
            break
    ans += letter * (cnts[letter]//2)

if not chk:
    print("".join(sorted(list(ans))) + oddlet*(cnts[oddlet]%2) + "".join(sorted(list(ans), reverse=True)))