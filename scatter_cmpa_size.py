import matplotlib.pyplot as p
import numpy as np

x=np.array([2,23,56,45,12,23,56,])
y=np.array([21,83,56,45,72,23,45])
color=np.array([13,4,51,7,8,4,9])
size=np.array([100,200,560,780,450,650,700])
p.scatter(x,y,c=color,cmap='viridis',s=size,alpha=0.5)
p.show()
