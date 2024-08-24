import cv2
import matplotlib.pyplot as plt

fig,ax = plt.subplots()

# Open default camera (index 0)
cap = cv2.VideoCapture(1)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Unable to open camera.")
    exit()

# Capture a frame
ret, frame = cap.read()

# Check if the frame is captured successfully
if not ret:
    print("Error: Unable to capture frame.")
    exit()

# Release the camera
cap.release()


print(type(ret))
print(type(frame))
print(ret)
print(frame.shape)
ax.imshow(frame)

plt.show()