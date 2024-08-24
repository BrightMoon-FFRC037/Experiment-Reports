import cv2
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(3,sharex=True)
#Change a piture to gray scale

def color_to_gray (array):
    ans = []
    for x in range(array.shape[0]):
        temp = []
        for y in range(array.shape[1]):
            #calculate the norm of (r,g,b) vector
            v = array[x,y]
            rho = np.ones(3)*np.sqrt(1/3)
            v = np.dot(v,rho)
            temp.append(v)
        ans.append(temp)
    return np.array(ans)

#Calculate the average intensity of each column
def intensity_of_each_column(array):
    ans = []
    for column in range(array.shape[1]):
        ans.append(array.T[column].mean())
    ans = np.array(ans)
    ans = ans/(ans.max())
    ans = ans**4
    return ans

#Use two laser to calibrate the spectrum
def criterion(array):
    #Given that wavelength is linearly depends on position
    pos_red = array[0]#the position of red laser in picture
    pos_green = array[1]#the position of green laser in picture
    N = array[2]#the number of columns
    w_red = 650 #Wave length of red laser
    w_green = 532 #Wave length of green laser
    start = w_red-(w_red-w_green)*(pos_red-0)/(pos_red-pos_green)
    end =  w_green+(w_red-w_green)*(N-pos_green)/(pos_red-pos_green)
    start = int(start)
    end = int(end)
    #find out the start and end wavelength
    return [start,w_red,w_green,end]

# Open default camera (index 0)
cap = cv2.VideoCapture(0)
# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Unable to open camera.")
    exit()
# Capture a frame
ret, frame = cap.read()
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# Check if the frame is captured successfully
if not ret:
    print("Error: Unable to capture frame.")
    exit()
# Release the camera
cap.release()

#Only keep the useful part of the whole picture
cut = False
if cut:
    width = [350,620]#useful width
    height = [190,210]#useful height
    frame = frame[height[0]:height[1],width[0]:width[1],:]
#get the gray scale picture
img_gray = color_to_gray(frame)

#Use the two laser to calibrate, scince we already know the wavelength of them
calibrate = False

if calibrate:
    position_of_red = 34.8#find the positon of red laser manually
    position_of_green = 137#find the positon of red laser manually
    para = [position_of_red,position_of_green,img_gray.shape[1]]
    wavelength = criterion(para)
    #relabel the x axis
    plt.xticks([0,position_of_red,position_of_green,img_gray.shape[1]-1],wavelength)

#show the picture with color
ax[0].imshow(frame)
ax[0].set_title('Picture with Color')
#show the picture in the aspect of intensity
ax[1].imshow(img_gray,cmap='gray')
ax[1].set_title('Picture in the aspect of Intensity')
#show the spectrum (intensity for every wave length)
intensity = intensity_of_each_column(img_gray)
ax[2].bar(np.arange(len(intensity)),intensity)
ax[2].set_title('Diffraction Spectrum')
ax[2].set_xlabel('Wavelength (nm)')
plt.show()
print('Successful!!!')
