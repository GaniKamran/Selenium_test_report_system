import logging
import sys
import os

# Function to set up logging configuration for each test
class LogSystem():
    def __init__(self, test_name) -> None:
        self.test_name = test_name
        self.logger = self.setup_logging()
        
    def setup_logging(self):
        logger = logging.getLogger(self.test_name)

        if not logger.handlers:
            log_folder = os.path.join(os.getcwd(), 'log_folder', 'makelogfile')  # Adjust the path as needed
            os.makedirs(log_folder, exist_ok=True)

            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

            # Add a FileHandler to write log messages to a file
            file_handler = logging.FileHandler(os.path.join(log_folder, f'{self.test_name}_log.log'))
            file_handler.setFormatter(formatter)
 
            # Add a StreamHandler to also output log messages to the terminal
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
            logger.setLevel(logging.INFO)

        return logger

    def clear_log_file(self):
        log_folder = os.path.join(os.getcwd(), 'log_folder', 'makelogfile')  # Adjust the path as needed
        log_file_path = os.path.join(log_folder, f'{self.test_name}_log.log')

        try:
            # Open the log file in write mode, effectively clearing its content
            with open(log_file_path, 'w'):
                pass
        except FileNotFoundError:
            print(f"Log file not found: {log_file_path}")