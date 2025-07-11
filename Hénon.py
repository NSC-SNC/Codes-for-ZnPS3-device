import numpy as np
import pandas as pd

a = 1.4
b = 0.3
n = 2000
x = np.zeros(n)
y = np.zeros(n)

x[0] = 0
y[0] = 0

for i in range(1, n):
    x[i] = 1 - a * x[i-1]**2 + y[i-1]
    y[i] = b * x[i-1]

df = pd.DataFrame({'x(n)': x, 'y(n)': y})
df.to_excel('D:/Hénon_map.xlsx', index=False)