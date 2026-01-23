import logging
import os
from logging.handlers import QueueHandler, QueueListener

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

def setup_logger_listener(log_queue, log_filename):
    log_dir = os.path.dirname(log_filename)
    os.makedirs(log_dir, exist_ok=True) 
    formatter = logging.Formatter(LOG_FORMAT)

    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    listener = QueueListener(log_queue, file_handler, stream_handler)
    listener.start()
    return listener

def get_logger(log_queue, name="ProcessorLogger"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = QueueHandler(log_queue)
        logger.addHandler(handler)
        logger.propagate = False

    return logger
