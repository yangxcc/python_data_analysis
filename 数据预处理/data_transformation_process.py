import pandas as pd
import numpy as np

# 虚拟变量
df = pd.DataFrame({'name':pd.Series(['小明','小红','小李','小王']),
                   'gender':pd.Series(['男','女','男','女']),
                   'age':pd.Series([23,24,25,26]),
                   'class':pd.Series(['1班','2班','3班','4班'])})
print(pd.get_dummies(df['gender']))
print(pd.get_dummies(df['class']))

# 函数变换
a = np.random.randint(10,size=(3,4))
print(a)
df = pd.DataFrame(a)
print(df.where(df%3==0,-df))
print(df.where(df>0,-df))
print(df.apply(lambda x:x**2))
def f(x):
    if x > 5:
        return 1
    else:
        return 0
print(df.applymap(f))

# 连续属性离散化
print('连续属性离散化')
s = np.random.rand(20)
print(s)
cuts = pd.cut(s,4)   # 等宽分成4个组
print(cuts)
print(cuts.codes)       # 数据在哪个区间
print(cuts.categories,type(cuts.categories))
print(cuts.value_counts(cuts))
cuts = pd.cut(s,[0,0.2,0.4,0.6,0.8,1])  # 自定义区间宽度和数量
print(cuts.codes)
print(cuts.categories,type(cuts.categories))
print(cuts.value_counts(cuts))

ss = np.random.rand(30)
cuts = pd.qcut(ss,5)   # 等频法，5个组中数据个数相同
print(cuts)
print(cuts.codes)
print(cuts.categories,type(cuts.categories))
print(cuts.value_counts(cuts))

# 数据规范化
df = pd.DataFrame({'a':np.random.randint(1,10,100),
                   'b':np.random.randint(500,1000,100)})
print('待规范的数据')
print(df)
print('最小-最大规范化，离差标准化')
print(df.apply(lambda x:(x-x.min())/(x.max()-x.min())))   # 最小-最大规范化，离差标准化
print('零-均值规范化，标准差规范化')
print(df.apply(lambda x:(x-x.mean())/x.std()))            # 零-均值规范化，标准差规范化
print('小数定标标准化')
print(df.apply(lambda x:(x/10**np.ceil(np.log10(x.abs().max())))))    # 小数定标标准化

# 随机采样
data = np.arange(50).reshape(10,5)
df = pd.DataFrame(data)
sampler = np.random.permutation(len(df))
print('全部数据为')
print(df)
print('行随机排列')
print(df.take(sampler))
print('列随机排列')
print(df.take(np.random.permutation(5),axis=1))
print('行数据随机取样3个')
print(df.take(sampler)[:3])

print('sample函数的应用')
data1 = np.arange(50).reshape(10,5)
df = pd.DataFrame(data1)
print('按比例')
print(df.sample(frac=0.5))
print('按数量')
print(df.sample(n=4))