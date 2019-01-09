# import the necessary packages
from threading import Thread
import cv2
import numpy as np
import ctypes
from ctypes import *
from struct import *
import os

'''
### import IP cam sdk lib from the camera vendor
'''
## 1. Import the ip camera lib
cu_path = os.path.split(os.path.realpath(__file__))[0]
CDLL = ctypes.cdll.LoadLibrary  
ip_cam_lib = CDLL(cu_path + "/libBL.so")  

## 2. Open the connection to the ip camera
def IPVideoCapture(ip, port):
    #ip = '192.168.1.80'
    #port = 3521
    ip_cap = ip_cam_lib.tsdOpenDev(c_char_p(bytes(ip.encode('utf-8'))),port,0)
    if (ip_cap == None):
        return False, ip_cap
    else:
        return True, ip_cap

## 3. Get one image from the ip camera, and change to numpy array.
def IPVideoRead(ip_cap):
    BitmapType = c_char*2073600          # 2073600 = 1920 * 1080
    buffer = BitmapType()
    img_len = ip_cam_lib.tsd_AcqureImage(ip_cap, buffer, 2073600, 3000)
    if img_len <= 0:
        return False, None
    else:
        a = np.frombuffer(buffer, dtype=np.uint8)
        a = cv2.imdecode(a, cv2.IMREAD_COLOR)
        return True, a
    
## 4. Close the connection to the ip camera.
def IPVideoClose(ip_cap):
    ip_cam_lib.tsdCloseDev(ip_cap,0)
    return True

class IpCamVideoStream:
    def __init__(self, ip='192.168.30.11', port=3521):
        # initialize the video camera stream and read the first frame
        # from the stream
        
        ## Open the connection to the ip camera
        self.ip = ip
        self.port = port
        self.isOpened, self.stream = IPVideoCapture(self.ip,self.port)
        if not(self.isOpened):
            print("Camera Connection Open Failed")
        
        ## Read the first frame
        (self.grabbed, self.frame) = IPVideoRead(self.stream)

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = IPVideoRead(self.stream)

    def read(self):
        # return the frame most recently read
        return self.grabbed, self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True
    
    def release(self):
        # indicate that the thread should be stopped
        self.stop()
        IPVideoClose(self.stream)
        