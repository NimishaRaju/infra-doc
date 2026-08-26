import logging


def logging_setup():
    logging.basicConfig(level=logging.INFO, 
        format="%(asctime)s [%(levelname)s] %(message)s", 
        handlers=[
            logging.FileHandler("app.log"),  
            logging.StreamHandler()
        ])
    logger = logging.getLogger(__name__)
    logger.debug("logging initialzed successfully")