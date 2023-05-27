# -*- encoding: utf-8 -*-
"""
hackertarget parser

:Copyright: © 2023, Krypton612.
:License: BSD (see /LICENSE).
"""
import requests


def parse(domains):
    """
    This function performs a request to hackertarget and after having
    parsed its output returns a cleaned list of unique domains

    Args:
    domains -- the list of input domain to query

    Returns:
    a cleaned list of unique subdomains obtained after querying hackertarget
    """
    subdomains = []
    for domain in domains:
        url = 'https://api.hackertarget.com/hostsearch/?q={}'.format(domain)
        resp = requests.get(url)
        lines = resp.text.split()
        for line in lines:
            subdomains.append(line.split(',')[0])
    return subdomains
