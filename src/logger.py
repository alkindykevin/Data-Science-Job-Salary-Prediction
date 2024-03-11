import logging  # Importing the logging module
import os  # Importing the os module
from datetime import datetime  # Importing datetime module from datetime package

# Creating a log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating a directory path for storing logs based on the current working directory
logs_path = os.path.join(os.getcwd(), "logs")

# Creating the directory if it doesn't exist, using exist_ok=True to avoid raising an error if the directory already exists
os.makedirs(logs_path, exist_ok=True)

# Creating the full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuring the logging module
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Setting the log file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Setting the log format
    level=logging.INFO,  # Setting the logging level to INFO
)

# test logger
#if __name__=="__main__":
#    logging.info("Logging has started")