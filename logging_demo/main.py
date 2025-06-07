import logging
"""
This script demonstrates how to set up logging in Python.
It configures the logging module to log messages to a file named 'mylog.log'.
The log messages will include the timestamp, log level, and the message itself.
The logging level is set to DEBUG, meaning all messages of this level and above will be logged.
显示所在文件和错误行


"""

logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level to DEBUG
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
    filename='mylog.log',
    filemode='w',  # 'w' to overwrite the log file, 'a' to append
    encoding='utf-8'  # Set the logging format
)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")