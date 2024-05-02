import numpy as np

def FE_DFun(m, n1):
    #задаем матрицу соответстви¤ локальных перемещений глобальным
    td=0
    s=0
    FE_D = np.array([])
    for i in range(1,m):
        s=s+1

        FE_D[i,1]=i+td
        FE_D[i,2]=i+td+1
        FE_D[i,3]=n1+2+i+td
        FE_D[i,4]=n1+1+i+td
        if s==n1:
            s=0
            td=td+1



