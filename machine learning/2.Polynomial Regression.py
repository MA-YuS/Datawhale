'''
    多项式回归
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 导入波士顿房屋数据集
boston = fetch_california_housing()

# 提取特征和目标变量
X = boston.data     #特征矩阵
y = boston.target   #特征向量

# 将特征向量转换为多项式特征
# 通过这两行代码，原始特征矩阵 X 中的每个特征都将与其他特征进行组合，
# 生成所有可能的二次多项式交互特征。
# PolynomialFeatures 类的目的是生成原始特征的所有可能的多项式组合，包括交互项。

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
powers = poly.powers_# 查看该类的幂运算数组

# 使用多项式回归模型进行拟合
model = LinearRegression()
model.fit(X_poly, y)

# 预测新的房屋价格
x_new = X[0].reshape(1, -1)
X_new_poly = poly.transform(x_new)
y_new = model.predict(X_new_poly)

# 计算模型的性能指标
y_pred = model.predict(X_poly)
mse = mean_squared_error(y, y_pred)

# 绘制原始数据散点图和拟合曲线图
plt.scatter(X[:, 0], y, color='blue', label='Actual')
plt.scatter(x_new[:, 0], y_new, color='red', label='Prediction')
plt.plot(X[:, 0], y_pred, color='green', label='Regression')
plt.xlabel('CRIM')
plt.ylabel('Price')
plt.legend()
plt.show()

print(f"Predicted price for new house: {y_new}")
print(f"Mean Squared Error: {mse}")






