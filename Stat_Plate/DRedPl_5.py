import numpy as np


# Гр ус 5
# удаляются нулевые моменты (#Mx по 'левой' и 'правой' кромкам)

def DRedPl_5(n1, n2):
    tr = 1
    DRedPl5 = np.array([])
    for i in range(1, int(n2) - 1):
        DRedPl5[tr] = (i * n1 + i) * 2 + 1
        tr += 1
        DRedPl5[tr] = (i * n1 + n1 + i) * 2 + 1
        tr += 1
    return DRedPl5

