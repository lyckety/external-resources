"""
Initialization of package
"""

from .mikrotik import ip_prefixes_to_address_list, ips_for_domain_to_address_list


__all__ = [
    'ip_prefixes_to_address_list',
    'ips_for_domain_to_address_list',
]
