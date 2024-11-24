from typing import List

def sort(func):
    def wrapper(self, *args, **kwargs):
        self.insertion_sort_columnwise()
        return func(self, *args, **kwargs)
    return wrapper

class MatrixTool:
    def __init__(self, matrix: List[List[int]]):
        self.__matrix = matrix

    def insertion_sort_columnwise(self,) -> List[List[int]]:

        rows = len(self.__matrix)
        cols = len(self.__matrix[0])

        for col in range(cols):
            for i in range(1, rows):
                key = self.__matrix[i][col]
                j = i - 1
                while j >= 0 and self.__matrix[j][col] > key:
                    self.__matrix[j + 1][col] = self.__matrix[j][col]
                    j -= 1
                self.__matrix[j + 1][col] = key
        return self.__matrix

    @sort
    def geometric_mean_above_diagonal(self):
        rows = len(self.__matrix)
        cols = len(self.__matrix[0])
        geo_means = []

        for i in range(rows):
            above_diag = [self.__matrix[i][j] for j in range(i + 1, cols)]
            if above_diag:
                product = 1
                count = 0
                for num in above_diag:
                    if num > 0:
                        product *= num
                        count += 1
                geo_mean = product ** (1 / count) if count > 0 else 0
                geo_means.append(geo_mean)
            else:
                geo_means.append(0)

        return geo_means, sum(geo_means)

    def __add__(self, other: List[List[int]]) -> List[List[int]]:
        other = other.__matrix

        result = []
        for i in range(len(self.__matrix)):
            row = []
            for j in range(len(self.__matrix[i])):
                row.append(self.__matrix[i][j] + other[i][j])
            result.append(row)

        return result

    def __mul__(self, other):
        other = other.__matrix

        result = []
        for i in range(len(self.__matrix)):
            row = []
            for j in range(len(other[0])):
                cell_sum = 0
                for k in range(len(other)):
                    cell_sum += self.__matrix[i][k] * other[k][j]
                row.append(cell_sum)
            result.append(row)

        return result