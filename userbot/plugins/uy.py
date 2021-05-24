from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("م25"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("لـعࢪض اۅٛمـر المـتحركات  :\n\n `.متحركه 1`\n `.متحركه 2`\n `.متحركه 3`\n `.متحركه 4`\n `.متحركه 5`\n `.متحركه 6`\n `.متحركه 7`\n `.متحركه 8`\n `.متحركه 9`\n `.متحركه 10`\n\n  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon") 