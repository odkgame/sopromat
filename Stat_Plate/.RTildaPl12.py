import numpy as np
np.set_printoptions(precision=3)
# создаем локальную матрицу rt
def RTildaPl12(a, b, Dx, Dy, Dk, MuX, MuY):
    RT = np.zeros((4, 8))

    RT[0, 0] = (Dk * Dx * MuX * b ** 2 - Dk * Dy * a ** 2 + 10 * Dx * Dy * MuX * MuY * b ** 2 - 10 * Dx * Dy * b ** 2) / (
                30 * Dx * Dy * MuX * MuY * a * b - 30 * Dx * Dy * a * b)
    RT[1, 2] = RT[0,0]
    RT[2, 4] = RT[0,0]
    RT[3, 6] = RT[0,0]
    RT[1, 0] = (-Dk * Dx * MuX * b ** 2 + Dk * Dy * a ** 2 - 10 * Dx * Dy * MuX * MuY * b ** 2 + 10 * Dx * Dy * b ** 2) / (
                30 * Dx * Dy * MuX * MuY * a * b - 30 * Dx * Dy * a * b)
    RT[0, 2] = RT[1, 0]
    RT[2, 6] = RT[1, 0]
    RT[3, 4] = RT[1, 0]
    RT[2, 0] = (Dk * Dx * MuX * b ** 2 - Dk * Dy * a ** 2 - 5 * Dx * Dy * MuX * MuY * b ** 2 + 5 * Dx * Dy * b ** 2) / (
                30 * Dx * Dy * MuX * MuY * a * b - 30 * Dx * Dy * a * b)
    RT[0, 4] = RT[2, 0]
    RT[1, 6] = RT[2, 0]
    RT[3, 2] = RT[2, 0]
    RT[3, 0] = (-Dk * Dx * MuX * b ** 2 + Dk * Dy * a ** 2 + 5 * Dx * Dy * MuX * MuY * b ** 2 - 5 * Dx * Dy * b ** 2) / (
                30 * Dx * Dy * MuX * MuY * a * b - 30 * Dx * Dy * a * b)
    RT[0, 6] = RT[3, 0]
    RT[1, 4] = RT[3, 0]
    RT[2, 2] = RT[3, 0]

    RT[0, 1] = (-Dk * Dx * b ** 2 + Dk * Dy * MuY * a ** 2 + 10 * Dx * Dy * MuX * MuY * a ** 2 - 10 * Dx * Dy * a ** 2) / (
                30 * Dx * Dy * MuX * MuY * a * b - 30 * Dx * Dy * a * b)
    RT[1, 3] = RT[0, 1]
    RT[2, 5] = RT[0, 1]
    RT[3, 7] = RT[0, 1]
    RT[1, 1] = (Dk * Dx * b ** 2 - Dk * Dy * MuY * a ** 2 + 5 * Dx * Dy * MuX * MuY * a ** 2 - 5 * Dx * Dy * a ** 2) / (
                30 * Dx * Dy * MuX * MuY * a * b - 30 * Dx * Dy * a * b)
    RT[0, 3] = RT[1, 1]
    RT[2, 7] = RT[1, 1]
    RT[3, 5] = RT[1, 1]
    RT[2, 1] = (-Dk * Dx * b ** 2 + Dk * Dy * MuY * a ** 2 - 5 * Dx * Dy * MuX * MuY * a ** 2 + 5 * Dx * Dy * a ** 2) / (
                30 * Dx * Dy * MuX * MuY * a * b - 30 * Dx * Dy * a * b)
    RT[0, 5] = RT[2, 1]
    RT[1, 7] = RT[2, 1]
    RT[3, 3] = RT[2, 1]
    RT[3, 1] = (Dk * Dx * b ** 2 - Dk * Dy * MuY * a ** 2 - 10 * Dx * Dy * MuX * MuY * a ** 2 + 10 * Dx * Dy * a ** 2) / (
                30 * Dx * Dy * MuX * MuY * a * b - 30 * Dx * Dy * a * b)
    RT[0, 7] = RT[3, 1]
    RT[1, 5] = RT[3, 1]
    RT[2, 3] = RT[3, 1]

    return RT

print(RTildaPl12(0.25,0.25,1,1,0.7,0.3,0.3))
