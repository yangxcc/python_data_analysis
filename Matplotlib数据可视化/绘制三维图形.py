import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# #三维曲线图
# ax=plt.axes(projection='3d')
# x=np.linspace(0,40,1000)
# y=np.sin(x)
# z=np.cos(x)
# ax.plot3D(x,y,z,c='blue')
# plt.show()
#
# #散点图
# axs=plt.axes(projection='3d')
# m,n,p=np.random.random(500),np.random.random(500),np.random.random(500)
# axs.scatter(m,n,p)
# plt.show()

# #曲面图
from mpl_toolkits.mplot3d import Axes3D
#
# fig=plt.figure()
# ax=Axes3D(fig)
# X=Y=np.linspace(-2.048,2.048,100)
# x,y=np.meshgrid(X,Y)
# z=100*(y-x-2)**2+(1-x)**2
# ax.plot_surface(x,y,z)
# plt.show()

# 等高线
ax=plt.axes(projection='3d')
X=np.linspace(-5.12,5.12,100)
Y=X
x,y=np.meshgrid(X,Y)
z=(3/(0.05+x**2+y**2))**2+(x**2+y**2)**2
ax.contour(x,y,z,30)   #30是等高线的条数
plt.show()

# 绘制z轴等高线
plt.subplot(2,2,1)
ax1=plt.axes(projection='3d')
ax1.plot_surface(x,y,z)
plt.contour(x,y,z,30,offset=1,zdir='z')   #zdir是等高线的方向。xyz，默认为z
plt.show()

#绘制二维等高线
plt.contour(x,y,z,1000)
plt.show()