# creating a basic logger file 
import os
import sys
import logging

# this code will show the time and messege in the logertxt
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = 'logs'
log_filepath = os.path.join(log_dir,"running_logs.log")
os.mkdir(log_dir, exist_ok=True)

# basci config of logging
logging.basicConfig(
    level=logging.INFO,
    format= logging_str,
    
    handlers=[
        logging.FileHandler(log_filepath),# Sends log messages to a file specified by log_filepath.
        logging.StreamHandler(sys.stdout)# Sends log messages to the standard output terminal(console).
    ]
)

logger = logging.getLogger("mlProjectLogger")# Initializes a logger