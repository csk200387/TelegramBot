from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
from telegram import Update
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def unset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    await update.message.reply_text("It is just a test")


def main() -> None:
    """Run bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("unset", unset))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()