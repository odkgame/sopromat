import numpy as np
from DelPl12 import DelPl12
from DG12_4 import DG12_4
from DRedPl_4 import DRedPl_4
from DRedPl_5 import DRedPl_5
from DRedPl_6 import DRedPl_6
from DRedPl_137 import DRedPl_137
from DTG12_4 import DTG12_4
from FE_DFun import FE_DFun
from FE_FFun import FE_FFun
from PGP12_4 import PGP12_4
from PpPl12_plus import PpPl12_plus
from RedMatrCol import RedMatrCol
from RedMatrRow import RedMatrRow
from RG12_4 import RG12_4
from RPl12 import RPl12
from RRedFunPl_1_2_4 import RRedFunPl_1_2_4
from RRedFunPl_3_5 import RRedFunPl_3_5
from RRedFunPl_6 import RRedFunPl_6
from RRedFunPl_7 import RRedFunPl_7
from RTG12_4 import RTG12_4
from RTildaPl12 import RTildaPl12

np.set_printoptions(suppress=True, precision=5)

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

# создаем глобальную матрицу DTGl
DTGl = DTG12_4(DT, FE_F, FE_D, m)

# создаем глобальную матрицу DGl
DGl = DG12_4(Del, FE_F, m)

# создаем глобальный вектор Pp
PGlP = PGP12_4(Pp, FE_D, m)

print("Выберите тип граничных условий(номер): ")
print("1. Свободное опирание по контуру ")
print("2. Жесткое защемление по контуру ")
print("3. Две кромки свободно оперты, две остальные свободны от связей ")
print("4. Две кромки свободно оперты, две остальные жестко защемлены ")
print("5. Две кромки жестко защемлены, две остальные свободны от связей ")
print("6. Одна кромка жестко защемлена, остальные свободны от связей ")
print("7. Шарнирное опирание по 4 угловым точкам")
type = int(input())

# Обрабатываем результат выбора
match type:
    case 1:
        # вектор редуцир перемещений
        RRed = RRedFunPl_1_2_4(n1, n2)

        # вектор редуцир усилий
        DRed = DRedPl_137(n1, n2)

        # редуцируем все матрицы и векторы
        RGlR = RedMatrCol(RGl, RRed)
        RGlR = RedMatrRow(RGlR, RRed)
        RTGlR = RedMatrCol(RTGl, DRed)
        RTGlR = RedMatrRow(RTGlR, RRed)
        DTGlR = RedMatrCol(DTGl, RRed)
        DTGlR = RedMatrRow(DTGlR, DRed)
        DGlR = RedMatrCol(DGl, DRed)
        DGlR = RedMatrRow(DGlR, DRed)

        PGPR = RedMatrRow(PGlP, RRed)

    case 2:
        # вектор редуцирования перемещений
        RRed = RRedFunPl_1_2_4(n1, n2)

        # редуцируем все матрицы и веторы
        RGlR = RedMatrCol(RGl, RRed)
        RGlR = RedMatrRow(RGlR, RRed)
        RTGlR = RedMatrRow(RTGl, RRed)
        DTGlR = RedMatrCol(DTGl, RRed)
        DGlR = [DGl]

        PGPR = RedMatrRow(PGlP, RRed)

    case 3:
        # вектор редуцирования перемещений
        RRed = RRedFunPl_3_5(n1, n2)

        # вектор редуцир усилий
        DRed = DRedPl_137(n1, n2)

        # редуцируем все матрицы и векторы
        RGlR = RedMatrCol(RGl, RRed)
        RGlR = RedMatrRow(RGlR, RRed)
        RTGlR = RedMatrCol(RTGl, DRed)

        RTGlR = RedMatrRow(RTGlR, RRed)
        DTGlR = RedMatrCol(DTGl, RRed)
        DTGlR = RedMatrRow(DTGlR, DRed)
        DGlR = RedMatrCol(DGl, DRed)
        DGlR = RedMatrRow(DGlR, DRed)

        PGPR = RedMatrRow(PGlP, RRed)

    case 4:
        # вектор редуцир перемещений
        RRed = RRedFunPl_1_2_4(n1, n2)

        # вектор редуцир усилий
        DRed = DRedPl_4(n1, n2)

        # редуцируем все матрицы и векторы 

        RGlR = RedMatrCol(RGl, RRed)
        RGlR = RedMatrRow(RGlR, RRed)
        RTGlR = RedMatrCol(RTGl, DRed)
        RTGlR = RedMatrRow(RTGlR, RRed)
        DTGlR = RedMatrCol(DTGl, RRed)
        DTGlR = RedMatrRow(DTGlR, DRed)
        DGlR = RedMatrCol(DGl, DRed)
        DGlR = RedMatrRow(DGlR, DRed)

        PGPR = RedMatrRow(PGlP, RRed)

    case 5:

        # вектор редуцир перемещений
        RRed = RRedFunPl_3_5(n1, n2)

        # вектор редуцир усилий
        DRed = DRedPl_5(n1, n2)

        # редуцируем все матрицы и векторы
        RGlR = RedMatrCol(RGl, RRed)
        RGlR = RedMatrRow(RGlR, RRed)
        RTGlR = RedMatrCol(RTGl, DRed)
        RTGlR = RedMatrRow(RTGlR, RRed)
        DTGlR = RedMatrCol(DTGl, RRed)
        DTGlR = RedMatrRow(DTGlR, DRed)
        DGlR = RedMatrCol(DGl, DRed)
        DGlR = RedMatrRow(DGlR, DRed)

        PGPR = RedMatrRow(PGlP, RRed)

    case 6:

        # вектор редуцир перемещений
        RRed = RRedFunPl_6(n1, n2)

        # вектор редуцир усилий
        DRed = DRedPl_6(n1, n2)

        # редуцируем все матрицы и векторы
        RGlR = RedMatrCol(RGl, RRed)
        RGlR = RedMatrRow(RGlR, RRed)
        RTGlR = RedMatrCol(RTGl, DRed)
        RTGlR = RedMatrRow(RTGlR, RRed)
        DTGlR = RedMatrCol(DTGl, RRed)
        DTGlR = RedMatrRow(DTGlR, DRed)
        DGlR = RedMatrCol(DGl, DRed)
        DGlR = RedMatrRow(DGlR, DRed)

        PGPR = RedMatrRow(PGlP, RRed)

    case 7:
        # вектор редуцир перемещений
        RRed = RRedFunPl_7(n1, n2)

        # вектор редуцир усилий
        DRed = DRedPl_137(n1, n2)

        # редуцируем все матрицы и векторы
        RGlR = RedMatrCol(RGl, RRed)
        RGlR = RedMatrRow(RGlR, RRed)
        RTGlR = RedMatrCol(RTGl, DRed)
        RTGlR = RedMatrRow(RTGlR, RRed)
        DTGlR = RedMatrCol(DTGl, RRed)
        DTGlR = RedMatrRow(DTGlR, DRed)
        DGlR = RedMatrCol(DGl, DRed)
        DGlR = RedMatrRow(DGlR, DRed)

        PGPR = RedMatrRow(PGlP, RRed)

PGDR = np.zeros((np.shape(DGlR)[0], 1))

# Формируем глабальную матрицу откликов
MOG_sub1 = np.concatenate((RGlR, RTGlR), axis=1)
MOG_sub2 = np.concatenate((DTGlR, DGlR), axis=1)
MOG = np.concatenate((MOG_sub1, MOG_sub2), axis=0)

PG1 = np.concatenate((PGPR,PGDR), axis=0)


