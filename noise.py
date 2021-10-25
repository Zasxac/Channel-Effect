#vẽ đồ thị của hàm số y(t)=-10cos(40pit)+4sin(120pit) sau khi qua FSPL
#Pout=Gt.Gr/L.Pin
#Gt=90db, Gr=30db
#l=5km
#Bn=60Khz
#N/2=10**(-11)
import math
import numpy as np
import matplotlib.pyplot as plt
def function(a,f,l):
	Ldb=92.4+20*math.log10(f)+20*math.log10(l)
	L=120-Ldb
	Pout=(a**2)/2*(10**(L/10))
	return Pout
a1=math.sqrt(function(10,20,5)*2)
a2=math.sqrt(function(4,60,5)*2)
print("y(t)=-10cos(40pit)+4sin(120pit)")
print("yout(t)=",a1,"cos(40pit)+",a2,"cos(120pit)")
Sd=function(10,20,5)+function(4,60,5)
print("công xuất của tín hiệu sau pathloss=", Sd)
Nd=10**(-11)*2*60*(10**3)*10**(30/10)
Pout=Sd+Nd
print("công suất ngõ ra lúc cộng nhiễu=", Pout)
SNR=Sd/Nd
print("tỉ số tín hiệu trên nhiễu=", SNR) 
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