import numpy as np

# Гр ус 4
# удаляются нулевые моменты (Mу по 'верхней' и 'нижней' кромкам)
def DRedPl_4(n1, n2):
    DRedPl4 = np.array([])
    for i in range(2, n1+1):
        DRedPl4 = np.append(DRedPl4, (2 * i))

    s = ((n1 + 1) * n2) * 2 + 3
    for i in range(0, n1 - 1):
        # DRedPl_4(tr)=2*i+1
        DRedPl4 = np.append(DRedPl4, s)
        s += 2

    return DRedPl4
