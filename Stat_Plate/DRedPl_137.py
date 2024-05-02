import numpy as np

#Гр ус 1_3_7
#удаляются нулевые моменты в опорных узлах
# а также [Mу по 'верхней' и 'нижней' кромкам
#Mx по 'левой' и 'правой' кромкам]
def DRedPl_137(n1,n2):
    DRed137 = np.array([])
    DRed137[1]=1
    DRed137[2]=2

    tr=3
    for i in range(1,n1-1):
        DRed137[tr]=2*i+2
        tr+=1

    p=DRed137[tr-1]
    DRed137[tr]=p+1
    tr+=1
    DRed137[tr]=p+2
    tr+=1
    for i in range(1,n2-1):
        DRed137[tr] = [[n1+1]*2]*i+1
        tr+=1
        DRed137[tr] = [[n1+1]*2]*i+1+n1*2
        tr+=1

    p=DRed137[tr-1]
    DRed137[tr]=p+2
    tr+=1
    DRed137[tr]=p+3
    tr+=1
    s=[n1+1]*2*n2+4
    for i in range(1,n1-1):
        DRed137[tr]=s
        tr+=1
        s+=2

    p=DRed137[tr-1]
    DRed137[tr]=p+1
    tr+=1
    DRed137[tr]=p+2
    tr+=1

    return DRed137