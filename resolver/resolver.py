"""
The module implements obtaining a list of IP addresses for domain names using dns
"""

from typing import Dict, Tuple, List
import ipaddress
import socket
import logging as log


def resolve_ips(*domain_names: Tuple[str], ip_type: str = None) -> Dict[str, List[str]]:
    """resolve_ips implements a domain names resolver in ip
    :param ip_type: ip-protocol version (ipv4 or ipv6), defaults to None
    :type ip_type: str, optional

    :return: ip info (key - ip, value - list domain for ip)
    :rtype: Dict[str, List[str]]
    """
    resolved_ips: Dict[str, Dict[str, bool]] = {}

    for name in domain_names:
        log.warning(name)
        try:
            addr_info = socket.getaddrinfo(name, None)
            ips = [info[4][0] for info in addr_info]

            for ip in ips:
                if ip_type:
                    try:
                        if ip_type == 'ipv4':
                            ipaddress.IPv4Network(ip, strict=False)
                        elif ip_type == 'ipv6':
                            ipaddress.IPv6Network(ip, strict=False)
                    except ipaddress.AddressValueError:
                        continue

                if resolved_ips.get(ip) is None:
                    resolved_ips[ip]: Dict[str, bool] = {}

                if resolved_ips[ip].get(name) is None:
                    resolved_ips[ip][name] = True
        except socket.error as e:
            log.error("Unable to resolve %s: %s", name, str(e))

    result: Dict[str, List[str]] = {}

    for ip, domains in resolved_ips.items():
        result[ip] = list(domains.keys())

    return result
