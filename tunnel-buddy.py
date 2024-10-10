import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Сообщения на двух языках
WELCOME_MESSAGE_RU = """👋 Привет, интернет-ковбой! 🤠 Готов покорять просторы сети без ограничений? 
С Tunnel Buddy ты можешь смотреть видео в высоком разрешении и не париться о скорости! 🚀 Чекать свой eligible, бороздить Rutracker или серфить Pornhub без логина. Плюс, он стоит меньше, чем твой последний NFT! 💸
Подключай свои устройства и забудь о блокировках, как о своей последней неудачной криптоинвестиции! 😂"""

WELCOME_MESSAGE_EN = """👋 Hey, internet cowboy! 🤠 Ready to explore the web without restrictions?
With Tunnel Buddy, you can stream videos in high quality and not worry about speed! 🚀 Browse your eligible, surf Rutracker or scroll through Pornhub without logging in. Plus, it's cheaper than your last NFT! 💸
Connect your devices and forget about blocks like your last failed crypto investment! 😂"""

# Языковое меню
def language_menu():
    keyboard = [
        [InlineKeyboardButton("Русский", callback_data='lang_ru')],
        [InlineKeyboardButton("English", callback_data='lang_en')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Стартовая команда с выбором языка
async def start(update: Update, context):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text="Выберите язык / Choose your language:", reply_markup=language_menu())

# Обработчик выбора языка
async def language_handler(update: Update, context):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == 'lang_ru':
        # Отправляем русскую версию
        await context.bot.send_photo(chat_id=query.message.chat_id, photo="https://freeimage.host/i/29CFwn1")
        await context.bot.send_message(chat_id=query.message.chat_id, text=WELCOME_MESSAGE_RU, reply_markup=start_menu_ru())
    elif data == 'lang_en':
        # Отправляем английскую версию
        await context.bot.send_photo(chat_id=query.message.chat_id, photo="https://freeimage.host/i/29CFwn1")
        await context.bot.send_message(chat_id=query.message.chat_id, text=WELCOME_MESSAGE_EN, reply_markup=start_menu_en())

# Стартовое меню на русском
def start_menu_ru():
    keyboard = [
        [InlineKeyboardButton("Почему платный VPN лучше?", callback_data='why_vpn')],
        [InlineKeyboardButton("Выбрать подписку", callback_data='choose_subscription')],
        [InlineKeyboardButton("Инструкция по подключению", callback_data='instructions')],
        [InlineKeyboardButton("Скачать приложение", callback_data='download_app')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Стартовое меню на английском
def start_menu_en():
    keyboard = [
        [InlineKeyboardButton("Why Paid VPN is Better?", callback_data='why_vpn')],
        [InlineKeyboardButton("Choose a Subscription", callback_data='choose_subscription')],
        [InlineKeyboardButton("Connection Instructions", callback_data='instructions')],
        [InlineKeyboardButton("Download App", callback_data='download_app')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Обработчики других кнопок меню
async def menu_handler(update: Update, context):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == 'why_vpn':
        await context.bot.send_message(chat_id=query.message.chat_id, text="Платный VPN предлагает больше возможностей: улучшенная защита данных, высокая скорость и отсутствие рекламы.")
    elif data == 'choose_subscription':
        await context.bot.send_message(chat_id=query.message.chat_id, text="Доступные подписки: 1 месяц, 6 месяцев, 12 месяцев. Какую хотите выбрать?")
    elif data == 'instructions':
        await context.bot.send_message(chat_id=query.message.chat_id, text="Чтобы подключиться, скачайте приложение и следуйте инструкции на экране.")
    elif data == 'download_app':
        await context.bot.send_message(chat_id=query.message.chat_id, text="Скачайте приложение по этой ссылке: https://example.com")

# Основной код для запуска бота
if __name__ == '__main__':
    application = ApplicationBuilder().token('7906261755:AAHniCWm-5ybmJvFReY7iO8OJi64LvosM_I').build()

    # Команды и обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(language_handler, pattern='^lang_'))
    application.add_handler(CallbackQueryHandler(menu_handler, pattern='^why_vpn|choose_subscription|instructions|download_app$'))

    application.run_polling()
