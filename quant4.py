import numpy as np

# 矩阵及其运算

A = np.array([[0,1], [1,2]])  #数组
B = np.array([[2,5],[3,4]])   #数组

print(A);

print(B);

print("对应元素相乘：\n",A*B)

print("矩阵点乘：\n",A.dot(B))

print("矩阵点乘：\n",np.dot(A,B))  #(M行, N列) * (N行, Z列) = (M行, Z列)

print("横向相加：\n",np.hstack((A,B)))

print("纵向相加：\n",np.vstack((A,B)))