# -*- coding: utf-8 -*-

'''
### Example.1: 打开USB摄像头 
'''
import cv2
from videostream import VideoStream
from imutils.video import FPS

camera_id = 0

vs = VideoStream(camera_id)

vs.start()
fps = FPS().start()

while True:
    res, frame = vs.read()
    fps.update()
    if not(res):
        print("Camera Read Failed")
        break
    
    cv2.imshow("test", frame)
    waikey = cv2.waitKey(1) & 0xFF
    if waikey == ord('q'):
        break

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
vs.release()


'''
### Example.2: 打开 中惠的IP摄像头
'''
import cv2
from videostream import VideoStream
from imutils.video import FPS

camera_id = '192.168.30.12'

vs = VideoStream(src=camera_id, useIPCamera=True)

vs.start()
fps = FPS().start()

while True:
    res, frame = vs.read()
    fps.update()
    if not(res):
        print("Camera Read Failed")
        break
    
    cv2.imshow("test", frame)
    waikey = cv2.waitKey(1) & 0xFF
    if waikey == ord('q'):
        break

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
vs.release()