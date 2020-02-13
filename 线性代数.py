'''
x+y+z=6
2y+5z=-4
2x+5y-z=27
'''

#用solve（）函数来求解线性方程组

import numpy as np

A=np.mat("1 1 1;0 2 5;2 5 -1");   #创建一个矩阵
b=np.array([6,-4,27])
x=np.linalg.solve(A,b)
print('方程的解为：',x)
print(x.ndim)  #解的维数
print(np.dot(A,x))

