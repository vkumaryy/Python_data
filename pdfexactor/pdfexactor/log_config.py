import logging
import os
from datetime import datetime

# Define a directory for logs
LOGS_DIR = 'logs'
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# Define a custom formatter
class CustomFormatter(logging.Formatter):
    converter = datetime.fromtimestamp
    def format(self, record):
        s = "%s, %s, %s" % (self.converter(record.created).strftime('%Y-%m-%d %H:%M:%S'), record.levelname, record.getMessage())
        return s

def setup_logger(name, log_file, level=logging.INFO):
    """Function to setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(CustomFormatter())

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Import the setup_logger function
from .log_config import setup_logger

# Setup your logger
logger = setup_logger('pdf_extraction', 'logs/pdf_extraction.log')
