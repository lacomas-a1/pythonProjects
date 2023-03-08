#create and plot sin() and cos() in 2 different subplots.
import numpy as np
import matplotlib.pyplot as plt

xstart =0
xstop =2*np.pi
increment =0.1

x = np.arange(xstart ,xstop, increment)
y = np.sin(x)
z =np.cos(x)

plt.subplot(2,1,1)
plt.plot(x,y,'g')
plt.title('sin')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid()
plt.show()

plt.subplot(2,1,2)
plt.plot(x,z,'r')
plt.title('cos')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.grid()
plt.show()