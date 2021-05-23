import time

from . import StartTime, get_readable_time, reply_id

DEFAULTUSER = "JMTHON"
CAT_IMG1 = "https://telegra.ph/file/7c01aac20ed94df6255e9.mp4"
CAT_IMG2 = "https://telegra.ph/file/651a70a0e4c10b1bf1cad.mp4"
CAT_IMG3 = "https://telegra.ph/file/6aea95f46e60944c81ab5.mp4"
CAT_IMG4 = "https://telegra.ph/file/76826f289ca69ee1d669f.mp4"
CAT_IMG5 = "https://telegra.ph/file/4c6acf2596684b9415da2.mp4"
CAT_IMG6 = "https://telegra.ph/file/58933ca52708d95ed1bd4.mp4"
CAT_IMG7 = "https://telegra.ph/file/8c3b557f1dd8ae3bce60c.mp4"
CAT_IMG8 = "https://telegra.ph/file/2f68313af8a8962dc2c70.mp4"
CAT_IMG9 = "https://telegra.ph/file/f184e9a5d07a2fa673b11.mp4"
CAT_IMG10 = "https://telegra.ph/file/46f271081734b24ca7313.mp4"
CUSTOM_JM_TEXT = ""
EMOJI = " ⌁ "


@bot.on(admin_cmd(outgoing=True, pattern="متحركه 1$"))
@bot.on(sudo_cmd(pattern="متحركه 1$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG1:
        cat_caption = f"**المتـحࢪڪه الأولـى**\n\n"
        cat_caption += f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG1, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**المتـحࢪڪه الأولـى**\n\n"
            f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**",
        )

@bot.on(admin_cmd(outgoing=True, pattern="متحركه 2$"))
@bot.on(sudo_cmd(pattern="متحركه 2$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG2:
        cat_caption = f"**المتـحࢪڪه الـثانيه**\n\n"
        cat_caption += f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG2, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**المتـحࢪڪه الـثانيه**\n\n"
            f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**",
        )
        
@bot.on(admin_cmd(outgoing=True, pattern="متحركه 3$"))
@bot.on(sudo_cmd(pattern="متحركه 3$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG3:
        cat_caption = f"**المتـحࢪڪه الـثالـثة**\n\n"
        cat_caption += f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG3, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**المتـحࢪڪه الـثالـثة**\n\n"
            f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**",
        )
        
@bot.on(admin_cmd(outgoing=True, pattern="متحركه 4$"))
@bot.on(sudo_cmd(pattern="متحركه 3$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG4:
        cat_caption = f"**المتـحࢪڪه الـࢪابعـة**\n\n"
        cat_caption += f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**"
        await alive.client.send_file(
            alive.chat_id, CAT4_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**المتـحࢪڪه الـࢪابعـة**\n\n"
            f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**",
        )
        
@bot.on(admin_cmd(outgoing=True, pattern="متحركه 5$"))
@bot.on(sudo_cmd(pattern="متحركه 5$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG5:
        cat_caption = f"**المتـحࢪڪه الـخامسه**\n\n"
        cat_caption += f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG5, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**المتـحࢪڪه الـخامسه**\n\n"
            f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**",
        )
        
@bot.on(admin_cmd(outgoing=True, pattern="متحركه 6$"))
@bot.on(sudo_cmd(pattern="متحركه 6$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG6:
        cat_caption = f"**المتـحࢪڪه السـادسه**\n\n"
        cat_caption += f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG6, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**المتـحࢪڪه السـادسه**\n\n"
            f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**",
        )

@bot.on(admin_cmd(outgoing=True, pattern="متحركه 7$"))
@bot.on(sudo_cmd(pattern="متحركه 7$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG7:
        cat_caption = f"**المتـحࢪڪه الـسابعـة**\n\n"
        cat_caption += f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG7, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**المتـحࢪڪه الـسابعـة**\n\n"
            f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**",
        )
        
@bot.on(admin_cmd(outgoing=True, pattern="متحركه 8$"))
@bot.on(sudo_cmd(pattern="متحركه 8$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG8:
        cat_caption = f"**المتـحࢪڪه الـثامـنة**\n\n"
        cat_caption += f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG8, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**المتـحࢪڪه الـثامـنة**\n\n"
            f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**",
        )

@bot.on(admin_cmd(outgoing=True, pattern="متحركه 9$"))
@bot.on(sudo_cmd(pattern="متحركه 9$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG9:
        cat_caption = f"**المتـحࢪڪه الـتاسـعة**\n\n"
        cat_caption += f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG9, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**المتـحࢪڪه الـتاسـعة**\n\n"
            f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**",
       )
       
@bot.on(admin_cmd(outgoing=True, pattern="متحركه 2$"))
@bot.on(sudo_cmd(pattern="متحركه 2$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG10:
        cat_caption = f"**المتـحࢪڪه الـعاشرة**\n\n"
        cat_caption += f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG10, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**المتـحࢪڪه الـعاشرة**\n\n"
            f"**  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon**",
        )
   

def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "✾"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "↫ "
        is_database_working = True
    return is_database_working, output