
# @Jmthon


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "الاوامر":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "⌔︙ قائمه الاوامر\n\n⌔︙ م1 -› لعرض اوامر الادمن\n⌔︙ م2 -› لعرض اوامر التسليه\n⌔︙ م3 -› لعرض اوامر الترحيب\n⌔︙ م4 -› لعرض اوامر الردود\n⌔︙ م5 -› لعرض اوامر الرفع\n⌔︙ م6 -› لعرض اوامر الحمايه\n⌔︙ م7 -› لعرض اوامر التليـكراف\n⌔︙ م8 -› لعرض اوامر حمايه المجموعه\n⌔︙ م9 -› لعرض اوامر التاك\n⌔︙ م10 -› لعرض اوامر الكشف\n⌔︙ م11 -› لعرض اوامر المجموعه\n⌔︙ م12 -› لعرض اوامر الترجمه\n⌔︙ م13 -› لعرض اوامر البحث\n⌔︙ م14 -› لعرض اوامر الانتحال\n⌔︙ م15 -› لعرض اوامر النت\n⌔︙ م16 -› لعرض اوامر البوت\n⌔︙ م17 -› لعرض اوامر الحساب\n⌔︙ م18 -› لعرض اوامر التقليد\n⌔︙ م19 -› لعرض اوامر الحساب الوقتي\n⌔︙ م20 -› لعرض اوامر القائمه السوداء\n⌔︙ م21 -› لعرض الاوامر الجانبية \n⌔︙ م22 -› لعرض اوامر الملصقات \n⌔︙ م23 -› لعرض اوامر التمبلر\n⌔︙ م24 -› لعرض اوامر هيروكو\n  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "⌔︙ قائمه الاوامر\n\n⌔︙ م1 -› لعرض اوامر الادمن\n⌔︙ م2 -› لعرض اوامر التسليه\n⌔︙ م3 -› لعرض اوامر الترحيب\n⌔︙ م4 -› لعرض اوامر الردود\n⌔︙ م5 -› لعرض اوامر الرفع\n⌔︙ م6 -› لعرض اوامر الحمايه\n⌔︙ م7 -› لعرض اوامر التليـكراف\n⌔︙ م8 -› لعرض اوامر حمايه المجموعه\n⌔︙ م9 -› لعرض اوامر التاك\n⌔︙ م10 -› لعرض اوامر الكشف\n⌔︙ م11 -› لعرض اوامر المجموعه\n⌔︙ م12 -› لعرض اوامر الترجمه\n⌔︙ م13 -› لعرض اوامر البحث\n⌔︙ م14 -› لعرض اوامر الانتحال\n⌔︙ م15 -› لعرض اوامر النت\n⌔︙ م16 -› لعرض اوامر البوت\n⌔︙ م17 -› لعرض اوامر الحساب\n⌔︙ م18 -› لعرض اوامر التقليد\n⌔︙ م19 -› لعرض اوامر الحساب الوقتي\n⌔︙ م20 -› لعرض اوامر القائمه السوداء\n⌔︙ م21 -› لعرض الاوامر الجانبية \n⌔︙ م22 -› لعرض اوامر الملصقات \n⌔︙ م23 -› لعرض اوامر التمبلر\n⌔︙ م24 -› لعرض اوامر هيروكو\n  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


