#import required libraries
import cv2
import mediapipe as mp
import time
import math
from tensorflow.keras.models import load_model
import numpy as np
import serial

# assign the communication port and baud rate
arduino = serial.Serial('COM5',9600)
# counter is used to increase the robustness of the detection. 
# Anomalous pose will be counted and serial data for anomaly is passed only after a minimum of 3 anomaly detections.
count = 0
# passes anomaly status to the arduino. Assign a random number to the anomaly_status variable
anomaly_status = '3'

# initialize objects required for MediaPipe model
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

# initialize the camera
cap = cv2.VideoCapture(0)

# load the trained Artificial Neural Network Model
model = load_model("pose_model11.h5")

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    lmList = [] # create an empty array every time
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS) # draw landmarks on the image
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            #print(h,w,c)
            #print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h) # compute the x, y coordinates of the key points based on the image shape
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED) # draw circles on top of key points. Can be used if needed.
            lmList.append([cx, cy]) # append the key points to the empty list

    if len(lmList) != 0:
        print(lmList)
        # convert the key points into a format required by the ANN model
        lmList = np.array(lmList)
        key_points = lmList.flatten()
        res = model.predict_classes(key_points.reshape(1, 66))
        # check the output with the following conditions and update the anomaly_status
        if(res == [0]):
            cv2.putText(img, str("Climb"), (70, 50), cv2.FONT_HERSHEY_PLAIN, 5,(0, 0, 255), 4)
            cv2.rectangle(img, (0, 0), (640, 480), (0, 0, 255),6)
            anomaly_status= '1'
            count = count + 1
        elif(res == [1]):
            cv2.putText(img, str("Crawl"), (70, 50), cv2.FONT_HERSHEY_PLAIN, 5,(0, 0, 255), 4)
            cv2.rectangle(img, (0, 0), (640, 480), (0, 0, 255), 6)
            anomaly_status = '1'
            count = count + 1
        elif(res == [2]):
            cv2.putText(img, str("Normal"), (70, 50), cv2.FONT_HERSHEY_PLAIN, 5,(0, 255, 0), 4)
            cv2.rectangle(img, (0, 0), (640, 480), (0, 255, 0), 6)
            anomaly_status = '2'
            count = 0 # Re-initialize the counter if the pose is normal
        elif(res == [3]):
            cv2.putText(img, str("Squat"), (70, 50), cv2.FONT_HERSHEY_PLAIN, 5,(0, 0, 255), 4)
            cv2.rectangle(img, (0, 0), (640, 480), (0, 0, 255), 6)
            anomaly_status = '1'
            count = count + 1

    if (count >= 3 and anomaly_status=='1'):
        arduino.write(str.encode(anomaly_status))
        print(str.encode(anomaly_status))
        count = 0
        time.sleep(0.8) # this time delay makes signal to be sent every 1 sec including the processing time on an average.
    elif(anomaly_status=='2'):
        arduino.write(str.encode(anomaly_status))
        print(str.encode(anomaly_status))
        time.sleep(0.2) # this time delay is used to avoid overload in the serial buffer of Arduino.

    cv2.imshow("Image", img)
    cv2.waitKey(2)