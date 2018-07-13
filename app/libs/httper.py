import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        return r.json() if return_json else r.text
