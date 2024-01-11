from bs4 import BeautifulSoup
import requests


def get_hotdeal() -> list:
    """## 에펨코리아의 핫딜 정보를 리스트로 반환
    Returns:
        * result -> list
        * article_id -> int
        * title -> str
        * price -> str
        * category -> str
        * store -> str
        * link -> str
    """
    url = 'https://www.fmkorea.com/hotdeal'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    hotdeal = soup.find('div', class_='fm_best_widget _bd_pc').find('ul').find_all('li')
    result = []

    for i in hotdeal:
        title = i.find('h3', class_='title').text.strip()
        store, price, _ = (content.text for content in i.find('div', class_='hotdeal_info').find_all('a', class_='strong'))
        category = i.find('span', class_='category').text.strip()[:-2]
        id = i.find('a').get('href')[1:]
        result.append({
            'article_id': int(id),
            'title': title,
            'price': price,
            'category': category,
            'store': store,
            'link': 'https://www.fmkorea.com/'+id
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