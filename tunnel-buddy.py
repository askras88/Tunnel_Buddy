from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен вашего бота
TOKEN = '7906261755:AAHniCWm-5ybmJvFReY7iO8OJi64LvosM_I'

# Прямая ссылка на изображение
IMAGE_PATH = "https://freeimage.host/i/dbPhDcQ"  # Укажите здесь путь к изображению

# Стартовое меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Почему платный VPN лучше?", callback_data='why_paid_vpn')],
        [InlineKeyboardButton("Выбрать подписку", callback_data='choose_subscription')],
        [InlineKeyboardButton("Инструкция по подключению", callback_data='instructions')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Если это сообщение, то используем message.reply_text
    if update.message:
        await update.message.reply_text(
            "👋 Привет, интернет-ковбой! 🤠 Готов покорять просторы сети без ограничений?\n"
            "С Tunnel Buddy ты можешь смотреть видео в высоком разрешении и не париться о скорости! 🚀 "
            "Чекать свой eligible, бороздить Rutracker, играть в покер 🃏 или серфить Pornhub без логина. "
            "Плюс, он стоит меньше, чем твой последний NFT! 💸\n"
            "Подключай свои устройства и забудь о блокировках, как о своей последней неудачной криптоинвестиции! 😂",
            reply_markup=reply_markup
        )
        # Отправка изображения
        await update.message.reply_photo(photo=InputFile(IMAGE_PATH))

    # Если это callback, используем callback_query.edit_message_text
    elif update.callback_query:
        await update.callback_query.edit_message_text(
            "👋 Привет, интернет-ковбой! 🤠 Готов покорять просторы сети без ограничений?\n"
            "С Tunnel Buddy ты можешь смотреть видео в высоком разрешении и не париться о скорости! 🚀 "
            "Чекать свой eligible, бороздить Rutracker, играть в покер 🃏 или серфить Pornhub без логина. "
            "Плюс, он стоит меньше, чем твой последний NFT! 💸\n"
            "Подключай свои устройства и забудь о блокировках, как о своей последней неудачной криптоинвестиции! 😂",
            reply_markup=reply_markup
        )

# Меню с преимуществами платного VPN
async def why_paid_vpn(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        "🤔 **Почему стоит выбрать платный VPN?**\n\n"
        "1. 🚀 **Максимальная скорость** — с Tunnel Buddy ваша интернет-скорость остается такой же быстрой, как у вашего провайдера. Никаких урезаний или лагов!\n"
        "2. 💸 **Лучшее соотношение цены и качества** — один из самых дешёвых VPN на рынке, но с премиальными возможностями. Отличная экономия на каждом подключении!\n"
        "3. 📱💻🖥️ **Мультиустройство** — подключайте сразу несколько устройств, не переплачивая за дополнительные подписки. Все гаджеты защищены одним щитом!\n"
        "4. 🔐 **Приватность на 100%** — ваши данные остаются полностью конфиденциальными, ни одного следа в сети. Даже ваш провайдер не узнает, где вы были!\n"
        "5. 🌍 **Доступ ко всему миру** — обходите блокировки и наслаждайтесь контентом без ограничений: будь то стриминг в 4K, покер-румы, или любые другие сайты!"
    )
    
    keyboard = [[InlineKeyboardButton("Назад", callback_data='back_to_start')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.callback_query.edit_message_text(text=text, reply_markup=reply_markup, parse_mode='Markdown')

# Меню выбора подписки
async def choose_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("1 месяц / 2 USDT", callback_data='1_month')],
        [InlineKeyboardButton("3 месяца / 5 USDT", callback_data='3_months')],
        [InlineKeyboardButton("1 год / 15 USDT", callback_data='1_year')],
        [InlineKeyboardButton("Назад", callback_data='back_to_start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text="Выберите подписку:", reply_markup=reply_markup)

# Меню выбора способа оплаты
async def payment_method(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Оплатить картой", callback_data='pay_card')],
        [InlineKeyboardButton("Оплатить криптовалютой", callback_data='pay_crypto')],
        [InlineKeyboardButton("Назад", callback_data='back_to_choose_subscription')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text="Выберите способ оплаты:", reply_markup=reply_markup)

# Обработка всех callback-запросов
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'why_paid_vpn':
        await why_paid_vpn(update, context)

    elif query.data == 'choose_subscription':
        await choose_subscription(update, context)

    elif query.data in ['1_month', '3_months', '1_year']:
        await payment_method(update, context)

    elif query.data == 'instructions':
        await query.edit_message_text(
            text="Гайд по установке и добавлению VPN туннеля.\n\nНажмите 'Назад' для возврата.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data='back_to_start')]])
        )

    elif query.data == 'pay_card':
        await query.edit_message_text(text="Номер карты: 1234 5678 9012 3456\nПосле оплаты отправьте чек на @askras88.",
                                       reply_markup=InlineKeyboardMarkup([
                                           [InlineKeyboardButton("Отправить чек", url='https://t.me/askras88')],
                                           [InlineKeyboardButton("Назад", callback_data='back_to_payment_method')]
                                       ]))

    elif query.data == 'pay_crypto':
        await query.edit_message_text(text="Номер кошелька: 0x34b46b61f1ea155de045c4b840932067c6087918\nПринимаю $USDT в сетях: ERC20, BSC, POLYGON, BASE, SCROLL.\nОтправьте адрес транзакции на @askras88.",
                                       reply_markup=InlineKeyboardMarkup([
                                           [InlineKeyboardButton("Отправить txid", url='https://t.me/askras88')],
                                           [InlineKeyboardButton("Назад", callback_data='back_to_payment_method')]
                                       ]))

    # Обработка кнопок "Назад"
    elif query.data == 'back_to_start':
        await start(update, context)

    elif query.data == 'back_to_choose_subscription':
        await choose_subscription(update, context)

    elif query.data == 'back_to_payment_method':
        await payment_method(update, context)

# Основная функция для запуска бота
def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()