# @Jmthon


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م1":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "قائمه اوامر الادمن :\n⌁ `.حظر`\n⌁ `.تقيد`\n⌁  `.الغاء تقيد`\n⌁  `.رفع القيود`\n⌁  `.كتم`\n⌁  `.الغاء كتم`\n ⌁  `.تثبيت`  \n⌁  `.الغاء التثبيت` \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "قائمه اوامر الادمن :\n⌁ `.حظر`\n⌁ `.تقيد`\n⌁  `.الغاء تقيد`\n⌁  `.رفع القيود`\n⌁  `.كتم`\n⌁  `.الغاء كتم`\n ⌁  `.تثبيت`  \n⌁  `.الغاء التثبيت` \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م2":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "** قائـمه اوامر التسليه :**\n⌁ `.قمر`\n⌁ `.اقمار`\n⌁ `.قمور`\n⌁ `.قلوب`\n⌁ `.قلب `\n⌁ `.جيم`\n⌁ `.افكر`\n⌁ `.افكرر`\n⌁ `.شنوو `\n⌁ `.مح `\n⌁ `.متت `\n⌁ `.النضام الشمسي `\n⌁ `.موسيقى `\n⌁ `.قنبله `\n⌁ `.مكبعات `\n⌁ `.افعى `\n⌁ `.طائره `\n⌁ `.نجمه `\n⌁ `.دائره `\n⌁ `.شرطه `\n⌁ `.فايروس `\n⌁ `.غبي `\n⌁ `.العد التنازلي`\n - `.يد`\n - `.تهكير`\n - `.قرد `\n - `.بشره `\n - `.انيم `\n - `.نيكول `\n - `.مربع`\n - `.قاتل `\n - `.تحميل`\n - `.رجل `\n - `.شنوو `\n - `.ريبي `\n - `.تفريغ `\n - `.حلويات `\n - `.فليم`\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر التسليه :**\n⌁ `.قمر`\n⌁ `.اقمار`\n⌁ `.قمور`\n⌁ `.قلوب`\n⌁ `.قلب `\n⌁ `.جيم`\n⌁ `.افكر`\n⌁ `.افكرر`\n⌁ `.شنوو `\n⌁ `.مح `\n⌁ `.متت `\n⌁ `.النضام الشمسي `\n⌁ `.موسيقى `\n⌁ `.قنبله `\n⌁ `.مكبعات `\n⌁ `.افعى `\n⌁ `.طائره `\n⌁ `.نجمه `\n⌁ `.دائره `\n⌁ `.شرطه `\n⌁ `.فايروس `\n⌁ `.غبي `\n⌁ `.العد التنازلي`\n - `.يد`\n - `.تهكير`\n - `.قرد `\n - `.بشره `\n - `.انيم `\n - `.نيكول `\n - `.مربع`\n - `.قاتل `\n - `.تحميل`\n - `.رجل `\n - `.شنوو `\n - `.ريبي `\n - `.تفريغ `\n - `.حلويات `\n - `.فليم`\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م3":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "* قائـمه اوامر الترحيب :**\n⌁ `.ترحيب `\n⌁ `.مسح ترحيب `\n⌁ `.الترحيب `\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر الترحيب :**\n⌁ `.ترحيب `\n⌁ `.مسح ترحيب `\n⌁ `.الترحيب `\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م4":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "* قائـمه اوامر الردود :**\n⌁ `.اضف رد `\n⌁ `.حذف رد `\n⌁ `.حذف الردود `\n - `.الردود `\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر الردود :**\n⌁ `.اضف رد `\n⌁ `.حذف رد `\n⌁ `.حذف الردود `\n - `.الردود `\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م5":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "* قائـمه اوامر الرفع :**\n⌁ `.رفع مطي `\n⌁ `.رفع جلب `\n⌁ `.رفع بكلبي `\n - `.رفع مرتي `\n⌁ `.رفع تاج `\n⌁ `.رفع جريذي `\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر الرفع :**\n⌁ `.رفع مطي `\n⌁ `.رفع جلب `\n⌁ `.رفع بكلبي `\n - `.رفع مرتي `\n⌁ `.رفع تاج `\n⌁ `.رفع جريذي `\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م6":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "* قائـمه اوامر الحمايه :**\n⌁ `.الكل `\n⌁ `.المسموح لهم `\n⌁ `.سماح `\n - `.رفض `\n⌁ `.بلوك `\n⌁ `.انبلوك `\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر الحمايه :**\n⌁ `.الكل `\n⌁ `.المسموح لهم `\n⌁ `.سماح `\n - `.رفض `\n⌁ `.بلوك `\n⌁ `.انبلوك `\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م7":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "* قائـمه اوامر التلكراف :**\n⌁ `.تلكراف ميديا `\n⌁ `.تلكراف نص ` \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر التلكراف :**\n⌁ `.تلكراف ميديا `\n⌁ `.تلكراف نص ` \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م8":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "الأوامر رقم 8\n— — — — — — — — —\n\n⌔ قائمه اوامر القفل :\n⌁ .قفل  + الاضافه | لقفل المجموعه من امر معين \n⌁ .فتح  +الاضافه   | لفتح المجموعه من امر معين\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "الأوامر رقم 8\n— — — — — — — — —\n\n⌔ قائمه اوامر القفل :\n⌁ .قفل  + الاضافه | لقفل المجموعه من امر معين \n⌁ .فتح  +الاضافه   | لفتح المجموعه من امر معين\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م9":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "* قائـمه اوامر التاك :**\n⌁ `.تاك `\n⌁ `.للكل ` + الكلام \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر التاك :**\n⌁ `.تاك `\n⌁ `.للكل ` + الكلام \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م10":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "* قائـمه اوامر الكشف :**\n⌁ `.الايدي `\n⌁ `.ايدي `\n⌁ `.رابط الحساب ` \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر الكشف :**\n⌁ `.الايدي `\n⌁ `.ايدي `\n⌁ `.رابط الحساب ` \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon #


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م11":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "* قائـمه اوامر المجموعه :**\n⌁ `.المجموعه `\n⌁ `.رفع مشرف `\n⌁ `.رفع مالك `\n⌁ `.تك `\n⌁ `.الاحصائيات `\n⌁ `.تنظيف الحسابات `\n⌁ `.الاعضاء ` \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر المجموعه :**\n⌁ `.المجموعه `\n⌁ `.رفع مشرف `\n⌁ `.رفع مالك `\n⌁ `.تك `\n⌁ `.الاحصائيات `\n⌁ `.تنظيف الحسابات `\n⌁ `.الاعضاء ` \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م12":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "* قائـمه اوامر الترجمه :**\n⌁ `.ترجمه ar` لترجمه من اي لغه الى العربيه\n⌁ `.ترجمه en` لترجمه من اي لغه الى الانكليزيه \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر الترجمه :**\n⌁ `.ترجمه ar` لترجمه من اي لغه الى العربيه\n⌁ `.ترجمه en` لترجمه من اي لغه الى الانكليزيه \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م13":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "* قائـمه اوامر البحث :**\n⌁ `.بحث` للبحث عن اغنيه + .بحث عشق\n⌁ `.كوكل` + اسم لجلب صوره من موقع كوكل \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر البحث :**\n⌁ `.بحث` للبحث عن اغنيه + .بحث عشق\n⌁ `.كوكل` + اسم لجلب صوره من موقع كوكل \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


