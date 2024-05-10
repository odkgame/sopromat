import numpy as np


def PGP12_4(Pp, FE_D, m):
    # создаем глобальный вектор Pp
    sub_FE_D = FE_D - 1
    s = int(np.max(FE_D))
    PGlP = np.zeros((s, 1))
    for i in range(0, m):
        for j in range(0, 4):
            PGlP[int(sub_FE_D[i, j])] += Pp[j]

    sub_FE_D = None
    return PGlP
