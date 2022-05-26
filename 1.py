import random  # 주사위를 굴리는데 필요


class Node:  # 노드 생성
    def __init__(self, item):
        self.data = item
        self.rlink = None
        self.llink = None


class Linkedlist:
    def __init__(self):  # 빈 순환 연결 리스트 생성
        self.first = None
        self.last = None

    def find(self, item):
        temp = self.first
        for i in range(16):  # 연결리스트의 노드 수가 16으로 고정되어 있으므로 16번 반복
            if temp.data == item:
                return temp
            temp = temp.rlink
        return None

    def view(self):
        temp = self.first
        print("[", end=" ")
        for i in range(16):
            print(temp.data, end=" ")
            temp = temp.rlink
        print("]", end=" ")
        print()

    def add(self, item):
        node = Node(item)
        if self.first is None:  # 빈 연결리스트라면 처음 노드가 시작이자 끝이 됨
            self.first = node
            self.last = self.first
        else:  # 기존 노드 뒤에 노드를 추가하는 코드
            node.llink = self.last
            node.rlink = self.first
            self.last.rlink = node
            self.last = self.last.rlink
            self.first.llink = self.last

    def reverse(self):  # 진행방향 뒤집기
        return -1

    def change(self):  # 말의 위치 교환
        temp1 = self.find(1)
        temp2 = self.find(2)
        temp1.data = 2
        temp2.data = 1

    def back(self, item, d):  # 뒤로 한 칸 이동
        temp = self.find(item)
        temp.data = 0
        if d == 1:  # 진행방향이 정방향이라면
            temp = temp.llink  # 왼쪽으로 한 칸 이동
        elif d == -1:  # 진행방향이 역방향이라면
            temp = temp.rlink  # 오른쪽으로 한 칸 이동
        temp.data = item
        if self.find(3 - item) is None:  # 만약 말이 이동해서 다른 말을 잡았다면 연결리스트에 다른 말의 값을 갖는 노드가 없을 것
            raise  # 이 점을 이용해 검사하여 만약 다른 말을 잡아 다른 노드가 없다면 오류 발생 후 except 문으로 넘어감

    def move(self, item, d, r):  # 주사위 눈 수의 합 만큼 말 이동
        temp = self.find(item)
        temp.data = 0
        if d == 1:  # 진행방향이 정방향이라면
            for i in range(r):  # rlink를 타고 이동
                temp = temp.rlink
        elif d == -1:
            for i in range(r):  # 진행방향이 역방향이라면
                temp = temp.llink  # llink를 타고 이동
        temp.data = item
        if self.find(3 - item) is None:
            raise  # 말이 다른 말은 잡았는지 검사


def dice(a, b):
    if (a, b) == (6, 6):
        return 0
    elif (a, b) == (5, 5):
        return 1
    elif (a, b) == (1, 1):
        return -1
    else:
        return a + b


l = Linkedlist()  # 초기값 설정
for item in [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]:
    l.add(item)

try:
    count = 0
    player = 0
    direction = 1  # 1 이면 시계방향 이동, -1 이면 반시계방향 이동
    print("Game start!")
    print("player 초기 위치")
    l.view()

    while True:
        (a, b) = (random.randint(1, 6), random.randint(1, 6))  # 1번 주사위, 2번 주사위 굴리기
        roll = dice(a, b)
        count += 1  # 횟수가 홀수면 p1, 짝수면 p2
        if count % 2 == 1:
            player = 1
        elif count % 2 == 0:
            player = 2

        if roll == 0:
            print_text = "이동방향 전환"
            direction *= l.reverse()  # 1 이면 시계방향 이동, -1 이면 반시계방향 이동
            print(player, (a, b), print_text)
        elif roll == 1:
            print_text = "말의 위치 교환"
            l.change()
            print(player, (a, b), print_text)
            l.view()
        elif roll == -1:
            print_text = "뒤로 한칸"
            l.back(player, direction)
            print(player, (a, b), print_text)
            l.view()
        else:
            print_text = str(roll) + "칸 전진"
            l.move(player, direction, roll)
            print(player, (a, b), print_text)
            l.view()

except:
    print(player, (a, b), print_text)
    print("%d player won!" % player)
