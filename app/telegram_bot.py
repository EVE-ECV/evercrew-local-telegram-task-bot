"""
Telegram Bot Connector

Receives boss messages from Telegram and sends
workflow responses back to Telegram.
"""

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

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
    session_id = result["session_id"]

    keyboard = [
        [
            InlineKeyboardButton(
                "Confirm",
                callback_data=f"confirm:{session_id}"
            )
        ],
        [
            InlineKeyboardButton(
                "Cancel",
                callback_data=f"cancel:{session_id}"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    reply = (
        "Task Preview\n\n"
        f"Employee: {task['employee']}\n"
        f"Task: {task['task']}\n"
        f"Deadline: {task['deadline']}\n"
        f"Priority: {task['priority']}\n\n"
        f"Summary: {task['summary']}\n\n"
        f"{task['confirmation_question']}"
    )

    await update.message.reply_text(
        reply,
        reply_markup=reply_markup
    )


async def handle_confirmation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle Confirm and Cancel button clicks.
    """

    query = update.callback_query
    await query.answer()

    action, session_id = query.data.split(":", 1)

    if action == "confirm":
        result = engine.confirm_task(session_id)

        if result["status"] == "assigned":
            task = result["task"]

            reply = (
                "Task confirmed and assigned.\n\n"
                f"Employee: {task['employee']}\n"
                f"Task: {task['task']}\n"
                f"Deadline: {task['deadline']}\n"
                f"Priority: {task['priority']}\n\n"
                "Next step: employee notification will be added in the next version."
            )
        else:
            reply = result["message"]

    elif action == "cancel":
        result = engine.cancel_task(session_id)

        if result["status"] == "cancelled":
            reply = "Task cancelled. No employee message was sent."
        else:
            reply = result["message"]

    else:
        reply = "Unknown action."

    await query.edit_message_text(reply)


def run_bot():
    """
    Start the Telegram bot.
    """

    if not TELEGRAM_BOT_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is missing. Please update your .env file.")

    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(handle_confirmation))

    print("Telegram bot is running...")
    app.run_polling()
