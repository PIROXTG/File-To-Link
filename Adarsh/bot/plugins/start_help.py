#Adarsh goel
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

                      
@StreamBot.on_message(filters.command('start'))
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        await m.reply_text(
            text="**𝘏𝘦𝘭𝘭𝘰 𝘛𝘩𝘦𝘳𝘦...⚡\n𝘐'𝘮 𝘈 𝘚𝘪𝘮𝘱𝘭𝘦 𝘛𝘦𝘭𝘨𝘳𝘢𝘮 𝘍𝘪𝘭𝘦 𝘛𝘰 𝘓𝘪𝘯𝘬 𝘉𝘰𝘵.**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🚀 𝘜𝘱𝘥𝘢𝘵𝘦𝘴 🚀", url="https://telegram.dog/piroxbots")]
                ]
            ),
            
        )
    else:

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id)

        msg_text = "**𝘠𝘰𝘶𝘳 𝘓𝘪𝘯𝘬 𝘐𝘴 𝘎𝘦𝘯𝘦𝘳𝘢𝘵𝘦𝘥.⚡\n\n📧 𝘍𝘪𝘭𝘦 𝘕𝘢𝘮𝘦:-\n{}\n {}\n\n💌 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘓𝘪𝘯𝘬 :- {}**"
        await m.reply_text(            
            text=msg_text.format(file_name, file_size, stream_link),
            
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡ 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘕𝘰𝘸 ⚡", url=stream_link)]])
        )

@StreamBot.on_message(filters.command('help'))
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
              
    await message.reply_text(
            text="""**𝘑𝘶𝘴𝘵 𝘍𝘰𝘳𝘸𝘢𝘳𝘥 𝘛𝘩𝘦 𝘍𝘪𝘭𝘦 & 𝘠𝘰𝘶 𝘞𝘪𝘭𝘭 𝘎𝘦𝘵 𝘛𝘩𝘦 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘓𝘪𝘯𝘬.**""", disable_web_page_preview=True,  quote=True,
            )

@StreamBot.on_message(filters.command('about'))
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    await message.reply_text(
            text="""<b>
○ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href='https://telegram.dog/piroxbots'>[𝖯𝖨𝖱𝖮]</a>
○ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : <a href='https://www.python.org/downloads/release/python-3106/'>𝖯𝗒𝗍𝗁𝗈𝗇 𝟥</a>
○ 𝖲𝖾𝗋𝗏𝖾𝗋 : <a href='https://cloud.google.com/learn/what-is-a-virtual-private-server'>VPS</a>
○ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 : <a href='https://www.mongodb.com'>𝖬𝗈𝗇𝗀𝗈𝖣𝖡 𝖥𝗋𝖾𝖾 𝖳𝗂𝖾𝗋</a></b>""", disable_web_page_preview=True,  quote=True,
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🚀 𝘜𝘱𝘥𝘢𝘵𝘦𝘴 🚀", url="https://telegram.dog/piroxbots")]
                ]
            ))
