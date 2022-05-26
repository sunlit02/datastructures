# prime 최소 비용 신장 트리 구현 25점
# 시작 노드를 사용자로부터 입력 받음
# 신장 트리에 간선이 추가되는 순서대로 출력
# 교재 238 페이지 문제 3의 그래프를 생성하여 코드 테스트

class Node:
    def __init__(self, value):
        self.data = value


class Graph:
    def __init__(self):
        self.graph = {}
        self.v_list = []
        self.total = 0

    def create(self, v, data, weight):   # 인접리스트 graph[v]에 node 추가
        node = Node(data)
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append((node, weight))

    def sort_edge(self, network):   # 간선 비용으로 오름차순 정렬
        temp = []
        for v1, v2, cost in network:
            temp.append((cost, v1, v2))
        temp.sort()
        return temp

    def prim(self):
        temp = int(input("Starting Node : "))   # 시작 노드를 입력받음
        self.v_list.append(temp)
        print('set list =', self.v_list)
        sort_network = self.sort_edge(network)
        print('cost sorted (cost,v1,v2)', sort_network)
        numlist = []
        for v1, v2, cost in network:
            if v1 not in numlist:
                numlist.append(v1)
            if v2 not in numlist:
                numlist.append(v2)

        while True:
            if len(self.v_list) == len(numlist):
                break
            templ = []
            for cost, v1, v2 in sort_network:
                if v1 in self.v_list and v2 in self.v_list:    # 같은 집합에 있다면 사이클을 형성하므로 추가하지 않고 넘어감
                    # print("the same set. rejected for cycle")
                    continue
                for i in self.v_list:
                    if i == v1:
                        templ.append((cost, v2, v1))
                    elif i == v2:
                        templ.append((cost, v1, v2))

            templ.sort()
            print()
            print("connected edge (cost, v1, v2)", templ)

            self.v_list.append(templ[0][1])
            self.total += templ[0][0]
            print(self.v_list)


g = Graph()
network = [(1,2,5), (1,4,3), (2,5,10), (4,5,6), (3,5,8), (4,6,7), (3,7,11), (5,7,13), (6,7,15)]

for v, node, weight in network:
    g.create(v, node, weight)

print('network =', network)
g.prim()
print()
print('Spanning tree vertices = ', g.v_list)
print('cost total = ', g.total)
