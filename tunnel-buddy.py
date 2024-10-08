from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, InlineKeyboardButton, InlineKeyboardMarkup

# Увеличьте таймаут для запросов к API Telegram (в секундах)
bot = Bot(token="7906261755:AAHniCWm-5ybmJvFReY7iO8OJi64LvosM_I", request_timeout=30)

# Инициализация бота с увеличенным таймаутом
app = Application.builder().token("7906261755:AAHniCWm-5ybmJvFReY7iO8OJi64LvosM_I").bot(bot).build()

# Функция для команды /start
async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Почему платный VPN лучше?", callback_data='why_paid')],
        [InlineKeyboardButton("Выбрать подписку", callback_data='choose_subscription')],
        [InlineKeyboardButton("Инструкция по подключению", callback_data='setup_instructions')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 Привет, интернет-ковбой! 🤠 Готов покорять просторы сети без ограничений?\n\n"
        "С Tunnel Buddy ты можешь смотреть видео в высоком разрешении и не париться о скорости! 🚀 "
        "Чекать свой eligible, бороздить Rutracker, играть в покер 🃏 или серфить Pornhub без логина. "
        "Плюс, он стоит меньше, чем твой последний NFT! 💸\n\n"
        "Подключай свои устройства и забудь о блокировках, как о своей последней неудачной криптоинвестиции! 😂",
        reply_markup=reply_markup
    )

# "Почему платный VPN лучше?"
async def why_paid(update: Update, context):
    query = update.callback_query
    await query.answer()
    
    keyboard = [[InlineKeyboardButton("Назад", callback_data='start')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "🤔 **Почему стоит выбрать платный VPN?**\n\n"
        "1. 🚀 **Максимальная скорость** — с Tunnel Buddy ваша интернет-скорость остается такой же быстрой, как у вашего провайдера.\n\n"
        "2. 💸 **Лучшее соотношение цены и качества** — один из самых дешёвых VPN на рынке, но с премиальными возможностями.\n\n"
        "3. 📱💻🖥️ **Мультиустройство** — подключайте сразу несколько устройств, не переплачивая за дополнительные подписки.\n\n"
        "4. 🔐 **Приватность на 100%** — ваши данные остаются полностью конфиденциальными.\n\n"
        "5. 🌍 **Доступ ко всему миру** — обходите блокировки и наслаждайтесь контентом без ограничений.",
        reply_markup=reply_markup
    )

# Выбор подписки
async def choose_subscription(update: Update, context):
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("1 месяц / 2 $USDT / 200 RUB", callback_data='pay_crypto')],
        [InlineKeyboardButton("3 месяца / 5 $USDT / 500 RUB", callback_data='pay_crypto')],
        [InlineKeyboardButton("1 год / 15 $USDT / 1500 RUB", callback_data='pay_crypto')],
        [InlineKeyboardButton("Назад", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text("Выберите подписку:", reply_markup=reply_markup)

# Способы оплаты
async def pay_crypto(update: Update, context):
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("Криптовалютой", callback_data='crypto_payment')],
        [InlineKeyboardButton("Банковской картой", callback_data='card_payment')],
        [InlineKeyboardButton("Назад", callback_data='choose_subscription')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text("Выберите способ оплаты:", reply_markup=reply_markup)

# Оплата криптовалютой
async def crypto_payment(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    keyboard = [[InlineKeyboardButton("Назад", callback_data='pay_crypto')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "💰 **Номер кошелька:** 0x34b46b61f1ea155de045c4b840932067c6087918\n"
        "Принимаем $USDT в сетях: ERC20, BSC, POLYGON, BASE, SCROLL.\n\n",
        reply_markup=reply_markup
    )

# Оплата картой
async def card_payment(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    keyboard = [[InlineKeyboardButton("Скопировать номер карты", callback_data='copy_card_number')],
                [InlineKeyboardButton("Назад", callback_data='pay_crypto')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "💳 Номер карты: 2204320368112944\n",
        reply_markup=reply_markup
    )

# Обработчик копирования номера карты
async def copy_card_number(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    # Копируем номер карты в кэш (в этом случае просто отправим его обратно пользователю)
    await query.message.reply_text("Номер карты скопирован в кэш: 2204320368112944")

# Инструкция по подключению
async def setup_instructions(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("Скачать приложение", callback_data='download_app')],
        [InlineKeyboardButton("Добавить туннель", callback_data='add_tunnel')],
        [InlineKeyboardButton("Назад", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text("Гайд по установке и добавлению VPN туннеля:", reply_markup=reply_markup)

# Скачать приложение
async def download_app(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("iPhone", url="https://itunes.apple.com/app/outline-app/id1356177741")],
        [InlineKeyboardButton("Android", url="https://play.google.com/store/apps/details?id=org.outline.android.client")],
        [InlineKeyboardButton("Windows", url="https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe")],
        [InlineKeyboardButton("macOS", url="https://itunes.apple.com/app/outline-app/id1356178125")],
        [InlineKeyboardButton("Назад", callback_data='setup_instructions')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text("Выберите ваше устройство:", reply_markup=reply_markup)

# Добавить туннель
async def add_tunnel(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    keyboard = [[InlineKeyboardButton("Назад", callback_data='setup_instructions')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "🛠️ **Инструкция по добавлению туннеля в VPN Outline:**\n\n"
        "1. Установите приложение Outline.\n"
        "2. Откройте приложение и выберите 'Добавить туннель'.\n"
        "3. Вставьте ключ доступа.\n"
        "4. Нажмите 'Подключиться'.\n"
        "5. Готово! Теперь вы можете пользоваться интернетом через VPN Tunnel Buddy.",
        reply_markup=reply_markup
    )

# Главная функция для запуска бота
def main():
    application = Application.builder().token("7906261755:AAHniCWm-5ybmJvFReY7iO8OJi64LvosM_I").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(why_paid, pattern='why_paid'))
    application.add_handler(CallbackQueryHandler(choose_subscription, pattern='choose_subscription'))
    application.add_handler(CallbackQueryHandler(pay_crypto, pattern='pay_crypto'))
    application.add_handler(CallbackQueryHandler(crypto_payment, pattern='crypto_payment'))
    application.add_handler(CallbackQueryHandler(card_payment, pattern='card_payment'))
    application.add_handler(CallbackQueryHandler(copy_card_number, pattern='copy_card_number'))  # Новый обработчик
    application.add_handler(CallbackQueryHandler(setup_instructions, pattern='setup_instructions'))
    application.add_handler(CallbackQueryHandler(download_app, pattern='download_app'))
    application.add_handler(CallbackQueryHandler(add_tunnel, pattern='add_tunnel'))

    application.run_polling()

if __name__ == '__main__':
    main()
