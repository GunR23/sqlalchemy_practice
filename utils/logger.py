import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler(__name__.log)
file_handler.setLevel(logging.WARNING)
log_file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(log_file_format)

logger.addHandler(file_handler)
