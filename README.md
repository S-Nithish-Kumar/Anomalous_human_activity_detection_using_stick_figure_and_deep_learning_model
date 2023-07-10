## Contents:
1. [Problem Statement](https://s-nithish-kumar.github.io/Anomalous_human_activity_detection_using_stick_figure_and_deep_learning_model/#1-problem-statement)
2. [Objectives](https://s-nithish-kumar.github.io/Anomalous_human_activity_detection_using_stick_figure_and_deep_learning_model/#2-objectives)
3. [Pose Estimation Model](https://s-nithish-kumar.github.io/Anomalous_human_activity_detection_using_stick_figure_and_deep_learning_model/#3-pose-estimation-model)
4. [Process Flow](https://s-nithish-kumar.github.io/Anomalous_human_activity_detection_using_stick_figure_and_deep_learning_model/#4-process-flow)
5. [Data Collection](https://s-nithish-kumar.github.io/Anomalous_human_activity_detection_using_stick_figure_and_deep_learning_model/#5-data-collection)
6. [Data Visualization and Preprocessing](https://s-nithish-kumar.github.io/Anomalous_human_activity_detection_using_stick_figure_and_deep_learning_model/#6-data-visualization-and-preprocessing)
7. [Model Training and Results](https://s-nithish-kumar.github.io/Anomalous_human_activity_detection_using_stick_figure_and_deep_learning_model/#7-model-training-and-results)
8. [Output](https://s-nithish-kumar.github.io/Anomalous_human_activity_detection_using_stick_figure_and_deep_learning_model/#8-output)
9. [Problems and Troubleshooting](https://s-nithish-kumar.github.io/Anomalous_human_activity_detection_using_stick_figure_and_deep_learning_model/#9-problems-and-troubleshooting)
10. [Conclusion](https://s-nithish-kumar.github.io/Anomalous_human_activity_detection_using_stick_figure_and_deep_learning_model/#10-conclusion)
11. [References](https://s-nithish-kumar.github.io/Anomalous_human_activity_detection_using_stick_figure_and_deep_learning_model/#11-references)

### 1. Problem Statement:
- Advanced security measures at airport borders and prisons are crucial due to the persistent threat posed by potential intruders.
+ It will be very helpful for supervisors and security guards if some intelligent system helps them with surveillance.

### 2. Objectives:
- Use an existing pose estimation algorithm to collect data points that can be used for training a Deep Learning model.
+ Visualize and preprocess the collected data points and train an Artificial Neural Network model to classify different poses such as Normal, Squat, Crawl, and Climb.
+ Based on the classification, send the signal to a microprocessor to turn on an alarm or notify authorities through a message.

### 3. Pose Estimation Model:
- MediaPipe is a Python package that consists of many pre-trained models.
+ BlazePose is one such model in MediaPipe for human pose estimation, specifically designed for applications like exercise, yoga, etc.
+ BlazePose outputs 33 key points along with two virtual key points (one at the human body center and another at the circumference of the circle).
+ The picture below shows the key points corresponding to the body parts.
<p align="center">
<img src="images/pose_landmarks.jpg" height="110%" width="110%">
</p>
<p align="center">Figure 1 Pose landmarks of the BlazePose model</p>


### 4. Process Flow:
- Figure 2 shows the block diagram of the overall working of the project. The input image is taken from the integrated webcam of the laptop and has a size of 640 by 480 pixels.
- The image is given to the BlazePose model to obtain the key points of the human body present in the image. The key points are then fed into the trained ANN model, which outputs the pose (one of the four classes—normal, climb, crawl, squat).
- The output pose, thus obtained, is sent to a microcontroller, which is programmed to turn on LEDs and a buzzer when the pose is anomalous.

<p align="center">
<img src="images/block_diagram_overall_working.png" height="110%" width="110%">
</p>
<p align="center">Figure 2 Block diagram - Overall working</p>

- Figure 3 shows the sequence flow diagram of the process. In Step 1, the input is obtained from the integrated web of the laptop and passed to the BlazePose model to check the detection confidence.
- If detection confidence is above the threshold, landmarks (key points) will be returned by the BlazePose model. The key points are sent to a deep Learning model to identify the pose.
- After the pose is found, it will be displayed on the monitor, and a signal will be sent to the Arduino microcontroller. Upon detection of anomalous activity, the buzzer connected to the controller will turn on.

<p align="center">
<img src="images/sequence_flow_diagram.png" height="110%" width="110%">
</p>
<p align="center">Figure 3 Sequence flow diagram</p>

### 5. Data Collection:
Key points from the BlazePose model are stored in a .csv file. Key points are collected for a total of four poses. Normal with labels as ‘n’; climb, squat, crawl with ‘c’, ‘q’, and "r, respectively, as labels. More details on data collection are available in the conference paper.

### 6. Data Visualization and Preprocessing:
- The collected data is visualized using correlation plots, box plots, and scatter plots.
- Using the Correlation plot, the correlation between key points and poses is identified. It has been found that only a few key points are highly correlated with the poses.
- All those highly correlated key points are visualized using box plots to find the outliers and are removed to ensure proper training of the model.
- Scatter plots are used to plot the key points of all the poses to visualize how well the poses are differentiated from each other.
- More information on data visualization and preprocessing is available in the conference paper.

### 7. Model Traning and Results:
- After data preprocessing, a three-layer deep learning ANN model is trained. The training accuracy is 94.63%, and the test data accuracy is 94.51%.
- The graph projecting the accuracy of the model for each epoch is shown in Figure 4. The accuracy of both the training and test datasets is almost similar since there is not much difference between the data points.

<p align="center">
<img src="images/model_training_accuracy.png" height="110%" width="110%">
</p>
<p align="center">Figure 4 Model training and test dataset accuracy</p>

### 8. Output:
The model has been tested with real-time inputs. Figure 5 shows the output of the model for different poses. The output from the model is sent to the Arduino microcontroller, which turns on three LEDs sequentially with a delay of 1 second after the anomalous activity is detected. Even after 3 seconds, if anomalous activity is detected, the fourth LED glows (shown in Figure 5), which confirms the anomalous activity. Instead of the fourth LED, a buzzer could be replaced.

<p align="center">
<img src="images/output_and_arduino_implementation.png" height="110%" width="110%">
</p>
<p align="center">Figure 5 Output of the ANN model and implementation using Arduino microcontroller</p>

### 9. Problems and Troubleshooting:
- The trained ANN model has limitations in terms of detection distance and camera position. The model performs well till a distance of 15 feet from the camera.
- The camera must be positioned exactly at the same angle as it was during data collection.
- To overcome the above mentioned problems, a CNN model can be trained, which is the scope of my next project.

### 10. Conclusion:
A prebuilt human pose estimation model is chosen based on the requirements, and a deep learning model is trained to classify the pose based on the inputs from the prebuilt pose estimation model, which has been successfully deployed using an Arduino microcontroller.

### 11. References:
1. Artacho B, Savakis A (2020) UniPose—unified human pose estimation in single images and videos
2. Wei S-E, Ramakrishna V, Kanade T, Sheikh Y (2016) Convolutional pose machines. The Robotics Institute Carnegie Mellon University
3. Cao Z, Hidalgo G, Simon T, Wei S-E, Sheikh Y (2018) OpenPose—realtime multi-person 2D pose estimation using part affinity fields
4. Groos D, Ramampiaro H, Ihlen EAF (2020) EfficientPose—scalable single-person pose estimation
5. Zhang H (2019) A study on human pose data anomaly detection
6. Penmetsa S, Minhuj F, Singh A, Omkar SN (2014) Autonomous UAV for suspicious action detection using pictorial human pose estimation and classification
7. Ichihara K, Takeuchi M, Katto J (2020) Accuracy evaluations of video anomaly detection using human pose estimation. In: IEEE ınternational conference on consumer electronics (ICCE)
8. https://google.github.io/mediapipe/solutions/pose.html




