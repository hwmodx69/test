import requests
import os
import time
import asyncio
from pytgcalls import idle
from callsmusic import run
from handlers import __version__
from pyrogram import Client as Bot
from config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN

# --- Time sync attempt ---
print("[INFO]: Attempting to sync time...")
os.system("apk add --no-cache busybox-extras || true")
os.system("ntpd -q -p pool.ntp.org || true")
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

async def start_bot():
    try:
        print("[INFO]: Starting bot...")
        await bot.start()
    except Exception as e:
        print(f"[WARNING]: Bot start failed ({e}), retrying in 5s...")
        await asyncio.sleep(5)
        await bot.start()

async def main():
    await start_bot()
    run()
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    
