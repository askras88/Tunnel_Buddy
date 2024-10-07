from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен вашего бота
TOKEN = '7906261755:AAHniCWm-5ybmJvFReY7iO8OJi64LvosM_I'

# Стартовое меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Почему платный VPN лучше?", callback_data='why_paid_vpn')],
        [InlineKeyboardButton("Выбрать подписку", callback_data='choose_subscription')],
        [InlineKeyboardButton("Инструкция по подключению", callback_data='instructions')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "👋 Привет, интернет-ковбой! 🤠 Готов покорять просторы сети без ограничений? "
        "С Tunnel Buddy ты можешь смотреть видео в высоком разрешении и не париться о скорости! 🚀 "
        "Чекать свой eligible, бороздить Rutracker, играть в покер 🃏 или серфить Pornhub без логина. "
        "Плюс, он стоит меньше, чем твой последний NFT! 💸 "
        "Подключай свои устройства и забудь о блокировках, как о своей последней неудачной криптоинвестиции! 😂"
    )
    
    await update.message.reply_photo(photo='https://freeimage.host/i/dp52ix4', caption=welcome_text, reply_markup=reply_markup)

# Обработка кнопок
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'why_paid_vpn':
        response_text = (
            "🤔 **Почему стоит выбрать платный VPN?**\n\n"
            "1. 🚀 **Максимальная скорость** — с Tunnel Buddy ваша интернет-скорость остается такой же быстрой, как у вашего провайдера. Никаких урезаний или лагов!\n\n"
            "2. 💸 **Лучшее соотношение цены и качества** — один из самых дешёвых VPN на рынке, но с премиальными возможностями. Отличная экономия на каждом подключении!\n\n"
            "3. 📱💻🖥️ **Мультиустройство** — подключайте сразу несколько устройств, не переплачивая за дополнительные подписки. Все гаджеты защищены одним щитом!\n\n"
            "4. 🔐 **Приватность на 100%** — ваши данные остаются полностью конфиденциальными, ни одного следа в сети. Даже ваш провайдер не узнает, где вы были!\n\n"
            "5. 🌍 **Доступ ко всему миру** — обходите блокировки и наслаждайтесь контентом без ограничений: будь то стриминг в 4K, покер-румы, или любые другие сайты!"
        )
        await query.edit_message_text(text=response_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data='back_to_start')]]))

    elif query.data == 'choose_subscription':
        subscription_keyboard = [
            [InlineKeyboardButton("1 месяц / 2 USDT", callback_data='1_month')],
            [InlineKeyboardButton("3 месяца / 5 USDT", callback_data='3_months')],
            [InlineKeyboardButton("1 год / 15 USDT", callback_data='1_year')],
            [InlineKeyboardButton("Назад", callback_data='back_to_start')]
        ]
        await query.edit_message_text(text="Выберите подписку:", reply_markup=InlineKeyboardMarkup(subscription_keyboard))

    elif query.data == 'instructions':
        instruction_keyboard = [
            [InlineKeyboardButton("Скачать приложение", callback_data='download_app')],
            [InlineKeyboardButton("Добавить туннель", callback_data='add_tunnel')],
            [InlineKeyboardButton("Назад", callback_data='back_to_start')]
        ]
        await query.edit_message_text(text="Гайд по установке и добавлению VPN туннеля", reply_markup=InlineKeyboardMarkup(instruction_keyboard))

    elif query.data == 'download_app':
        device_keyboard = [
            [InlineKeyboardButton("iPhone", url="https://itunes.apple.com/app/outline-app/id1356177741")],
            [InlineKeyboardButton("Android", url="https://play.google.com/store/apps/details?id=org.outline.android.client")],
            [InlineKeyboardButton("Windows", url="https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe")],
            [InlineKeyboardButton("macOS", url="https://itunes.apple.com/app/outline-app/id1356178125")],
            [InlineKeyboardButton("Назад", callback_data='back_to_instructions')]
        ]
        await query.edit_message_text(text="Выберите ваше устройство:", reply_markup=InlineKeyboardMarkup(device_keyboard))

    elif query.data == 'add_tunnel':
        tunnel_instructions = (
            "🛠️ **Инструкция по добавлению туннеля в VPN Outline:**\n\n"
            "1. Установите приложение Outline на ваше устройство.\n\n"
            "2. Откройте приложение и выберите 'Добавить туннель'.\n\n"
            "3. Вставьте ваш ключ доступа, который вы получили от вашего провайдера.\n\n"
            "4. Нажмите 'Подключиться'.\n\n"
            "5. После подключения вы сможете наслаждаться безопасным и быстрым интернетом."
        )
        await query.edit_message_text(text=tunnel_instructions, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data='back_to_instructions')]]))

    elif query.data in ['1_month', '3_months', '1_year']:
        payment_keyboard = [
            [InlineKeyboardButton("Криптовалютой", callback_data='pay_with_crypto')],
            [InlineKeyboardButton("Банковской картой", callback_data='pay_with_card')],
            [InlineKeyboardButton("Назад", callback_data='choose_subscription')]
        ]
        await query.edit_message_text(text="Выберите способ оплаты:", reply_markup=InlineKeyboardMarkup(payment_keyboard))

    elif query.data == 'pay_with_crypto':
        crypto_response = (
            "💰 **Номер кошелька:** 0x34b46b61f1ea155de045c4b840932067c6087918\n"
            "Принимаем $USDT в сетях: ERC20, BSC, POLYGON, BASE, SCROLL\n\n"
            "📩 Нажмите 'Отправить txid' для отправки транзакции."
        )
        await query.edit_message_text(text=crypto_response, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Отправить txid", url="https://t.me/askras88")]]))

    elif query.data == 'pay_with_card':
        card_response = (
            "💳 **Номер карты:** 2204320368112944\n\n"
            "📩 Нажмите 'Отправить чек' для отправки подтверждения."
        )
        await query.edit_message_text(text=card_response, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Отправить чек", url="https://t.me/askras88")]]))

    elif query.data == 'back_to_start':
        await start(update, context)

    elif query.data == 'back_to_instructions':
        await button(update, context)

# Основная функция для запуска бота
def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()
