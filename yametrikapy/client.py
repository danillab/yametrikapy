# coding: utf-8

import requests
from urllib.parse import urlencode, urlparse

class APIClient(object):

    def __init__(self):
        self.status = 0
        self.reason = ''
        self.user_agent = ''
        self.HEADERS = {}

    def urlencode(self, **kwargs):
        return urlencode(kwargs)

    def request(self, method, url, params=None, headers=None):
        if not headers:
            headers = self.HEADERS

        if method == 'POST':
            r = requests.post(url, headers=headers, data=params, timeout=60*10)
        else:
            r = requests.get(url, headers=headers, timeout=60*10)

        self.status = r.status_code

        return r.text
