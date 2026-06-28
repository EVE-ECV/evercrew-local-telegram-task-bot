"""
Telegram Bot Connector

Receives boss messages from Telegram and sends
workflow responses back to Telegram.
"""

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

from config import TELEGRAM_BOT_TOKEN
from workflow import WorkflowEngine


engine = WorkflowEngine()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle the /start command.
    """

    await update.message.reply_text(
        "Hello, I am EVE.\n\n"
        "Send me a boss instruction and I will convert it into a clear employee task."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle normal Telegram messages.
    """

    message = update.message.text
    result = engine.process_message(message)
    task = result["task"]

    reply = (
        "Task detected:\n\n"
        f"Employee: {task['employee']}\n"
        f"Task: {task['task']}\n"
        f"Deadline: {task['deadline']}\n"
        f"Priority: {task['priority']}\n\n"
        f"Summary: {task['summary']}\n\n"
        f"{task['confirmation_question']}"
    )

    await update.message.reply_text(reply)


def run_bot():
    """
    Start the Telegram bot.
    """

    if not TELEGRAM_BOT_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is missing. Please update your .env file.")

    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Telegram bot is running...")
    app.run_polling()
