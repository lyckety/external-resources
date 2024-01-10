"""
Module implements REST API
"""

from typing import List, Dict
import ipaddress
import requests

DEFAULT_HTTP_REQUEST_TIMEOUT_SEC = 10


def get_info(number: int):
    """get_info implements obtaining general information about the autonomous system

    :param number: number as
    :type number: int
    :return: informatiom about the autonomous system
    :rtype: Any
    """
    url = f"https://stat.ripe.net/data/as-overview/data.json?resource=AS{number}"

    response = requests.get(url, timeout=DEFAULT_HTTP_REQUEST_TIMEOUT_SEC)
    data = response.json()

    return data.get('data')

def get_ip_prefix_announces(number: int, ip_type: str = None) -> List[str]:
    """get_ip_prefix_announces implements obtaining a list of current
    announcements for the autonomous system

    :param number: number as
    :type number: int
    :param ip_type: ip-protocol version (ipv4 or ipv6), defaults to None
    :type ip_type: str, optional
    :return: announcements
    :rtype: List[str]
    """
    url = f"https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS{number}"

    response = requests.get(url, timeout=DEFAULT_HTTP_REQUEST_TIMEOUT_SEC)
    data = response.json()

    all_ip_list: List[str] = [entry['prefix'] for entry in data['data']['prefixes']]

    if ip_type:
        filtered_ip_list: List[str] = []

        for ip in all_ip_list:
            try:
                if ip_type == 'ipv4':
                    ipaddress.IPv4Network(ip, strict=False)

                    filtered_ip_list.append(ip)
                elif ip_type == 'ipv6':
                    ipaddress.IPv6Network(ip, strict=False)

                    filtered_ip_list.append(ip)
            except ipaddress.AddressValueError:
                continue

        return filtered_ip_list

    return all_ip_list

def get_full_info(number:int) -> Dict[str, any]:
    """get_full_info implements obtaining general information about the autonomous system
    including the current list of announcements

    :param number: number as
    :type number: int
    :return: informatiom about the autonomous system and current list of announcements
    :rtype: Dict[str, any]
    """
    info = get_info(number)

    info['announces'] = get_ip_prefix_announces(number)

    return info
