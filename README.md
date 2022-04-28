### DeepLearning
# Files Consist of:
1. MotionCapture.py
* Takes an input mp4 file and runs MediaPipe markerless motion capture
* Produces a txt file of the positions for each of the keypoints generated during the video
2. results.py
* Cosine Similarity for evaluating Pose Estimation 
3. AnimationCode.cs
* Creates an animation from the txt file with keypoints from MotionCapture.py
* This runs the Unity3D animation file
5. Lines.cs
* Contains connecting segements between keypoints for Unity3D

6. JohnHollinger.mp4
* Video of pro soccer player for the Maryland Bobcats

7. OpenPose_KeyPoints.zip
* Key points files generated through OpenPose

8. Vicon_Motion_Capture_keypoints.zip
* Key points files generated through Vicon motion capture system
![image](https://user-images.githubusercontent.com/66143861/165653343-d844a4b0-2f47-483b-8439-00561dd89b7f.png)
