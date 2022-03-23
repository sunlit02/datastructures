# 문자열이 회문인지 검사하는 함수를 리스트 슬라이싱을 사용하지 않고 재귀함수로 작성
char = 'eye'
def palindrome(s):
    if len(s) == 1:
        return True
    elif s[0] == s[-1]:
        sh = s.strip(s[0])
        return palindrome(sh)
    else:
        return False

print(palindrome(char))