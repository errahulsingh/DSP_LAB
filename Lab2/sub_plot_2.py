import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-10,10,0.1)
x=np.sin(2*np.pi*t)
x1=np.cos(2*np.pi*t)
x2=x**2+x1**2  
x3=x+x1  # addition of two signals
x4=x*x1  # Multiplication of two signals
x5=np.sinc(t) 
x6=np.exp(t)
xn=np.arange(-10,8,0.1)
fig=plt.figure()
ax1=fig.add_subplot(6,1,1)
ax1.plot(t,x)
plt.title("x")
ax1=fig.add_subplot(6,1,2)
ax1.plot(t,x1)
plt.title("x1")
ax1=fig.add_subplot(6,1,3)
ax1.plot(t,x2)
plt.title("x*2 +x1*2")
ax1=fig.add_subplot(6,1,4)
ax1.plot(t,x3)
plt.title("x+x1")
ax1=fig.add_subplot(6,1,5)
ax1.plot(t,x4)
plt.title("x*x1")
ax1=fig.add_subplot(6,1,6)
ax1.plot(t,x5)
plt.title("sinc(t)")
ax1=fig.add_subplot(6,1,6)
ax1.plot(t,x6)
plt.title("exp(t)")
ax1=fig.add_subplot(6,1,6)
ax1.plot(t,x5)
plt.figure()
plt.plot(t,x6)
plt.show()
