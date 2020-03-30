import pandas as pd
import numpy as np

data={'name':pd.Series(['小明','小红','小李','小花']),
      'age':pd.Series([11,12,13,14]),
      'gender':pd.Series(['男','女','男','女']),
      'class': pd.Series(['1班','2班','1班','2班'])
      }
df=pd.DataFrame(data,columns=['name','age','gender','class'])
print('元数据帧：')
print(df)

print('转置')
print(df.T)

print('轴序列：',df.axes)   # 行轴标签和列轴标签作为成员

print('数据类型')
print(df.dtypes)

print('是否为空',df.empty)

print('维度',df.ndim)

print('形状',df.shape)

print('元素数量',df.size)

print('实际的NumPy表示')
print(df.values)

print('前三行数据')
print(df.head(3))

print('后三行数据')
print(df.tail(3))
