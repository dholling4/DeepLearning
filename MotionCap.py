import cv2
from cvzone.PoseModule import PoseDetector
import os
from mediapipe.python.solutions import pose
from sklearn.metrics.pairwise import cosine_similarity
trial_name = "JohnHollinger"
cap = cv2.VideoCapture(trial_name + '.mp4')

# Create Detector
detector = PoseDetector()
posList = []

while True:
    try:
        success, img = cap.read()
        assert isinstance(img, object)
        img = detector.findPose(img)
        # Find landmarks from a list
        lmList, bboxInfo = detector.findPosition(img)

        # Do something (send to list) if bounding box is empty
        if bboxInfo:
            lmString = ''  # create string containing 33 key points to loop through
            for lm in lmList:
                # create fstring for eachs keypoint
                # x, y, z location (OpenCV origin -> top left, Unity3D starting point -> bottom left)
                lmString += f'{(lm[1])}, {img.shape[0] - lm[2]}, {lm[3]},'  # each frame of animation
            posList.append(lmString)

        print('Frame: ', len(posList), 'Time: ', len(posList) / 30)
        #       'Co similarity', cosine_similarity())

        cv2.imshow("Image", img)
        # Save whenever you press the 's' key on your keyboard
        key = cv2.waitKey(1)
        #if key == ord('s'):
        #if (len(posList) <= 261):
    except:
        break;

with open(trial_name + ".txt", 'w') as f:
    # loop through all position items in the list and insert it line by line
    f.writelines(["%s\n" % item for item in posList])

#############################################################################################
# # Run live pose estimation
#############################################################################################
# from cvzone.PoseModule import PoseDetector
# import cv2
#
# cap = cv2.VideoCapture(0)
# detector = PoseDetector()
# while True:
#     success, img = cap.read()
#     img = detector.findPose(img)
#     lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
#     if bboxInfo:
#         center = bboxInfo["center"]
#         cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
#
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)
#
#
# import cv2
# import numpy as np
# import time
# import math
#
#
# class LivePlot:
#     def __init__(self, w=640, h=480, yLimit=[0, 100],
#                  interval=0.001, invert=False, char=' '):
#
#         self.yLimit = yLimit
#         self.w = w
#         self.h = h
#         self.invert = invert
#         self.interval = interval
#         self.char = char[0]
#         self.imgPlot = np.zeros((self.h, self.w, 3), np.uint8)
#         self.imgPlot[:] = 225, 225, 225
#
#         cv2.rectangle(self.imgPlot, (0, 0),
#                       (self.w, self.h),
#                       (0, 0, 0), cv2.FILLED)
#         self.xP = 0
#         self.yP = 0
#
#         self.yList = []
#
#         self.xList = [x for x in range(0, 100)]
#         self.ptime = 0
#
#     def update(self, y, color=(255, 0, 255)):
#
#         if time.time() - self.ptime > self.interval:
#
#             # Refresh
#             self.imgPlot[:] = 225, 225, 225
#             # Draw Static Parts
#             self.drawBackground()
#             # Draw the text value
#             cv2.putText(self.imgPlot, str(y),
#                         (self.w - (125), 50), cv2.FONT_HERSHEY_PLAIN,
#                         3, (150, 150, 150), 3)
#             if self.invert:
#                 self.yP = int(np.interp(y, self.yLimit,
#                                         [self.h, 0]))
#             else:
#                 self.yP = int(np.interp(y, self.yLimit,
#                                         [0, self.h]))
#             self.yList.append(self.yP)
#             if len(self.yList) == 100:
#                 self.yList.pop(0)
#
#             for i in range(0, len(self.yList)):
#                 if i < 2:
#                     pass
#                 else:
#                     cv2.line(self.imgPlot, (int((self.xList[i - 1] * (self.w // 100))) - (self.w // 10),
#                                             self.yList[i - 1]),
#                              (int((self.xList[i] * (self.w // 100)) - (self.w // 10)),
#                               self.yList[i]), color, 2)
#             self.ptime = time.time()
#
#         return self.imgPlot
#
#     def drawBackground(self):
#         # Draw Background Canvas
#         cv2.rectangle(self.imgPlot, (0, 0),
#                       (self.w, self.h),
#                       (0, 0, 0), cv2.FILLED)
#
#         # Center Line
#         cv2.line(self.imgPlot, (0, self.h // 2), (self.w, self.h // 2), (150, 150, 150), 2)
#
#         # Draw Grid Lines
#         for x in range(0, self.w, 50):
#             cv2.line(self.imgPlot, (x, 0), (x, self.h),
#                      (50, 50, 50), 1)
#
#         for y in range(0, self.h, 50):
#             cv2.line(self.imgPlot, (0, y), (self.w, y),
#                      (50, 50, 50), 1)
#             #  Y Label
#             cv2.putText(self.imgPlot,
#                         f'{int(self.yLimit[1] - ((y / 50) * ((self.yLimit[1] - self.yLimit[0]) / (self.h / 50))))}',
#                         (10, y), cv2.FONT_HERSHEY_PLAIN,
#                         1, (150, 150, 150), 1)
#         cv2.putText(self.imgPlot, self.char,
#                     (self.w - 100, self.h - 25), cv2.FONT_HERSHEY_PLAIN,
#                     5, (150, 150, 150), 5)
#
#
# def main():
#     xPlot = LivePlot(w=1200, yLimit=[-100, 100], interval=0.01)
#     x = 0
#     while True:
#
#         x += 1
#         if x == 360: x = 0
#         imgPlot = xPlot.update(int(math.sin(math.radians(x)) * 100))
#
#         cv2.imshow("Image", imgPlot)
#         cv2.imshow("Image", img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#
# if __name__ == "__main__":
#     main()
#


