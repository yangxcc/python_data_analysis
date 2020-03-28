import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'a':[1,2,33,4],
                   'b':[5,6,7,8],
                   'c':[9,10,11,122],
                   'd':[13,14,15,16]})
df['e'] = [1,2,3,4]   # 添加一列e
df.boxplot()        # 画箱型图
df.plot(kind='scatter',x='e',y='a')   # 画散点图
plt.show()