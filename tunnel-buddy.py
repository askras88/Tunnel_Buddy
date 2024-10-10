import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Welcome message
WELCOME_MESSAGE = """👋 Hey, internet cowboy! 🤠 Ready to explore the web without restrictions?
With Tunnel Buddy, you can stream videos in high quality and not worry about speed! 🚀 Browse your eligible, surf Rutracker, play poker 🃏 or scroll through Pornhub without logging in. Plus, it's cheaper than your last NFT! 💸
Connect your devices and forget about blocks like your last failed crypto investment! 😂"""

# Start menu keyboard
def start_menu():
    keyboard = [
        [InlineKeyboardButton("Why Paid VPN is Better?", callback_data='why_vpn')],
        [InlineKeyboardButton("Choose a Subscription", callback_data='choose_subscription')],
        [InlineKeyboardButton("Connection Instructions", callback_data='instructions')],
        [InlineKeyboardButton("Download App", callback_data='download_app')]
    ]
    return InlineKeyboardMarkup(keyboard)

# /start command
async def start(update: Update, context):
    chat_id = update.effective_chat.id
    await context.bot.send_photo(chat_id=chat_id, photo="https://freeimage.host/i/dpppkxI")
    await context.bot.send_message(chat_id=chat_id, text=WELCOME_MESSAGE, reply_markup=start_menu())

# "Why Paid VPN is Better?" block
WHY_VPN_TEXT = """🤔 Why choose a paid VPN?

1. 🚀 Maximum speed — with Tunnel Buddy, your internet speed remains as fast as your provider. No throttling or lags!
2. 💸 Best value — one of the cheapest VPNs on the market with premium features.
3. 📱💻🖥️ Multi-device — connect multiple devices without extra subscriptions.
4. 🔐 100% privacy — your data stays confidential, with no traces on the web.
5. 🌍 Global access — bypass blocks and enjoy unrestricted content!"""

async def why_vpn(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=WHY_VPN_TEXT, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data='back_to_start')]]))

# "Choose Subscription" block
def subscription_menu():
    keyboard = [
        [InlineKeyboardButton("1 month / 2 $USDT / 200 RUB", callback_data='sub_1m')],
        [InlineKeyboardButton("3 months / 5 $USDT / 500 RUB", callback_data='sub_3m')],
        [InlineKeyboardButton("1 year / 15 $USDT / 1500 RUB", callback_data='sub_1y')],
        [InlineKeyboardButton("Back", callback_data='back_to_start')]
    ]
    return InlineKeyboardMarkup(keyboard)

async def choose_subscription(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Choose a subscription:", reply_markup=subscription_menu())

# "Pay with Crypto" block
CRYPTO_PAYMENT = """💰 Wallet Address: `0x34b46b61f1ea155de045c4b840932067c6087918`
We accept $USDT on: ERC20, BSC, POLYGON, BASE, SCROLL"""

async def crypto_payment(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text=CRYPTO_PAYMENT, 
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Send txid", url="https://t.me/askras88")],
            [InlineKeyboardButton("Back", callback_data='back_to_payment')]
        ]),
        parse_mode='Markdown'
    )

# "Pay with Card" block
CARD_PAYMENT = """💳 Card Number: `2204320368112944`"""

async def card_payment(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=CARD_PAYMENT, parse_mode='MarkdownV2', reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Send receipt", url="https://t.me/askras88")],
        [InlineKeyboardButton("Back", callback_data='back_to_payment')]
    ]))

# "Connection Instructions" block
INSTRUCTIONS_TEXT = """🛠️ Connection Guide for Outline VPN:

1. Install the Outline app on your device.
2. Open the app and choose "Add server" or click "+". 
3. Paste the access key you received from Buddy.
4. Click "Connect".
5. Done! Now you're browsing the web securely and anonymously. 🌐"""

async def instructions(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=INSTRUCTIONS_TEXT, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data='back_to_start')]]))

# "Download App" block
async def download_app(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Select your device:", reply_markup=download_menu())

# Download app menu
def download_menu():
    keyboard = [
        [InlineKeyboardButton("iPhone", url="https://itunes.apple.com/app/outline-app/id1356177741")],
        [InlineKeyboardButton("Android", url="https://play.google.com/store/apps/details?id=org.outline.android.client")],
        [InlineKeyboardButton("Windows", url="https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe")],
        [InlineKeyboardButton("macOS", url="https://itunes.apple.com/app/outline-app/id1356178125")],
        [InlineKeyboardButton("Back", callback_data='back_to_start')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Button handler
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
        await query.edit_message_text(text="You chose 1 month subscription. Select a payment method:", reply_markup=payment_menu())
    elif data == 'sub_3m':
        await query.edit_message_text(text="You chose 3 months subscription. Select a payment method:", reply_markup=payment_menu())
    elif data == 'sub_1y':
        await query.edit_message_text(text="You chose 1 year subscription. Select a payment method:", reply_markup=payment_menu())
    elif data == 'instructions':
        await instructions(update, context)
    elif data == 'download_app':
        await download_app(update, context)
    elif data == 'back_to_start':
        await start(update, context)
    elif data == 'back_to_payment':
        await query.edit_message_text(text="Select a payment method:", reply_markup=payment_menu())
    elif data == 'crypto':
        await crypto_payment(update, context)
    elif data == 'card':
        await card_payment(update, context)

# Payment method menu
def payment_menu():
    keyboard = [
        [InlineKeyboardButton("Crypto", callback_data='crypto')],
        [InlineKeyboardButton("Bank Card", callback_data='card')],
        [InlineKeyboardButton("Back", callback_data='choose_subscription')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Main code
if __name__ == '__main__':
    application = ApplicationBuilder().token('7906261755:AAHniCWm-5ybmJvFReY7iO8OJi64LvosM_I').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    application.run_polling()
