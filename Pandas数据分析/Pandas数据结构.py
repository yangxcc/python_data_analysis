'''
Pandas有三种数据结构：系列（Series）,数据帧（DataFrame）和面板（Panel），这些数据结构可以建立在NumPy数组之上
'''
import pandas as pd
import numpy as np
from warnings import simplefilter              # 这两句来解决FutureWarning问题
simplefilter(action='ignore', category=FutureWarning)

'''
pandas.Series(data.index,dtype,copy)
data  数据采取各种形式，如ndarray  int  constants
index 索引值必须是唯一的和散列的，与数据的长度相同
dtype dtype用于指定数据类型。如果没有，将推断数据类型
copy 复制数据，默认为false
'''
data=np.array(['a','b','c','d','e'])
s1=pd.Series(data)
print('默认索引：')
print(s1)

s2=pd.Series(data,index=[100,101,102,103,104])   #必须与数据长度一致
print("指定索引：")
print(s2)

print(s2[100])
print(s2[[101,104]])        #[ [ ] ]
print(s2[s2 < 'c'])

'''
Pandas.DataFrame(data,index,columns,dtype,copy)
data 数据采取各种形式，如ndarray,series,map,lists,dict,constant和另一个DataFrame
index 对于行标签，要用于结果帧的索引时可选默认值np.arrange(n)
columns 对于列表前，可选默认值语法是np.arrange(n)
dtype 每列的数据类型
copy 如果默认值是False，则此命令用于复制数据
'''

df=pd.DataFrame()
print('创建空数据帧;')
print(df)

data=np.arange(11,15)
df1=pd.DataFrame(data)
print('df1=')
print(df1)    #多出来一个0 ？？？

data=[{'name':'小明','gender':'男'},{'name':'小红','gender':'女'}]
df2=pd.DataFrame(data,index=['1','2'],columns=['name','gender'])
print('df2=')
print(df2)

d={'a':pd.Series(np.arange(3),index=['1','2','3']),
   'b':pd.Series(np.arange(4),index=['1','2','4','5'])
   }
df3=pd.DataFrame(d)
print('df3=')
print(df3)

print('df3.index=',df3.index)    # df3的行
print('df3.columns=',df3.columns) # df3的列


'''
pandas.Panel(data,items,major_axis,minor_axis,dtype,copy)
data  数据采取各种形式
items axis=0
major_axis  axis=1
minor_axis  axis=2
dtype  每列的数据类型
copy   复制数据，默认为False
'''

# data=np.random.rand(2,4,5)
# p=pd.Panel(data)
# print(p)

data={'item1': pd.DataFrame(np.random.rand(4,3)),
      'item2': pd.DataFrame(np.random.rand(4,2))
      }
p=pd.Panel(data)
print(p)