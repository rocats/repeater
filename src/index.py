import os
from telegram import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext import (
    Updater,
    MessageHandler,
    Filters,
)

from tool.logger import logger
from component.repeat import repeat


def ErrorHandler(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


if __name__ == "__main__":
    # add updater and dispatcher
    updater = Updater(os.getenv("TELEGRAM_APITOKEN"), use_context=True)
    dp = updater.dispatcher

    # add filter
    repeat_filters = Filters.text & ~Filters.command

    # add handlers
    dp.add_error_handler(ErrorHandler)
    dp.add_handler(MessageHandler(repeat_filters, repeat))
    dp.add_handler(MessageHandler(Filters.all & ~repeat_filters, repeat))

    # Start the Bot
    logger.info("Server starts!")
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
