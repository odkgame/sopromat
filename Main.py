
import numpy as np
from decimal import Decimal
import math

print("Введите а")
a = float(input())
KoR = np.array(
    [[0, 0, a, 0]])

Rf = np.array([[100], [0], [0], [0], [0], [0]])
print('Вектор нагружения=', '\n', Rf)

print("Матрица KoR = ", "\n", KoR)


def DcosFramework(kor) -> np.ndarray:
    n, m = np.shape(kor)
    Le = np.zeros((n, 3))
    for i in range(0, n):
        Le[i][0] = math.sqrt((kor[i][2] - kor[i][0]) ** 2 + (kor[i][3] - kor[i][1]) ** 2)
        Le[i][1] = (kor[i][3] - kor[i][1]) / Le[i][0]
        Le[i][2] = (kor[i][2] - kor[i][0]) / Le[i][0]

    return Le


def d_matrix_type0(dcos_matrix, EA) -> np.ndarray:
    r = np.zeros((4, 4))

    delta_tilda = np.array([[1 - (dcos_matrix[0][1] ** 2), dcos_matrix[0][1],
                             -1 - (dcos_matrix[0][1] ** 2), -dcos_matrix[0][1]]])
    r_tilda = -(np.transpose(delta_tilda))
    delta = np.array([[dcos_matrix[0][0] / (EA)]])

    sub1 = np.concatenate((r, delta_tilda), axis=0)
    sub2 = np.concatenate((r_tilda, delta), axis=0)
    d = np.concatenate((sub1, sub2), axis=1)

    return d


def d_matrix_type1(dcos_matrix, EA, EI) -> np.ndarray:
    r = np.zeros((6, 6))

    L = dcos_matrix[0][0]
    cosa = dcos_matrix[0][1]
    sina = dcos_matrix[0][2]

    delta = np.zeros((3, 3))
    delta[0][0] = (((L) ** 3) / (12 * EI))
    delta[1][1] = (L / (EI))
    delta[2][2] = (L / (EA))

    r_tilda = np.array([[cosa, 0, -sina],
                        [-(L / 2), 1, 0],
                        [-sina, 0, -cosa],
                        [-cosa, 0, sina],
                        [-(L / 2), -1, 0],
                        [sina, 0, cosa]])

    delta_tilda = -(np.transpose(r_tilda))

    sub1 = np.concatenate((r, delta_tilda), axis=0)
    sub2 = np.concatenate((r_tilda, delta), axis=0)
    d = np.concatenate((sub1, sub2), axis=1)

    return d


def d_matrix_type2(dcos_matrix, EA, EI) -> np.ndarray:
    r = np.zeros((6, 6))

    L = dcos_matrix[0][0]
    cosa = dcos_matrix[0][1]
    sina = dcos_matrix[0][2]

    delta = np.zeros((3, 3))
    delta[0][0] = (L / EI)
    delta[1][1] = (L / (3 * EI))
    delta[2][2] = (L / (3 * EA))
    delta[2][1] = (L / (6 * EI))
    delta[1][2] = (L / (6 * EI))

    delta_tilda = np.array([[cosa, sina, 0, -cosa, -sina, 0],
                            [sina / L, -(cosa / L), -1, -(sina / L), cosa / L, 0],
                            [-(sina / L), cosa / L, 0, sina / L, -(cosa / L), 1]])

    r_tilda = -(np.transpose(delta_tilda))

    sub1 = np.concatenate((r, delta_tilda), axis=0)
    sub2 = np.concatenate((r_tilda, delta), axis=0)
    d = np.concatenate((sub1, sub2), axis=1)

    return d

#удаляю ненужные столбцы
def remove_reactions(d_matrix) -> np.ndarray:
    i = 0
    while i < 3:
        d_matrix = np.delete(d_matrix, 0, 0)
        d_matrix = np.delete(d_matrix, 0, 1)
        i += 1

    return d_matrix

#Решаю матричное уравнение
def matrix_equation(d_with_opora) -> np.ndarray:
    d_with_opora = np.linalg.inv(d_with_opora)
    d_with_opora = d_with_opora.dot(-Rf)

    return d_with_opora


print("Матрица направляющих косинусов = ", DcosFramework(KoR))
print("Введите EА и EI")
ea = float(input())
ei = float(input())
print("Матрица d нулевого типа = ", "\n", d_matrix_type0(dcos_matrix=DcosFramework(KoR),
                                                         EA=ea))

print("матрица d первого типа = ", "\n", d_matrix_type1(dcos_matrix=DcosFramework(KoR),
                                                        EA=ea,
                                                        EI=ei))

print("матрица d второго типа = ", "\n", d_matrix_type2(dcos_matrix=DcosFramework(KoR),
                                                        EA=ea,
                                                        EI=ei).round(3).astype(Decimal))

print("Матрица d второго КЭ с жесткой звделкой = ", "\n",
      remove_reactions(d_matrix_type1(dcos_matrix=DcosFramework(KoR),
                                      EA=ea,
                                      EI=ei)).round(3).astype(Decimal))

print("Решение матричного уравнение, матрица q, для КЭ первого типа = ", "\n",
      matrix_equation(remove_reactions(d_matrix_type1(dcos_matrix=DcosFramework(KoR),
                                                      EA=ea,
                                                      EI=ei))))

print("Решение матричного уравнение, матрица q, для второго КЭ = ", "\n",
      matrix_equation(remove_reactions(d_matrix_type2(dcos_matrix=DcosFramework(KoR),
                                                      EA=ea,
                                                      EI=ei))).astype(Decimal))
