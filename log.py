import logging
logger=logging.getlonger(__name__)

fileHandler=logging.fileHandler(logfile.log)
formatter=logging.Formatter(%(asctime)s : %(levelname)s : %(name)s : %(message)s)
fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)

logger setlevel()
logger.debug("debug statement")
logger.info("info statement")
logger.warning("warning statement")
logger.error("error statement")
logger.critical("critical statement")