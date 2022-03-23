# n번째 조화수를 구하는 재귀함수 작 조화수 : Hn = 1 + 1/2 + 1/3 + ... + 1/n
def harmonicnumber(a, s):
    if a == 1:
        return s+1
    else:
        s += 1/a
        return harmonicnumber(a-1, s)

print(harmonicnumber(3,0))