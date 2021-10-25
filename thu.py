#vẽ đồ thị của hàm số y(t)=-10cos(2fpit) sau khi qua pathloss
#l=10km
import math
import numpy as np
import matplotlib.pyplot as plt
Pin=10*10/2
l=10
print(Pin,"W")
stt=int(input("nhập một số tự nhiên từ 1 tới 7:"))
if stt==1:
	a=0.05
	f=1
	t1=-1
	t2=1
	print("sóng truyền trong open-wire pair(0.3 cm diameter)")
	print("tần số của sóng mang",f,"kHz")
elif stt==2:
	f=int(input("chọn tần số sóng mang(10,100,300kHz):"))
	if f==10:
		a=2
		t1=-0.1
		t2=0.1
	elif f==100:
		a=3
		t1=-0.01
		t2=0.01
	elif f==300:
		a=6
		t1=-0.003
		t2=0.003
	print("sóng truyền trong Twisted-wire pair(16 gauge)")
	print("tần số của sóng mang",f,"kHz")
elif stt==3:
	f=float(input("chọn tần số sóng mang(0.1,1,3MHz):"))
	if f==0.1:
		a=1
		t1=-10
		t2=10
	elif f==1:
		a=2
		t1=-1
		t2=1
	elif f==3:
		a=4
		t1=-0.3
		t2=0.3
	print("sóng truyền trong Coixal cable(1 cm diameter)")
	print("tần số của sóng mang",f,"MHz")
elif stt==4:
	a=1.5
	f=100
	t1=-0.01
	t2=0.01
	print("sóng truyền trong Coixal cable(15 cm diameter)")
	print("tần số của sóng mang",f,"MHz")
elif stt==5:
	a=5
	f=10
	t1=-0.1
	t2=0.1
	print("sóng truyền trong Rectangular waveguide(5x2.5cm)")
	print("tần số của sóng mang",f,"GHz")
elif stt==6:
	a=1.5
	f=100
	t1=-0.01
	t2=0.01
	print("sóng truyền trong Helical waveguide(5 cm diameter")
	print("tần số của sóng mang",f,"GHz")
elif stt==7:
	f=int(input("chọn tần số sóng mang(360,240,180 ngàn GHz):"))
	if f==360:
		a=1
		t1=-0.005
		t2=0.005
	elif f==240:
		a=2
		t1=-0.01
		t2=0.01
	elif f==180:
		a=4
		t1=-0.01
		t2=0.01
	print("sóng truyền trong Fiber-optic cable")
	print("tần số của sóng mang",f,"GHz")
print("hệ số suy hao",a)
L=10**(-a*l/10)
print("số lần suy hao",L)
Pout=L*Pin
print("công cuất của tín hiệu ngõ ra",Pout)
a1=math.sqrt(Pout*2)
t=np.arange(t1,t2,0.000001)
y=10*np.cos(np.pi*t*2*f)
yout=a1*np.cos(np.pi*t*2*f)
plt.style.use('seaborn-whitegrid')
plt.plot(t,yout, color="red", label="yout(t)")
plt.plot(t,y, color="blue", label="y(t)")
plt.legend()
plt.xlabel("giá trị của t")
plt.ylabel("giá trị của hàm ")
plt.title("COSE SINE WAVE")
plt.axis("tight")
plt.show()






