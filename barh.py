import matplotlib.pyplot as p
import numpy as np

x=np.array(['physics','maths','chemistry','english'])
y=np.array([5,4,7,8])

p.barh(x,y)
p.show()

