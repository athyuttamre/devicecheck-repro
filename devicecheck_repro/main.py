import devicecheck
import logging

logger = logging.getLogger()


def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("MY LOGS - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def main():
    setup_logger()
    logger.info("This is a log message from the client application.")


if __name__ == "__main__":
    main()
