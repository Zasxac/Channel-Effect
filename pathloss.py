#vẽ đồ thị của hàm số y(t)=-10cos(40pit)+4sin(120pit) sau khi qua FSPL
#Pout=Gt.Gr/L.Pin
#Gt=90db, Gr=30db
#l=5km
import math
import numpy as np
import matplotlib.pyplot as plt
print("y=-10cos(40pit)+4sin(120pit)")
def function(a,f,l):
	Ldb=92.4+20*math.log10(f)+20*math.log10(l)
	L=120-Ldb
	Pout=(a**2)/2*(10**(L/10))
	c=math.sqrt(Pout*2)
	return c
a1=function(10,20,5)
a2=function(4,60,5)
print("yout=",a1,"cos(40pit)",a2,"sin(120pit)")
t=np.arange(-0.05,0.05,0.001)
y=-10*np.cos(np.pi*t*40-np.pi/3)+4*np.sin(np.pi*t*120)
yout=-a1*np.cos(np.pi*t*40-np.pi/3)+a2*np.sin(np.pi*t*120)
plt.style.use('seaborn-whitegrid')
plt.plot(t,yout, color="red", label="yout(t)")
plt.plot(t,y, color="blue", label="y(t)")
plt.legend()
plt.xlabel("giá trị của t")
plt.ylabel("giá trị của hàm ")
plt.title("COSE SINE WAVE")
plt.axis("tight")
plt.show()