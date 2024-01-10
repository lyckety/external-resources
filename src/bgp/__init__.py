"""
Initialization of package
"""

from .bgp import get_info, get_ip_prefix_announces, get_full_info


__all__ = [
    'get_info',
    'get_ip_prefix_announces',
    'get_full_info',
]
