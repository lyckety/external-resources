"""
Module implements initialization config for application
"""

import os


class Config(object):
    """
    Config for application
    """
    def __init__(self) -> None:
        self.__http_bind_address: str = os.getenv('HTTP_BIND_ADDRESS', '0.0.0.0')
        self.__http_bind_port: str = os.getenv('HTTP_BIND_PORT', '8080')
        self.__log_level: str = os.getenv('LOG_LEVEL', 'info')
        self.__flask_debug: bool = os.getenv('DEBUG_FLASK', 'False').lower() == 'True'.lower()

    @property
    def http_bind_address(self) -> str:
        """
        http_bind_address ip-address for listen
        """
        return self.__http_bind_address

    @property
    def http_bind_port(self) -> str:
        """
        http_bind_port tcp port for listen
        """
        return self.__http_bind_port

    @property
    def is_debug_flask(self) -> bool:
        """
        flask mode is debug
        """
        return self.__flask_debug

    @property
    def log_level(self) -> str:
        """
        log_level level for logger
        """
        return self.__log_level
