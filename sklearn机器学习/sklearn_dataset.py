from sklearn.datasets import load_iris        #加载自带的鸢尾花数据集
import numpy as np

iris = load_iris()
print('数据属性',iris.keys())
print(iris.data.shape)
print(iris.data)
# print(type(iris.data))
print(iris.target)
print(iris.target_names)  # 结果集，包含三种不同的鸢尾花种类
print(iris.DESCR) # describtion 鸢尾花数据集的描述
print()
print(iris.feature_names)   # 属性名
print(iris.filename)

# 鸢尾花数据集的柱状图
print('---------------------鸢尾花数据集的柱状图-------------------------')
import matplotlib.pyplot as plt

x_index = 3
color = ['green','red','blue']
'''
当zip()函数有两个参数时,zip(a,b)zip()函数分别从a和b依次各取出一个元素组成元组，
再将依次组成的元组组合成一个新的迭代器--新的zip类型数据。要求a与b的维数相同，
当两者具有相同的行数与列数时，正常组合对应位置元素即可；
当a与b的行数或列数不同时，取两者结构中最小的行数和列数，依照最小的行数和列数将对应位置的元素进行组合；
这时相当于调用itertools.zip_longest(*iterables)函数。
'''
for lable,color in zip(range(len(iris.target_names)),color):
    plt.hist(iris.data[iris.target==lable,x_index],label=iris.target_names[lable],color=color)
    plt.xlabel(iris.feature_names[x_index])
    print(iris.data[iris.target==lable,x_index])
    print(len(iris.data[iris.target==lable,x_index]))
    plt.legend()
plt.show()
print('y轴是某个宽度鸢尾花的个数')

print('---------------------鸢尾花散点图------------------------------')
x_index = 0
y_index = 1
colors = ['red','blue','green']
for lable,color in zip(range(len(iris.target_names)),colors):
    plt.scatter(iris.data[iris.target==lable,x_index],iris.data[iris.target==lable,y_index],
                label=iris.target_names[lable],c=color)        # c=color不能是c=colors???
    plt.xlabel(iris.feature_names[x_index])
    plt.ylabel(iris.feature_names[y_index])
    plt.legend()
plt.show()
print('c=color不能是c=colors???')
print()

print('--------------------------乳腺癌数据集------------------------')

from sklearn.datasets import load_breast_cancer
breast_cancer = load_breast_cancer()
print('简单经典的用于二分类任务的数据集')
print('数据属性',breast_cancer.keys())

print()
print('其他数据集')
from sklearn.datasets import load_boston
from sklearn.datasets import load_diabetes
from sklearn.datasets import load_digits
from sklearn.datasets import load_linnerud
from sklearn.datasets import load_wine
print('波士顿房价数据集load-boston是经典的用于回归任务的数据集')
print('波士顿房价数据集的数据属性为',load_boston().keys())
print('糖尿病数据集load-diabetes是经典的用于回归任务的数据集')
print('手写数字数据集load_digits适用于多分类任务的数据集')
print('体能训练数据集load-linnerud是经典的用于多变量回归任务的数据集，其内部包含两个小数据集'
      '：Excise是对三个训练变量（引体向上、仰卧起坐、立定跳远）的20次观测；physiological是对'
      '三个生理学变量（体重、腰围、脉搏）的20次观测')
print(load_linnerud().keys())
print(load_linnerud().target)
print(load_linnerud().target_names)
print(load_linnerud().feature_names)
print('葡萄酒数据集load-wine包括了3中酒中13中不同成分的数量，共178个样本，对应三种葡萄酒')
print(load_wine().target_names)
print(load_wine().keys())
print(load_wine().feature_names)