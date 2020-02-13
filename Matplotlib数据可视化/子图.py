import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-np.pi,np.pi,50)
y1,y2=np.sin(x),np.cos(x)

# fig=plt.figure(figsize=(5,2))
# plt.plot(x,y1)
# fig=plt.figure(figsize=(5,2))
# plt.plot(x,y2)
# plt.show()

y3,y4=np.tan(x),np.power(x,2)
# plt.subplot(2,2,1)       #subplot(nrows,ncols,plot_number),参数nrows,ncols表示行数和列数，plot_number表示当前是第几个字图
# plt.plot(x,y1)
# plt.subplot(2,2,2)
# plt.plot(x,y2)
# plt.subplot(2,2,3)
# plt.plot(x,y3)
# plt.subplot(2,2,4)
# plt.plot(x,y4)
# plt.show()

# fig,ax=plt.subplots(2,2)   #把画布分成2行2列
# # print(ax)
# # print(fig)
# ax[0,0].plot(x,y1)
# ax[0,1].plot(x,y2)
# ax[1,0].plot(x,y3)
# ax[1,1].plot(x,y4)
# plt.show()

#子图坐标系设置

fig,ax=plt.subplots(1,2)
axes=ax[0]
axes.plot(x,y1,label='sin')
axes.set_xlabel('x轴',fontproperties='SimHei')
axes.set_ylabel('y轴',fontproperties='SimHei')
axes.set_title('正弦函数',fontproperties='SimHei')
axes.text(0,0,'正弦曲线',fontproperties='SimHei')
axes.set_xlim(-np.pi,np.pi)
axes.set_ylim(-1,1)
axes.set_xticks([-np.pi,np.pi])
axes.set_yticks([-1,0,1])
axes.plot(x,y2,label='cos')
axes.legend()
axes=ax[1]
axes.plot(x,y3,'r*--')
axes.set_title('正切弦函数',fontproperties='SimHei')
plt.show()

#图形嵌套

fig=plt.figure()
xx=np.linspace(1,4*np.pi,100)
left,bottom,width,height=0.1,0.1,0.8,0.8
ax1=fig.add_axes([left,bottom,width,height])
ax1.plot(xx,np.power(xx,2),'r')
ax1.set_title('power')
left,bottom,width,height=0.2,0.6,0.25,0.25
ax2=fig.add_axes([left,bottom,width,height])
ax2.plot(xx,np.sqrt(xx),'g')
ax2.set_title('sqrt')
plt.axes([bottom,left,width,height])
plt.plot(xx,np.sin(xx),'b')
plt.title('sin')
plt.show()