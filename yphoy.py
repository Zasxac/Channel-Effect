#vẽ đồ thị cảu hàm số y(t)=7-10cos(40pit)+4sin(120pit)
import numpy as np
import matplotlib.pyplot as plt
print("y=7-10cos(4pit+4sin(120pit)")
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,5),sharey= True,dpi=150)
t=np.arange(-0.05,0.05,0.001)
y=7-10*np.cos(np.pi*t*40-np.pi/3)+4*np.sin(np.pi*t*120)
plt.style.use('seaborn-whitegrid')
ax1.plot(t,y, color="red", label="y(t)")
ax1.set(title="cose sine wave",
		xlabel="giá trị của t",
		ylabel="giá trị của hàm ")

#vẽ phổ của đồ thị y(t)
f=[-60,-20,0,20,60]
pho=[2,5,7,5,2]
width=2
ax2.bar(f,pho,width)
ax2.set(title="Phổ của y(f)",
	   xlabel="tần số",
	   ylabel="biên độ")
plt.axis("tight")

plt.legend()
plt.show()