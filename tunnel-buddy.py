from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Токен вашего бота
TOKEN = '7906261755:AAHniCWm-5ybmJvFReY7iO8OJi64LvosM_I'

async def start(update: Update, context: CallbackContext) -> None:
    print("Бот запущен и ожидает команд.")
    keyboard = [
        [InlineKeyboardButton("Выбрать подписку", callback_data='choose_subscription')],
        [InlineKeyboardButton("Инструкция по пользованию", callback_data='instructions')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Добро пожаловать! Вот баннер-знакомство.",
        reply_markup=reply_markup
    )

async def choose_subscription(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("1 месяц / 2 USDT", callback_data='1_month')],
        [InlineKeyboardButton("3 месяца / 5 USDT", callback_data='3_months')],
        [InlineKeyboardButton("1 год / 15 USDT", callback_data='1_year')],
        [InlineKeyboardButton("Старт", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text="Выберите подписку:", reply_markup=reply_markup)

async def payment_method(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Оплатить картой", callback_data='pay_card')],
        [InlineKeyboardButton("Оплатить криптовалютой", callback_data='pay_crypto')],
        [InlineKeyboardButton("Старт", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text="Выберите способ оплаты:", reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'choose_subscription':
        await choose_subscription(update, context)

    elif query.data in ['1_month', '3_months', '1_year']:
        await payment_method(update, context)

    elif query.data == 'instructions':
        await query.edit_message_text(
            text="Гайд по установке и добавлению VPN туннеля.\n\nНажмите 'Старт' для возврата.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Старт", callback_data='start')]])
        )

    elif query.data == 'pay_card':
        await query.edit_message_text(text="Номер карты: 1234 5678 9012 3456\nПосле оплаты отправьте чек на @askras88.",
                                       reply_markup=InlineKeyboardMarkup([
                                           [InlineKeyboardButton("Отправить чек", url='https://t.me/askras88')],
                                           [InlineKeyboardButton("Старт", callback_data='start')]
                                       ]))

    elif query.data == 'pay_crypto':
        await query.edit_message_text(text="Номер кошелька: 0x34b46b61f1ea155de045c4b840932067c6087918\nПринимаю $USDT в сетях: ERC20, BSC, POLYGON, BASE, SCROLL.\nОтправьте адрес транзакции на @askras88.",
                                       reply_markup=InlineKeyboardMarkup([
                                           [InlineKeyboardButton("Отправить txid", url='https://t.me/askras88')],
                                           [InlineKeyboardButton("Старт", callback_data='start')]
                                       ]))

    elif query.data == 'start':
        await start(update, context)

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()
