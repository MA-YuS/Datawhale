import numpy as np

'1-数组创建'
#使用 numpy.array() 从列表或元组创建数组
#从列表创建数组
np.array([1, 2, 3])
#从元组创建数组
np.array((4,5,6))

# 使用 numpy.zeros()、numpy.ones()、numpy.empty() 创建特定大小的数组
#创建全0数组
np.zeros(5)
#创建全1数组
np.ones(5)
#创建未初始化数组
np.empty(5)    #输出随机数
#创建全0矩阵
np.zeros((3, 4))
#创建全1矩阵
np.ones((2, 3))
#创建未初始化矩阵
np.empty((2, 2))

# 使用 numpy.arange()、numpy.linspace() 创建数值范围内的数组
#使用 arange 创建数组
np.arange(1, 10, 2)
np.arange(10)
#使用 linspace 创建等间距的点
np.linspace(0, 1, 5)
np.linspace(0, 10, 10)



