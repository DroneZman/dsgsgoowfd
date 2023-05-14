from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from response_generator import generate_response

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Приветствую! Я ChatGPT, готов помочь вам.')

def respond(update: Update, context: CallbackContext) -> None:
    """Generate response for the user message."""
    text = update.message.text
    response = generate_response(context.user_data, text)
    update.message.reply_text(response)

def context_on(update: Update, context: CallbackContext) -> None:
    context.user_data['context_on'] = True
    update.message.reply_text('Функция поддержания контекста включена.')

def context_off(update: Update, context: CallbackContext) -> None:
    context.user_data['context_on'] = False
    update.message.reply_text('Функция поддержания контекста выключена.')

def main() -> None:
    """Start the bot."""
    updater = Updater("5438377499:AAFI1IWWSre8SdmCgKVQgtYvAqDf46RuIjw", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("context_on", context_on))
    dispatcher.add_handler(CommandHandler("context_off", context_off))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, respond))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
