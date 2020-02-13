#数组的运算支持向量化运算，并且比python具有更快的运算速度

#数组和标量间的运算
'''
数组和标量的算术运算，以及相同维度的数组的算术运算都是直接应用到元素中，也就是元素级运算
'''
import numpy as np

a=np.arange(6)
print(a)
b=a.reshape(2,3)
c=a*10
d=b*100
print(b)
print(c)
print(d)
e=a.__pow__(2)
print(e)

#广播

'''
广播是指NumPy在算术运算期间处理不同形状的数组的能力
如果两个阵列具有完全相同的形状，则这些操作可被无缝执行
如果两个数组的维数不相同，则元素到元素的操作是不可能的，然而在NumPy中仍然可以对形状不相似
的数组进行操作，因为他拥有广播功能。较小的数组会被广播到较大数组的大小，以便使它们的形状可兼容

（1）数组拥有相同形状
（2）数组拥有相同的维数，每个维度拥有相同的长度，或者长度为1
（3）数组拥有极少的维度，可以在其前面追加长度为1的维度，使上述条件成立
数组必须至少满足上述条件中的一条，才可以被称为可广播的
'''

x=np.array([1,2])
y=np.array([11,12])
z=np.array([[11,12],[13,14]])
print('x+y=',x+y)
print('x+z=',x+z)


#集合运算
'''
NumPy库提供了针对一维数组的基本集合运算

numpy.unique(arr,return_index,return_inverse,return_counts)
arr：输入数组，如果不是一维数组则会展开
return_index：如果为true，返回新列表元素在旧列表中的位置（下标），并以列表形式存储
return_inverse:如果为true，返回旧列表元素在新列表中的位置（下标），并以列表形式存储
return_counts:如果为true，返回去重数组中的元素在原数组中出现的次数
'''
aa=np.array([1,2,3,4,5,6,2,2,3,4,5,6,7,9])
print('aa=',aa)
print('去重之后的数组：',np.unique(aa))
u,indices=np.unique(aa,return_index=True)
print('去重数组的索引数组：',indices)
u,indices=np.unique(aa,return_inverse=True)
print('下标为：',indices)
print('使用下标重构原数组(还原原数组)：',u[indices])
print('返回去重元素的重复数量')
u,indices=np.unique(aa,return_counts=True)
print(u)
print(indices)

xx=np.array([1,2,3,4])
yy=np.array([1,2,3,6])
zz=np.array([1,3,2,4])
print(np.in1d(xx,yy))   #  xx的元素是否在yy中
print(np.in1d(xx,zz))

'''
排序
NumPy中提供了各种排序相关功能。这些排序函数实现不同的排序算法，排序算法的不同在于
执行速度，最坏情况性能，所需工作空间和算法的稳定性

numpy.sort(a,axis,kind,order)
a：要排序的数组
axis：沿着他排序数组的轴，如果没有数组会被展开，沿着最后的轴排序
kind：排序算法，有quicksort(快速排序)【默认】，mergesort(归并排序)，heapsort(堆排序)
order：如果数组包含字段，则是要排序的字段
'''

m=np.array([[2,5,6],[8,6,4],[6,4,9]])
print('m=',m)
print('m排序后（默认最后1轴）:',np.sort(m))
print('m按照0轴排序',np.sort(m,0))
dt=np.dtype([('sno','S10'),('score','int8')])
n=np.array([('1908',56),('1902',98),('1903',72),('1909',88),('1906',65)],dtype=dt)
print(n)
print(np.sort(n,order='sno'))

#  argsort()不懂

'''
搜索
'''
aa=np.arange(9.).reshape(3,3)
print(aa)
print('大于3的索引是：',np.where(aa>3))
print('大于3的元素是：',aa[np.where(aa>3)])  # where的第一种写法
print(np.where(aa<3,'小','大'))            #where的第二种写法
print('extract()函数，整除2的数:',np.extract(np.mod(aa,2)==0,aa))#extract()函数返回满足任何条件的元素
print('nonzero:',np.nonzero(aa))    #nonzero()函数返回输入数组中非0元素的索引
print('aa中非零数：',aa[np.nonzero(aa)])