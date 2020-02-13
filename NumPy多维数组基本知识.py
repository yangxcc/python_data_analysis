'''
通过array（）函数创建narray数组
'''

import numpy as np
#一维列表当作array参数
a1=np.array([1,2,3,4,5])
print(a1)

#二位列表作为array参数
a2=np.array([[1,2,3],[4,5,6]])    #有两个[]
print(a2)

#字符串作为array参数
a3=np.array('abcdefg')
print(a3)

#元组作为array参数
a4=np.array((1,2,3))
print(a4)

#字典作为array参数
a5=np.array({'zahngsan':12,'lisi':'13'})
print(a5)

'''
NumPy提供了创建特殊数组的函数
'''
b1=np.empty((2,3))  #创建2行3列的二维数组，创建的是没有具体值的数
print(b1)

b2=np.zeros((3,5))  #创建3行5列的二维数组，其元素都为0
print(b2)

b3=np.ones((4,2))  #创建4行2列的二维数组，其元素都为1
print(b3)

b4=np.eye(3)      #eye,identity均为创建N*N单位矩阵
print(b4)

b5=np.ones_like(b1)  #以另一个数组为参考，根据其形状和dtype创建全1的数组，创建与b1结构相同的数组，其元素的值均为1
print(b5)
'''zeros_like()、empty_like()和ones_like相似'''


#从数值范围创建数组的Numpy函数有3个：arange()   linspace()   logspace()
c1=np.arange(10)
print(c1)     #该函数根据start和stop指定的范围以及step设置步长，生成一个ndarray对象
              #numpy.arange（start，stop，step，dtype）

c2=np.linspace(1,10,10)
print(c2)    #该函数用于创建一个一维数组，数组是由一个等差数列构成的
             #numpy.linspace（start，stop，num=50，endpoint=True，retstep=False，dtype=None）

c3=np.logspace(10,100,10)
print('c3=',c3)   #用于创建一个对数运算的等比数列
                  #numpy.logspace（start，stop，num=50，endpoint=True，base=10.0，dtype=None）
                  #base指的是对数log的底数
                  #endpoint=true时，数组中包含stop

'''asarray（）把python的列表、元组等转换成Numpy数组
其格式如下：numpy.asarray（a,dtype=None,order=None）
a是任意形式的输入参数，可以是列表、列表的元组、元组、元组的元组、元组的列表、多维数组
numpy数组中没有逗号，是以空格分隔的，不同于python列表，numpy数组通过tolist（）转换成python（）列表
'''
d1=[1,2,3,4,5]
d2=np.asarray(d1)
d3=d2.tolist()
print('d2=',d2)
print('d3=',d3)

#创建随机数数组
a=np.random.rand(2,4)#如果没参数就产生一个[0,1)之间的一个float随机数，2行4列
print(a)

b=np.random.uniform(3,5,(2,4))  #返回一个【low,high）中均匀分布的数组
print(b)

c=np.random.uniform(size=(2,4))
print(c)

'''randn()函数返回一个指定形状的数组，数组中的值服从标准正态分布
（均值为0，方差为1），numpy.random.randn(d0,...,dn)
如果没有参数，则返回一个标准正态分布的float型随机数
   normal()函数生成一个由size指定形状的数组，数组中的值服从，μ=loc,σ=scale的正态分布
   numpy.random.normal(loc=0.0,scale=1.0,size=None)
   randint()函数生成了一个在区间[low,high)中离散均匀抽样的数组
   numpy.random.randint(low,high=None,size=None,dtype='1')   dtype:可选参数，指定数据类型
   numpy.random.random(),random()函数生成【0，1）之间均匀抽样的数组
'''

#ndarray对象属性
'''
ndim 秩，即数据轴的个数
shape 数组的维度
size 元素的总个数
dtype 数据类型
itemsize 数组中每个元素的字节大小
nbytes 存储整个数组所需的字节数量，是itemsize属性值和size属性值之积
T 数组的转置
flat 返回一个numpy.flatiter对象，可以使用flat的迭代器来遍历数组
'''
x=np.array([np.arange(3),np.linspace(3,5,3)])
print(x.T)
print('x=')
print(x)
print('x数组中的各个属性是：')
print(x.ndim,x.shape,x.dtype,x.itemsize,x.nbytes)
for i in x.flat:
    print(i,end='')


'''
dtype指定数据类型
astype转换数据类型，astype()函数可以把数组元素转换成指定类型，注意：
  1、指定类型类型有两种写法，以float64为例，np.float64和“float64”，这两种方式效果相同
  2、将浮点数据转换成整数时元素的小数部分被截断，而不是四舍五入
  3、数值型的字符串可以通过astype方法将其转化为数值类型，但如果字符串中有非数值型字符进行转化就会报错
  4、astype方法会创建一个新的数组，并不会改变原有数组的数据类型
'''

e=np.array([[1.1,2.2],[3.3,4.4]],dtype=float)
f=e.astype(np.int)
print('e=',e)
print('f=',f)
c=np.arange(5,dtype=np.int8)
print('c.dtype=',c.dtype)
print('数据类型转换后的dtype=',c.astype(np.float).dtype)
print('c的数据类型没有改变，c.dtype=',c.dtype)
