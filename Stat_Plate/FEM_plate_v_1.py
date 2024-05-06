import numpy as np
from DelPl12 import DelPl12
# import DG12_4
# import DRedPl_4
# import DRedPl_5
# import DRedPl_6
# import DRedPl_137
# import DTG12_4
# import FE_DFun
# import FE_FFun
# import PGP12_4
# import PpPl12_plus
# import RedMatrCol
# import RedMatrRow
# import RG12_4
from RPl12 import RPl12
# import RRedFunPl_1_2_4
# import RRedFunPl_3_5
# import RRedFunPl_6
# import RRedFunPl_7
# import RTG12_4
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
#DT = np.dot([RT])
#Del = DelPl12(a, b, Dx, Dy, Dk, MuX, MuY)
