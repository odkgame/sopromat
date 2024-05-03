import numpy as np


def RG12_4(R, FE_D, m):
    # создаем глобальную матрицу r
    s = np.max(FE_D)
    RGl = np.zeros((s, s))
    for i in range(1, m):
        for j in range(1, m):
            for k in range(1, m):
                RGl[int(FE_D[i, j]), int(FE_D[i, k])] += R[j, k]

    return RGl
