import numpy as np
from DelPl12 import DelPl12
# import DG12_4
# import DRedPl_4
# import DRedPl_5
# import DRedPl_6
# import DRedPl_137
# import DTG12_4
from FE_DFun import FE_DFun
from FE_FFun import FE_FFun
# import PGP12_4
from PpPl12_plus import PpPl12_plus
# import RedMatrCol
# import RedMatrRow
from RG12_4 import RG12_4
from RPl12 import RPl12
# import RRedFunPl_1_2_4
# import RRedFunPl_3_5
# import RRedFunPl_6
# import RRedFunPl_7
from RTG12_4 import RTG12_4
from RTildaPl12 import RTildaPl12

# исходные данные надо будет в будущем поменять на автоматическое заполнение, пока сделаю с константами
# исходные данные

c1 = 1
c2 = 1
h = 0.1
E = 1.092E7
Mu = 0.3
MuX = 0.3
MuY = 0.3
D = 1
Dx = 1
Dy = 1
Dk = 0.7
q = 1
n1 = 4
n2 = 4
m = n1 * n2
a = 0.25
b = 0.25

R = RPl12(a, b, Dk)
RT = RTildaPl12(a, b, Dx, Dy, Dk, MuX, MuY)
DT = np.transpose(RT) * (-1)
Del = DelPl12(a, b, Dx, Dy, Dk, MuX, MuY)
Pp = PpPl12_plus(a, b, q)

# задаем матрицу соответств локальных усилий глобальным
FE_D = FE_DFun(m, n1)

# задаем матрицу соответств локальных перемещений глобальным
FE_F = FE_FFun(m, FE_D)

# создаем глобальную матрицу RGl
RGl = RG12_4(R, FE_D, m)

# создаем глобальную матрицу RTGl
RTGl = RTG12_4(RT, FE_F, FE_D, m)
