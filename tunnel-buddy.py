import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Стартовое сообщение
WELCOME_MESSAGE = """👋 Привет, интернет-ковбой! 🤠 Готов покорять просторы сети без ограничений? 
С Tunnel Buddy ты можешь смотреть видео в высоком разрешении и не париться о скорости! 🚀 Чекать свой eligible, наслаждаться Youtube или Instagram, бороздить Rutracker, играть в покер 🃏 или серфить Pornhub без логина. Плюс, он стоит меньше, чем твой последний NFT! 💸
Подключай свои устройства и забудь о блокировках, как о своей последней неудачной криптоинвестиции! 😂"""

# Клавиатура стартового меню
def start_menu():
    keyboard = [
        [InlineKeyboardButton("Почему платный VPN лучше?", callback_data='why_vpn')],
        [InlineKeyboardButton("Выбрать подписку", callback_data='choose_subscription')],
        [InlineKeyboardButton("Инструкция по подключению", callback_data='instructions')],
        [InlineKeyboardButton("Скачать приложение", callback_data='download_app')],
        [InlineKeyboardButton("Скачать другое приложение", callback_data='download_other_app')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Команда /start
async def start(update: Update, context):
    chat_id = update.effective_chat.id
    await context.bot.send_photo(chat_id=chat_id, photo="https://freeimage.host/i/dpppkxI")
    await context.bot.send_message(chat_id=chat_id, text=WELCOME_MESSAGE, reply_markup=start_menu())

# Блок «Почему платный VPN лучше?»
WHY_VPN_TEXT = """🤔 Почему стоит выбрать платный VPN?

1. 🚀 Максимальная скорость — с Tunnel Buddy ваша интернет-скорость остается такой же быстрой, как у вашего провайдера. Никаких урезаний или лагов!
2. 💸 Лучшее соотношение цены и качества — один из самых дешёвых VPN на рынке, но с премиальными возможностями.
3. 📱💻🖥️ Мультиустройство — подключайте несколько устройств без дополнительных подписок.
4. 🔐 Приватность на 100% — ваши данные конфиденциальны, ни одного следа в сети.
5. 🌍 Доступ ко всему миру — обходите блокировки и наслаждайтесь контентом без ограничений!"""

async def why_vpn(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=WHY_VPN_TEXT, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data='back_to_start')]]))

# Блок «Выбрать подписку»
def subscription_menu():
    keyboard = [
        [InlineKeyboardButton("1 месяц / 2 $USDT / 200 RUB", callback_data='sub_1m')],
        [InlineKeyboardButton("3 месяца / 5 $USDT / 500 RUB", callback_data='sub_3m')],
        [InlineKeyboardButton("1 год / 15 $USDT / 1500 RUB", callback_data='sub_1y')],
        [InlineKeyboardButton("Назад", callback_data='back_to_start')]
    ]
    return InlineKeyboardMarkup(keyboard)

async def choose_subscription(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Выберите подписку:", reply_markup=subscription_menu())

# Блок «Оплата криптовалютой»
CRYPTO_PAYMENT = """💰 Номер кошелька копируется при нажатии: `0x99f5b3748f9e8d5e13e20639cc986ab53b6be753`
Принимаем $USDT в сетях: ERC20, BSC, POLYGON, BASE, SCROLL"""

async def crypto_payment(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text=CRYPTO_PAYMENT, 
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Отправить txid", url="https://t.me/askras88")],
            [InlineKeyboardButton("Назад", callback_data='back_to_payment')]
        ]),
        parse_mode='Markdown'  # Добавлено для поддержки моноширокого шрифта
    )

# Блок «Оплата банковской картой»
CARD_PAYMENT = """💳 Номер карты копируется при нажатии `2204320368112944`"""

async def card_payment(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=CARD_PAYMENT, parse_mode='MarkdownV2', reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Отправить чек", url="https://t.me/askras88")],
        [InlineKeyboardButton("Назад", callback_data='back_to_payment')]
    ]))

