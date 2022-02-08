import os

os.system("pip install telethon")
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

okvai = input("Enter 69 to continue: ")
if okvai == "69":
    print("Please go to my.telegram.org and get your API Id and API Hash to proceed.")
    APP_ID = int(input("Enter APP ID here: "))
    API_HASH = input("Enter API HASH here: ")

    with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
        print(client.session.save())
        client.send_message("me", client.session.save())
        client.send_message(
            "me",
            "Above is your #AKSHITBOT STRING SESSION \nPaste this string in Heroku Var.\n\n[Team AkshitBot](t.me/OFFICIAL_USERBOTBYAKSHIT)",
        )

else:
    print("Bhag jaa bhosdike warna")
