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