########### by ~ @Jmthon ###########


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م14":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "* قائـمه اوامر الانتحال :**\n⌁ `.نسخ` \n⌁ `.اعاده` \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر الانتحال :**\n⌁ `.نسخ` \n⌁ `.اعاده` \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م15":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "* قائـمه اوامر النت :**\n⌁ `.بنك` \n⌁ `.سرعه النت` \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر النت :**\n⌁ `.بنك` \n⌁ `.سرعه النت` \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م16":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "* قائـمه اوامر البوت :**\n⌁ `.اعاده تشغيل` \n⌁ `.ايقاف `\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر البوت :**\n⌁ `.اعاده تشغيل` \n⌁ `.ايقاف `\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 
import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م17":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "* قائـمه اوامر الحساب :**\n⌁ `.ضع اسم` | لتغير اسم حسابك\n⌁ `.ضع صوره` | لتغير صوره حسابك\n⌁ `.ضع معرف ` | لتغير معرف حسابك\n⌁ `.كروباتي ` لعرض المجموعات التي انشأتها\n⌁ `.مسح الصور ` لحذف جميع صور حسابك\n⌁ `.حذف صوره ` | لحذف صوره واحده من حسابك\n⌁ `.الحساب ` لعرض معلومات الحساب \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "* قائـمه اوامر الحساب :**\n⌁ `.ضع اسم` | لتغير اسم حسابك\n⌁ `.ضع صوره` | لتغير صوره حسابك\n⌁ `.ضع معرف ` | لتغير معرف حسابك\n⌁ `.كروباتي ` لعرض المجموعات التي انشأتها\n⌁ `.مسح الصور ` لحذف جميع صور حسابك\n⌁ `.حذف صوره ` | لحذف صوره واحده من حسابك\n⌁ `.الحساب ` لعرض معلومات الحساب \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


###########  by ~ @Jmthon ###########


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م18":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "قائمه اوامر التقليد :\n⌁ `.تقليد`  + الرد على الشخص | لتقليد رسائل الشخص \n⌁ `.الغاء التقليد`   | لالغاء التقليد \n⌁ `.المقلدهم`  لأظهار قائمه  الاشخاص التم تقليدهم\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                " قائمه اوامر التقليد :\n⌁ `.تقليد` + الرد على الشخص  | لتقليد رسائل الشخص\n⌁ `.الغاء التقليد`   | لألغاء التقليد \n⌁ `.المقلدهم`  لأظهار قائمه الاشخاص التم تقليدهم\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )

