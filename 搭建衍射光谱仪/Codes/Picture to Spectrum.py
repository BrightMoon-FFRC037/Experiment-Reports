import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(2,sharex=True)
#读入照片
name = 'Hydrogen'
#name = 'Light in Library'
#name = 'Oxygen'
img = Image.open(name+'.png')
gray_img = img.convert('L')
color_img = img.convert('RGB')


width, height = img.size
gray_data = []
color_data = []
for y in range(height):
    gray_temp = []
    color_temp = []
    for x in range(width):
        gray_temp.append(gray_img.getpixel((x,y)))
        color_temp.append(color_img.getpixel((x,y)))
    gray_data.append(gray_temp)
    color_data.append(color_temp)

gray_data = np.array(gray_data)
color_data = np.array(color_data)
#显示彩色原图
ax[0].imshow(color_data)


#对灰度图按列纵向分割，每列计算灰度平均值
average = []
for i in range(gray_data.shape[1]):#列中循环
    average.append(gray_data.T[i].mean())
average = np.array(average)
average = average/(average.max())

#绘制光谱图
ax[1].bar(np.arange(len(average)),average)
plt.title('Spectrum of '+name)
plt.show()
