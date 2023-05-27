# -*- encoding: utf-8 -*-
"""
urlscan parser

:Copyright: © 2023, Krypton612.
:License: BSD (see /LICENSE).
"""
import json
import requests
from utils import find


def parse(domains):
    """
    This function performs a request to urlscan and after having
    parsed its output returns a cleaned list of unique domains

    Args:
    domains -- the list of input domain to query

    Returns:
    a cleaned list of unique subdomains obtained after querying urlscan
    """
    subdomains = []
    for domain in domains:
        url = 'https://urlscan.io/api/v1/search/?q=domain:{}'.format(domain)
        json_resp = json.loads(requests.get(url).text)
        subdomains += list(set(find('domain', json_resp)))
    return list(set(subdomains))
