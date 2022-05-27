# 이진 탐색 트리 25
# 프로그램 12.3 에 다음 기능 추가
# 기존 코드는 삭제 노드를 왼쪽 서브 트리의 최대값으로 대체하고 있음.
# 노드를 삭제할 때, 왼쪽 서브트리의 최대값과 오른쪽 서브트리의 최소값를 선택하고 이 중 전체 트리의 높이가 낮아지는 것을 대체 노드로 선택한다.
# (높이가 동일할 경우 왼쪽 서브 트리의 노드 선택)
# 대체 노드를 이동하면 또다른 삭제 연산이 재귀적으로 발생하며 이를 처리

#교재 코드
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.tree = None
        self.temp = None
        self.prev = None
        self.direction = None

    def insert(self, item):
        node = Node(item)
        if not self.tree:
            self.tree = node
        else:
            temp = self.tree
            prev = None
            while True:
                prev = temp
                if item < prev.data:
                    temp = temp.left
                    if not temp:
                        prev.left = node
                        return
                elif item > prev.data:
                    temp = temp.right
                    if not temp:
                        prev.right = node
                        return
                else: return

    def delete_node(self, node, item):
        if node is None:
            return None
        if node.data > item:
            node.left = self.delete_node(node.left, item)
            return node     # 변경된 전체 트리 반환
        elif node.data < item:
            node.right = self.delete_node(node.right, item)
            return node     # 변경된 전체 트리 반환
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            elif node.left is None and node.right is None:
                return None
            else:
                left_max = self.find_max(node.left)   # max in left ST
                right_min = self.find_min(node.right)     # min in right ST
                if left_max.data <= right_min.data:
                    node.data = left_max.data
                    node.left = self.delete_node(node.left, left_max.data)
                else:
                    node.data = right_min.data
                    node.right = self.delete_node(node.left, right_min.data)
                return node

    def find_delete(self, item):
        self.tree = self.delete_node(self.tree, item)     # 변경된 트리 업데이트

    def find(self, root, item):
        if not root: return None
        if root.data == item: return root
        else:
            node1 = self.find(root.left, item)
            if node1: return node1
            node2 = self.find(root.right, item)
            if node2: return node1
            return None

    def height_node(self, root, item):   # 노드의 높이 구하기
        node = self.find(root, item)
        if node: return self.height(node)
        else: return None

    def height(self, root):   # 트리의 높이 구하기
        if not root: return 0
        if root.left:
            l_height = 1 + self.height(root.left)
        else: l_height = 0
        if root.right:
            r_height = 1 + self.height(root.right)
        else: r_height = 0;

        if l_height >= r_height: return l_height
        else: return r_height

    def find_max(self, root):
        if not root: return None
        node = root
        while node.right:
            node = node.right
        return node

    def find_min(self, root):
        if not root: return None
        node = root
        while node.left:
            node = node.left
        return node

    def postorder(self, ptr):
        if ptr:
            self.postorder(ptr.left)
            self.postorder(ptr.right)
            print(ptr.data, end=' ')


bst = BST()
for i in [30, 20, 10, 40, 60, 50, 25]:
    bst.insert(i)
    bst.postorder(bst.tree)
    print()
print()
for i in [30, 25, 40, 50, 20, 60]:
    bst.find_delete(i)
    bst.postorder(bst.tree)
    print()
