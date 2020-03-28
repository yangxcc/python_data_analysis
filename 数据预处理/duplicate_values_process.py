import pandas as pd
import numpy as np

df = pd.DataFrame({'a':np.random.randint(1,3,1000),'b':np.random.randint(3,5,1000),
                   'c':np.random.randint(5,7,1000)})
print('原数据',df)
print('原数据shape',df.shape)
# print(df.duplicated()[1])
num_false = 0
num_true = 0
for i in range(df.shape[0]):
    if (df.duplicated()[i] == True):
        num_true = num_true+1
    else:
        num_false = num_false+1
print('不重复的行（第一次出现）',num_false)
print('重复行',num_true)
print(df.duplicated())
df1 = df.drop_duplicates()
print('去重后的数据shape',df1.shape)
print('去重后原数据shape不变',df.shape)
'''
drop_duplicates()函数可以删除重复记录。
参数subset用于识别重复的列标签或列标签序列，默认None表示所有列标签
参数keep是特定字符串，表示重复时保留哪个记录数据。first表示第一条，last表示保留最后一条
false表示重复的都不保留，默认为first
参数inplace是一个布尔值，表示是否在原数据上进行操作，默认为False，当inplace为True时，drop_duplicates()函数
没有返回值，原DataFrame数据发生修改。
'''
df.drop_duplicates(subset=('a','b'),keep='last',inplace=True)
print(df)
print(df.shape)