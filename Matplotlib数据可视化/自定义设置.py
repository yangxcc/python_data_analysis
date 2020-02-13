#图例设置

import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
x=np.linspace(0,2*np.pi,200)
y1=np.sin(x)
y2=np.cos(x)
y3=np.sqrt(x)
plt.plot(x,y1,'--',label='sin')
plt.plot(x,y2,'r:',label='cos')
plt.plot(x,y3,'b-',label='sqrt')
plt.legend(loc='upper left',fontsize=12,edgecolor='r',facecolor='g')
plt.show()

'''
loc 图例所有figure位置
fontsize 字号大小
markerscale 图例标记与原始标记的相对大小
edgecolor 图例框的边界颜色
facecolor 图例框的颜色
'''

#坐标网格设置

plt.figure(2)
z1=np.sin(x)
z2=np.cos(x)
plt.plot(x,z1,'--',label='sin')
plt.plot(x,z2,'r:',label='cos')
plt.grid(color='g',linestyle='-',linewidth=2)
plt.show()
'''
axis 默认axis='both'，还可以设置为‘x’或者'y'，分别表示表格线是垂直于x轴还是y轴
color 设置表格线的颜色
linestyle 设置表格线的线形，例如linestyle=‘-’
linewidth 设置表格线的宽度，例如linewidth=2
'''

#坐标系设置
plt.figure(3)
z3=np.sin(x)
plt.plot(x,z3,'--',label='sin')
plt.title('正弦函数图象',fontproperties='SimHei')   #添加标题
plt.xlabel('x轴',fontproperties='SimHei')  #添加x轴名称
plt.ylabel('y轴',fontproperties='SimHei')   #添加y轴名称
plt.xlim([-np.pi,2*np.pi])       #指定x轴范围，是一个区间
plt.ylim([-2,2])                 #指定y周范围，是一个区间
plt.xticks([-3,-2,-1,0,1,2,3])   #指定x轴的数目和取值
plt.yticks([-1,0,1,2])           #指定y轴的数目和取值
plt.show()

#样式设置和注解

print('matplotlib提供的绘制图形的样式：',plt.style.available)
plt.style.use('ggplot')
plt.subplot(2,2,1)   #两行两列，第一个图
plt.plot(x,np.sin(x))
plt.text(np.pi/2,1,'最大值',fontproperties='SimHei') #在任意位置增加文本，前两个参数是横纵坐标
plt.annotate('最小值',(3*np.pi/2,-1),(3*np.pi/2,-0.5),fontproperties='SimHei',arrowprops=dict(facecolor='black',shrink=0.05))
plt.style.use('bmh')
plt.subplot(2,2,2)
plt.plot(x,np.cos(x))
plt.show()

#pyplot使用Rc配置文件来自定义图形的各种默认属性，因此可以通过设置Rc参数修改图形的属性，比如现款、线条样式、坐标轴、字体等
'''
Rc参数设置的配置文件。所以设置后的图形绘制都会改变，与通过函数设置只改变当前一个作图不同
'''