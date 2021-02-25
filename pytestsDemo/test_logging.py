import logging

def testloggingDemo() :

    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    logger.setLevel(logging.INFO)
    logger.critical("Critical issue")
    logger.info("Info message")
    logger.debug("Debug message")
    logger.warning("warning message")
    logger.error("Error message")