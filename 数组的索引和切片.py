'''
一维NumPy数组的索引与python列表的索引相同
二维数组的索引在单个或者多个轴向上完成，在某一轴上与一维数组索引相同
'''
import numpy as np

a=np.arange(12).reshape(3,4)
print('数组a为')
print(a)
print('a[0]=',a[0])    #第0行
print('a[1]=',a[1])
print('a[0][0]=',a[0][0])
print('a[1][2]=',a[1][2])
a[1]=666
print("数组a已经被修改,修改后为")
print(a)
a[0][0]=111
print(a)

#一维数组切片
b=np.arange(12)
print('b=',b)
print('b[1:3]=',b[1:3])
print('b[1:7:2]=',b[1:7:2])
print('b[9:]=',b[9:])
print('b[:]=',b[:])

#二维数组切片
c=np.arange(12).reshape(3,4)
print('c=',c)
'''
二维数组切片取得是两个区间的的交集
'''
print('c[0:2][1:3]=',c[0:2][1:3])
print('c[2:][:2]=',c[2:][1:2])  #####
print('c[:]=',c[:])

'''
布尔型索引是指使用布尔数组来索引目标数组，以此来找出与布尔数组中值为
true的对应的目标数组中的数据
'''
#布尔数组的长度必须与目标数组对应的轴的长度一致
names=np.array(['赵','王','李','上官','公孙','顿山'])
data=np.random.randn(6,3)
print(data)
print('上官对应的行：',data[names=='上官'])

d=np.arange(12).reshape(3,4)
print(d)
print('d>5',d>5)
print('d[d>5]',d[d>5])


#花式索引
