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
                return_val = True
            else:
                return_val = False
        except Exception as e:
            print(e)
            return_val = False
        return return_val

    def log_status(self,status, logger=csv_logger):
        print()