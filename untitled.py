import matplotlib.pyplot as p
import numpy as np
x=np.random.randint(100,size=(100))
y=np.random.randint(100,size=(100))
color=np.random.randint(100,size=(100))
size=7*np.random.randint(100,size=(100))
p.scatter(x,y,s=size,c=color,cmap='nipy_spectral')
p.colorbar()
p.show()
