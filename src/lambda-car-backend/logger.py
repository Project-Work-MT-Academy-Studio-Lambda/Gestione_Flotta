import logging
from typing import Callable
from .settings import load_settings

_settings = load_settings()


def _configure_root_logger() -> None:
    root_logger = logging.getLogger("lambda-car-backend")

    if root_logger.handlers:
        return

    root_logger.setLevel(_settings.log_level.upper())

    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    handler.setFormatter(formatter)
    root_logger.addHandler(handler)


def get_logger(name: str) -> logging.Logger:
    _configure_root_logger()
    return logging.getLogger(name)


def get_logger_factory() -> Callable[[str], logging.Logger]:
    _configure_root_logger()
    return get_logger