import numpy as np


def RRedFunPl_7(n1, n2):
    # удаление перемещений в опрных узлах
    # Шарнирное опирание
    RRed_7 = np.zeros((4, 1))
    RRed_7[0] = 1
    RRed_7[1] = n1 + 1
    RRed_7[2] = n1 * n2 + n1 + 1
    RRed_7[3] = RRed_7[2] + n2

    return RRed_7
