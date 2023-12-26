
import numpy as np
from sklearn.linear_model import LinearRegression

# Create a simple linear regression model
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3

reg = LinearRegression().fit(X, y)

# Testing
print(reg.score(X, y))  # 1.0
print(reg.coef_)  # array([1., 2.])
print(reg.intercept_)  # 3.0
print(reg.predict(np.array([[3, 5]])))  # array([16.])
