# vitool
VI tool

三个功能：
1. 图像压缩与解压缩
2. 日志管理
3. 摄像头读取

详细应用，请查看example.py

安装vitool到本地python site-packages
1. 将setup.py移动到 vitool上一级目录，即跟vitool同级。
2. 执行pyton setup.py install安装
3. 验证，执行以下指令没有报错，即OK
from vitool.videostream import VideoStream
from vitool import ViLogging
from vitool import ImageCompress
