from matrix_tool import MatrixTool

matrix = [
    [34, 45, 65, 23, 98],
    [1, -4, 67, -3, -18],
    [23, -5, -1, 94, -25],
    [2, 24, -4, 79, -63],
    [10, 29, 25, 30, -6]
]
matrix_2 = [
    [34, 45, 65, 23, 98],
    [1, -4, 67, -3, -18],
    [23, -5, -1, 94, -25],
    [2, 24, -4, 79, -63],
    [10, 29, 25, 30, -6]

 ]

matrix_tool = MatrixTool(matrix)
matrix_tool_2 = MatrixTool(matrix_2)

print(matrix_tool.geometric_mean_above_diagonal())