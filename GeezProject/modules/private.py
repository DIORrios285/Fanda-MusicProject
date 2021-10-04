# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from GeezProject.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from GeezProject.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME, OWNER
logging.basicConfig(level=logging.INFO)

@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hallo anak yatim {message.from_user.first_name} Gua {PROJECT_NAME}\n
Gua adalah Bot Music Group, Yang bisa Muterin Lagu di VCG/OS lu
Gua Punya Banyak Fitur Seperti :
• Muterin Musik di VCG lu.
• Mendownload Lagu.
• Cari lagu yang mau lu Puter atau Download.
• Pake Perintah » /help « Biar tau fitur lengkapnya

📌 Makasih sebelumnya udh bikin gua : {OWNER}

Mau masukin gua ke gc lu? Masukin aja buru!
</b>""",

# Edit Yang Seharusnya Lu Edit Aja:D
# Tapi Jangan di Hapus Special Thanks To nya Yaaa :'D

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Masukin gua ke gc lu ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "📢 Channel informasi", url=f"https://t.me/{UPDATES_CHANNEL}"), 
                    InlineKeyboardButton(
                        "⚔️ Group Support", url=f"https://t.me/{SUPPORT_GROUP}")
                ],[
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url=f"https://{SOURCE_CODE}")
                ],[
                    InlineKeyboardButton(
                        "💳 Donasi", url=f"https://t.me/uurfavboys1")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = 'Next »', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton("➕ Masukin gua ke gc lu ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = '📢 Channel informasi', url=f"https://t.me/{UPDATES_CHANNEL}"),
             InlineKeyboardButton(text = '⚔️ Group Support', url=f"https://t.me/{SUPPORT_GROUP}")],
            [InlineKeyboardButton(text = '🛠 Source Code 🛠', url=f"https://{SOURCE_CODE}")],
            [InlineKeyboardButton(text = '«', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '«', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '»', callback_data = f"help+{pos+1}")
            ],
        ]
    return button


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "🧐 **Lu mau nyari link YouTube?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ Y", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ G ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**Teken tombol di bawah ini biar lu tau cara make gua**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 Cara make gua 📜", url="https://telegra.ph/CCARA-PAKE-FANDA-MUSIC-BOT-09-30"
                    )
                ]
            ]
        ),
    )  


@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""✅ Bot **udah dimulai ulang!**\n\n• **Daftar etmin** udah **diperbarui nyet**\n\n• **Anak kontol anak anjing kalo make bot gratisan tuh jangan spam req atau lagu ya bangsat tar bot eror baru lu ngoceh ngoceh ga jelas kontol**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Join gc gua yuk", url=f"https://t.me/fandaproject"
                    ),
                    InlineKeyboardButton(
                        "yg buat gua", url=f"https://t.me/uurfavboys1"
                    )
                ]
            ]
        )
   )

