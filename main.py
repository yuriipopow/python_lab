
matrix = [
    [34, 45, 65, 23, 98],
    [1, -4, 67, -3, -18],
    [23, -5, -1, 94, -25],
    [2, 24, -4, 79, -63],
    [10, 29, 25, 30, -6]
]


def insertion_sort_columnwise(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for col in range(cols):
        for i in range(1, rows):
            key = matrix[i][col]
            j = i - 1
            while j >= 0 and matrix[j][col] > key:
                matrix[j + 1][col] = matrix[j][col]
                j -= 1
            matrix[j + 1][col] = key
    return matrix


def geometric_mean_above_diagonal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    geo_means = []

    for i in range(rows):
        above_diag = [matrix[i][j] for j in range(i + 1, cols)]
        print(above_diag)
        if above_diag:
            # Calculate geometric mean
            product = 1
            count = 0
            for num in above_diag:
                if num > 0:  # Only include positive numbers for the geometric mean
                    product *= num
                    count += 1
            if count > 0:
                geo_mean = product ** (1 / count)
            else:
                geo_mean = 0
            geo_means.append(geo_mean)
        else:
            geo_means.append(0)

    return geo_means, sum(geo_means)


sorted_matrix = insertion_sort_columnwise([row[:] for row in matrix])  # Make a copy of the matrix
print("Matrix after sorting columns:")
for row in sorted_matrix:
    print(row)
print()
geo_means, geo_means_sum = geometric_mean_above_diagonal(sorted_matrix)
print("\nGeometric means above the diagonal (per row):", geo_means)
print("Sum of geometric means:", geo_means_sum)