#@Jmthon 


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م19":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "قائمه الـوقتي :\n⌁ `.اسم تلقائي` لوضع وقت يتغير مع اسم حسابك \n⌁ `.انهاء اسم تلقائي` \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "قائمه الـوقتي :\n⌁ `.اسم تلقائي` لوضع وقت يتغير مع اسم حسابك \n⌁ `.انهاء اسم تلقائي` \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
            
            #Jmthon 
            
import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م20":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "قائمه اوامر القائمه السوداء :\n⌁ `.منع` + الكلمه   | لمنع ارسال هذع الكلمه\n⌁ `.الغاء منع`   | للسماح بهذه الكلمه \n⌁ `.الممنوعات`  لأظهار قائمه الكلمات المحظوره\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "قائمه اوامر القائمه السوداء :\n⌁ `.منع` + الكلمه   | لمنع ارسال هذع الكلمه\n⌁ `.الغاء منع`   | للسماح بهذه الكلمه \n⌁ `.الممنوعات`  لأظهار قائمه الكلمات المحظوره\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
            
            
           #Jmthon
           
import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م21":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "الاوامر الجانبيه :\n⌁ `.تكرار` +  رقم + الكلمه  | لتكرار الرسالة \n⌁ `.حساب` + المعادلة | لحساب معادلة رياضيات\n⌁ `.تنصيب` | لتنصيب ملف على البوت\n⌁ `.الغاء التنصيب`  | لالغاء تنصيب الملف\n⌁ `.الغاء تنصيب الكل` | لحذف الملفات التي تم تنصيبها \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "الاوامر الجانبيه :\n⌁ `.تكرار` +  رقم + الكلمه  | لتكرار الرسالة \n⌁ `.حساب` + المعادلة | لحساب معادلة رياضيات\n⌁ `.تنصيب` | لتنصيب ملف على البوت\n⌁ `.الغاء التنصيب`  | لالغاء تنصيب الملف\n⌁ `.الغاء تنصيب الكل` | لحذف الملفات التي تم تنصيبها \n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
            
            #Jmthon
            
import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م22":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                " قائمه اوامر الملصقات :\n⌁ `.ملصق`\n⌁ `.حزمه`\n⌁  `.معلومات الملصق`\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                " قائمه اوامر الملصقات :\n⌁ `.ملصق`\n⌁ `.حزمه`\n⌁  `.معلومات الملصق`\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
            
            #Jmthon
            
            
