import colorama
from colorama import Fore, Style
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

colorama.init(autoreset=True)
AKSHITBOT_PIC = "https://telegra.ph/file/8488fc6758ff283061324.jpg"


okbro = input("Enter y or yes continue: ")

if okbro == "y" or "yes":
    print(
        Fore.GREEN
        + Style.BRIGHT
        + """\t\t

╭━━━┳╮╱╱╱╱╭╮╱╱╭╮╭╮╱╱╱╱╭╮
┃╭━╮┃┃╱╱╱╱┃┃╱╭╯╰┫┃╱╱╱╭╯╰╮
┃┃╱┃┃┃╭┳━━┫╰━╋╮╭┫╰━┳━┻╮╭╯
┃╰━╯┃╰╯┫━━┫╭╮┣┫┃┃╭╮┃╭╮┃┃
┃╭━╮┃╭╮╋━━┃┃┃┃┃╰┫╰╯┃╰╯┃╰╮
╰╯╱╰┻╯╰┻━━┻╯╰┻┻━┻━━┻━━┻━╯
       """
    )
    print("\nChoose String Type \n1.Telethon\n2.Pyrogram")
    library = input("\nYour Choice:")
    if library == "1":
        print("Welcome To Telethon String Generator")
        APP_ID = int(input("Enter APP ID - "))
        API_HASH = input("Enter API HASH - ")
        try:
            with TelegramClient(StringSession(), APP_ID, API_HASH) as bot:
                string_session = bot.session.save()
                print(
                    "You can Get Your String Session In Saved Message of Your Telegram Account. Remember To Make New String Session Whenever You Terminate Sessions."
                )
                bot.send_file(
                    "me",
                    AKSHITBOT_PIC,
                    caption=f"`{string_session}`\n\n• __Dont Share String Session With Anyone__\n• __Dont Invite Anyone To Heroku__",
                )
        except Exception as e:
            print(f"{e}")
    elif library == "2":
        print("Welcome To Pyrogram String Session")
        APP_ID = int(input("\nEnter Ur APP ID ~: "))
        API_HASH = input("\nEnter Ur API_HASH ~: ")
        try:
            with Client(":memory:", api_id=APP_ID, api_hash=API_HASH) as boy:
                sweetie = boy.export_session_string()
                print(
                    "Successfully Pyrogram String Session Has Been Generated \nCheck Ur Saved Message \nIf U Terminate Sessions Then U Have To Generate Gain\nDont Try To Share STRING SESSION with Anyone"
                )
                boy.send_message("me", f"Pyrogram String Session\n\n`{sweetie}`")
        except Exception as e:
            print(f"{e}")
    else:
        print(
            "\nohh sorry Ab Fir Se Start karo & \nChoose 1 For Userbot \nChoose 2 For Pyrogram \n Pahle Run karo fir se Tab 1 ya 2 Koi Ek Select Karna"
        )
