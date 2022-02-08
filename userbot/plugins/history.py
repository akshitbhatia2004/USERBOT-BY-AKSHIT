from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from AKSHITBOT.utils import admin_cmd
from AKSHITBOT.utils import edit_or_reply as eor
from AKSHITBOT.utils import sudo_cmd
from userbot import CmdHelp, bot


@bot.on(admin_cmd(pattern="history ?(.*)"))
@bot.on(sudo_cmd(pattern="history ?(.*)", allow_sudo=True))
async def _(AKSHITevent):
    if AKSHITevent.fwd_from:
        return
    if not AKSHITevent.reply_to_msg_id:
        await eor(AKSHITevent, "`Please Reply To A User To Get This Module Work`")
        return
    reply_message = await AKSHITevent.get_reply_message()
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
        await eor(AKSHITevent, "Need actual users. Not Bots")
        return
    await eor(AKSHITevent, "Checking...")
    async with AKSHITevent.client.conversation(chat) as conv:
        try:
            response1 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            response2 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            response3 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            await conv.send_message("/search_id {}".format(victim))
            response1 = await response1
            response2 = await response2
            response3 = await response3
        except YouBlockedUserError:
            await AKSHITevent.reply("Please unblock ( @Sangmatainfo_bot ) ")
            return
        if response1.text.startswith("No records found"):
            await eor(AKSHITevent, "User never changed his Username...")
        else:
            await AKSHITevent.delete()
            await AKSHITevent.client.send_message(
                AKSHITevent.chat_id, response2.message
            )


@bot.on(admin_cmd(pattern="unh ?(.*)"))
@bot.on(sudo_cmd(pattern="unh ?(.*)", allow_sudo=True))
async def _(AKSHITevent):
    if AKSHITevent.fwd_from:
        return
    if not AKSHITevent.reply_to_msg_id:
        await eor(AKSHITevent, "`Please Reply To A User To Get This Module Work`")
        return
    reply_message = await AKSHITevent.get_reply_message()
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
        await eor(AKSHITevent, "Need actual users. Not Bots")
        return
    await eor(AKSHITevent, "Checking...")
    async with AKSHITevent.client.conversation(chat) as conv:
        try:
            response1 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            response2 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            response3 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            await conv.send_message("/search_id {}".format(victim))
            response1 = await response1
            response2 = await response2
            response3 = await response3
        except YouBlockedUserError:
            await AKSHITevent.reply("Please unblock ( @Sangmatainfo_bot ) ")
            return
        if response1.text.startswith("No records found"):
            await eor(AKSHITevent, "User never changed his Username...")
        else:
            await AKSHITevent.delete()
            await AKSHITevent.client.send_message(
                AKSHITevent.chat_id, response3.message
            )


CmdHelp("history").add_command(
    "history", "<reply to a user>", "Fetches the name history of replied user."
).add_command(
    "unh", "<reply to user>", "Fetches the Username History of replied users."
).add()
