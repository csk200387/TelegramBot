from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests


def get_hotdeal():
    url = 'https://arca.live/b/hotdeal'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    hotdeal = soup.find_all('div', class_='vrow hybrid')

    result = []

    for i in hotdeal:
        title = i.find('a', class_='title hybrid-title').text.strip().split('\n')[0]
        price = i.find('span', class_='deal-price').text.strip()
        category = i.find('a', class_='badge').text
        id = i.find('span', class_='vcol col-id').text
        store = i.find('span', class_='deal-store').text
        link = i.find('a', class_='title hybrid-title').get('href')
        result.append({
            'article_id': int(id),
            'title': title,
            'price': price,
            'category': category,
            'store': store,
            'link': 'https://arca.live'+link
            })
    return result

if __name__ == "__main__":
    for i in get_hotdeal():
        print(i['title'])
        print(i['price'])
        print(i['link'])
        print(i['store'])
        print(i['category'])
        print(i['article_id'])
        print()