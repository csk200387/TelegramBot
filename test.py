import telegram
import asyncio
import os
from dotenv import load_dotenv
import src.fmkorea
import src.arcalive
from src.util import send_hook

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
LAST_ARTICLE_ID = 0

bot = telegram.Bot(token=TOKEN)


async def function_fmkorea():
    print("function_fmkorea")
    global LAST_ARTICLE_ID
    try:
        while True:
            articles = src.fmkorea.get_hotdeal()
            for article in articles:
                if article['article_id'] > LAST_ARTICLE_ID:
                    LAST_ARTICLE_ID = article['article_id']
                    title = article['title']
                    price = article['price']
                    category = article['category']
                    store = article['store']
                    link = article['link']

                    # await bot.send_message(chat_id=CHAT_ID, text=f'[{category}] {title}\n{price}\n{store}\n{link}')
                    send_hook(title, link, price, category, store, "에펨코리아")
            await asyncio.sleep(60)
    except Exception as e:
        await bot.send_message(chat_id=CHAT_ID, text=f'에러 발생\n{e}')


async def function_arcalive():
    print("function_arcalive")
    global LAST_ARTICLE_ID
    try:
        while True:
            articles = src.arcalive.get_hotdeal()
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


async def main():
    tasks = [asyncio.create_task(function_fmkorea()), asyncio.create_task(function_arcalive())]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())