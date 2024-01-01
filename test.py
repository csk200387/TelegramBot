import telegram
import asyncio
import os
from dotenv import load_dotenv
from src.hotdeal import get_hotdeal
from src.util import send_hook

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
LAST_ARTICLE_ID = 0

bot = telegram.Bot(token=TOKEN)

async def main():
    global LAST_ARTICLE_ID
    while True:
        articles = get_hotdeal()
        for article in articles:
            if article['article_id'] > LAST_ARTICLE_ID:
                LAST_ARTICLE_ID = article['article_id']
                title = article['title']
                price = article['price']
                category = article['category']
                store = article['store']
                link = article['link']

                # await bot.send_message(chat_id=CHAT_ID, text=f'[{category}] {title}\n{price}\n{store}\n{link}')
                await send_hook(title, link, price, category, store, "아카라이브")
        await asyncio.sleep(60)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        bot.send_message(chat_id=CHAT_ID, text='프로그램 종료됨\n'+str(e)))