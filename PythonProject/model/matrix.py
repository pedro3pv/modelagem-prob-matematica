from model.operation_model import OperationsModel


# Created by Pedro Augusto on 07/09/24.

class MatrixModel(list):
    def __init__(self, n: int):
        super().__init__()
        self.n = n
        self.__make_matrix__()

    def __make_matrix__(self):
        column = []
        for i in range(0, self.n):
            column.append(0)
        for i in range(0, self.n):
            self.append(column)

    def define_column(self, i: int, column: list):
        self[i] = column

    def execute_operation(self, op: OperationsModel):
        if op.operation == 1:
            self.__change_line__(int(op.entries[0]), int(op.entries[1]))
        if op.operation == 2:
            self.__multiplication__(int(op.entries[0]), op.entries[1])
        if op.operation == 3:
            self.__SumMultiplication__(int(op.entries[0]), int(op.entries[1]), op.entries[2])

    def __change_line__(self, i: int, j: int):
        x = self[i]
        self[i] = self[j]
        self[j] = x

    def __multiplication__(self, i: int, k):
        column = []
        for item in self[i]:
            item = round(item * k, 2)
            column.append(item)
        self[i] = column

    def __SumMultiplication__(self, i: int, j: int, k):
        column = []
        for item in self[i]:
            item = round(item * k, 2)
            column.append(item)
        for i, item in enumerate(column):
            self[j][i] += item

    def print(self):
        print("Matriz:")
        for i, column in enumerate(self):
            print(f"{i}: {column}")
