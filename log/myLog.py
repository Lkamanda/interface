import logging, os, time

class Logger(object):

    def __init__(self, logger):
        self.logger = logging.getLogger()
