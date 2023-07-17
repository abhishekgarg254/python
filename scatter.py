import matplotlib.pyplot as p
import numpy as np

x=np.array([2,23,56,45,12,23,56,9,4,64,32,3,64,31,64,13,85,95,])
y=np.array([21,83,56,45,72,23,45,8,6,55,72,3,74,71,65,19,65,75,])
p.scatter(x,y,color='green')
x1=np.array([2,23,56,45,12,23,56,9,4,6])
y1=np.array([21,83,56,45,72,23,45,8,6,55])
p.scatter(x1,y1,color='red')
p.show()
