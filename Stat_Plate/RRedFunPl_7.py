import numpy as np


def RRedFunPl_7(n1, n2):
    # удаление перемещений в опрных узлах
    # Шарнирное опирание
    RRed_7 = np.array([])
    RRed_7[1] = 1
    RRed_7[2] = n1 + 1
    RRed_7[3] = n1 * n2 + n1 + 1
    RRed_7[4] = RRed_7[3] + n2

    return RRed_7
