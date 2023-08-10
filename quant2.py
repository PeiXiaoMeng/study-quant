import numpy as np

# 常用函数
# arange指定范围和数值间的间隔生成 array，注意范围包左不包右
# 注意：系统自带的range生成的是tupe,要产生list需要使用循环取出元素

a = [1,2,3,4,5,6,7,8];

# 使用range产生list
L = [i for i in a]
print(L);


b=np.arange(10)     #注意包含0，不包含10  [0 1 2 3 4 5 6 7 8 9]
c=np.arange(0,10,2) #2表示间隔  [0 2 4 6 8]
d=np.arange(1,10,3) #3表示间隔  [1 4 7]
print(b,c,d)


# 金融分析常常需要产生随机数，Numpy的random函数派上用场。
# 均匀分布：
a=np.random.rand(3,4)      #创建指定为3行4列)的数组(范围在0至1之间)
b=np.random.uniform(0,100) #创建指定范围内的一个数
c=np.random.randint(0,100) #创建指定范围内的一个整数
print("创建指定为3行4列)的数组：\n",a)   #\n 表示换行
print("创建指定范围内的一个数：%.2f" %b) #%.2f 表示结果保留2位小数
print("创建指定范围内的一个整数：",c)


# 正态分布
# 给定均值/标准差/维度的正态分布np.random.normal(u, r, (x, y)) 数组的索引
# 正态生成3行4列的二维数组
a= np.random.normal(1.5, 3, (3, 4))  #均值为1.5，标准差为3
print(a)
# 截取第1至2行的第2至3列(从第0行、0列算起算起)
b = a[1:3, 2:4]
print("截取第1至2行的第2至3列: \n",b)