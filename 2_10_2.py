#convert sparse matrix to tuple, and convert tuple to sparse matrix 
class SparseMatrix:
    def __init__(self):
        self.matrix = [[0, 3, 0, 2], [8, 0, 4, 0], [0,0,0,5]]
        self.sparse_list = []
        self.convert = []

    def toTuple(self):
        row = count = 0
        for rows in self.matrix:
            col = 0
            for value in rows:
                if value != 0:
                    count += 1
                    self.sparse_list.append((row, col, value))
                col += 1
            row += 1
        height = len(self.matrix)
        width = len(self.matrix[0])
        self.sparse_list.insert(0, (height, width, count))

    def toMatrix(self):
        row_m = self.sparse_list[0][0]
        col_m = self.sparse_list[0][1]
        num = self.sparse_list[0][2]
        for i in range(row_m*col_m):
            self.convert.append(0)
        for j in range(1, num+1):
            self.convert.insert(self.sparse_list[j][0]*col_m + self.sparse_list[j][1], self.sparse_list[j][2])
            self.convert.pop()
        a = 0
        for h in range(len(self.convert)):
            print(self.convert[h], end=" ")
            a +=1
            if a%col_m== 0:
                print(end="\n")

s = SparseMatrix()
s.toTuple()
print(s.sparse_list)
s.toMatrix()
