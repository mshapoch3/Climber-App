"""
Setting up logger to import for logging
"""

import logging


def get_logger(name: str = __name__, level: int = logging.DEBUG) -> logging.Logger:
    """
    Returns a configured logger with clean, aligned formatting.
    Can be imported and reused across scripts.
    """
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(level)

        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt='| %(levelname)-8s | %(asctime)s | %(filename)-1s, L %(lineno)-4d | %(message)s',
            datefmt='%H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger



if __name__ == "__main__":
    logger = get_logger()

    logger.debug("🐛 This is a debug message.")
    logger.info("ℹ️  This is an info message.")
    logger.warning("⚠️  This is a warning message.")
    logger.error("❌ This is an error message.")
