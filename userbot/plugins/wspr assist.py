from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("الهمسه"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اذا تريد ترسل همسه يجب كتابه اولا .همسه ثم الرساله ثم تكتب معرف الي تريد تهمسله وترسل الرساله وبس 🖤✨.\n  .همسه  +  الرسالة  + معرف الشخص")
