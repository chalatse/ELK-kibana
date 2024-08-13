import logging
import logging.handlers
import os

class LoggerSetup:
    def __init__(self) -> None:
        self.logger = logging.getLogger('')
        self.setup_logging()

    def setup_logging(self):
        # Add log format
        LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

        # Configure formatter for logger
        formatter = logging.Formatter(LOG_FORMAT)

        # Configure console handler
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        
        # Configure the log exist
        log_file = "ELK_kibana/logs/fastapi-efk.log"
        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
       

        # Configure TimedRotatingFileHandler
        file = logging.handlers.TimedRotatingFileHandler(filename=log_file, when="midnight", backupCount=5)
        file.setFormatter(formatter)

        # Add handlers
        self.logger.addHandler(console)
        self.logger.addHandler(file)


