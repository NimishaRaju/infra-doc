#Define a function that prints the basic details on the app
import logging

from logging_config import logging_setup

logging_setup()
logger = logging.getLogger(__name__)

def startup():
    logger.info("Hello")
    logger.info("Welcome to infrasture health check platform")
    logger.info("application is starting now...")
#Execute the startup function only if the file name is specified
if __name__=='__main__':
    startup()