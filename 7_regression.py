import numpy as np
from sklearn.linear_model import LinearRegression

x = np.load("./data/data_x.npy")
y = np.load("./data/data_y.npy")

X = np.column_stack([x**3, x, np.log(x), np.ones_like(x)])

model = LinearRegression(fit_intercept=False)
model.fit(X, y)

A, B, C, D = model.coef_
print(f"A = {A}, B = {B}, C = {C}, D = {D}")
