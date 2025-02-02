#Jmthon

import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import parse_pre, sanga_seperator


@bot.on(admin_cmd(pattern="(تاريخ|sgu)($| (.*))"))
@bot.on(sudo_cmd(pattern="(تاريخ|sgu)($| (.*))", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(
            event,
            "** قم بالـرد على الشخص للحصول على معلوماته ⌁**",
        )
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await event.client.get_entity(input_str)
            except ValueError:
                await edit_delete(
                    event, "**اعطي ايدي او معرف الشخص لايجاد معلوماته"
                )
            uid = u.id
    else:
        uid = reply_message.sender_id
    chat = "@SangMataInfo_bot"
    catevent = await edit_or_reply(event, "**⌁**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"/search_id {uid}")
        except YouBlockedUserError:
            await edit_delete(catevent, "`unblock @Sangmatainfo_bot and then try`")
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await event.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await edit_delete(catevent, "هنالك خطا غير معروف>")
    if "No records found" in responses:
        await edit_delete(catevent, "** هذا المستخدم ليس لديه اي تاريخ قديم**")
    names, usernames = await sanga_seperator(responses)
    cmd = event.pattern_match.group(1)
    if cmd == "تاريخ":
        sandy = None
        for i in names:
            if sandy:
                await event.reply(i, parse_mode=parse_pre)
            else:
                sandy = True
                await catevent.edit(i, parse_mode=parse_pre)
    elif cmd == "sgu":
        sandy = None
        for i in usernames:
            if sandy:
                await event.reply(i, parse_mode=parse_pre)
            else:
                sandy = True
                await catevent.edit(i, parse_mode=parse_pre)


CMD_HELP.update(
    {
        "sangmata": "**Plugin : **`sangmata`\
    \n\n**Syntax : **`.sg <username/userid/reply>`\
    \n**Function : **__Shows you the previous name history of user.__\
    \n\n**Syntax : **`.sgu <username/userid/reply>`\
    \n**Function : **__Shows you the previous username history of user.__\
    "
    }
)
