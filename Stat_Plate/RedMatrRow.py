import numpy as np


# Удаление строк из блоков
def RedMatrRow(Matr, RRed):
    RedMatrR = np.array([])
    if RRed[1] != 0:
        n = len(RRed)
    k = 0
    for i in range(1, n):
        Matr[RRed[i] - k] = []
        k += 1

    RedMatrR = Matr
    return RedMatrR
