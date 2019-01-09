# -*- coding: utf-8 -*-

##1. 图片压缩与解压缩

from imagecompress import ImageCompress

import numpy as np
import cv2

# 初始化一个图片压缩加压缩对象
ic = ImageCompress()

# 新建一个图片，并显示
image = np.zeros((480, 640, 3), np.uint8) + 255
cv2.imshow('test', image)

# 图片压缩
image_compressed = ic.b64encode_img_with_compress(image)

# 图片解压缩
image_decompressed = ic.b64decode_img_with_decompress(image_compressed)

# 显示解压缩后的图片
cv2.imshow("decompress", image_decompressed)


##2. 日志
from vilogging import ViLogging

# 默认情况下，保存最多5个log文件，每个文件大小最大是 10M，可以通过指定maxfile参数，修改最多文件数。logfile = ViLogging(logfile=log_file_name, maxfile=10)
log_file_name = "test_log.txt"
logfile = ViLogging(log_file_name)

# 添加info日志
logfile.addinfolog("this is a info log")
logfile.addinfolog("this is a info log")
logfile.addinfolog("this is a info log")

# 添加error日志
logfile.adderrorlog("this is a error log")


##3. 摄像头

'''
### Example.1: 打开USB摄像头 
'''
import cv2
from video.videostream import VideoStream
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