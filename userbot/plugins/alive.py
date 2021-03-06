import time
from platform import python_version

from telethon import version

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP, StartTime, catdef, catversion, hmention, mention

CAT_IMG = Config.ALIVE_PIC
JISAN = (
    str(Config.CUSTOM_ALIVE_TEXT)
    if Config.CUSTOM_ALIVE_TEXT
    else "<code>PanglimaTempur is running...</code>"
)


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = await catdef.get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    if CAT_IMG:
        cat_caption = f"{JISAN}\n"

        cat_caption += f"┏━━━━━━━━━━━━━━━━━━━━━━━━\n"
        cat_caption += f"┣[ 👤 <code>User       :</code> {hmention}\n"
        cat_caption += f"┣[ 🕒 <code>Bot Uptime :</code> {uptime}\n"
        cat_caption += f"┣[ 🐍 <code>Python     :</code> v{python_version()}\n"
        cat_caption += f"┣[ ⚙️ <code>Telethon   :</code> v{version.__version__}\n"
        cat_caption += f"┣[ 🤖 <code>Bot        :</code> v{catversion}\n"
        cat_caption += f"┣[ 💻 <code>Database   :</code> {check_sgnirts}✓\n"
        cat_caption += f"┗━━━━━━━━━━━━━━━━━━━━━━━━\n"
        cat_caption += "I do exist but not in your heart<a href = https://github.com/iunderhere/PanglimaTempur>🌹</a>"

        await alive.client.send_file(
            alive.chat_id,
            CAT_IMG,
            caption=cat_caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"{JISAN}\n"
            f"┏━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"┣[ 👤 <code>User       :</code> {hmention}\n"
            f"┣[ 🕒 <code>Bot Uptime :</code> {uptime}\n"
            f"┣[ 🐍 <code>Python     :</code> v{python_version()}\n"
            f"┣[ ⚙️ <code>Telethon   :</code> v{version.__version__}\n"
            f"┣[ 🤖 <code>Bot        :</code> v{catversion}\n"
            f"┣[ 💻 <code>Database   :</code> {check_sgnirts}✓\n"
            f"┗━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "I do exist but not in your heart<a href = https://github.com/iunderhere/PanglimaTempur>🌹</a>",
            parse_mode="html",
        )


@bot.on(admin_cmd(outgoing=True, pattern="ialive$"))
@bot.on(sudo_cmd(pattern="ialive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
    reply_to_id = alive.message
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    cat_caption = f"`PanglimaTempur is running...`\n"
    cat_caption += f"`Lord             :` {mention}\n"
    cat_caption += f"`Python Version   :` v{python_version()}\n`"
    cat_caption += f"`Telethon version :` v{version.__version__}\n`"
    cat_caption += f"`Bot Version      :` v{catversion}`\n"
    results = await bot.inline_query(tgbotusername, cat_caption)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()


# UniBorg Telegram UseRBot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# വിവരണം അടിച്ചുമാറ്റിക്കൊണ്ട് പോകുന്നവർ
# ക്രെഡിറ്റ് വെച്ചാൽ സന്തോഷമേ ഉള്ളു..!
# uniborg


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Var.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "__**PLUGIN NAME :** Alive__\
      \n\n✅** CMD ➥** `.alive`\
      \n**USAGE   ➥  **buat liat bot hidup apa kgk\
      \n\n✅** CMD ➥** `.ialive`\
      \n**USAGE   ➥  **__Status of bot will be showed by inline mode with button__."
    }
)
