from setup_logger import logger


class DataConsole:

    def __init__(self):
        self.data = self.get_data()

    def get_data(self):
        logger.info('instanciation DataConsole and get data')
        return [
            ('Amiga CD32', 1993, 'Commodore', 'Console'),
            ('Playstation Vita', 2011, 'Sony', 'Console portable'),
            ('Nintendo 3DS', 2011, 'Nintendo', 'Console portable'),
            ('Wii U', 2012, 'Nintendo', 'Console'),
            ('Neo-Geo', 1990, 'SNK', 'Console - Arcade'),
            ('Xbox', 2001, 'Microsoft', 'Console'),
            ('Playstation', 1994, 'Sony', 'Console'),
        ]
