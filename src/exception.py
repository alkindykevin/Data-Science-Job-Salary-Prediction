import sys
from src.logger import logging  # Importing logging from src.logger module

def error_message_detail(error, error_detail: sys):
    """
    Function to extract error details including file name and line number.

    Args:
    - error: The error message.
    - error_detail: The error details including the traceback.

    Returns:
    - error_message (str): Formatted error message containing file name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message


class CustomException(Exception):
    """
    Custom Exception class to handle errors and log details.

    Args:
    - error_message: The error message.
    - error_detail: The error details including the traceback.

    Attributes:
    - error_message: Formatted error message containing file name, line number, and error message.
    """

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        Returns the error message as a string.
        """
        return self.error_message
