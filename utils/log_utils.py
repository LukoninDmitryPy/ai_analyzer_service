import logging
import os


HANDLER = logging.StreamHandler()
HANDLER.setFormatter(logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
))

def getLogger(name, mode=os.getenv('MODE')) ->logging.Logger:
    logger = logging.getLogger(name)

    if mode == 'debug':
        logger.setLevel(logging.DEBUG)
    elif mode == 'work':
        logger.setLevel(logging.INFO)
    else:
        raise Exception('Bad mode parameter! Should be: "debug" or "work"')

    logger.addHandler(HANDLER)
    return logger
