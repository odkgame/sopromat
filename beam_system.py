import numpy as np
from decimal import Decimal

from Main import DcosFramework

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
    r = np.array([[L[0][1], L[0][2], 0, -L[0][1], -L[0][2], 0],
                  [L[0][2], -L[0][1], -L[0][0] / 2, -L[0][2], L[0][1], -L[0][0] / 2],
                  [0, 0, 1, 0, 0, -1]])
    return r


j = 0
W = np.zeros((n, n))
for i in range(1, 3 * n, 3):
    W[j, 0] = j + 1
    W[j, 1] = i
    W[j, 2] = i + 1
    W[j, 3] = i + 2
    j = j + 1

# задаем матрицу соответствия локальных перемещений глобальным (ее нужно задавать вручную)
S = np.array([[1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9],
              [1, 2, 3, 7, 8, 9], [7, 8, 9, 10, 11, 12]])

b_test = np.array([])
j = 0
for i in range(1, 3 * n, 3):
    b_test = np.append(b_test, DelR(L=Le[j][0], E=E[j], I=I[j], F=F[j]))
    j += 1

B = np.diag(b_test)
B_sub = np.linalg.inv(B)

Rp = np.zeros((3 * n, 12))

for i in range(0, n - 1):
    Rbl = DTRE(L=Le)
    for t in range(0, 3):
        for k in range(0, 6):
            Rp[int(W[i, t])][int(S[i, k])] = Rp[int(W[i, t])][int(S[i][k])] + Rbl[t][k]

R = [Rp[:, 4:9], Rp[:, 11]]

print(R)
