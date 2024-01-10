"""
Module for init globally configuration logging
"""

import sys
import logging as log


__DEFAULT_FORMATTER = log.Formatter(
    fmt='%(asctime)s%(msecs)s: %(module)s.%(funcName)s.%(lineno)d: %(levelname)s: %(message)s',
)

__DEBUG_FORMATTER = log.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')


def init_logger(log_level: str) -> None:
    """
    init_logger implement init config logger globally
    """

    stdout_handler = log.StreamHandler(sys.stdout)
    if log_level == 'debug':
        stdout_handler.setFormatter(__DEBUG_FORMATTER)
    else:
        stdout_handler.setFormatter(__DEFAULT_FORMATTER)

    match log_level:
        case 'debug':
            log.basicConfig(
                handlers=[stdout_handler],
                level=log.DEBUG,
                encoding='utf-8'
            )
        case 'info':
            log.basicConfig(
                handlers=[stdout_handler],
                level=log.INFO,
                encoding='utf-8'
            )
        case 'warning':
            log.basicConfig(
                handlers=[stdout_handler],
                level=log.WARNING,
                encoding='utf-8'
            )
        case 'error':
            log.basicConfig(
                handlers=[stdout_handler],
                level=log.ERROR,
                encoding='utf-8'
            )
        case 'critical':
            log.basicConfig(
                handlers=[stdout_handler],
                level=log.CRITICAL,
                encoding='utf-8'
            )
        case _:
            raise AttributeError(f'unknown log level {log_level}')
