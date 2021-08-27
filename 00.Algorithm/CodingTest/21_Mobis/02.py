import sys  
sys.setrecursionlimit(10**8)

def chk(s):
    if not s or 'a' not in s:
        return False

    if 'b' not in s:
        return True

    # 여기서부턴 둘 다 있는 경우
    if s[0]=='a' or s[-1]=='a':
        s = s.strip('a')
        return chk(s)

    anum = s.count('a')
    bchk = 'b'*anum
    if s[:anum]!=bchk or s[-anum:]!=bchk:
        return False
    else:
        s = s[anum:-anum]
        return chk(s)

def solution(a):
    answer = []
    
    for s in a:
        answer.append(chk(s))
    
    return answer

a = ['bbbb','a',"aaa","abab","bbaa","bababa","bbbabababbbaa","aba"]
a = ["abab","bbaa","bababa","bbbabababbbaa"]
a = ['bbbbbaabbabbb']
# a = ["bbbabababbbaa"]
# a = ["a"]
a = ["baaab"]
print(solution(a))