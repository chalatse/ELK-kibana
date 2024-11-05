import logging
import logging.handlers
import os

class LoggerSetup:

    def __init__(self) -> None:
        self.logger = logging.getLogger('')
        self.setup_logging()

    def setup_logging(self):
        # Log format
        LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

        # Configure formatter
        formatter = logging.Formatter(LOG_FORMAT)

        # Configure console handler
        console = logging.StreamHandler()
        console.setFormatter(formatter)

        # Configure TimeRotatingFileHandler
        log_dir = "ELK-KIBANA/logs"
        log_file = f"{log_dir}/fastapi-efk.log"

        # Check if directory exists, if not, create it
        os.makedirs(log_dir, exist_ok=True)

        # Configure file handler with rotation
        file = logging.handlers.TimedRotatingFileHandler(filename=log_file, when="midnight", backupCount=5)
        file.setFormatter(formatter)

        # Add handlers
        self.logger.addHandler(console)
        self.logger.addHandler(file)