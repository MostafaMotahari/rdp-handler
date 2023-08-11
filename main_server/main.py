import os
from pyrogram import Client
from pyrogram.handlers import MessageHandler
import handlers

app = Client(
    "RDP_Handler",
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ.get('API_HASH'),
    bot_token=os.environ.get('BOT_TOKEN')
)

app.add_handler(MessageHandler(handlers.take_screenshot))
app.run()