###################################################################################################
################ Pose Module https://github.com/cvzone/cvzone/blob/master/cvzone/PoseModule.py
"""
Pose Module
By: Computer Vision Zone
Website: https://www.computervision.zone/
"""
# import cv2
# import mediapipe as mp
# import math
#
#
# class PoseDetector:
#     """
#     Estimates Pose points of a human body using the mediapipe library.
#     """
#
#     def __init__(self, mode=False, smooth=True,
#                  detectionCon=0.5, trackCon=0.5):
#         """
#         :param mode: In static mode, detection is done on each image: slower
#         :param upBody: Upper boy only flag
#         :param smooth: Smoothness Flag
#         :param detectionCon: Minimum Detection Confidence Threshold
#         :param trackCon: Minimum Tracking Confidence Threshold
#         """
#
#         self.mode = mode
#         self.smooth = smooth
#         self.detectionCon = detectionCon
#         self.trackCon = trackCon
#
#         self.mpDraw = mp.solutions.drawing_utils
#         self.mpPose = mp.solutions.pose
#         self.pose = self.mpPose.Pose(static_image_mode=self.mode,
#                                      smooth_landmarks=self.smooth,
#                                      min_detection_confidence=self.detectionCon,
#                                      min_tracking_confidence=self.trackCon)
#
#     def findPose(self, img, draw=True):
#         """
#         Find the pose landmarks in an Image of BGR color space.
#         :param img: Image to find the pose in.
#         :param draw: Flag to draw the output on the image.
#         :return: Image with or without drawings
#         """
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         self.results = self.pose.process(imgRGB)
#         if self.results.pose_landmarks:
#             if draw:
#                 self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
#                                            self.mpPose.POSE_CONNECTIONS)
#         return img
#
#     def findPosition(self, img, draw=True, bboxWithHands=False):
#         self.lmList = []
#         self.bboxInfo = {}
#         if self.results.pose_landmarks:
#             for id, lm in enumerate(self.results.pose_landmarks.landmark):
#                 h, w, c = img.shape
#                 cx, cy, cz = int(lm.x * w), int(lm.y * h), int(lm.z * w)
#                 self.lmList.append([id, cx, cy, cz])
#
#             # Bounding Box
#             ad = abs(self.lmList[12][1] - self.lmList[11][1]) // 2
#             if bboxWithHands:
#                 x1 = self.lmList[16][1] - ad
#                 x2 = self.lmList[15][1] + ad
#             else:
#                 x1 = self.lmList[12][1] - ad
#                 x2 = self.lmList[11][1] + ad
#
#             y2 = self.lmList[29][2] + ad
#             y1 = self.lmList[1][2] - ad
#             bbox = (x1, y1, x2 - x1, y2 - y1)
#             cx, cy = bbox[0] + (bbox[2] // 2), \
#                      bbox[1] + bbox[3] // 2
#
#             self.bboxInfo = {"bbox": bbox, "center": (cx, cy)}
#
#             if draw:
#                 cv2.rectangle(img, bbox, (255, 0, 255), 3)
#                 cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
#
#         return self.lmList, self.bboxInfo
#
#     def findAngle(self, img, p1, p2, p3, draw=True):
#         """
#         Finds angle between three points. Inputs index values of landmarks
#         instead of the actual points.
#         :param img: Image to draw output on.
#         :param p1: Point1 - Index of Landmark 1.
#         :param p2: Point2 - Index of Landmark 2.
#         :param p3: Point3 - Index of Landmark 3.
#         :param draw:  Flag to draw the output on the image.
#         :return:
#         """
#
#         # Get the landmarks
#         x1, y1 = self.lmList[p1][1:]
#         x2, y2 = self.lmList[p2][1:]
#         x3, y3 = self.lmList[p3][1:]
#
#         # Calculate the Angle
#         angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
#                              math.atan2(y1 - y2, x1 - x2))
#         if angle < 0:
#             angle += 360
#
#         # Draw
#         if draw:
#             cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
#             cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
#             cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
#             cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
#             cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
#             cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
#             cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
#             cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
#             cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
#                         cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
#         return angle
#
#     def findDistance(self, p1, p2, img, draw=True, r=15, t=3):
#         x1, y1 = self.lmList[p1][1:]
#         x2, y2 = self.lmList[p2][1:]
#         cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
#
#         if draw:
#             cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
#             cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
#             cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
#             cv2.circle(img, (cx, cy), r, (0, 0, 255), cv2.FILLED)
#         length = math.hypot(x2 - x1, y2 - y1)
#
#         return length, img, [x1, y1, x2, y2, cx, cy]
#
#     def angleCheck(self, myAngle, targetAngle, addOn=20):
#         return targetAngle - addOn < myAngle < targetAngle + addOn
#
#
# def main():
#     cap = cv2.VideoCapture(0)
#     detector = PoseDetector()
#     while True:
#         success, img = cap.read()
#         img = detector.findPose(img)
#         lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
#         if bboxInfo:
#             center = bboxInfo["center"]
#             cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
#
#         cv2.imshow("Image", img)
#         cv2.waitKey(1)

# if __name__ == "__main__":
#     main()