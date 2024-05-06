import numpy as np


# входные параметры:
# RT - блок RT конечного элемента (предполагается, что все КЭ обладают одиноковыми свойствами)
# FE_F - матрица соответствия локальных усилий глобальным
# FE_D - матрица соответствия локальных перемещений глобальным
# m - количество КЭ

def RTG12_4(RT, FE_F, FE_D, m):
    # создаем глобальную матрицу rt

    s1 = np.max(FE_F)
    s2 = np.max(FE_D)
    RTGl = np.zeros(s2, s1)
    for i in range(1, m):
        for j in range(1, 4):
            for k in range(1, 8):
                RTGl[int(FE_D[i, j]), int(FE_F[i, k])] += RT[j, k]

    return RTGl
