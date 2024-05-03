import numpy as np


# формируем вектор воздейств нагрузок
def PpPl12_plus(a, b, P):
    Pp = np.array([])
    Pp[1, 1] = P * a * b / 4
    Pp[2, 1] = Pp[1, 1]
    Pp[3, 1] = Pp[1, 1]
    Pp[4, 1] = Pp[1, 1]

    return Pp
