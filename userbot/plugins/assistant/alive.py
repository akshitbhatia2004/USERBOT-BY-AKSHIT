from telethon import events

from userbot import *

from . import *

PM_IMG = "https://telegra.ph/file/f6f6f8006a1861383c566.jpg"
pm_caption = f"⚜『彡aͥksͣhͫᎥτ彡』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{akshit_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『彡aͥksͣhͫᎥτ彡』~ `{AKSHITversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/OFFICIAL_USERBOTBYAKSHIT)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/akshitbhatia2004/USERBOTBYAKSHIT/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『彡aͥksͣhͫᎥτ彡』 ](https://t.me/AKSHIT_USERBOT)\n"
pm_caption += f"┣Assistant ~ By [『aͥksͣhͫᎥτẞøy』 ](https://t.me/Its_AkshitBoy)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『彡aͥksͣhͫᎥτ彡』](https://t.me/AKSHIT_USERBOT) «««"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
