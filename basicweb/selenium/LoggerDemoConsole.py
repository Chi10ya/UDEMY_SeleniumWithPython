import logging

class LoggerDemoConsole():

    def testLog(self):
        # Create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        # Create console handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M:%S %p')

        # add formatter to console handler --> chandler
        chandler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(chandler)

        # logging messages
        logger.warning("Warning message")
        logger.info("Info message")
        logger.error("Error message")
        logger.debug("Debug message")
        logger.critical("Critical message")

demo = LoggerDemoConsole()
demo.testLog()