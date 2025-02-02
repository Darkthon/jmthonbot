# Heroku manager for Extrathon

import asyncio
import math
import os

import heroku3
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY

Heroku_cmd = (
    "**ϟ قائـمه اوامر هيروكو :** \n"
    "- `.set var` + الفار + المتغير\n"
    "- `.get var` + الفار لعرض ما في المتغير \n"
    "- `.del var` + الفار لحذف الفار \n"
    "- `.استخدامي` \n\n"
    "-  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon"
)

@bot.on(admin_cmd(pattern=r"(set|get|del) var (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"(set|get|del) var (.*)", allow_sudo=True))
async def variable(var):
    if Config.HEROKU_API_KEY is None:
        return await ed(
            var,
            "ϟ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(
            var,
            "ϟ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        ics = await edit_or_reply(var, "**ϟ جاري الحصول على المعلومات. **")
        await asyncio.sleep(1.0)
        try:
            variable = var.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await ics.edit(
                    ""
                    f"\n **ϟ** `{variable} = {heroku_var[variable]}` .\n"
                )
            return await ics.edit(
                ""
                f"\n **ϟ خطا :**\n-> {variable} غيـر موجود. "
            )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await bot.send_file(
                        var.chat_id,
                        "configs.json",
                        reply_to=var.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await ics.edit(
                        "`[HEROKU]` ConfigVars:\n\n"
                        "================================"
                        f"\n```{result}```\n"
                        "================================"
                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        variable = "".join(var.text.split(maxsplit=2)[2:])
        ics = await edit_or_reply(var, "**ϟ جاري اعداد المعلومات**")
        if not variable:
            return await ics.edit("ϟ .set var `<ConfigVars-name> <value>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if not value:
            return await ics.edit("ϟ .set var `<ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await ics.edit("**ϟ تم تغيـر** `{}` **:**\n **- المتغير :** `{}`".format(variable, value))
        else:
            await ics.edit("**ϟ تم اضافه** `{}` **:** \n**- المضاف اليه :** `{}`".format(variable, value))
        heroku_var[variable] = value
    elif exe == "del":
        ics = await edit_or_reply(var, "ϟ الحصول على معلومات لحذف المتغير. ")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await ics.edit("ϟ يرجى تحديد `Configvars` تريد حذفها. ")
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
            return await ics.edit(f"ϟ `{variable}`**  غير موجود**")

        await ics.edit(f"**ϟ** `{variable}`  **تم حذفه بنجاح. **")
        del heroku_var[variable]


@bot.on(admin_cmd(pattern="استخدامي$", outgoing=True))
@bot.on(sudo_cmd(pattern="استخدامي$", allow_sudo=True))
async def dyno_usage(dyno):
    """
    Get your account Dyno Usage
    """
    if HEROKU_APP_NAME is None:
        return await ed(
            dyno,
            "ϟ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    if HEROKU_API_KEY is None:
        return await ed(
            dyno,
            "ϟ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    dyno = await edit_or_reply(dyno, "**ϟ جاري المعـالجه..**")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Config.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("ϟ خطا:** شي سيء قد حدث **\n" f" ϟ `{r.reason}`\n")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    # - Used -
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    # - Current -
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    return await dyno.edit(
        ""
        f"**ϟ اسم التطبيق في هيروكو :**\n"
        f"**    - معرف اشتراكك - {Config.HEROKU_APP_NAME}**"
        f"\n\n"
        f" **ϟ مدة اسـتخدامك لبوت جـمثون : **\n"
        f"     -  `{AppHours}`**ساعه**  `{AppMinutes}`**دقيقه**  "
        f"**-**  `{AppPercentage}`**%**"
        "\n\n"
        " **ϟ الساعات المتبقيه لاستخدامك : **\n"
        f"     -  `{hours}`**ساعه**  `{minutes}`**دقيقه**  "
        f"**-**  `{percentage}`**%**"
    )


@bot.on(admin_cmd(pattern="herokulogs$", outgoing=True))
@bot.on(sudo_cmd(pattern="herokulogs$", allow_sudo=True))
async def _(dyno):
    if HEROKU_APP_NAME is None:
        return await ed(
            dyno,
            "Set the required var in heroku to function this normally `HEROKU_APP_NAME`.",
        )
    if HEROKU_API_KEY is None:
        return await ed(
            dyno,
            "Set the required var in heroku to function this normally `HEROKU_API_KEY`.",
        )
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply(
            " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
        )
    data = app.get_log()
    key = (
        requests.post("https://nekobin.com/api/documents", json={"content": data})
        .json()
        .get("result")
        .get("key")
    )
    url = f"https://nekobin.com/{key}"
    reply_text = f"Recent 100 lines of heroku logs: [here]({url})"
    await edit_or_reply(dyno, reply_text)


def prettyjson(obj, indent=2, maxlinelength=80):
    items, _ = getsubitems(
        obj,
        itemkey="",
        islast=True,
        maxlinelength=maxlinelength - indent,
        indent=indent,
    )
    return indentitems(items, indent, level=0)

@borg.on(admin_cmd("م24"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("قائمـة حـساب هـيروكو\n\n`.استخدامي`\n**استخدامي: لعرض ساعات استخدامي الحاليه والمتبقيه**") 



