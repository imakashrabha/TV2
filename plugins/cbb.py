#(©) AxomBotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b><b>○ 𝖮𝗐𝗇𝖾𝗋 : <a href='tg://user?id={OWNER_ID}'>𝖠𝗄𝖺𝗌𝗁</a>\n○ 𝖬𝗈𝗏𝗂𝖾𝗌 : <a href='https://t.me/+RnKzgKCQ2Uw2NzJl'>𝖠ʟʟ 𝖬ᴏᴠɪᴇ𝗌𝖧ᴜʙ 𝖮ғғɪᴄɪᴀʟ 🍿🎥</a>\n○ 𝖼𝗈𝗆𝗆𝗎𝗇𝗂𝗍𝗒 : <a href='https://t.me/+yft5ysRDW4BiOTc9'>𝖼𝗈𝗆𝗆𝗎𝗇𝗂𝗍𝗒</a>\n</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('ᴄᴏᴍᴍᴜɴɪᴛʏ', url='https://t.me/+yft5ysRDW4BiOTc9')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
