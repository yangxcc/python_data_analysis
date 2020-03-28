import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate

df = pd.DataFrame({'a':[1,2,np.nan,4],          #写的是a这一列的值
                   'b':[2,3,4,np.nan],
                   'c':[3,np.nan,5,6],
                   'd':[4,7,8,9]})

a = [1,2,3,4,5,6,9,10,11,12]
b = [10,16,21,32,35,43,58,62,67,70]

# print('原数据')
# print(df)
# print(df.isnull())
# df.isnull()函数返回df数据帧中的数据是否为NaN值的boolean型数据矩阵，如果数据为NaN，矩阵对应
# 位置为True，否则为False


class process:
    def __init__(self,data,x,y):
        self.data = data
        self.x = x
        self.y = y

    def delete_data(self,flag):
        if flag==True:
            data = pd.DataFrame(self.data).dropna()  #删除空值所在的行
        if flag == False:
            data = pd.DataFrame(self.data).dropna(axis = 1)   #删除控制所在的列
        return data

    def replace_data(self):
        data = pd.DataFrame(self.data).replace(np.nan,9)
        return data

    def fill_data(self,tag):
        if tag == True:
            data = pd.DataFrame(self.data).fillna(df.mean())  #用平均值填充
        if tag == False:
            data = pd.DataFrame(self.data).fillna(method='bfill')  #向后填充  ffill向前填充
        return data

    def Interpolation(self):
        linear = interpolate.interp1d(self.x,self.y,kind='linear')  #线性插值法根据已知数值构建线性方程组，通过求解线性方程组
        plt.plot(linear([1,2,3,4,5,6,7,8,9,10,11,12]),'-.')         #获取缺失值
        print('线性插值法求出的ss[7:9]=',linear([7,8]))
        lagrange = interpolate.lagrange(self.x,self.y)            #多项式插值是通过拟合多项式，通过多项式求解缺失值，多项式插值中
        plt.plot(lagrange([1,2,3,4,5,6,7,8,9,10,11,12]),'--')     #最常用的是拉格朗日插值法和牛顿插值法
        print('拉格朗日插值法求出的ss[7:9]=',lagrange([7,8]))
        plt.show()

    def spline(self):
        x = np.linspace(-np.pi,np.pi,10)
        y = np.sin(x)
        plt.plot(x,y)
        tck = interpolate.splrep(x,y)
        x_new = np.linspace(-np.pi,np.pi,100)
        y_spine = interpolate.splev(x_new,tck)
        plt.figure()    #同时生成两张图
        plt.plot(x_new,y_spine)
        plt.show()

df1 = process(df,a,b)
print('输出元数据')
print(df1)
print('删除法处理缺失值')
df2 = df1.delete_data(flag=True)
print(df2)
print('固定值替换法处理缺失值')
df3 = df1.replace_data()
print(df3)
print('填充法处理缺失值')
df4 = df1.fill_data(tag=False)
print(df4)
print('插值法处理缺失值')
df5 = df1.Interpolation()
print('样条插值法处理缺失值')
df1.spline()



