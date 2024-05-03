import numpy as np


# Удаление столбцов из блоков
def RedMatrCol(Matr, TRed):
    RedMatrC = np.array([])
    if TRed(1) != 0:
        n = len(TRed)

    k = 0
    for i in range(1, n):
        Matr[int(TRed[i]) - k] = []
        k = k + 1

    RedMatrC = Matr

    return RedMatrC
