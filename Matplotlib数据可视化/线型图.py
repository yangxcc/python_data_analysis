import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-np.pi,np.pi,25)  #线的平滑程度取决于点的多少，为了显示平滑曲线，需要设置足够多的坐标点
y,z=np.sin(x),np.cos(x)
#plt.plot(x,y,x,z)
plt.figure(1)
plt.plot(x,y,marker='D',linewidth=1)
plt.plot(x,z,marker='o',linewidth=5)
plt.plot([0.5,1,-0.5,1])
plt.show()

#散点图
plt.figure(2)
m=np.random.randn(500)
n=np.random.randn(500)
plt.scatter(m,n,c='red',marker='d',s=4,alpha=0.3)
plt.show()

#柱形图
plt.figure(3)
xx=np.array([2013,2014,2015,2016,2017,2018,2019])
yy=np.array([20000,32000,35000,58000,45000,55000,66000])
zz=np.array([10000,24000,30000,28000,5200,51000,60000])
plt.rcParams['font.sans-serif']=['SimHei']  #黑体字体
plt.rcParams['font.serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False  #解决保存图像是符号‘-’显示为方块问题，或者转换负号为字符串
plt.bar(xx,yy,width=0.4,color='r',label='a公司收入')
plt.bar(xx,zz,width=0.4,color='b',label='b公司收入')
plt.legend(loc=0)
plt.show()

#条形图
plt.figure(4)
position=np.arange(1,6)
a=np.random.random(5)
b=np.random.random(5)
plt.barh(position,a,color='b',label='a')
plt.barh(position,-b,color='r',label='b')
plt.legend(loc=0)
plt.show()

#饼图
plt.figure(5)
x=[12,23,18,16]
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.serif']=['SimHei']
labels=['张三','李四','王五','赵六']
colors=['red','yellow','blue','green']
explode=[0,0.1,0,0]
plt.pie(x,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90,radius=1.5)
plt.show()

#直方图
plt.figure(6)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
data=np.random.randn(10000)
plt.hist(data,bins=40,density=0,facecolor='yellow',edgecolor='blue',alpha=0.7)
#MatplotlibDeprecationWarning:The 'normed' kwarg was deprecated in Matplotlib 2.1 and will
# be removed in 3.1. Use 'density' instead.
plt.xlabel('区间')
plt.ylabel('频数/频率')
plt.title('频数/频率分布直方图')
'''
bins直方图的长条形数目，可选项，默认为0
normed是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率
facecolor长条形的颜色    edgecolor长条形边框颜色     alpha 透明度
'''
plt.show()

#箱线图
plt.figure(7)
data=np.random.rand(12,4)   #竖着的
print(data)
plt.boxplot(data)
plt.show()