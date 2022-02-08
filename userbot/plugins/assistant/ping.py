import os

from telethon import Button, events

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

AKSHIT_IMG = os.environ.get(
    "BOT_PING_PIC", "https://telegra.ph/file/f6f6f8006a1861383c566.jpg"
)
ms = 4
ALIVE = Config.ALIVE_NAME

AkshitBoy = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("⚜ 彡aͥksͣhͫᎥτ彡 ⚜", "https://t.me/AKSHIT_USERBOT")]]
    await tgbot.send_file(event.chat_id, AKSHIT_IMG, caption=AkshitBoy, buttons=GOOD)
