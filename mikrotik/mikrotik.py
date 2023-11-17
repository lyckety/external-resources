"""
Helper functions for mikrotik
"""

from typing import List, Dict


def ip_prefixes_to_address_list(ip_prefixes: List[str], list_name: str, comment: str) -> str:
    """ip_prefixes_to_address_list implements mikrotik address list from ip prefixes

    :param ip_prefixes: ip prefixes
    :type ip_prefixes: List[str]
    :param list_name: address list name
    :type list_name: str
    :param comment: comment for address list
    :type comment: str
    :return: script
    :rtype: str
    """
    if len(ip_prefixes) == 0:
        return ""

    script = "/ip firewall address-list\n"

    for ip in ip_prefixes:
        script += f"add list={list_name} address={ip} comment={comment}\n"

    return script

def ips_for_domain_to_address_list(ips_info: Dict[str, List[str]], list_name: str, comment_prefix: str) -> str:
    """ips_for_domain_to_address_list convert ips and domains to mikrotik address list

    :param ips_info: ip info (key - ip, value - list domains for ip)
    :type ips_info: Dict[str, List[str]]
    :param list_name: address list name
    :type list_name: str
    :param comment_prefix: comment prefix for address list record (<comment_prefix>: <domain1, domain2>)
    :type comment: str
    :return: script
    :rtype: str
    """
    if len(ips_info) == 0:
        return ""

    script = "/ip firewall address-list\n"

    for ip, domains in ips_info.items():
        comment_suffix: str = ','.join(domains)
        comment = f'{comment_prefix}:{comment_suffix}'

        script += f"add list={list_name} address={ip} comment={comment}\n"

    return script
