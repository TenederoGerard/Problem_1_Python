import numpy as np
import matplotlib.pyplot as plt

#Values in which the function will be based on
f=np.arange(0,100)

#Value of the index
for i in range(0,100): 
    if f[i]<=9:
        f[i]=(f[i]**2)-7
 
#Returns the value of the index to 10       
    elif f[i]>=10:
        f[i]=f[i-10]
        
plt.stem(f,use_line_collection=True)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show

