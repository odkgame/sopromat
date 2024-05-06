import numpy as np


# формируем вектор воздейств нагрузок
def PpPl12_plus(a, b, P):
    Pp = np.zeros((4,1))
    Pp[0, 0] = P * a * b / 4
    Pp[1, 0] = Pp[0, 0]
    Pp[2, 0] = Pp[0, 0]
    Pp[3, 0] = Pp[0, 0]

    return Pp
