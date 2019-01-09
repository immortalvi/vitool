# -*- coding: utf-8 -*-

import logging
import logging.handlers
import sys

class ViLogging:
    def __init__(self, logfile, maxfile=5):
        self.logfile = logfile
        self.logcounter = 0
        self.maxfile = maxfile
        self.logger = self.initlogging()
        
    def initlogging(self):
        
        # 获取logger实例，如果参数为空则返回root logger
        logger = logging.getLogger("AppName")
        
        # 指定logger输出格式
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
        
        # 文件日志, 定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
        #file_handler = logging.FileHandler(self.logfile)
        file_handler = logging.handlers.RotatingFileHandler(self.logfile, maxBytes=1024*1024, backupCount=self.maxfile)
        file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
        
        # 控制台日志
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.formatter = formatter  # 也可以直接给formatter赋值
        
        # 为logger添加的日志处理器，可以自定义日志处理器让其输出到其他地方
        logger.addHandler(file_handler)
        #logger.addHandler(console_handler)
        
        # 指定日志的最低输出级别，默认为WARN级别
        logger.setLevel(logging.INFO)

        return logger
    
    def addinfolog(self, logcontent):
        self.logger.info(logcontent)
        self.logcounter += 1
    
    def adderrorlog(self, logcontent):
        self.logger.error(logcontent)
        self.logcounter += 1

        
# 输出不同级别的log
#logger.debug('this is debug info')
#logger.info('this is information')
#logger.warn('this is warning message')
#logger.error('this is error message')
#logger.fatal('this is fatal message, it is same as logger.critical')
#logger.critical('this is critical message')

# 2016-10-08 21:59:19,493 INFO    : this is information
# 2016-10-08 21:59:19,493 WARNING : this is warning message
# 2016-10-08 21:59:19,493 ERROR   : this is error message
# 2016-10-08 21:59:19,493 CRITICAL: this is fatal message, it is same as logger.critical
# 2016-10-08 21:59:19,493 CRITICAL: this is critical message

# 移除一些日志处理器
#logger.removeHandler(file_handler)