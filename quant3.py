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



# 统计运算：
# 需要知道二维数组的最大最小值怎么办？想计算全部元素的和、按行求和、按列求和怎么办？NumPy的ndarray类已经做好函数了

a=np.arange(20).reshape(4,5) # 0-19 4行 5列
print("原数组a:\n",a)
print("a全部元素和: ", a.sum())
print("a的最大值: ", a.max())
print("a的最小值: ", a.min())
print("a每行的最大值: ", a.max(axis=1))  #axis=1代表行
print("a每列的最小值: ", a.min(axis=0))  #axis=0代表列
print("a每行元素的求和: ", a.sum(axis=1)) 
print("a每行元素的均值：",np.mean(a,axis=1))
print("a每行元素的标准差：",np.std(a,axis=1))

