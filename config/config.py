"""
Module implements initialization config for application
"""
from typing import List
import os
from environs import Env


class Config(object):
    """
    Config for application
    """
    def __init__(self) -> None:
        self.__http_bind_address: str = os.getenv('HTTP_BIND_ADDRESS', '0.0.0.0')
        self.__http_bind_port: str = os.getenv('HTTP_BIND_PORT', '8080')
        self.__log_level: str = os.getenv('LOG_LEVEL', 'info')
        self.__flask_debug: bool = os.getenv('DEBUG_FLASK', 'False').lower() == 'True'.lower()
        self.__default_nameservers: List[str] = self.init_env_var_as_list('DEFAULT_NAMESERVERS')

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

    @property
    def default_nameservers(self) -> List[str]:
        """
        list of default nameservers
        """
        return self.__default_nameservers

    @staticmethod
    def init_env_var_as_list(var_name: str) -> List[str]:
        """init_env_var_as_list init variables as string

        :param var_name: environment variable with list (example: SERVERS=8.8.8.8,77.88.8.8)
        :type var_name: str
        :return: list values
        :rtype: List[str]
        """
        env = Env()
        env.read_env()

        return env.list(var_name)
