import asyncio
import random

from telethon import events

from . import *


@borg.on(events.NewMessage(pattern=r"\.belo", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Typing...")
    await asyncio.sleep(1)
    x = random.randrange(1, 96)
    if x == 1:
        await event.edit(
            '`"Underwater bubbles and raindrops are total opposites of each other."`'
        )
    if x == 2:
        await event.edit(
            '`"If you buy an eraser you are literally paying for your mistakes."`'
        )
    if x == 3:
        await event.edit(
            '`"The Person you care for most has the potential to destroy you the most."`'
        )
    if x == 4:
        await event.edit(
            '`"If humans colonize the moon, it will probably attract retirement homes as the weaker gravity will allow the elderly to feel stronger."`'
        )

    if x == 5:

        await event.edit(
            '`"Any video with “wait for it” in the title is simply too long."`'
        )

    if x == 6:

        await event.edit(
            '`"Your age in years is how many times you’ve circled the Sun, but your age in months is how many times the Moon has circled you."`'
        )

    if x == 7:

        await event.edit(
            '`"Biting your tongue while eating is a perfect example of how you can still screw up, even with decades of experience."`'
        )

    if x == 8:

        await event.edit(
            '`"Saying that your home is powered by a wireless Nuclear fusion reactor that is 93 Million miles away sounds way cooler than just saying you have solar panels on your roof."`'
        )

    if x == 9:

        await event.edit(
            '`"The most crushing feeling is when someone smiles at you on the street and you don’t react fast enough to smile back."`'
        )

    if x == 10:

        await event.edit(
            '`"Teeth constantly require maintenance to prevent their decay when alive, and yet they manage to survive for thousands of years buried as fossils."`'
        )

    if x == 11:

        await event.edit('`"A folder is for things that you don\'t want to fold."`')

    if x == 12:

        await event.edit(
            '`"Waking up in the morning sometimes feels like resuming a shitty movie you decided to quit watching."`'
        )

    if x == 13:

        await event.edit(
            '`"If everything goes smoothly, you probably won\'t remember today."`'
        )

    if x == 14:

        await event.edit(
            '`"When you meet new people in real life, you unlock more characters for your dream world."`'
        )

    if x == 15:

        await event.edit(
            '`"Maybe if they renamed sunscreen to “anti-cancer cream” more people would wear it."`'
        )

    if x == 16:

        await event.edit(
            '`"200 years ago, people would never have guessed that humans in the future would communicate by silently tapping on glass."`'
        )

    if x == 17:

        await event.edit(
            '`"Parents worry about what their sons download and worry about what their daughters upload."`'
        )

    if x == 18:

        await event.edit(
            '`"It\'s crazy how you can be the same age as someone, but at a completely different stage in your life."`'
        )

    if x == 19:

        await event.edit(
            "`\"When you think you wanna die, you really don't wanna die, you just don't wanna live like this.\"`"
        )

    if x == 20:

        await event.edit('`"Technically, no one has ever been in an empty room."`')

    if x == 21:

        await event.edit(
            '`"An onion is the bass player of food. You would probably not enjoy it solo, but you’d miss it if it wasn’t there."`'
        )

    if x == 22:

        await event.edit(
            "`\"We run everywhere in videogames because we're too lazy to walk, but In real life we walk everywhere because we're too lazy to run.\"`"
        )

    if x == 23:

        await event.edit(
            '`"Every single decision you ever made has brought you to read this sentence."`'
        )

    if x == 24:

        await event.edit("`\"The word 'quiet' is often said very loud.\"`")

    if x == 25:

        await event.edit(
            '`"Everybody wants you to work hard, but nobody wants to hear about how hard you work."`'
        )

    if x == 26:

        await event.edit(
            '`"We brush our teeth with hair on a stick and brush our hair with teeth on a stick."`'
        )

    if x == 27:

        await event.edit(
            '`"No one remembers your awkward moments but they’re too busy remembering their own."`'
        )

    if x == 28:

        await event.edit(
            '`"Dumb people try to say simple ideas as complex as possible while smart people try to say complex ideas as simple as possible."`'
        )

    if x == 29:

        await event.edit(
            "`\"Some people think they're better than you because they grew up richer. Some people think they're better than you because they grew up poorer.\"`"
        )

    if x == 30:

        await event.edit(
            '`"The biggest irony is that computers & mobiles were invented to save out time!"`'
        )

    if x == 31:

        await event.edit(
            '`"After honey was first discovered, there was likely a period where people were taste testing any available slime from insects."`'
        )

    if x == 32:

        await event.edit(
            '`"You know you’re getting old when your parents start disappointing you, instead of you disappointing them."`'
        )

    if x == 33:

        await event.edit(
            '`"Humans are designed to learn through experience yet the education system has made it so we get no experience."`'
        )

    if x == 34:

        await event.edit(
            '`"By focusing on blinking, you blink slower... Same for breathing."`'
        )

    if x == 35:

        await event.edit(
            '`"Drivers in a hurry to beat traffic usually cause the accidents which create the traffic they were trying to avoid."`'
        )

    if x == 36:

        await event.edit(
            '`"Characters that get married in fiction were literally made for each other."`'
        )

    if x == 37:

        await event.edit(
            '`"Babies are a clean hard drive that can be programmed with any language."`'
        )

    if x == 38:

        await event.edit(
            "`\"There could be a miracle drug that cures every disease to man, that we'll never know about because it doesn't work on rats.\"`"
        )

    if x == 39:

        await event.edit(
            "`\"Rhinos evolved to grow a horn for protection, but it's what's making them go extinct.\"`"
        )

    if x == 40:

        await event.edit(
            '`"Maybe we don\'t find time travelers because we all die in 25-50 years."`'
        )

    if x == 41:

        await event.edit(
            '`"Sleep is the trial version of death, It even comes with ads based on your activity."`'
        )

    if x == 42:

        await event.edit(
            '`"The most unrealistic thing about Spy movies is how clean the air ventilation system is!"`'
        )

    if x == 43:

        await event.edit(
            '`"In games we play through easy modes to unlock hard modes. In life we play through hard modes to unlock easy modes."`'
        )

    if x == 44:

        await event.edit(
            '`"Silent people seem smarter than loud people, because they keep their stupid thoughts to themselves."`'
        )

    if x == 45:

        await event.edit('`"If Greenland actually turns green, we\'re all screwed."`')

    if x == 46:

        await event.edit(
            '`"If someone says clever things in your dream, it actually shows your own cleverness."`'
        )

    if x == 47:

        await event.edit(
            '`"Famous movie quotes are credited to the actor and not the actual writer who wrote them."`'
        )

    if x == 48:

        await event.edit(
            '`"No one actually teaches you how to ride a bicycle. They just hype you up until you work it out."`'
        )

    if x == 49:

        await event.edit('`"Ask yourself why the the brain ignores the second the."`')

    if x == 50:

        await event.edit(
            '`"You’ve probably forgot about 80% of your entire life and most of the memories you do remember are not very accurate to what actually happened."`'
        )

    if x == 51:

        await event.edit(
            '`"It will be a lot harder for kids to win against their parents in video games in the future."`'
        )

    if x == 52:

        await event.edit(
            '`"Everyone has flaws, if you don\'t recognize yours, you have a new one."`'
        )

    if x == 53:

        await event.edit('`"Raising a child is training your replacement."`')

    if x == 54:

        await event.edit(
            "`\"'O'pen starts with a Closed circle, and 'C'lose starts with an open circle.\"`"
        )

    if x == 55:

        await event.edit(
            '`"There\'s always someone who hated you for no reason, and still does."`'
        )

    if x == 56:

        await event.edit(
            '`"After popcorn was discovered, there must have been a lot of random seeds that were roasted to see if it would have the same effect."`'
        )

    if x == 57:

        await event.edit(
            '`"The more important a good night\'s sleep is, the harder it is to fall asleep."`'
        )

    if x == 58:

        await event.edit(
            '`"Blessed are those that can properly describe the type of haircut they want to a new stylist."`'
        )

    if x == 59:

        await event.edit(
            "`\"Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like!\"`"
        )

    if x == 60:

        await event.edit(
            '`"Theme park employees must be good at telling the difference between screams of horror and excitement."`'
        )

    if x == 61:

        await event.edit('`"6 to 6:30 feels more half-an-hour than 5:50 to 6:20"`')

    if x == 62:

        await event.edit(
            '`"Getting your password right on the last login attempt before lockout is the closest thing to disarming a bomb at the last minute that most of us will experience."`'
        )

    if x == 63:

        await event.edit(
            '`"Listening to podcasts before bed is the adult version of story-time."`'
        )

    if x == 64:

        await event.edit(
            '`"If all criminals stopped robbing then the security industry would fall in which they could then easily go back to robbing."`'
        )

    if x == 65:

        await event.edit('`"A ton of whales is really only like half a whale."`')

    if x == 66:

        await event.edit(
            '`"When you get old, the old you is technically the new you, and your young self is the old you."`'
        )

    if x == 67:

        await event.edit(
            '`"You probably won\'t find many negative reviews of parachutes on the Internet."`'
        )

    if x == 68:

        await event.edit(
            '`"We show the most love and admiration for people when they\'re no longer around to appreciate it."`'
        )

    if x == 69:

        await event.edit(
            "`\"We've practiced sleeping thousands of times, yet can't do it very well or be consistent.\"`"
        )

    if x == 70:

        await event.edit(
            '`"Humans are more enthusiastic about moving to another planet with hostile environment than preserving earth - the planet they are perfectly shaped for."`'
        )

    if x == 71:

        await event.edit(
            "`\"The happiest stage of most people's lives is when their brains aren't fully developed yet.\"`"
        )

    if x == 72:

        await event.edit('`"The most effective alarm clock is a full bladder."`')

    if x == 73:

        await event.edit(
            '`"You probably just synchronized blinks with millions of people."`'
        )

    if x == 74:

        await event.edit(
            '`"Since we test drugs on animals first, rat medicine must be years ahead of human medicine."`'
        )

    if x == 75:

        await event.edit(
            '`"Night before a day off is more satisfying than the actual day off."`'
        )

    if x == 76:

        await event.edit('`"We put paper in a folder to keep it from folding."`')

    if x == 77:

        await event.edit(
            '`"Somewhere, two best friends are meeting for the first time."`'
        )

    if x == 78:

        await event.edit(
            '`"Our brain simultaneously hates us, loves us, doesn\'t care about us, and micromanages our every move."`'
        )

    if x == 79:

        await event.edit(
            '`"Being a male is a matter of birth. Being a man is a matter of age. But being a gentleman is a matter of choice."`'
        )

    if x == 80:

        await event.edit(
            '`"Soon the parents will be hiding their social account from their kids rather than kids hiding their accounts from the parents."`'
        )

    if x == 81:

        await event.edit('`"Wikipedia is what the internet was meant to be."`')

    if x == 82:

        await event.edit(
            '`"A theme park is the only place that you can hear screams in the distance and not be concerned."`'
        )

    if x == 83:

        await event.edit(
            '`"A wireless phone charger offers less freedom of movement than a wired one."`'
        )

    if x == 84:

        await event.edit(
            "`\"If you repeatedly criticize someone for liking something you don't, they won't stop liking it. They'll stop liking you.\"`"
        )

    if x == 85:

        await event.edit(
            '`"Somewhere there is a grandmother, whose grandson really is the most handsome boy in the world."`'
        )

    if x == 86:

        await event.edit(
            '`"If someday human teleportation becomes real, people will still be late for work."`'
        )

    if x == 87:

        await event.edit(
            '`"The first humans who ate crabs must have been really hungry to try and eat an armored sea spider"`'
        )

    if x == 88:

        await event.edit(
            '`"Doing something alone is kind of sad, but doing it solo is cool af."`'
        )

    if x == 89:

        await event.edit(
            '`"Your brain suddenly becomes perfect at proofreading after you post something."`'
        )

    if x == 90:

        await event.edit(
            '`"There\'s always that one song in your playlist that you always skip but never remove."`'
        )

    if x == 91:

        await event.edit(
            '`"Kids next century will probably hate us for taking all the good usernames."`'
        )

    if x == 92:

        await event.edit('`"Bubbles are to fish what rain is to humans."`')

    if x == 93:

        await event.edit(
            '`"The more people you meet, the more you realise and appreciate how well your parents raised you."`'
        )

    if x == 94:

        await event.edit('`"A comma is a short pause, a coma is a long pause."`')

    if x == 95:

        await event.edit('`"Someday you will either not wake up or not go to sleep."`')

    if x == 96:

        await event.edit(
            '`"Bermuda Triangle might be the exit portal of this simulation."`'
        )


img1 = "https://t.me/AKSHIT_Mr_Xmas/2"
img2 = "https://t.me/AKSHIT_Mr_Xmas/3"
img3 = "https://t.me/AKSHIT_Mr_Xmas/4"
img4 = "https://t.me/AKSHIT_Mr_Xmas/5"
img5 = "https://t.me/AKSHIT_Mr_Xmas/6"
img6 = "https://t.me/AKSHIT_Mr_Xmas/7"
img7 = "https://t.me/AKSHIT_Mr_Xmas/8"
img8 = "https://t.me/AKSHIT_Mr_Xmas/9"
img9 = "https://t.me/AKSHIT_Mr_Xmas/10"
img10 = "https://t.me/AKSHIT_Mr_Xmas/11"
img11 = "https://t.me/AKSHIT_Mr_Xmas/12"
img12 = "https://t.me/AKSHIT_Mr_Xmas/13"
img13 = "https://t.me/AKSHIT_Mr_Xmas/14"
img14 = "https://t.me/AKSHIT_Mr_Xmas/15"
img15 = "https://t.me/AKSHIT_Mr_Xmas/16"
img16 = "https://t.me/AKSHIT_Mr_Xmas/17"
img17 = "https://t.me/AKSHIT_Mr_Xmas/18"
img18 = "https://t.me/AKSHIT_Mr_Xmas/19"
img19 = "https://t.me/AKSHIT_Mr_Xmas/20"
img20 = "https://t.me/AKSHIT_Mr_Xmas/21"
img21 = "https://t.me/AKSHIT_Mr_Xmas/22"
img22 = "https://t.me/AKSHIT_Mr_Xmas/23"
img23 = "https://t.me/AKSHIT_Mr_Xmas/24"
img24 = "https://t.me/AKSHIT_Mr_Xmas/25"
img25 = "https://t.me/AKSHIT_Mr_Xmas/26"
img26 = "https://t.me/AKSHIT_Mr_Xmas/27"
img27 = "https://t.me/AKSHIT_Mr_Xmas/28"
img28 = "https://t.me/AKSHIT_Mr_Xmas/29"
img29 = "https://t.me/AKSHIT_Mr_Xmas/30"
img30 = "https://t.me/AKSHIT_Mr_Xmas/31"


@bot.on(admin_cmd(outgoing=True, pattern="xmas"))
async def _(event):

    if event.fwd_from:
        await event.edit(
            '`"If we put solar panels above parking lots, then our cars wouldn\'t get hot and we would have a lot of clean energy."`'
        )
        return
    await event.edit("**.\n\n😊 ℍ𝕠 ℍ𝕠 ℍ𝕠... 🎅🏻\n\n.**")
    await sleep(1.6)
    await event.edit("🎉")
    await sleep(3)
    await event.edit("🎊")
    await sleep(3)
    await event.edit("💔")
    await sleep(1.5)
    await event.edit("❤")
    await sleep(3)
    await event.edit(".\n\n\n😊𝓜𝓔𝓡𝓡𝓨 𝓒𝓗𝓡𝓘𝓢𝓣𝓜𝓐𝓢😁\n\n\n.")
    await sleep(3)
    await event.edit("🥳")
    await sleep(3.3)
    await event.edit("⛄")
    await sleep(3.4)
    await event.edit("🌨🌨🌨🌨🌨\n\n❄❄❄❄❄\n❄️❄️❄️❄️❄️")
    await sleep(2.8)
    await event.edit("☃️")
    await sleep(3.7)
    await event.edit("🥶")
    await sleep(3.7)
    await event.edit("🎄")
    await sleep(3.2)
    await event.edit(".\n\n\n**𝐌𝒆𝒓𝒓𝒚 𝑪𝒉𝒊𝒔𝒕𝒎𝒂𝒔😊😊**\n\n\n.")
    await sleep(2.9)
    danish = await bot.send_file(event.chat_id, "https://t.me/mcmc2021/36")
    await sleep(4)
    x = random.randrange(0, 30)
    if x == 1:
        await bot.send_file(event.chat_id, img1)

    if x == 2:
        await bot.send_file(event.chat_id, img2)

    if x == 3:
        await bot.send_file(event.chat_id, img3)

    if x == 4:
        await bot.send_file(event.chat_id, img4)

    if x == 5:
        await bot.send_file(event.chat_id, img5)

    if x == 6:
        await bot.send_file(event.chat_id, img6)

    if x == 7:
        await bot.send_file(event.chat_id, img7)

    if x == 8:
        await bot.send_file(event.chat_id, img8)

    if x == 9:
        await bot.send_file(event.chat_id, img9)

    if x == 10:
        await bot.send_file(event.chat_id, img10)

    if x == 11:
        await bot.send_file(event.chat_id, img11)

    if x == 12:
        await bot.send_file(event.chat_id, img12)

    if x == 13:
        await bot.send_file(event.chat_id, img13)

    if x == 14:
        await bot.send_file(event.chat_id, img14)

    if x == 15:
        await bot.send_file(event.chat_id, img15)

    if x == 16.0:
        await bot.send_file(event.chat_id, img16)

    if x == 17:
        await bot.send_file(event.chat_id, img17)

    if x == 18:
        await bot.send_file(event.chat_id, img18)

    if x == 19:
        await bot.send_file(event.chat_id, img19)

    if x == 20:
        await bot.send_file(event.chat_id, img20)

    if x == 21:
        await bot.send_file(event.chat_id, img21)

    if x == 22:
        await bot.send_file(event.chat_id, img22)

    if x == 23:
        await bot.send_file(event.chat_id, img23)

    if x == 24:
        await bot.send_file(event.chat_id, img24)

    if x == 25:
        await bot.send_file(event.chat_id, img25)

    if x == 26:
        await bot.send_file(event.chat_id, img26)

    if x == 27:
        await bot.send_file(event.chat_id, img27)

    if x == 28:
        await bot.send_file(event.chat_id, img28)

    if x == 29:
        await bot.send_file(event.chat_id, img29)

    if x == 30:
        await bot.send_file(event.chat_id, img30)


CmdHelp("randomly").add_command("xmas", None, "Use and see").add_command(
    "belo", None, "Use and See"
).add_warning("Harmless Module").add_info("Its Random String Plugin").add_type(
    "Addons"
).add()
