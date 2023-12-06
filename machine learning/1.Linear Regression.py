'''
    线性回归（Linear Regression）

    计算步骤：
    1、导入必要的库和数据集
    2、数据准备：分割数据集为 特征（X）和目标变量（Y）
    3、模型训练：使用线性回归模型拟合数据
    4、模型评估：计算拟合直线的性能指标（如均方误差）
    5、结果可视化：绘制拟合直线和实际观测值的散点图

'''

#导入必要的库
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#加载波士顿房屋数据集
boston = fetch_california_housing()

#数据准备
x = boston.data
y = boston.target

# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#创建线性回归模型实例
model = LinearRegression()

# 模型训练
model.fit(X_train, y_train)

#模型预测
y_pred = model.predict(X_test)

# 计算均方误差
mse = np.mean((y_pred - y_test) ** 2)
print("均方误差：", mse)

# 结果可视化
# 预测准的情况下就应该是y_test, y_pred在一条对角直线上
plt.scatter(y_test, y_pred)
plt.plot( [y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2 )
plt.xlabel('actual_price')
plt.ylabel('predict_price')
plt.title('linear')
plt.show()
print([y_test.min(), y_test.max()])

