"""
This file contains logic for logger
"""
import logging


def get_logger():
    """
    :return: return logger object with level set to INFO
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    return logger
