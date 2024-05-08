import numpy as np


# входные параметры:
# RT - блок RT конечного элемента (предполагается, что все КЭ обладают одиноковыми свойствами)
# FE_F - матрица соответствия локальных усилий глобальным
# FE_D - матрица соответствия локальных перемещений глобальным
# m - количество КЭ

def RTG12_4(RT, FE_F, FE_D, m, ):
    # создаем глобальную матрицу rt

    sub_FE_F = FE_F - 1
    sub_FE_D = FE_D - 1
    s1 = int(np.max(FE_F)-2)
    s2 = int(np.max(FE_D)-1)
    RTGl = np.zeros((s2, s1))
    for i in range(m - 1):
        for j in range(4):
            for k in range(8):
                RTGl[int(sub_FE_D[i, j])][int(sub_FE_F[i, k])] += RT[j, k]

    sub_FE_F = None
    sub_FE_D = None
    return RTGl
