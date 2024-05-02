import numpy as np


def DTG12_4(DT, FE_F, FE_D, m):
    # создаем глобальную матрицу dt
    s1 = np.max(FE_F)
    s2 = np.max(FE_D)
    DTGl = np.zeros((s1, s2))
    t = 0
    for i in range(1, m):
        for j in range(1, 8):
            for k in range(1, 4):
                DTGl[int(FE_F[i, j]), int(FE_D[i, k])] += DT[j, k]

            t = t + 4

    return DTGl
