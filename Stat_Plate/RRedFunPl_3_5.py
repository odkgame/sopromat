import numpy as np


def RRedFunPl_3_5(n1, n2):
    # вектор редуцир перемещ по противоположным краям пластины

    test_tr = 0
    for i in range(1, n1 + 2):
        test_tr += 1
    s = (n1 + 1) * n2 + 1
    for i in range(s, s + n1 + 1):
        test_tr += 1


    tr = 0
    RRed_3_5 = np.zeros((test_tr, 1))
    for i in range(1, n1+2):
        RRed_3_5[tr] = i
        tr += 1

    s = (n1 + 1) * n2 + 1
    for i in range(s, s + n1 + 1):
        RRed_3_5[tr] = i
        tr += 1

    return RRed_3_5
