import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.datasets import make_classification
from sklearn.datasets import make_circles

print('make_blobs()函数生成数据集')
center = [[1,1,1],[-1,-1,-1],[1,-1,1]]
cluster_std = 0.3   # 表示每个类别的方差
X,labels = make_blobs(n_samples=200,centers=center,n_features=2,cluster_std=cluster_std,random_state=0)
# n_feature表示每个样本的特征数
print('X.shape',X.shape)
print(X)
print('labels',set(labels))
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0,1,len(unique_labels)))
print('color',colors)
for k,col in zip(unique_labels,colors):
    x_k = X[labels==k]
    print('-----------')
    print(col)
    plt.plot(x_k[:,0],x_k[:,1],'o',markerfacecolor=col,markeredgecolor='k',markersize=4)
plt.show()

print('-----------------------------------')

print('make_classification()函数生成数据集')
X,labels = make_classification(n_samples=200,n_features=2,n_redundant=0,n_informative=2,random_state=1,n_clusters_per_class=2)
# make_classification()为每个类分配一个或者多个正态分布的点集，提供为数据添加噪声的方法，包括维度相关性，无效特征以及冗余特征等。
unique_labels = set(labels)
print(unique_labels)
print(X.shape)
colors = plt.cm.Spectral(np.linspace(0,1,len(unique_labels)))
for k,col in zip(unique_labels,colors):
    x_k = X[labels==k]
    plt.plot(x_k[:, 0], x_k[:, 1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=8)
plt.show()

print('make_circle()函数生成数据集')
# make_circles()产生二维二元分类数据集来测试某些算法的性能，可以为数据集增加噪声，可以为二元分类器产生一些球形
# 判决界面的数据
data,target = make_circles(n_samples=200,noise=0.2,factor=0.2,random_state=1)
print('X.shape',data.shape)
print('labels:',set(target))
unique_labels = set(target)
colors = plt.cm.Spectral(np.linspace(0,1,len(unique_labels)))
for k,col in zip(unique_labels,colors):
    x_k = data[target==k]
    plt.plot(x_k[:, 0], x_k[:, 1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=8)
plt.show()