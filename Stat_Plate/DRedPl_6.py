import numpy as np


# Гр ус 6
# удаляются нулевые моменты (Mу по 'верхней' и 'нижней' кромкам
# Mx по 'правой' кромке)
def DRedPl_6(n1, n2):
    DRedPl6 = np.array([])
    tr = 1
    for i in range(1, n1 - 1):
        DRedPl6[tr] = 2 * i + 2
        tr += 1

    for i in range(1, n2 - 1):
        DRedPl6[tr] = (i * n1 + n1 + i) * 2 + 1
        tr += 1

    s = (n1 + 1) * 2 * n2 + 4
    for i in range(1, n1 - 1):
        DRedPl6[tr] = s
        tr += 1
        s += 2

    return DRedPl6
