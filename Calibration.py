import cv2
import numpy as np
import glob
import os
# Load the checkerboard images
#image_dir = '/home/aman/Documents/images/*.jpg'



# Detect the checkerboard corners in each image
pattern_size = (7,10) # Number of inner corners per checkerboard row and column


obj_points = [] # 3D point coordinates in real world space
img_points = [] # 2D point coordinates in image plane

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
corner = np.zeros((1, pattern_size[0] * pattern_size[1], 3), np.float32)
corner[0, :, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)
prev_img_shape = None




images = glob.glob('/home/aman/Documents/*.jpg')
for image in images:
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    found, corners = cv2.findChessboardCorners(gray, pattern_size, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
    if found == True:
        obj_points.append(corner)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        img_points.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(gray, pattern_size, corners2, found)
# Calibrate the camera
h,w = img.shape[:2]
found, K, distortion, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[1::-1], None, None)
print("Camera matrix : \n")
print(K)
print("distortion : \n")
print(distortion)
print("rvecs : \n")
print(rvecs)
print("tvecs : \n")
print(tvecs)