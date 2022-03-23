# 리스트의 원소 중 최대값을 찾는 프로그램을 반복문을 사용하지 않고 재귀 함수로 작성
# find maximum element of list 'a' not using loop, using recursive function.
a = [1, 2, 4, 5, 6, 11, 23, 0, 3]

def maximum(list):
    if len(list) == 1:
        return list[0]
    elif list[0] >= list[1]:
        del list[1]
        return maximum(list)
    else:
        del list[0]
        return maximum(list)

print(maximum(a))
