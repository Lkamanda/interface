import logging, os, time


class Logger(object):

    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler,用于控制台输出
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setLevel(logging.DEBUG)

        # 设置输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger


mylogger = Logger(logger="Logger").get_log()