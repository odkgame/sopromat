import numpy as np
import pandas as pd
np.set_printoptions(precision=5,suppress=True)
file_name = "Plate.xlsx"

dfs = pd.read_excel(io=file_name, engine="openpyxl", sheet_name="Итерации по второй ветви", usecols="AGX", header=0,
                    nrows=289, skiprows=881)
unsorted_list = dfs.to_numpy()
unsorted_array = unsorted_list.reshape(17, 17)

sorted_array = np.array([])


for j in range(0, 17, 2):
    for i in range(0, 17, 2):
        sorted_array = np.append(sorted_array, unsorted_array[i][j])



sorted_array = sorted_array.reshape(9, 9)
df = pd.DataFrame(sorted_array)



print(df)




