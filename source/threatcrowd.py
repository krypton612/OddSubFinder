# -*- encoding: utf-8 -*-
"""
threatcrowd parser

:Copyright: © 2023, Krypton612.
:License: BSD (see /LICENSE).
"""
import json
import requests


def parse(domains):
    """
    This function performs a request to threatcrowd and after having
    parsed its output returns a cleaned list of unique domains

    Args:
    domains -- the list of input domain to query

    Returns:
    a cleaned list of unique subdomains obtained after querying threatcrowd
    """
    subdomains = []
    for domain in domains:
        url = 'https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={}'.format(domain)
        resp = requests.get(url)
        json_resp = json.loads(resp.text)
        if 'subdomains' in json_resp.keys():
            subdomains += json_resp['subdomains']
    return subdomains
