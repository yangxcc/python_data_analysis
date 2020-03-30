import pandas as pd
import numpy as np

# Series算术运算
s1=pd.Series([1,2,3],index=['a','b','c'])
s2=pd.Series([11,12,13],index=['a','b','d'])

print('s1=',s1)
print('s2=',s2)

print(s1+s2)
'''
Pandas的Series数据对象在进行算术运算时，如果有相同的索引，
则对相同索引的数据进行运算，如果没有相同索引，则引入缺失值

pandas的DataFrame数据对象进行算术运行时，如果有相同的索引和列名
则对相同索引和列名数据进行运算，如果没有相同的索引和列名，则引入缺失值

pandas的Series和DataFrame对象也可以进行算术运算，因为维度不同，所以运算规则
遵循广播规则，即Series对象根据DataFrame对象结构拓展为二维，变为多行的DataFrame
每行数据都是Series本身
'''

# DataFrame 算术运算
d1 = {'a':[1,2],
      'b':[3,4],
      'c':[5,6]
      }
df1=pd.DataFrame(d1)
d2 = {'a':[11,12],
      'b':[13,14],
      'd':[14,15]
      }
df2=pd.DataFrame(d2)
print(df1+df2)
print(d1)

# print(np.arange(3).reshape(3,1))
# print(np.arange(3))

# Series和DataFrame算术运算

s=pd.Series([1,2,3],index=['a','b','c'])
d={'a':[1,2],
   'b':[3,4],
   'c':[5,6]
   }
df = pd.DataFrame(d)
print(s + df)

'''
函数应用与映射运算
'''

'''
函数pipe（）将其他函数套用在DataFrame上，即通过函数对DataFrame整体执行操作

函数apply（）将其他函数套用到整个DataFrame上，可以通过指定axis的值设置作用行还是列
axis的默认值是0，作用域DataFrame的列，axis = 1时，作用与dataframe的行

函数applymap（）将其他函数套用到DataFrame()的每一个元素上

函数map() 将其他函数套用在Series的每个元素中，DataFrame的行或者列都是
Series对象
'''

# pipe（）函数,作用于dataframe对象整体

def fun(ele):
    return ele * 2

data=np.arange(9).reshape(3,3)
df=pd.DataFrame(data,columns=['a','b','c'])
print(df.pipe(fun))

# apply（）函数

df=pd.DataFrame(np.arange(12).reshape(3,4),columns=['a','b','c','d'])
print(df)
print(df.apply(np.mean))
print(df.apply(np.mean,axis=1))
print(df.apply(lambda x:np.sum(x)))

# map()函数

print(df.applymap(lambda x:np.power(x,2)))

'''
排序
'''
data=np.array([[1,2,6,4],[4,5,3,8],[8,9,12,56]])
df=pd.DataFrame(data,index=[0,4,2],columns=['a','b','c','d'])
print('原数据帧')
print(df)
print('按行索引升序')
print(df.sort_index())
print('按行索引降序')
print(df.sort_index(ascending=False))
print('按列索引升序')
print(df.sort_index(axis=1))
print('按列索引降序')
print(df.sort_index(axis=1,ascending=False))
print('sort_values()用法')
print(df.sort_values(by='b'))   # 按照b这一列的数据进行排序
print(df.sort_values(by=['c','b']))  # 先按照c来排序，再按照b排序


'''
迭代
'''

# DataFrame