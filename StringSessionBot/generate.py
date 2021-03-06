from asyncio.exceptions import TimeoutError
from Data import Data
from pyrogram import Client, filters
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

ERROR_MESSAGE = "Oops! An exception occurred! \n\n**Error** : {} " \
            "\n\nPlease forward this to @BTS_CHAT_ZONE if this message doesn't contain any " \
            "sensitive information and for your information : **These kinda error logs are not stored in our database!**"


photo = "https://te.legra.ph/file/601603022035e64d435be.jpg"

alpha = "https://te.legra.ph/file/ca0fa4f4e821944ad08da.jpg"

@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate@alpha'))
async def main(_, msg):
    await msg.reply_photo(alpha,
        caption="ᴄʜᴏᴏsᴇ ᴡʜɪᴄʜ ᴛʏᴘᴇ ᴏғ sᴇssɪᴏɴ ʏᴏᴜ ɴᴇᴇᴅᴇᴅ !",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ sᴇssɪᴏɴ", callback_data="pyrogram"),
            InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴ", callback_data="telethon")
        ]])
    )


async def generate_session(bot, msg, telethon=False):
    await msg.reply_photo(photo,
                      caption="{} sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ sᴛᴀʀᴛᴇᴅ ʙʏ ᴀʟᴘʜᴀ !".format("ᴛᴇʟᴇᴛʜᴏɴ" if telethon else "ᴘʏʀᴏɢʀᴀᴍ"))
    user_id = msg.chat.id

    api_id = "14151343"
    api_hash = "9330f17086496c4580bdc8f8b24ec364"

    phone_number_msg = await bot.ask(user_id, 'ɴᴏᴡ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀʟᴏɴɢ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴜɴᴛʀʏ ᴄᴏᴅᴇ. \nsᴀᴍᴇ ᴀs : `+𝟿𝟷𝟿𝟿𝟾𝟾𝟽𝟽𝟼𝟼𝟻𝟻`', filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    await msg.reply("sᴇɴᴅɪɴɢ ᴏᴛᴘ...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    else:
        client = Client(":memory:", api_id, api_hash)
    await client.connect()
    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply('ᴀᴘɪ ɪᴅ ᴀɴᴅ ᴀᴘɪ ʜᴀsʜ ᴄᴏᴍʙɪɴᴀᴛɪᴏɴ ɪs ɪɴᴠᴀʟɪᴅ. ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply('ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪs ɪɴᴠᴀʟɪᴅ. ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = await bot.ask(user_id, "ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ғᴏʀ ᴀɴ ᴏᴛᴘ ɪɴ ᴏғғɪᴄɪᴀʟ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ. ɪғ ʏᴏᴜ ɢᴏᴛ ɪᴛ, sᴇɴᴅ ᴏᴛᴘ ʜᴇʀᴇ ᴀғᴛᴇʀ ʀᴇᴀᴅɪɴɢ ᴛʜᴇ ʙᴇʟᴏᴡ ғᴏʀᴍᴀᴛ. \nɪғ ᴏᴛᴘ ɪs ɪɴ ᴛʜᴇ ғᴏʀᴍ ~ `𝟷𝟸𝟹𝟺𝟻`, **ᴘʟᴇᴀsᴇ sᴇɴᴅ ɪᴛ ᴀs** `𝟷 𝟸 𝟹 𝟺 𝟻`.", filters=filters.text, timeout=600)
        if await cancelled(phone_number_msg):
            return
    except TimeoutError:
        await msg.reply('ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 𝟷𝟶 ᴍɪɴᴜᴛᴇs. ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    phone_code = phone_code_msg.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, phone_code, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, phone_code)
    except (PhoneCodeInvalid, PhoneCodeInvalidError):
        await msg.reply('ᴏᴛᴘ ɪs ɪɴᴠᴀʟɪᴅ. ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneCodeExpired, PhoneCodeExpiredError):
        await msg.reply('ᴏᴛᴘ ɪs ᴇxᴘɪʀᴇᴅ. ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (SessionPasswordNeeded, SessionPasswordNeededError):
        try:
            two_step_msg = await bot.ask(user_id, 'ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʜᴀs ᴇɴᴀʙʟᴇᴅ ᴛᴡᴏ-sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ. ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ ᴘᴀssᴡᴏʀᴅ.', filters=filters.text, timeout=300)
        except TimeoutError:
            await msg.reply('ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 𝟻 ᴍɪɴᴜᴛᴇs. ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        try:
            password = two_step_msg.text
            if telethon:
                await client.sign_in(password=password)
            else:
                await client.check_password(password=password)
            if await cancelled(phone_number_msg):
                return
        except (PasswordHashInvalid, PasswordHashInvalidError):
            await two_step_msg.reply('ɪɴᴠᴀʟɪᴅ ᴘᴀssᴡᴏʀᴅ ᴘʀᴏᴠɪᴅᴇᴅ. ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ᴀɢᴀɪɴ.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
    if telethon:
        string_session = client.session.save()
        try:
            await client(JoinChannelRequest("@BTS_CHAT_ZONE"))
            await client(LeaveChannelRequest("@Legend_Userbot"))
            await client(LeaveChannelRequest("@Official_LegendBot"))
        except BaseException:
            pass
    else:
        string_session = await client.export_session_string()
    L_PIC = "https://te.legra.ph/file/c5b0ca3cf63d3fe37e0c1.jpg"
    if telethon:
        await client.send_file("me", L_PIC, caption="**{} - STRING SESSION** \n\n`{}`\n\n• __Dont Share String Session With Anyone__\n• __Dont Invite Anyone To Heroku__".format("TELETHON" if telethon else "PYROGRAM", string_session))
    else:
        await client.send_message("me", "**{} ~ STRING SESSION** \n\n`{}` \n\n• __Dont Share String Session With Anyone__\n• __Dont Invite Anyone To Heroku__".format("TELETHON" if telethon else "PYROGRAM", string_session))
    await client.disconnect()
    await phone_code_msg.reply("sᴜᴄᴄᴇssғᴜʟʟʏ sᴛʀɪɴɢ sᴇssɪᴏɴ ʜᴀs ʙᴇᴇɴ ɢᴇɴᴇʀᴀᴛᴇᴅ {} ʙʏ ᴀʟᴘʜᴀ \n\nᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs!".format("TELETHON" if telethon else "PYROGRAM"), reply_markup=InlineKeyboardMarkup(Data.support_button))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("Cancelled the Process!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("Restarted the Bot!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("Cancelled the generation process!", quote=True)
        return True
    else:
        return False
