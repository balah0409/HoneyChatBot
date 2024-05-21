from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, ContextTypes

from AsuX import rani


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    msg = update.effective_message
    akboss = []
    akboss.append(
        [
            InlineKeyboardButton(
                text="𝐀ᴅᴅ 𝐌ᴇ",
                url=f"http://t.me/{context.bot.username}?startgroup=true"),
            InlineKeyboardButton(
                text="𝐃ᴀʀʟɪɴɢ",
                url=f"https://t.me/Idhayann"),
        ]
    
    )
    await msg.reply_text(
        f"ʜᴇʏᴀ\nɪ'ᴍ {context.bot.first_name}\nɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ᴄʜᴀᴛ \n",
        reply_markup=InlineKeyboardMarkup(akboss),
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    msg = update.effective_message
    akboss = []
    akboss.append(
        [
            InlineKeyboardButton(
                text="𝐀ᴅᴅ 𝐌ᴇ",
                url=f"http://t.me/{context.bot.username}?startgroup=true"),
            InlineKeyboardButton(
                text="𝐃ᴀʀʟɪɴɢ",
                url=f"https://t.me/Idhayann"),
        ]
    )
    await msg.reply_text(
        f"ʜᴇʏᴀ\nɪ'ᴍ {context.bot.first_name}\nɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ᴄʜᴀᴛ \n\nɪ ᴄᴀɴ ʀᴇꜱᴛʀɪᴄᴛ ᴡʜɪᴄʜ ᴄᴏɴᴛᴀɪɴꜱ ᴘᴜʙʟɪᴄ ᴄʜᴀᴛ ᴜꜱᴇʀɴᴀᴍᴇ ᴍᴇꜱꜱᴀɢᴇꜱ",
        reply_markup=InlineKeyboardMarkup(akboss),
    )


START = CommandHandler(["chatbot", "start"], start, block=False)
HELP = CommandHandler(["chelp", "help"], help, block=False)

rani.add_handler(START)
rani.add_handler(HELP)
