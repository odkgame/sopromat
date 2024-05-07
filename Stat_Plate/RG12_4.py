import numpy as np


def RG12_4(R, FE_D, m):
    # создаем глобальную матрицу r

    s = int(np.max(FE_D))
    RGl = np.zeros((s, s))
    for i in range(0, m-1):
        for j in range(0, 4):
            for k in range(0, 4):
                RGl[int(FE_D[i, j]), int(FE_D[i, k])] += R[j, k]

    return RGl



