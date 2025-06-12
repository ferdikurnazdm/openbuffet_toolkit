from typing import Optional
from openbuffet_toolkit.tool_logger import LoggerManager
from dotenv import load_dotenv
import os

class EnviroimentHandler:
    """
    Loads environment variables from a `.env` file and provides access to them.

    This class optionally logs the status of the environment loading process.
    It allows retrieval of environment-based configuration values using the `get()` method.

    Attributes:
        __logger (Optional[Logger]): Optional logger for internal logging.
    """

    def __init__(self, dotenv_path: str = None, logger_manager: Optional[LoggerManager] = None):
        """
        Initializes the configuration loader and loads the environment variables from a `.env` file.

        Args:
            dotenv_path (str, optional): Full path to the `.env` file. Defaults to a `.env` file in the current directory.
            logger_manager (LoggerManager, optional): Optional logger instance for logging config load status.
        """
        self.__logger = logger_manager.get_logger if logger_manager else None

        if dotenv_path is None:
            dotenv_path = os.path.join(os.path.dirname(__file__), ".env")

        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
            if self.__logger:
                self.__logger.info(f".env loaded from {dotenv_path}")
        else:
            if self.__logger:
                self.__logger.warning(f".env file not found at {dotenv_path}")

    def get(self, key: str, default: str = None) -> str:
        """
        Retrieves the value of an environment variable.

        Args:
            key (str): The name of the environment variable.
            default (str, optional): A default value to return if the variable is not set.

        Returns:
            str: The value of the environment variable, or the default value if not found.
        """
        return os.getenv(key, default)
