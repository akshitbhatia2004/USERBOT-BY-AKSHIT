from faker import Faker
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from AKSHITBOT import CmdHelp
from AKSHITBOT import bot as AKSHITBOT
from AKSHITBOT.utils import admin_cmd, edit_or_reply, sudo_cmd


@AKSHITBOT.on(admin_cmd("gencc$"))
@AKSHITBOT.on(sudo_cmd("gencc$", allow_sudo=True))
async def _(AKSHITevent):
    if AKSHITevent.fwd_from:
        return
    AKSHITcc = Faker()
    AKSHITname = AKSHITcc.name()
    AKSHITadre = AKSHITcc.address()
    AKSHITcard = AKSHITcc.credit_card_full()

    await edit_or_reply(
        AKSHITevent,
        f"__**👤 NAME :- **__\n`{AKSHITname}`\n\n__**🏡 ADDRESS :- **__\n`{AKSHITadre}`\n\n__**💸 CARD :- **__\n`{AKSHITcard}`",
    )


@AKSHITBOT.on(admin_cmd(pattern="bin ?(.*)"))
@AKSHITBOT.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    AKSHIT_input = event.pattern_match.group(1)
    chat = "@szbinscheckerbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2143004427)
            )
            await event.client.send_message(chat, f"/bin {AKSHIT_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @szbinscheckerbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@AKSHITBOT.on(admin_cmd(pattern="register ?(.*)"))
@AKSHITBOT.on(sudo_cmd(pattern="register ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    AKSHIT_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/register {AKSHIT_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@AKSHITBOT.on(admin_cmd(pattern="password ?(.*)"))
@AKSHITBOT.on(sudo_cmd(pattern="password ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    AKSHIT_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/password {AKSHIT_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


CmdHelp("carder").add_command("gencc", None, "Generates fake cc...").add_command(
    "register", None, "Register Ur Account Here"
).add_command("password", "<enter>", "Set ur Account Password On CXM.CARDS").add()
