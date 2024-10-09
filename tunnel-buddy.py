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
            await instructions(update, context)  # Возврат в инструкции
        elif context.user_data.get('prev_menu') == 'download_app':
            await download_app(update, context)  # Возврат в меню загрузки
        else:
            await start(update, context)  # Возврат в стартовое меню
    else:
        # Логика для других кнопок
        pass

# Блок «Почему платный VPN лучше?»
async def why_vpn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data['prev_menu'] = 'why_vpn'
    await query.edit_message_text(text="🤔 Почему стоит выбрать платный VPN?", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data='back')]]))

# Блок «Выбрать подписку»
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

# Основной код
if __name__ == '__main__':
    application = ApplicationBuilder().token('7906261755:AAHniCWm-5ybmJvFReY7iO8OJi64LvosM_I').build()

    # Команды и обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Запуск бота
    application.run_polling()
