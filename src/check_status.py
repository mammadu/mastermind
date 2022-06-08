import requests

class Status:
    def __init__(self, url=None):
        self.url = url

    def is_up(self, url=None):
        if url == None:
            url = self.url
        try:
            response = requests.get(url)
            if response.status_code >= 200 and response.status_code <= 299:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def log_status():
        print()