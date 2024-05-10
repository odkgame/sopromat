import numpy as np


# Удаление столбцов из блоков
def RedMatrCol(Matr, TRed):
    sub_TRed = TRed - 1
    RedMatrC = np.array([])
    if TRed[0] != 0:
        n = len(TRed)
        k = 0
        for i in range(0, n):
            Matr = np.delete(Matr, [int(sub_TRed[i]) - k], 1)
            k += 1

    RedMatrC = Matr
    sub_TRed = None
    return RedMatrC
