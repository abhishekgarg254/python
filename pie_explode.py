import matplotlib.pyplot as p
import numpy as np

x=np.array([45,56,25,23])
l=["Abhishek","Aditya","Ashish","Shivam"]
a=[0.1,0.6,0.4,0.2]
p.pie(x,labels=l,explode=a)
p.show()

