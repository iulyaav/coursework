def matrix_add(X, Y):
    pass

def matrix_multiply(X, Y):
    """
    Let X = | A  B | and Y = | E  F |
            | C  D |         | G  H |

    We have the products:
    P1 = A(F-H)
    P2 = (A+B)H
    P3 = (C+D)E
    P4 = D(G-E)
    P5 = (A+D)(E+H)
    P6 = (B-D)(G+H)
    P7 = (A-C)(E+F)

    Claim: X * Y = | (P5 + P4) - P2 + P6    P1 + P2                |
                   | P3 + P4                (P1 + P5) - (P3 +  P7) |

    Nb - This only supports matrice of nxn where n is even
    """

    if len(X) == len(Y) == 2:
        return [
            [X[0][0]*Y[0][0] + X[0][1]*Y[1][0], X[0][0]*Y[0][1] + X[0][1]*Y[1][1]],
            [X[1][0]*Y[0][0] + X[1][1]*Y[1][0], X[1][0]*Y[0][1] + X[1][1]*Y[1][1]]
            ]


def print_matrix(n):
    tmp = []
    for i in range(n):
        # print("{} row:".format(i+1))
        tmp.append([int(x) for x in input().split(' ')])
    return tmp


if __name__ == "__main__":
    print("Let's multiply matrices of n=")
    n = int(input())
    print("Let's write the first matrix")
    first = print_matrix(n)
    print("Let's write the second matrix")
    second = print_matrix(n)
    print(matrix_multiply(first, second))
