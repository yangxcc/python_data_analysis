import pandas as pd
import numpy as np

dfleft = pd.DataFrame({'a':np.arange(5),
                       'b':np.linspace(11,15,5)})
dfright = pd.DataFrame({'a':np.arange(2,7,1),
                        'd':np.linspace(3,7,5)})
print(dfleft)
print(dfright)
print(pd.merge(dfright,dfleft))
print(pd.merge(dfleft,dfright))
print(pd.merge(dfleft,dfright,on='a'))
print(pd.merge(dfleft,dfright,left_on='a',right_on='d'))   # 找出dfleft中a列和dfright中d列相同的行
print(pd.merge(dfleft,dfright,left_index=True,right_index=True))
print('连接类型对比')
print('inner连接')
print(pd.merge(dfleft,dfright))
print('outer连接')
print(pd.merge(dfleft,dfright,how='outer'))
print('left连接')
print(pd.merge(dfleft,dfright,how='left'))
print('right连接')
print(pd.merge(dfleft,dfright,how='right'))

# join连接
print('join连接')
print(dfleft.join(dfright,lsuffix='_left',rsuffix='_right'))
print(dfright.join(dfleft,lsuffix='_left',rsuffix='_right'))

# concat函数合并
print('concat合并')
print(pd.concat([dfleft,dfright],sort=False))
print(pd.concat([dfleft,dfright],axis=1))
print('设置索引和合并轴')
print(pd.concat([dfleft,dfright],keys=['one','two'],sort=False))
print(pd.concat([dfleft,dfright],axis=1,keys=[1,2]))

df1 = pd.DataFrame({'a':[1,2,np.nan,4],
                    'b':[5,np.nan,7,8]})
df2 = pd.DataFrame({'a':[9,10,11,np.nan],
                    'b':[13,14,15,16]})
df3 = pd.DataFrame({'c':[9,10,11,np.nan],
                    'd':[13,14,15,16]})
print('原数据')
print(df1)
print(df2)
print('相同列名combine_first')
print(df1.combine_first(df2))       # 用相同列名相同位置的数据填充
print('不同列名combine_first')
print(df1.combine_first(df3))      # 两个dataframe进行连接

# 数据重塑
print('数据重塑')
data = np.arange(12).reshape(3,4)
df = pd.DataFrame(data,columns=['a','b','c','d'],index=['fir','sec','thr'])
print('原数据')
print(df)
print('stack后')
print(df.stack())
print('unstack后')
print(df.unstack())
print('stack后再unstack')
print(df.stack().unstack())

dff = pd.DataFrame(data,columns=[['one','one','two','two'],['a','b','c','d']],index=['fir','sec','thr'])
print('原数据')
print(dff)
print('stack后')
print(dff.stack())
print('stack[0]后')
print(dff.stack(0))

