import numpy as np


def FE_DFun(m, n1):
    # задаем матрицу соответстви¤ локальных перемещений глобальным
    td = 1
    s = 0
    FE_D = np.zeros((m, n1))
    for i in range(m):

        FE_D[i, 0] = i + td
        FE_D[i, 1] = i + td + 1
        FE_D[i, 2] = n1 + 2 + i + td
        FE_D[i, 3] = n1 + 1 + i + td

        s += 1
        if s == n1:
            td += 1
            s = 0

    return FE_D



