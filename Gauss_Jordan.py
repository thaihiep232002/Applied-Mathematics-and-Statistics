def Row_switch(A, i, j):
    A[i], A[j] = A[j], A[i]
    return A


def Div_row(A, i, alpha):
    m = len(A[0])
    for k in range(m):
        A[i][k] = A[i][k] / alpha


def Row_plus_row(A, i, j, alpha):
    m = len(A[0])
    for k in range(m):
        A[i][k] += A[j][k] * alpha


def Inverse(A):
    """
        Input: Ma trận vuông
        Output: Ma trận nghịch đảo
    """
    n = len(A)
    m = len(A[0])

    A_copy = [[A[i][j] for j in range(m)] for i in range(n)]
    if n != m:
        print("Không phải là ma trận vuông")
        return None
    B = []
    for i in range(n):
        B.append([0 for j in range(n)])
        B[i][i] = 1

    for i in range(n):
        if A_copy[i][i] == 0:
            flag = 0
            for j in range(i + 1, n, 1):
                if A_copy[i][j] != 0:
                    flag = 1
                    Row_switch(B, i, j)
                    Row_switch(A_copy, i, j)
            if flag == 0:
                print("Ma trận không khả nghịch")
                return None
        if A_copy[i][i] != 1:
            Div_row(B, i, A_copy[i][i])
            Div_row(A_copy, i, A_copy[i][i])

        for c in range(n):
            if c != i:
                Row_plus_row(B, c, i, -A_copy[c][i])
                Row_plus_row(A_copy, c, i, -A_copy[c][i])
    return B


def print_matrix(A):
    if A == None:
        print("None")
        return
    n = len(A)
    for i in range(n):
        print(A[i])


if __name__ == "__main__":
    A = Inverse([
        [0, -1, 2],
        [1, -1, -1],
        [1, 1, 1]
    ])
    print_matrix(A)



