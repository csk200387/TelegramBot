import requests
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")


def send_hook(title:str, url:str, price:str, category:str, store:str, sitename:str) -> None:
    """## 디스코드 웹훅 전송
    Args:
        * title -> str
        * url -> str
        * price -> str
        * category -> str
        * store -> str
    """

    json = {
        "embeds": [
            {
                "title": title,
                "url": url,
                "fields": [
                    {
                        "name": "가격",
                        "value": price,
                        "inline": True
                    },
                    {
                        "name": "종류",
                        "value": category,
                        "inline": True
                    },
                    {
                        "name": "쇼핑몰",
                        "value": store,
                        "inline": True
                    }
                ],
                "author": {
                    "name": sitename,
                    "icon_url": "https://i.namu.wiki/i/uDNhs7D-YhK4rVCOjzk6NLNzbC58cvwSpMHw-b0mG8XGgPA1uxFI1JqUFBE1gLHvSWhq1LNrXuwchq6TPh1WIg.svg"
                    }
                }
            ]
        }
    
    url = DISCORD_WEBHOOK
    requests.post(url, json=json, headers={'Content-Type': 'application/json'})

if __name__ == "__main__":
    send_hook("테스트", "https://arca.live/b/hotdeal/123456", "1000원", "의류", "테스트", "홀리쉿")