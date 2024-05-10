import numpy as np


def RG12_4(R, FE_D, m):
    # создаем глобальную матрицу r
    s = int(np.max(FE_D))
    RGl = np.zeros((s, s))
    sub_FE_D = FE_D - 1
    for i in range(m):
        for j in range(4):
            for k in range(4):
                RGl[int(sub_FE_D[i, j]), int(sub_FE_D[i, k])] += R[j, k]
    sub_FE_D = None
    return RGl



