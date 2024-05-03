import logging
import datetime

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logger = logging.getLogger('my_logger')
            cls._instance.logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler = logging.FileHandler('log.txt')
            file_handler.setFormatter(formatter)
            cls._instance.logger.addHandler(file_handler)
        return cls._instance

    def log(self, level, message):
        if level == 'INFO':
            self.logger.info(message)
        elif level == 'WARNING':
            self.logger.warning(message)
        elif level == 'ERROR':
            self.logger.error(message)
        elif level == 'FATAL':
            self.logger.critical(message)
        else:
            self.logger.debug(message)

if __name__ == '__main__':
    logger = Logger()
    logger.log('INFO', 'This is an info message')
    logger.log('WARNING', 'This is a warning message')
    logger.log('ERROR', 'This is an error message')
    logger.log('FATAL', 'This is a fatal message')