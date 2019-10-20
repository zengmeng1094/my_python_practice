import requests
import urllib3
from urllib3 import HTTPConnectionPool


class HttpsClient:

    def __init__(self):
        pass

    @staticmethod
    def get(_url, _json={}, _header=None):
        urllib3.disable_warnings()
        _resp = requests.get(_url, _json, headers=_header, verify=False)
        return _resp.text

    @staticmethod
    def post(_url, _json={}, _header=None):
        urllib3.disable_warnings()
        _resp = requests.post(_url, _json, headers=_header, verify=False)
        return _resp.text


if __name__ == '__main__':
    print(HttpsClient.get('http://127.0.0.1:5000/test'))
