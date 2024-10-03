async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Выбрать подписку", callback_data='choose_subscription')],
        [InlineKeyboardButton("Почему платный VPN?", callback_data='why_paid_vpn')],
        [InlineKeyboardButton("Инструкция по пользованию", callback_data='instructions')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Привет, интернет-ковбой! 🤠 Готов покорять просторы сети без ограничений? 
        С Tunnel Buddy вы можете смотреть видео в высоком разрешении и не париться о скорости! 
        🚀 Чекать свой eligible, бороздить Rutracker, играть в покер 🃏 или серфить Pornhub без логина.
        Плюс, он стоит меньше, чем твой последний NFT! 💸 
        Подключайте свои устройства и забудьте о блокировках, как о своей последней неудачной криптоинвестиции! 😂",
        reply_markup=reply_markup
    )

async def why_paid_vpn(update: Update, context: CallbackContext) -> None:
    text = (
        "🤔 **Почему стоит выбрать платный VPN, а не бесплатный?**\n\n"
        "1. 🚀 **Максимальная скорость** — Без урезаний, без лагов. Ваша скорость останется на уровне провайдера!\n"
        "2. 💸 **Экономия** — Самый дешевый в своём классе, но с премиальными возможностями.\n"
        "3. 📱💻 **Мультиустройство** — Подключайте несколько устройств без доплаты!\n"
        "4. 🔐 **Приватность** — Полная защита данных, без следов в сети.\n"
        "5. 🌍 **Доступ ко всему миру** — Обходите блокировки и смотрите любой контент!"
    )

    keyboard = [[InlineKeyboardButton("Назад", callback_data='start')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.callback_query.edit_message_text(text=text, reply_markup=reply_markup, parse_mode='Markdown')

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(why_paid_vpn, pattern='why_paid_vpn'))
    application.add_handler(CallbackQueryHandler(start, pattern='start'))

    application.run_polling()

if __name__ == '__main__':
    main()
