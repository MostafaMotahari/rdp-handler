import requests
from pyrogram import Client
from datetime import datetime
from pyrogram.types import Message

def take_screenshot(client: Client, message: Message):
    server_ip = message.text.split(' ')[-1]

    with requests.get(f"http://{server_ip}:4323/take-screenshot", stream=True) as response:
        if response.status_code == 200:
            file_path = f"{datetime.now()}.png"
            with open(file_path, "wb") as image_file:
                for chunk in response.iter_content(chunk_size=8192):
                    image_file.write(chunk)

            client.send_photo(message.chat.id, file_path, caption=file_path)
