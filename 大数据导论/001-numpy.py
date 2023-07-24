import numpy as np

arr = np.zeros((5, 5))
arr[0, :] = 1  # 第一行
arr[-1, :] = 1  # 最后一行
arr[:, 0] = 1  # 第一列
arr[:, -1] = 1  # 最后一列

print(arr)
