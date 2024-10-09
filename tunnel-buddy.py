import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Стартовое сообщение
WELCOME_MESSAGE = """👋 Привет, интернет-ковбой! 🤠 Готов покорять просторы сети без ограничений? 
С Tunnel Buddy ты можешь смотреть видео в высоком разрешении и не париться о скорости! 🚀 Чекать свой eligible, бороздить Rutracker, играть в покер 🃏 или серфить Pornhub без логина. Плюс, он стоит меньше, чем твой последний NFT! 💸
Подключай свои устройства и забудь о блокировках, как о своей последней неудачной криптоинвестиции! 😂"""

# Клавиатура стартового меню
def start_menu():
    keyboard = [
        [InlineKeyboardButton("Почему платный VPN лучше?", callback_data='why_vpn')],
        [InlineKeyboardButton("Выбрать подписку", callback_data='choose_subscription')],
        [InlineKeyboardButton("Инструкция по подключению", callback_data='instructions')],
        [InlineKeyboardButton("Скачать приложение", callback_data='download_app')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_photo(chat_id=chat_id, photo="https://freeimage.host/i/dpppkxI")
    await context.bot.send_message(chat_id=chat_id, text=WELCOME_MESSAGE, reply_markup=start_menu())

# Блок «Почему платный VPN лучше?»
async def why_vpn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data['prev_menu'] = 'why_vpn'
    WHY_VPN_TEXT = """🤔 Почему стоит выбрать платный VPN?
    
1. 🚀 Максимальная скорость — с Tunnel Buddy ваша интернет-скорость остается такой же быстрой, как у вашего провайдера. Никаких урезаний или лагов!
2. 💸 Лучшее соотношение цены и качества — один из самых дешёвых VPN на рынке, но с премиальными возможностями.
3. 📱💻🖥️ Мультиустройство — подключайте несколько устройств без дополнительных подписок.
4. 🔐 Приватность на 100% — ваши данные конфиденциальны, ни одного следа в сети.
5. 🌍 Доступ ко всему миру — обходите блокировки и наслаждайтесь контентом без ограничений!"""
    
    await query.edit_message_text(text=WHY_VPN_TEXT, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data='back')]]))

# Блок «Выбрать подписку»
def subscription_menu():
    keyboard = [
        [InlineKeyboardButton("1 месяц / 2 $USDT / 200 RUB", callback_data='sub_1m')],
        [InlineKeyboardButton("3 месяца / 5 $USDT / 500 RUB", callback_data='sub_3m')],
        [InlineKeyboardButton("1 год / 15 $USDT / 1500 RUB", callback_data='sub_1y')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    return InlineKeyboardMarkup(keyboard)

async def choose_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data['prev_menu'] = 'choose_subscription'
    await query.edit_message_text(text="Выберите подписку:", reply_markup=subscription_menu())

# Блок «Инструкция по подключению»
async def instructions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data['prev_menu'] = 'instructions'
    await query.edit_message_text(text="🛠️ Инструкция по подключению:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data='back')]]))

# Блок «Скачать приложение»
async def download_app(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data['prev_menu'] = 'download_app'
    await query.edit_message_text(text="Выберите устройство:", reply_markup=download_menu())

# Меню для загрузки приложения
def download_menu():
    keyboard = [
        [InlineKeyboardButton("iPhone", url="https://itunes.apple.com/app/outline-app/id1356177741")],
        [InlineKeyboardButton("Android", url="https://play.google.com/store/apps/details?id=org.outline.android.client")],
        [InlineKeyboardButton("Windows", url="https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe")],
        [InlineKeyboardButton("macOS", url="https://itunes.apple.com/app/outline-app/id1356178125")],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Обработка нажатий кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    logger.info(f"Button pressed: {data}")
    await query.answer()

    if data == 'why_vpn':
        await why_vpn(update, context)
    elif data == 'choose_subscription':
        await choose_subscription(update, context)
    elif data == 'instructions':
        await instructions(update, context)
    elif data == 'download_app':
        await download_app(update, context)
    elif data == 'back':
        if context.user_data.get('prev_menu') == 'instructions':
            await instructions(update, context)
        elif context.user_data.get('prev_menu') == 'download_app':
            await download_app(update, context)
        else:
            await start(update, context)

# Основной код
if __name__ == '__main__':
    application = ApplicationBuilder().token('YOUR_TOKEN_HERE').build()

    # Команды и обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Запуск бота
    application.run_polling()
