import numpy as np


def RRedFunPl_6(n1, n2):
    # удаление перемещениий на защемл кромке
    # одна кромка жестко защемлена, остальные свободны от связей
    RRed = np.zeros((5, 1))
    j = 1
    RRed[0] = 1
    tr = 1
    for i in range(1, int(n2) + 1):
        RRed[tr] = n1 * j + j + 1
        tr += 1
        j += 1
    return RRed
