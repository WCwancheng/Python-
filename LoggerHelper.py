import logging
import sys

class Logger(object):
    def __init__(self,logName="Log.log"):
        self.logName = logName
        #获取logger实例
        self.logger = logger = logging.getLogger('baseSpider')
        self.__Start()
    
    def __Start(self):
        #输出格式
        self.formatter = logging.Formatter('%(asctime)s%(levelname)-8s:%(message)s')
        #文件日志
        self.file_handler = logging.FileHandler(self.logName)
        self.file_handler.setFormatter(self.formatter)
        #控制台日志
        self.console_handler = logging.StreamHandler(sys.stdout)
        self.console_handler.setFormatter(self.formatter)
        #为logger添加日志处理器
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)
        self.logger.setLevel(logging.INFO)

    def Log(self,message):
        self.logger.error(message)


