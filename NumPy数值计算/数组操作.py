import numpy as np
'''NumPy中包含了一些函数用于操作数组，大致分为六类：
   修改数组形状
   翻转数组
   修改数组维度
   连接数组
   分割数组
   数组元素的添加和删除
'''

#修改数组形状

a=np.arange(12).reshape(2,6)
b=a.reshape(3,4)   #3行4列
print('reshape输出')  #reshape()函数在不改变数据的条件下修改形状
print(a)
print(b)
print('flatten输出')  #faltten()函数返回一份数组复制，对复制所做的修改不会影响原始数组
c=a.flatten('F')    #C按行，F按列，A原顺序，k元素在内存中出现的顺序
c[0]=1000
print(c)
print(a)
print('ravel输出')  #ravel（）函数展平数组元素，顺序通常是’C风格‘，返回的是数组视图
d=a.ravel()
d[0]=100
print(d)
print(a)


#翻转数组 transpose()  swapaxes()
#连接数组 concatenate()  stack()  hstack() vstack()
#数组切割 split()  hsplit()  vsplit()

#数组元素的添加和删除
a1=np.arange(4).reshape(2,2)
print("a1=",a1)
#resize()函数
a1.resize((1,4))
print('一行四列a1=',a1)
a1.resize((4,1))
print('四行一列a1',a1)
'''
当新数组大小大于原始数组大小时
则包含原始数组中元素的副本'''

#append()函数
b1=np.arange(6).reshape(3,2)
print("数组b1=",b1)
b2=np.append(b1,[6,7])
print('append的b2是',b2)
b3=np.append(b1,[[11,12]],axis=0)   #当未指明axis时，会将数组展开输出，0代表横轴，1代表竖轴
print("append后的b3=",b3)
b4=np.append(b1,[[12,12],[11,11],[13,13]],axis=1)
print('append后的b4=',b4)

#insert函数
f=np.insert(b1,2,11)  #在b1数组中数值为2的元素前面加上一个数值为11的元素
print('f=',f)
h=np.insert(b1,2,10,axis=0) #在b1数组中第2行（从0开始）前加上一行10
print('h=',h)
i=np.insert(b1,1,10,axis=1)#在b1数组中第一列（从0开始）前加上一列10
print('i=',i)

#delete函数
j=np.delete(i,[1,2],axis=1)  #删除i数组的第一列和第二列（从0开始，注意是和，不是到）
print('j=',j)
k=np.delete(h,2,axis=0)   #删除h数组的第二行（从0开始）
print('k=',k)
l=np.delete(f,3)   #删除3位置前的数
print('l=',l)