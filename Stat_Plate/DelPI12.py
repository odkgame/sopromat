import numpy as np

Del = np.zeros((8, 8))


def DelPl12(a, b, Dx, Dy, Dk, MuX, MuY):
    Del[0, 0] = (
                        2 * Dk * Dx ** 2 * MuX ** 2 * b ** 4 - 5 * Dx * Dy ** 2 * MuX * MuY * a ** 2 * b ** 2 + 2 * Dk * Dy ** 2 * a ** 4 + 5 * Dx * Dy ** 2 * a ** 2 * b ** 2) / (
                        45 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 90 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 45 * Dx ** 2 * Dy ** 2 * a * b)
    Del[2, 2] = Del[0, 0]
    Del[4, 4] = Del[0, 0]
    Del[6, 6] = Del[0, 0]
    Del[0, 1] = (
                        -2 * Dk * Dx ** 2 * MuX * b ** 4 - 2 * Dk * Dy ** 2 * MuY * a ** 4 + 5 * Dx * Dy ** 2 * MuX * MuY ** 2 * a ** 2 * b ** 2 - 5 * Dx * Dy ** 2 * MuY * a ** 2 * b ** 2) / (
                        45 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 90 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 45 * Dx ** 2 * Dy ** 2 * a * b)
    Del[2, 3] = Del[0, 1]
    Del[4, 5] = Del[0, 1]
    Del[6, 7] = Del[0, 1]
    Del[0, 2] = (
                        -8 * Dk * Dx ** 2 * MuX ** 2 * b ** 4 + 7 * Dk * Dy ** 2 * a ** 4 - 10 * Dx * Dy ** 2 * MuX * MuY * a ** 2 * b ** 2 + 10 * Dx * Dy ** 2 * a ** 2 * b ** 2) / (
                        180 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 360 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 180 * Dx ** 2 * Dy ** 2 * a * b)
    Del[2, 0] = Del[0, 2]
    Del[4, 6] = Del[0, 2]
    Del[6, 4] = Del[0, 2]
    Del[0, 3] = (
                        8 * Dk * Dx ** 2 * MuX * b ** 4 - 7 * Dk * Dy ** 2 * MuY * a ** 4 + 10 * Dx * Dy ** 2 * MuX * MuY ** 2 * a ** 2 * b ** 2 - 10 * Dx * Dy ** 2 * MuY * a ** 2 * b ** 2) / (
                        180 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 360 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 180 * Dx ** 2 * Dy ** 2 * a * b)
    Del[2, 1] = Del[0, 3]
    Del[4, 7] = Del[0, 3]
    Del[6, 5] = Del[0, 3]
    Del[0, 4] = (
                        -7 * Dk * Dx ** 2 * MuX ** 2 * b ** 4 - 7 * Dk * Dy ** 2 * a ** 4 - 5 * Dx * Dy ** 2 * MuX * MuY * a ** 2 * b ** 2 + 5 * Dx * Dy ** 2 * a ** 2 * b ** 2) / (
                        180 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 360 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 180 * Dx ** 2 * Dy ** 2 * a * b)
    Del[4, 0] = Del[0, 4]
    Del[4, 6] = Del[0, 4]
    Del[6, 2] = Del[0, 4]
    Del[0, 5] = (
                        5 * Dx * Dy ** 2 * MuX * MuY ** 2 * a ** 2 * b ** 2 + 7 * Dk * Dx ** 2 * MuX * b ** 4 + 7 * Dk * Dy ** 2 * MuY * a ** 4 - 5 * Dx * Dy ** 2 * MuY * a ** 2 * b ** 2) / (
                        180 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 360 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 180 * Dx ** 2 * Dy ** 2 * a * b)
    Del[4, 1] = Del[0, 5]
    Del[2, 7] = Del[0, 5]
    Del[6, 3] = Del[0, 5]
    Del[0, 6] = (
                        7 * Dk * Dx ** 2 * MuX ** 2 * b ** 4 - 10 * Dx * Dy ** 2 * MuX * MuY * a ** 2 * b ** 2 - 8 * Dk * Dy ** 2 * a ** 4 + 10 * Dx * Dy ** 2 * a ** 2 * b ** 2) / (
                        180 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 360 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 180 * Dx ** 2 * Dy ** 2 * a * b)
    Del[6, 0] = Del[0, 6]
    Del[2, 4] = Del[0, 6]
    Del[4, 2] = Del[0, 6]
    Del[0, 7] = (
                        10 * Dx * Dy ** 2 * MuX * MuY ** 2 * a ** 2 * b ** 2 - 7 * Dk * Dx ** 2 * MuX * b ** 4 + 8 * Dk * Dy ** 2 * MuY * a ** 4 - 10 * Dx * Dy ** 2 * MuY * a ** 2 * b ** 2) / (
                        180 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 360 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 180 * Dx ** 2 * Dy ** 2 * a * b)
    Del[6, 1] = Del[0, 7]
    Del[2, 5] = Del[0, 7]
    Del[4, 3] = Del[0, 7]
    Del[1, 1] = (
                        2 * Dk * Dx ** 2 * b ** 4 + 2 * Dk * Dy ** 2 * MuY ** 2 * a ** 4 - 5 * Dx ** 2 * Dy * MuX * MuY * a ** 2 * b ** 2 + 5 * Dx ** 2 * Dy * a ** 2 * b ** 2) / (
                        45 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 90 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 45 * Dx ** 2 * Dy ** 2 * a * b)
    Del[3, 3] = Del[1, 1]
    Del[5, 5] = Del[1, 1]
    Del[7, 7] = Del[1, 1]
    Del[1, 0] = (
                        -2 * Dk * Dx ** 2 * MuX * b ** 4 - 2 * Dk * Dy ** 2 * MuY * a ** 4 + 5 * Dx ** 2 * Dy * MuX ** 2 * MuY * a ** 2 * b ** 2 - 5 * Dx ** 2 * Dy * MuX * a ** 2 * b ** 2) / (
                        45 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 90 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 45 * Dx ** 2 * Dy ** 2 * a * b)
    Del[3, 2] = Del[1, 0]
    Del[5, 4] = Del[1, 0]
    Del[7, 6] = Del[1, 0]
    Del[1, 2] = (
                        8 * Dk * Dx ** 2 * MuX * b ** 4 - 7 * Dk * Dy ** 2 * MuY * a ** 4 + 10 * Dx ** 2 * Dy * MuX ** 2 * MuY * a ** 2 * b ** 2 - 10 * Dx ** 2 * Dy * MuX * a ** 2 * b ** 2) / (
                        180 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 360 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 180 * Dx ** 2 * Dy ** 2 * a * b)
    Del[3, 0] = Del[1, 2]
    Del[5, 6] = Del[1, 2]
    Del[7, 4] = Del[1, 2]
    Del[1, 3] = (
                        -8 * Dk * Dx ** 2 * b ** 4 + 7 * Dk * Dy ** 2 * MuY ** 2 * a ** 4 - 10 * Dx ** 2 * Dy * MuX * MuY * a ** 2 * b ** 2 + 10 * Dx ** 2 * Dy * a ** 2 * b ** 2) / (
                        180 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 360 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 180 * Dx ** 2 * Dy ** 2 * a * b)
    Del[3, 1] = Del[1, 3]
    Del[5, 7] = Del[1, 3]
    Del[7, 5] = Del[1, 3]
    Del[1, 4] = (
                        7 * Dk * Dx ** 2 * MuX * b ** 4 + 7 * Dk * Dy ** 2 * MuY * a ** 4 + 5 * Dx ** 2 * Dy * MuX ** 2 * MuY * a ** 2 * b ** 2 - 5 * Dx ** 2 * Dy * MuX * a ** 2 * b ** 2) / (
                        180 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 360 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 180 * Dx ** 2 * Dy ** 2 * a * b)
    Del[3, 6] = Del[1, 4]
    Del[5, 0] = Del[1, 4]
    Del[7, 2] = Del[1, 4]
    Del[1, 5] = (
                        -7 * Dk * Dx ** 2 * b ** 4 - 7 * Dk * Dy ** 2 * MuY ** 2 * a ** 4 - 5 * Dx ** 2 * Dy * MuX * MuY * a ** 2 * b ** 2 + 5 * Dx ** 2 * Dy * a ** 2 * b ** 2) / (
                        180 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 360 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 180 * Dx ** 2 * Dy ** 2 * a * b)
    Del[3, 7] = Del[1, 5]
    Del[5, 1] = Del[1, 5]
    Del[7, 3] = Del[1, 5]
    Del[1, 6] = (
                        -7 * Dk * Dx ** 2 * MuX * b ** 4 + 8 * Dk * Dy ** 2 * MuY * a ** 4 + 10 * Dx ** 2 * Dy * MuX ** 2 * MuY * a ** 2 * b ** 2 - 10 * Dx ** 2 * Dy * MuX * a ** 2 * b ** 2) / (
                        180 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 360 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 180 * Dx ** 2 * Dy ** 2 * a * b)
    Del[3, 4] = Del[1, 6]
    Del[5, 2] = Del[1, 6]
    Del[7, 0] = Del[1, 6]
    Del[1, 7] = (
                        7 * Dk * Dx ** 2 * b ** 4 - 8 * Dk * Dy ** 2 * MuY ** 2 * a ** 4 - 10 * Dx ** 2 * Dy * MuX * MuY * a ** 2 * b ** 2 + 10 * Dx ** 2 * Dy * a ** 2 * b ** 2) / (
                        180 * Dx ** 2 * Dy ** 2 * MuX ** 2 * MuY ** 2 * a * b - 360 * Dx ** 2 * Dy ** 2 * MuX * MuY * a * b + 180 * Dx ** 2 * Dy ** 2 * a * b)
    Del[3, 5] = Del[1, 7]
    Del[5, 3] = Del[1, 7]
    Del[7, 1] = Del[1, 7]
    return Del


print(DelPl12(1, 2, 3, 4, 5, 6, 7, ))
