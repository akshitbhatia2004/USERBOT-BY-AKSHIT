# AkshitBot Assistant
from telethon import Button, custom

from userbot import ALIVE_NAME, bot

from . import *

OWNER_NAME = ALIVE_NAME
OWNER_ID = bot.uid


AKSHIT_USER = bot.me.first_name
Its_AkshitBoy = bot.uid

akshit_mention = f"[{AKSHIT_USER}](tg://user?id={Its_AkshitBoy})"
gban_pic = "./userbot/resources/pics/gban.mp4"
main_pic = "./userbot/resources/pics/main.jpg"
core_pic = "./userbot/resources/pics/core.jpg"
chup_pic = "./userbot/resources/pics/chup.mp4"
bsdk_pic = "./userbot/resources/pics/bsdk.jpg"
bsdkwale_pic = "./userbot/resources/pics/bsdk_wale.jpg"
chutiya_pic = "./userbot/resources/pics/chutiya.jpg"
AKSHITversion = "3.0"

perf = "[ †hê 彡aͥksͣhͫᎥτ彡 ]"


DEVLIST = ["2082798662"]


async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
