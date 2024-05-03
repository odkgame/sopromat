import numpy as np


def PGP12_4(Pp, FE_D, m):
    # создаем глобальный вектор Pp
    s = np.max(FE_D)
    PGlP = np.zeros((s, 1))
    for i in range(1, m):
        for j in range(1, 4):
            PGlP[FE_D[i, j]] += Pp[j]

    return PGlP
