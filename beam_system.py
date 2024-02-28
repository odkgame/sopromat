import numpy as np
from decimal import Decimal

from Main import DcosFramework

np.set_printoptions(precision=2, suppress= True)

# DcosFramework = DlRE

E1: int = 2 * 10 ** 4
b: float = 0.1
h: float = 0.1
I1: float = b * (h ** 3) / 12
F1: float = b * h
n: int = 4
E = np.array([])
I = np.array([])
F = np.array([])
p = np.array([])

for i in range(0, n):
    E = np.append(E, E1)
for i in range(0, n):
    I = np.append(I, I1)
for i in range(0, n):
    F = np.append(F, F1)

# for i in range(1, n):
#     p = np.append(E, p1)

# координаты задаются в следующм порядке: x,y начала элемента, x,y конца элемента
KoR = np.array([[0, 0, 0, 2], [0, 2, 2, 2], [0, 0, 2, 2], [2, 2, 2, 0]])

Le = DcosFramework(KoR)


# формируем вектор для формирования delta
def DelR(L, E, I, F) -> np.array:
    d = np.array([L / (E * F), (L ** 3) / (12 * E * I), L / (E * I)])
    return d


# полная dot delta для рамы
# L(i,j) - cos и sin для i-го КЭ, L(i,i) -длина i-го КЭ
def DTRE(L) -> np.array:
    if len(np.shape(L)) == 2:
        r = np.array([[L[0][1], L[0][2], 0, -L[0][1], -L[0][2], 0],
                      [L[0][2], -L[0][1], -L[0][0] / 2, -L[0][2], L[0][1], -L[0][0] / 2],
                      [0, 0, 1, 0, 0, -1]])
    else:
        r = np.array([[L[1], L[2], 0, -L[1], -L[2], 0],
                      [L[2], -L[1], -L[0] / 2, -L[2], L[1], -L[0] / 2],
                      [0, 0, 1, 0, 0, -1]])
    return r


count = 1
W = np.zeros((4, 3))
for i in range(4):
    for j in range(3):
        W[i][j] = count
        count += 1

# задаем матрицу соответствия локальных перемещений глобальным (ее нужно задавать вручную)
S = np.array([[1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9],
              [1, 2, 3, 7, 8, 9], [7, 8, 9, 10, 11, 12]])

W -= 1
S -= 1

b_test = np.array([])
j = 0
for i in range(1, 3 * n, 3):
    b_test = np.append(b_test, DelR(L=Le[j][0], E=E[j], I=I[j], F=F[j]))
    j += 1

B = np.diag(b_test)
B_sub = np.linalg.inv(B)

Rp = np.zeros((3 * n, 12))

Rbl = DTRE(L=Le)
for i in range(4):
    Rbl = DTRE(L=Le[i])
    for t in range(3):
        for k in range(6):
            Rp[int(W[i, t])][int(S[i, k])] += Rbl[t][k]

R = np.array(Rp[:, 3:9])
R_sub = np.array(Rp[:, 11:12])
R = np.concatenate((R, R_sub), axis=1)

C = np.transpose(R * -1)
C1 = C * (-1)
K = np.dot(C1, B_sub)
K = np.dot(K, R)

P1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
P2 = np.array([0, 0, 2 * 10 ^ 4, 10 ^ 5, 0, 0, 0])

P = np.concatenate((P1, P2), axis=0)

R_dot = np.zeros((7, 7))

