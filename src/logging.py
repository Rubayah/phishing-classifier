import logging 
import os
from datatime import datatime

LOG_FILE = f"{datatime.now().strtime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.mkdirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename==LOG_FILE_PATH,
    format="[%(asctime)s]"
)