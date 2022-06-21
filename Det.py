def sub(matrix, row, col):
    n = len(matrix)
    res = [[matrix[i][j] for j in range(n)] for i in range(n)]
    res.pop(row)
    for i in range(len(res)):
        res[i].pop(col)
    return res


def Det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    res = 0
    for i in range(len(matrix[0])):
        res += matrix[0][i] * pow(-1, 0 + i) * Det(sub(matrix, 0, i))
        return res


if __name__ == "__main__":
    print(Det([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 3],
    ]))
