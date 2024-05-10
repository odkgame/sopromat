import numpy as np

#создаем глобальную матрицу d (дельта)
def DG12_4(Del, FE_F, m):
    t = 0
    sub_FE_F = FE_F - 1
    s = int(np.max(FE_F))
    DGL = np.zeros((s, s))
    for i in range(0, m):
        for j in range(0, 8):
            for k in range(0, 8):
                DGL[int(sub_FE_F[i, j])][int(sub_FE_F[i, k])] += Del[j, k]
        t += 8

    sub_FE_F = None
    return DGL
