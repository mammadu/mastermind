import requests
import datetime
import pathlib
import csv


class CSVLogger:
    def __init__(self, location=None):
        if location == None:
            current_dir = pathlib.Path(__file__).resolve().parent
            log_file_path = str(current_dir.parent.joinpath("logs/random_api_status.csv"))
            self.location = log_file_path
        else:
            self.location = location

    def log(self, status, url):
        timestamp = datetime.datetime.now()
        row = [timestamp, url, status]
        with open(self.location, "a") as file:
            logwriter = csv.writer(file)
            logwriter.writerow(row)

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

    def log_status(self,status,logger=CSVLogger()):
        logger.log(status, self.url)
