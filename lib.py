import os
import time
import json
import requests
import urllib.request

class ParseManga:
    def __init__(self, url) -> None:
        self.url = f"{url}.json"
        self.data = self.load()["readableProduct"]

    def load(self):
        ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
        headers = {
            "User-Agent": ua
        }
        return json.loads(requests.get(self.url, headers=headers).text)
    
    def get_title(self) -> str:
        return self.data["series"]["title"]
    
    def get_episode(self) -> str:
        return self.data["title"]
    
    def get_pages(self) -> list[str]:
        return [page["src"] for page in self.data["pageStructure"]["pages"] if page["type"] == "main"]

class Download(ParseManga):
    def __init__(self, url) -> None:
        super().__init__(url)
        self.path = f"{self.get_title()}/{self.get_episode()}"
    def mkdirs(self):
        try:
            os.mkdir(self.get_title())
            os.mkdir(self.path)
        except:
            pass
    
    def save_pages(self) -> None:
        for i in range(len(self.get_pages())):
            urllib.request.urlretrieve(self.get_pages()[i], f"./{self.path}/{i}.png")
            time.sleep(1)

