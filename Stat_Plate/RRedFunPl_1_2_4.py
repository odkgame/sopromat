import numpy as np


def RRedFunPl_1_2_4(n1, n2):
    # вектор редуцир перемещ по всему контуру пластины
    RRed = np.array([])
    tr = 1
    for i in range(1, n1 + 1):
        RRed[tr] = i
        tr += 1

    for i in range(1, n2 - 1):
        RRed[tr] = i * n1 + i + 1
        tr += 1
        RRed[tr] = i * n1 + n1 + i + 1
        tr += 1

    for i in range(1, n1 + 1):
        RRed[tr] = RRed[tr - 1] + 1
        tr += 1

    return RRed
