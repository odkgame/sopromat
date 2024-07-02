import numpy as np


def RRedFunPl_6(n1, n2):
    # удаление перемещениий на защемл кромке
    # одна кромка жестко защемлена, остальные свободны от связей
    test_tr = 1
    for i in range(1, int(n2) + 1):
        test_tr += 1

    RRed = np.zeros((test_tr, 1))
    j = 1
    RRed[0] = 1
    tr = 1
    for i in range(1, int(n2) + 1):
        RRed[tr] = n1 * j + j + 1
        tr += 1
        j += 1
    return RRed
