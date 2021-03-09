from setup_logger import logger

class DataConsole:

    def __init__(self):
        self.data = self.get_data()

    def get_data(self):
        logger.info('instanciation DataConsole and get data')
