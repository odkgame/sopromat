import numpy as np
from FE_DFun import FE_DFun


def FE_FFun(m, FE_D):
    # задаем матрицу соответстви¤ локальных усилий глобальным
    FE_F = np.zeros((m, 8))
    t = np.max(FE_D)
    for i in range(0, m):
        FE_F[i, 0] = 2 * FE_D[i, 0] - 1
        FE_F[i, 1] = 2 * FE_D[i, 0]
        FE_F[i, 2] = 2 * FE_D[i, 1] - 1
        FE_F[i, 3] = 2 * FE_D[i, 1]
        FE_F[i, 4] = 2 * FE_D[i, 2] - 1
        FE_F[i, 5] = 2 * FE_D[i, 2]
        FE_F[i, 6] = 2 * FE_D[i, 3] - 1
        FE_F[i, 7] = 2 * FE_D[i, 3]

    return FE_F


F = FE_DFun(16, 4)

print(FE_FFun(16, F))
