import numpy as np


def DTG12_4(DT, FE_F, FE_D, m):
    # создаем глобальную матрицу dt
    sub_FE_F = FE_F - 1
    sub_FE_D = FE_D - 1
    s1 = int(np.max(FE_F))
    s2 = int(np.max(FE_D))
    DTGl = np.zeros((s1, s2))
    t = 0
    for i in range(m):
        for j in range(0, 8):
            for k in range(0, 4):
                DTGl[int(sub_FE_F[i, j]), int(sub_FE_D[i, k])] += DT[j, k]

        t += 4
    sub_FE_F = None
    sub_FE_D = None

    return DTGl
