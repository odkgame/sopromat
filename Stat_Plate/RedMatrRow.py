import numpy as np


# Удаление строк из блоков
def RedMatrRow(Matr, RRed):
    RedMatrR = np.zeros((9,9))
    if RRed[0] != 0:
        n = len(RRed)
        k = 0
        for i in range(0, n):
            Matr[int(RRed[i]) - k] = []
            k += 1

    RedMatrR = Matr
    return RedMatrR
