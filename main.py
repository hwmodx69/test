import requests
import os
import time
from pytgcalls import idle
from callsmusic import run
from handlers import __version__
from pyrogram import Client as Bot
from config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN

# --- Fix: Time sync before starting bot ---
try:
    os.system("ntpdate -u pool.ntp.org")
except:
    print("[WARNING]: Unable to sync time automatically")
time.sleep(2)

# --- Download foreground image ---
try:
    response = requests.get(BG_IMAGE)
    with open("./etc/foreground.png", "wb") as file:
        file.write(response.content)
except Exception as e:
    print(f"[WARNING]: Could not download BG image - {e}")

# --- Start Bot ---
bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers"),
)

print(f"[INFO]: VEEZ MUSIC v{__version__} STARTED !")
# Try syncing time inside Python (fallback)
os.system("ntpdate -u pool.ntp.org || true")
bot.start()
run()
idle()
