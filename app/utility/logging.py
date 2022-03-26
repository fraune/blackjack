from enum import Enum


class LogLevel(Enum):
    VERBOSE = 1
    INFO = 2
    WARN = 3
    ERROR = 4


CURRENT_LOG_LEVEL = LogLevel.VERBOSE


# TODO: Introduce optional file output?
def log(message: str, log_level: LogLevel = LogLevel.VERBOSE):
    if log_level.value > CURRENT_LOG_LEVEL.value:
        print(message)


def v(message):
    log(message, LogLevel.VERBOSE)


def i(message):
    log(message, LogLevel.INFO)


def w(message):
    log(message, LogLevel.WARN)


def e(message):
    log(message, LogLevel.ERROR)
