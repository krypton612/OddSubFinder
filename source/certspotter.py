# -*- encoding: utf-8 -*-
"""
certspotter parser

:Copyright: © 2023, Krypton612.
:License: BSD (see /LICENSE).
"""

import json
import requests


def parse(domains):
    """
    This function performs a request to certspotter and after having
    parsed its output returns a cleaned list of unique domains

    Args:
    domains -- the list of input domain to query

    Returns:
    a cleaned list of unique subdomains obtained after querying certspotter
    """
    subdomains = []
    for domain in domains:
        url = 'https://certspotter.com/api/v0/certs?domain={}'.format(domain)
        json_resp = json.loads(requests.get(url).text)
        try:
            doms = [e['dns_names'] for e in json_resp]
            for subs in doms:
                subdomains += subs
        except TypeError:
            print("\033[93m[*] \033[0m Cert Spotter API: Number of allowed requests exceeded")
    return list(set(subdomains))
