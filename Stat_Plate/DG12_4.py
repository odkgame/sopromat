import numpy as np

#создаем глобальную матрицу d (дельта)
def DG12_4(Del, FE_F, m):
    t = 0
    s = np.max(FE_F)
    DGL = np.zeros((s, s))
    for i in range(1, m):
        for j in range(1, 8):
            for k in range(1, 8):
                DGL[int(FE_F[i, j])][int(FE_F[i, k])] += Del[j, k]
        t += 8

    return DGL
