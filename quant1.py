import numpy as np

# numpy 金融里对数组、线性代数操作的库

# a是系列(list)
a = [1,2,3,4,5,6,7,8];
print(a);

# b是数组,不同于javaScript的数组
b = np.array(a);
print(b);

# <class 'list'>
print(type(a));

# <class 'numpy.ndarray'>
print(type(b));

# 改变数组的维度 一维 -> 二维
b = b.reshape(2,4); # 2行 4列

print(b);
print("取第1行第2列元素：",b[1][2])


# -> 三维
c = b.reshape(2, 2, 2);
print(c);

# 特殊的数组有特别定制的命令生成，如零和1矩阵:
d = (3,4); # 3行 4列
print(np.zeros(d)) # 零矩阵
print(np.ones(d)) # 1矩阵

# 默认生成的类型是浮点型，可以通过指定类型改为整型
print(np.ones(d,dtype=int))


# 常用函数

