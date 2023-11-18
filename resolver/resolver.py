"""
The module implements obtaining a list of IP addresses for domain names using dns
"""

from typing import Dict, List
import ipaddress
import logging as log
from dns import resolver

NUMBER_REQUESTS = 2

def resolve_ips(nameservers: List[str], domain_names: List[str], ip_type: str = None) -> Dict[str, List[str]]:
    """resolve_ips implements a domain names resolver in ip

    :param nameservers: nameservers for resolve. Вomain is resolved through EACH server
    :type nameservers: List[str]
    :param domain_names: domain names for resolve
    :type domain_names: List[str]
    :param ip_type: ip-protocol version (ipv4 or ipv6), defaults to None
    :type ip_type: str, optional

    :return: ip info (key - ip, value - list domain for ip)
    :rtype: Dict[str, List[str]]
    """
    resolved_ips: Dict[str, Dict[str, bool]] = {}

    # requests through different DNS servers return different IP addresses,
    # so each domain resolves through each nameserver
    for ns in nameservers:
        # sometimes an incomplete list of addresses is returned from the name server,
        # a rough way around this problem
        for _ in range(NUMBER_REQUESTS):
            for name in domain_names:
                try:
                    res = resolver.Resolver()
                    res.nameservers = [ns]

                    response = res.query(name)

                    for data in response:
                        if ip_type:
                            try:
                                if ip_type == 'ipv4':
                                    ipaddress.IPv4Network(data.address, strict=False)
                                elif ip_type == 'ipv6':
                                    ipaddress.IPv6Network(data.address, strict=False)
                            except ipaddress.AddressValueError:
                                continue

                        if resolved_ips.get(data.address) is None:
                            resolved_ips[data.address]: Dict[str, bool] = {}

                        if resolved_ips[data.address].get(name) is None:
                            resolved_ips[data.address][name] = True
                except resolver.Timeout as e:
                    log.error("Unable to resolve %s: %s", name, str(e))

    result: Dict[str, List[str]] = {}

    for ip, domains in resolved_ips.items():
        result[ip] = list(domains.keys())

    return result
