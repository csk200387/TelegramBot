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
    try:
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
                    send_hook(title, link, price, category, store, "아카라이브")
            await asyncio.sleep(60)
    except Exception as e:
        await bot.send_message(chat_id=CHAT_ID, text=f'에러 발생\n{e}')


if __name__ == "__main__":
    asyncio.run(main())