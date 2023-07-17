import matplotlib.pyplot as p
import numpy as np

x=np.array([2,23,56,45,12,23,56,])
y=np.array([21,83,56,45,72,23,45])
color=np.array(['green','blue','red','yellow','black','orange','pink'])
p.scatter(x,y,c=color)
p.show()
