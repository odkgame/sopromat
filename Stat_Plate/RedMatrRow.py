import numpy as np


# Удаление строк из блоков
def RedMatrRow(Matr, RRed):
    RedMatrR = np.array([])
    sub_RRed = RRed - 1
    if RRed[0] != 0:
        n = len(RRed)
        k = 0
        for i in range(0, n):
            Matr = np.delete(Matr, [int(sub_RRed[i]) - k], 0)
            k += 1

    RedMatrR = Matr
    sub_RRed = None
    return RedMatrR
