import logging
import os
import datetime

class Logger():

	def __init__(this):
		pass

	def get_logger()
		now = datetime.datetime.now()
		logger = logging.getLogger(str(now.strftime("%Y-%m-%d")) + " backup.log")
		logger.setLevel(logging.INFO)
		hdlr = logging.FileHandler(str(now.strftime("%Y-%m-%d")) + " backup.log")
		formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
		hdlr.setFormatter(formatter)
		logger.addHandler(hdlr)
		return logger
