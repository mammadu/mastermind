import requests

class Status:
    def __init__(self, url=None):
        self.url = url

    def is_up(self, url=None):
        if url == None:
            url = self.url
        response = requests.get(url)
        if response.status_code >= 200 or response.status_code <= 299:
            return True
        else:
            return False
