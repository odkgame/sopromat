import numpy as np


# создаем локальную матрицу r
def RPl12(a, b, Dk):
    R1 = np.zeros((4, 4))
    R1[0, 0] = 2 * Dk / (a * b)
    R1[0, 1] = -R1[0, 0]
    R1[0, 2] = R1[0, 0]
    R1[0, 3] = -R1[0, 0]
    R1[1, 0] = -R1[0, 0]
    R1[1, 1] = R1[0, 0]
    R1[1, 2] = -R1[0, 0]
    R1[1, 3] = R1[0, 0]
    R1[2, 0] = R1[0, 0]
    R1[2, 1] = -R1[0, 0]
    R1[2, 2] = R1[0, 0]
    R1[2, 3] = -R1[0, 0]
    R1[3, 0] = -R1[0, 0]
    R1[3, 1] = R1[0, 0]
    R1[3, 2] = -R1[0, 0]
    R1[3, 3] = R1[0, 0]

    return R1