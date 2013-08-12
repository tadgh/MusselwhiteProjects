import logging
import os
import datetime


class Logger():
    def __init__(this):
        pass

    def get_logger(this):
        now = datetime.datetime.now()
        logger = logging.getLogger('Logs\\' +str(now.strftime("%Y-%m-%d")) + " menu.log")
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler('Logs\\' + str(now.strftime("%Y-%m-%d")) + " menu.log")
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def info(self, msg):
        super(info(msg))
