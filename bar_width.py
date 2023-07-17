import matplotlib.pyplot as p
import numpy as np

x=np.array(['physics','maths','chemistry','english'])
y=np.array([5,4,7,8])

p.bar(x,y,color='red',width=0.2)
p.show()

