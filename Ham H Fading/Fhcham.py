import numpy as np
import matplotlib.pyplot as plt

# Sử dụng Clark's Models
fc = 10e4 #tần số tần số sóng mang Hz
Fs = 10e5 # tốc độ lấy mẫu
N = 100 #số lượng tính tổng sóng sin trên đường truyền
v = 30 # vận tốc m/s
fd = v*fc/3e8 # max Doppler shift

print("max Doppler shift:", fd)
t = np.arange(0, 4, 1/Fs) # vector thời gian (start, stop, step)
x = np.zeros(len(t)) # Tạo mảng 2 chiều theo t cho x
y = np.zeros(len(t)) # Tạo mảng 2 chiều theo t cho y

for i in range(N):
    alpha = (np.random.rand() - 0.5) * 2 * np.pi # tính alpha trong hàm cos 
    phi = (np.random.rand() - 0.5) * 2 * np.pi # tính phi của hàm hi và hq
    x = x + np.random.randn() * np.cos(2 * np.pi * fd * t * np.cos(alpha) + phi) # hàm hi
    y = y + np.random.randn() * np.sin(2 * np.pi * fd * t * np.cos(alpha) + phi) # hàm hq

z = (1/np.sqrt(N)) * (x + 1j*y) #hàm tính tổng và là hàm h(nT)
z_mag = np.abs(z) # lấy giá trị tuyệt đối 
z_mag_dB = 10*np.log10(z_mag) # chuyển sang dB

plt.plot(t, z_mag_dB)
plt.plot([0, 3], [0, 0], ':r') # hàm z , hàm 0dB 
plt.legend(['Rayleigh Fading', 'No Fading']) 
plt.xlabel("Thời gian t")
plt.ylabel("Giá trị của hàm ")
plt.title('Mô Phỏng Fading')
plt.grid(True)
plt.axis([0,4,-25,5])  # xmin, xmax, ymin, ymax
plt.show()