from time import sleep

import logging

from pythonjsonlogger import jsonlogger


def main():
    logger = get_logger()
    while True:
        logger.error("This is an error")
        logger.warning("This is a warning")
        logger.info("This is an info")
        logger.debug("This is a debug")
        sleep(1)


def get_logger():
    logger = logging.getLogger("demo_app")
    logger_handler = logging.StreamHandler()
    logger_formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(name)s %(levelname)s %(message)s",
        rename_fields={"levelname": "level"},
    )
    logger_handler.setFormatter(logger_formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logger_handler)
    logger.propagate = False
    return logger


if __name__ == "__main__":
    main()