import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "قائمه":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "**قائمه اوامر جـمثون قم بضغط على الامر لنسخه :**\n⌁ `.ترحيب`\n⌁ `.مسح ترحيب`\n⌁ `.الترحيب `\n⌁ `.حظر`\n⌁ `.الغاء حظر`\n⌁ `.المحظورين`\n⌁ `.كتم`\n⌁ `.الغاء كتم`\n⌁ `.تقيد`\n⌁ `.الغاء تقيد`\n⌁ `.رفع القيود`\n⌁ `.رفع` - مطي ، جلب\n⌁ `.تثبيت`\n⌁ `.الغاء تثبيت`\n⌁ `.الغاء تثبيت الكل`\n⌁ `.منع كلمه`\n⌁ `.الغاء منع`\n⌁ `.رفع مشرف`\n⌁ `.رفع مالك`\n⌁ `.تنظيف`  》》 يستخدم بالرد على الرساله\n⌁ `.نسخ`  》》لنسخ بروفايل الشخص\n⌁ `.اعاده` 》》لاعاده حسابك بعد نسخ الصوره.. الخ\n⌁ `نسبه الانوثه`\n⌁ `.اعادة التشغيل`\n⌁ `.ايقاف التشغيل`\n⌁ `.تحديث`  》 لتحديث السورس\n⌁ `.بحث` 》 مثلا  `.بحث عشك`\n⌁ `.صوره` 》 مثلا  .صوره طياره\n⌁ `.ايدي` 》 لعرض معلومات البوت\n⌁ `.بنك`  》 يعرض البنك\n⌁ `.سرعه النت` 》 قياس سرعه النت\n⌁ `.ترجمه ar`\n⌁ `.ترجمه en` \n⌁ `.تكرار`+الرقم + الكلمه\n⌁ `.سبام`  》 كذالك نفس التكرار\n⌁ `.سماح` 》الامر فقط لميزه  حمايه الخاص\n⌁ `.رفض` 》 كذالك\n⌁ `.الكل` 》 لرفض الكل وتشغيل الحمايه\n⌁ `.بلوك` 》 من الخاص\n⌁ `.انبلوك` 》》لرفع الحظر من الخاص \n⌁ `.المسموح لهم` 》لعرض قائمه السماح\n⌁ `.ايدي` 》 لعرض معلومات المستخدم\n⌁ `.الايدي`\n⌁ `.المجموعه 》》لعرض معلومات المجموعه `\n⌁ `.السورس 》》 لعرض معلومات السورس `\n⌁ `.مغادره` 》 تستخدم  لمغادره الكروب\n⌁ `.تاك` 》 لعمل تاك للكل\n⌁ `.للكل` + الكلام 》 لعمل تاك\n⌁ `.تلكراف ميديا` 》 يستخدم بالرد على الصوره\n⌁ `.تلكراف نص` 》 بالرد على الكتابه\n⌁ `.المطور` \n\n  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )
        else:
            await event.edit(
                "**قائمه اوامر جـمثون قم بضغط على الامر لنسخه :**\n⌁ `.ترحيب`\n⌁ `.مسح ترحيب`\n⌁ `.الترحيب `\n⌁ `.حظر`\n⌁ `.الغاء حظر`\n⌁ `.المحظورين`\n⌁ `.كتم`\n⌁ `.الغاء كتم`\n⌁ `.تقيد`\n⌁ `.الغاء تقيد`\n⌁ `.رفع القيود`\n⌁ `.رفع` - مطي ، جلب\n⌁ `.تثبيت`\n⌁ `.الغاء تثبيت`\n⌁ `.الغاء تثبيت الكل`\n⌁ `.منع كلمه`\n⌁ `.الغاء منع`\n⌁ `.رفع مشرف`\n⌁ `.رفع مالك`\n⌁ `.تنظيف`  》》 يستخدم بالرد على الرساله\n⌁ `.نسخ`  》》لنسخ بروفايل الشخص\n⌁ `.اعاده` 》》لاعاده حسابك بعد نسخ الصوره.. الخ\n⌁ `نسبه الانوثه`\n⌁ `.اعادة التشغيل`\n⌁ `.ايقاف التشغيل`\n⌁ `.تحديث`  》 لتحديث السورس\n⌁ `.بحث` 》 مثلا  `.بحث عشك`\n⌁ `.صوره` 》 مثلا  .صوره طياره\n⌁ `.ايدي` 》 لعرض معلومات البوت\n⌁ `.بنك`  》 يعرض البنك\n⌁ `.سرعه النت` 》 قياس سرعه النت\n⌁ `.ترجمه ar`\n⌁ `.ترجمه en` \n⌁ `.تكرار`+الرقم + الكلمه\n⌁ `.سبام`  》 كذالك نفس التكرار\n⌁ `.سماح` 》الامر فقط لميزه  حمايه الخاص\n⌁ `.رفض` 》 كذالك\n⌁ `.الكل` 》 لرفض الكل وتشغيل الحمايه\n⌁ `.بلوك` 》 من الخاص\n⌁ `.انبلوك` 》》لرفع الحظر من الخاص \n⌁ `.المسموح لهم` 》لعرض قائمه السماح\n⌁ `.ايدي` 》 لعرض معلومات المستخدم\n⌁ `.الايدي`\n⌁ `.المجموعه 》》لعرض معلومات المجموعه `\n⌁ `.السورس 》》 لعرض معلومات السورس `\n⌁ `.مغادره` 》 تستخدم  لمغادره الكروب\n⌁ `.تاك` 》 لعمل تاك للكل\n⌁ `.للكل` + الكلام 》 لعمل تاك\n⌁ `.تلكراف ميديا` 》 يستخدم بالرد على الصوره\n⌁ `.تلكراف نص` 》 بالرد على الكتابه\n⌁ `.المطور` \n\n  -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
            )


#@Jmthon 

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "ديڤ":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                " 𝗗𝗘𝗩 𝗨𝗦𝗘𝗥 ↬ @RRRD7 \n  𝗗𝗘𝗩 𝗜𝗗 ↬ 1614649021"
            )
        else:
            await event.edit(
                " 𝗗𝗘𝗩 𝗨𝗦𝗘𝗥 ↬ @RRRD7 \n  𝗗𝗘𝗩 𝗜𝗗 ↬ 1614649021"
            )


