# System modules.
import logging
from pathlib import Path
from logging import handlers

# Third-party modules.
from colorama import init, Fore

# Replaces ANSI escape sequences with equivalent Win32 codes.
init(autoreset=True)


class ColorFormatter(logging.Formatter):
    """Color formatter for logs with level-specific colors."""
    COLORS = {
        'INFO': Fore.LIGHTGREEN_EX,
        'DEBUG': Fore.LIGHTMAGENTA_EX,
        'ERROR': Fore.LIGHTRED_EX,
        'STATUS': Fore.LIGHTCYAN_EX,
        'WARNING': Fore.LIGHTYELLOW_EX
    }

    def format(self, record) -> str:
        """Returns a formatted log message with color based on level."""
        color = self.COLORS.get(record.levelname, '')
        formatted_msg = record.levelname = f'{color}{record.levelname:^8}{Fore.WHITE}'

        # If color has a value, use the above formatting; otherwise, use no formatting.
        formatted_msg if color else f'{record.levelname:^8}'
        return super().format(record)


class CustomLogger(logging.Logger):
    def __init__(self, name: str):
        """Initializes a custom logger."""
        super().__init__(name, logging.DEBUG)

        # Set formatting for both console logger and file logger
        console_formatter = ColorFormatter('[%(levelname)s] %(asctime)s - %(message)s', datefmt='%H:%M')
        file_formatter = logging.Formatter(fmt='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%Y-%m-%d | %H:%M')

        # Check if "logs" folder exists, and create it if not.
        log_path = Path('logs')
        log_path.mkdir(exist_ok=True)

        # Add a handler for file logging. See: https://tinyurl.com/RotatingFilehandler
        self.fileHandler = handlers.RotatingFileHandler(
            filename=log_path / 'todoist_backup_log.log',
            mode='w',
            encoding='utf-8',
            backupCount=10,
            maxBytes= 2048,  # Number of bytes equal to 2 megabytes.
            delay=True
        )

        # File handler for logging to a file.
        self.fileHandler.setFormatter(file_formatter)
        self.fileHandler.addFilter(lambda record: record.levelno not in [logging.CRITICAL])
        self.addHandler(self.fileHandler)

        # Add a stream handler to handle console output and set its format.
        self.consoleHandler = logging.StreamHandler()
        self.consoleHandler.setFormatter(console_formatter)
        self.consoleHandler.addFilter(lambda record: record.levelno not in [logging.CRITICAL])
        self.addHandler(self.consoleHandler)
