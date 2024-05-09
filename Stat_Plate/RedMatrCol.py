import numpy as np


# Удаление столбцов из блоков
def RedMatrCol(Matr, TRed):
    RedMatrC = np.zeros((9, 9))
    if TRed[0] != 0:
        n = len(TRed)

        k = 0
        for i in range(0, n):
            Matr[int(TRed[i]) - k] = []
            k += 1

    RedMatrC = Matr

    return RedMatrC