# Блок «Инструкция по подключению»
INSTRUCTIONS_TEXT = """ 🛠️ Инструкция по добавлению туннеля в VPN Outline:

1. Установите приложение Outline на ваше устройство.
2. Откройте приложение и выберите "Добавить туннель" или нажмите на «+».
3. Вставьте ключ доступа, который вы получили от Buddy.
4. Нажмите "Подключиться".
5. Готово! Теперь вы можете безопасно и анонимно пользоваться интернетом. 🌐"""

async def instructions(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=INSTRUCTIONS_TEXT, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data='back_to_start')]]))

# Блок «Скачать приложение»
async def download_app(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Выберите устройство:", reply_markup=download_menu())

# Меню для загрузки приложения
def download_menu():
    keyboard = [
        [InlineKeyboardButton("iPhone", url="https://itunes.apple.com/app/outline-app/id1356177741")],
        [InlineKeyboardButton("Android", url="https://play.google.com/store/apps/details?id=org.outline.android.client")],
        [InlineKeyboardButton("Windows", url="https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe")],
        [InlineKeyboardButton("macOS", url="https://itunes.apple.com/app/outline-app/id1356178125")],
        [InlineKeyboardButton("Назад", callback_data='back_to_start')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Обработка нажатий кнопок
async def button_handler(update: Update, context):
    query = update.callback_query
    data = query.data
    logger.info(f"Button pressed: {data}")
    await query.answer()
    
    # Блок «Скачать другое приложение»
async def download_other_app(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Выберите устройство:", reply_markup=other_app_menu())

# Меню для загрузки другого приложения
def other_app_menu():
    keyboard = [
        [InlineKeyboardButton("iPhone", url="https://apps.apple.com/ru/app/%D0%B4%D1%8F%D0%B4%D1%8F-%D0%B2%D0%B0%D0%BD%D1%8F-vpn/id1618096210")],
        [InlineKeyboardButton("Android", url="https://play.google.com/store/apps/details?id=com.vanyavpn.android.client")],
        [InlineKeyboardButton("Windows", url="https://amazonvpn.s3.amazonaws.com/VanyaVPN.exe")],
        [InlineKeyboardButton("macOS", url="https://apps.apple.com/ru/app/vanyavpn/id6444087613")],
        [InlineKeyboardButton("Назад", callback_data='back_to_start')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Обработка нажатий кнопок
async def button_handler(update: Update, context):
    query = update.callback_query
    data = query.data
    logger.info(f"Button pressed: {data}")
    await query.answer()

    if data == 'why_vpn':
        await why_vpn(update, context)
    elif data == 'choose_subscription':
        await choose_subscription(update, context)
    elif data == 'sub_1m':
        await query.edit_message_text(text="Вы выбрали подписку на 1 месяц. Выберите способ оплаты:", reply_markup=payment_menu())
    elif data == 'sub_3m':
        await query.edit_message_text(text="Вы выбрали подписку на 3 месяца. Выберите способ оплаты:", reply_markup=payment_menu())
    elif data == 'sub_1y':
        await query.edit_message_text(text="Вы выбрали подписку на 1 год. Выберите способ оплаты:", reply_markup=payment_menu())
    elif data == 'instructions':
        await instructions(update, context)
    elif data == 'download_app':
        await download_app(update, context)
    elif data == 'download_other_app':
        await download_other_app(update, context)
    elif data == 'back_to_start':
        await start(update, context)  # Возврат в стартовое меню
    elif data == 'back_to_payment':
        await query.edit_message_text(text="Выберите способ оплаты:", reply_markup=payment_menu())
    elif data == 'crypto':
        await crypto_payment(update, context)
    elif data == 'card':
        await card_payment(update, context)

# Меню способов оплаты
def payment_menu():
    keyboard = [
        [InlineKeyboardButton("Криптовалютой", callback_data='crypto')],
        [InlineKeyboardButton("Банковской картой", callback_data='card')],
        [InlineKeyboardButton("Назад", callback_data='choose_subscription')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Основной код
if __name__ == '__main__':
    application = ApplicationBuilder().token('7906261755:AAHniCWm-5ybmJvFReY7iO8OJi64LvosM_I').build()

    # Команды и обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Запуск бота
    application.run_polling()
