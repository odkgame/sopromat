import numpy as np


def FE_FFun(m, FE_D):
    # задаем матрицу соответстви¤ локальных усилий глобальным
    FE_F = np.array([])
    t = np.max(FE_D)
    for i in range(1, m):
        FE_F[i, 1] = 2 * FE_D[i, 1] - 1
        FE_F[i, 2] = 2 * FE_D[i, 1]
        FE_F[i, 3] = 2 * FE_D[i, 2] - 1
        FE_F[i, 4] = 2 * FE_D[i, 2]
        FE_F[i, 5] = 2 * FE_D[i, 3] - 1
        FE_F[i, 6] = 2 * FE_D[i, 3]
        FE_F[i, 7] = 2 * FE_D[i, 4] - 1
        FE_F[i, 8] = 2 * FE_D[i, 4]

    return FE_F
