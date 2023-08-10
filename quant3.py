import numpy as np

# 数组ndarray运算

a = np.array([1,2,3,4]) #1行4列
b = np.array(2)         #只有一个元素

print(a - b) # (array([-1,  0,  1,  2])
print(a + b) # array([3, 4, 5, 6]))


# python的次方使用**实现：
# File "<ipython-input-12-d58dcb39be5e>", line 1
# python的次方使用**实现：

# SyntaxError: invalid character in identifier

print(a**2)  #二次方，a里元素的平方
# array([ 1,  4,  9, 16], dtype=int32)

print(np.sqrt(a))  #开根号
# array([ 1.        ,  1.41421356,  1.73205081,  2.        ])

print(np.exp(a))  #e 求方
# array([  2.71828183,   7.3890561 ,  20.08553692,  54.59815003])

print(np.floor(10*np.random.random((2,2)))) #向下取整
# array([[ 1.,  8.],
#        [ 6.,  5.]])

print(a.resize(2,2)) #变换结构
print(a)
# array([[1, 2],
#        [3, 4]])