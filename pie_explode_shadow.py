import matplotlib.pyplot as p
import numpy as np

x=np.array([45,56,25,23])
l=["Abhishek","Aditya","Ashish","Shivam"]
a=[0.1,0.3,0.4,0]
p.pie(x,labels=l,explode=a,shadow=True)
p.show()

