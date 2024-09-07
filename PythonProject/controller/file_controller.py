from PythonProject.model.matrix import MatrixModel
from PythonProject.model.operation_model import OperationsModel


class FileController:
    @staticmethod
    def read_file(file: str):
        with open(file, 'r') as file:
            for i, linha in enumerate(file):
                if i == 0:
                    matrix = MatrixModel(int(linha))
                if i <= matrix.n and i != 0:
                    column = [float(valor) for valor in linha.split(" ")]
                    matrix.define_column(i - 1, column)
                if i > matrix.n:
                    print("antes da operação")
                    matrix.print()
                    items = [float(valor) for valor in linha.split(" ")]
                    op = OperationsModel(items)
                    op.print()
                    matrix.execute_operation(op)
                    print("após a operação")
                    matrix.print()