#@Jmthon 

from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع جلب(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع جلب(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f" المستخدم [{custom}](tg://user?id={user.id}) \n تـم رفعه جلب ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌁ المستخدم [{tag}](tg://user?id={user.id}) \n ⌁ تـم رفعه جلب ",
        )


async def get_user_from_event(event):
    """Get the user from argument or replied message."""
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


#@Jmthon 

from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع مطي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع مطي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌁ المستخدم [{custom}](tg://user?id={user.id}) \n ⌁ تم رفعه مطي هنا ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌁ المستخدم [{tag}](tg://user?id={user.id}) \n ⌁ تم رفعه مطي هنا ",
        )


async def get_user_from_event(event):
    """Get the user from argument or replied message."""
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


#@Jmthon 

from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع مرتي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع مرتي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌁ المستخدم [{custom}](tg://user?id={user.id}) \n ⌁ تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌁ المستخدم [{tag}](tg://user?id={user.id}) \n ⌁ تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
        )


#@Jmthon 
from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع تاج(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع تاج(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌁ المستخدم [{custom}](tg://user?id={user.id}) \n ⌁ تـم رفعـه تـاج 👑🔥 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌁ المستخدم [{tag}](tg://user?id={user.id}) \n ⌁ تـم رفعـه تـاج 👑🔥 ",
        )


#@Jmthon 

from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع بكلبي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع بكلبي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌁ المستخدم [{custom}](tg://user?id={user.id}) \n ⌁ تـم رفعـه بڪلبك 🖤 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌁ المستخدم [{tag}](tg://user?id={user.id}) \n ⌁ تـم رفعـه بڪلبك 🖤 ",
        )


#@Jmthon 

from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع جريذي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع جريذي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌁ المستخدم [{custom}](tg://user?id={user.id}) \n ⌁ تـم رفعـه جـࢪيذي ۿنـا 😹🐀 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌁ المستخدم [{tag}](tg://user?id={user.id}) \n ⌁ تـم رفعـه جـࢪيذي ۿنـا 😹🐀 ",
        )


#@Jmthon 

from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع فرخ(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع فرخ(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌁ المستخدم [{custom}](tg://user?id={user.id}) \n ⌁ تم رفعه فرخ هنا ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌁ المستخدم [{tag}](tg://user?id={user.id}) \n ⌁ تم رفعه فرخ هنا ",
        )


async def get_user_from_event(event):
    """Get the user from argument or replied message."""
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


#@Jmthon 

import random

from telethon.tl.types import MessageEntityMentionName

ppp = [
    "100% 🔱💕.",
    "90%",
    "80%",
    "70%",
    "60%",
    "50%",
    "40%",
    "30%",
    "20%",
    "10%",
    "0%",
]


@bot.on(admin_cmd(pattern="نسبه الانوثه(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="نسبه الانوثه(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    ioi = random.choice(ppp)
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌁ نسبه الانوثه لـ [{custom}](tg://user?id={user.id}) هي {ioi} ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌁ نسبه الانوثه لـ [{tag}](tg://user?id={user.id}) هي {ioi} ",
        )


async def get_user_from_event(event):
    """Get the user from argument or replied message."""
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


#@Jmthon 

import time

from . import StartTime, get_readable_time, reply_id

DEFAULTUSER = "𝗝𝗠𝗧𝗛𝗢𝗡"
CAT_IMG = "https://telegra.ph/file/aa0115dc4eb24a30394d0.jpg"
CUSTOM_ALIVE_TEXT = "𓆩 𝙎𝙊𝙐𝙍𝘾-𝗝𝗠𝗧𝗛𝗢𝗡  𓆪"
EMOJI = "  - "


@bot.on(admin_cmd(outgoing=True, pattern="المطور$"))
@bot.on(sudo_cmd(pattern="المطور$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        cat_caption += f"**{EMOJI}** 𝗗𝗘𝗩 𝗨𝗦𝗘𝗥 ↬ @RRRD7  \n"
        cat_caption += f"**{EMOJI}** 𝗗𝗘𝗩 𝗜𝗗 ↬ 1614649021 \n"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n"
            f"**{EMOJI}** 𝗗𝗘𝗩 𝗨𝗦𝗘𝗥 ↬ @RRRD7  \n"
            f"**{EMOJI}** 𝗗𝗘𝗩 𝗜𝗗 ↬ 1614649021 ",
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