class Matrix:
    def __init__(self, matrix_string):
        self.matrix_list = [[int(j) for j in i.split()] for i in matrix_string.splitlines()]

    def row(self, index):
        return [i for i in self.matrix_list[index-1]]

    def column(self, index):
        return [i[index-1] for i in self.matrix_list]
