import basicweb.selenium.custom_logger as custLog
import logging


class customLoggerDemo():
    log = custLog.customLogger(logging.DEBUG)

    def method1(self):
        self.log.warning("Warning message")
        self.log.info("Info message")
        self.log.error("Error message")
        self.log.debug("Debug message")
        self.log.critical("Critical message")

    def method2(self):
        m2Log = custLog.customLogger(logging.INFO)
        m2Log.warning("Warning message")
        m2Log.info("Info message")
        m2Log.error("Error message")
        m2Log.debug("Debug message")
        m2Log.critical("Critical message")

    def method3(self):
        m3Log = custLog.customLogger(logging.INFO)
        m3Log.warning("Warning message")
        m3Log.info("Info message")
        m3Log.error("Error message")
        m3Log.debug("Debug message")
        m3Log.critical("Critical message")


demo = customLoggerDemo()
demo.method1()
demo.method2()
demo.method3()