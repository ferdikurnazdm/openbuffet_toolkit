from threading import Lock
from logging import Logger
import logging
import os



class LoggerHandler:
    """
    A thread-safe singleton-style logger manager for creating and accessing a global logger instance.

    This class ensures that a single logger instance is created across the entire application,
    with both file and console handlers attached. The log file is stored under a "logs" directory
    with a default file name of 'log.txt'. The logger supports DEBUG-level logging to file and 
    INFO-level logging to console.

    Example:
        logger = LoggerManager().get_logger()
        logger.info("This is an info message.")
    """

    _logger_instance = None
    _lock = Lock()

    def __init__(self, log_file: str = "log.txt"):
        """
        Initializes the logger instance if it hasn't been created yet.

        Ensures thread-safe initialization using a class-level lock. The logger writes to both
        a file and the console with a common log format.

        Args:
            log_file (str): The name of the log file to write to. Defaults to 'log.txt'.
        """
        if LoggerHandler._logger_instance is None:
            with LoggerHandler._lock:
                if LoggerHandler._logger_instance is None:
                    logger = logging.getLogger("global_logger")
                    logger.setLevel(logging.DEBUG)
                    log_dir = "logs"
                    os.makedirs(log_dir, exist_ok=True)
                    log_path = os.path.join(log_dir, log_file)
                    file_handler = logging.FileHandler(log_path)
                    file_handler.setLevel(logging.DEBUG)
                    console_handler = logging.StreamHandler()
                    console_handler.setLevel(logging.INFO)
                    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                    file_handler.setFormatter(formatter)
                    console_handler.setFormatter(formatter)
                    if not logger.hasHandlers():
                        logger.addHandler(file_handler)
                        logger.addHandler(console_handler)
                    LoggerHandler._logger_instance = logger

    @property
    def get_logger(self) -> Logger:
        """
        Returns the singleton logger instance.

        Returns:
            logging.Logger: The shared global logger.
        """
        return LoggerHandler._logger_instance
