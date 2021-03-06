from Data import Data
from Yashvi import Keshav
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from StringSessionBot.generate import generate_session, ERROR_MESSAGE
from StringSessionBot.generatee import generatee_session

alpha = "https://te.legra.ph/file/ca0fa4f4e821944ad08da.jpg"

# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user["mention"]
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.message_id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
    elif query == "about":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif query == "help":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="** ᴘᴇʀғᴇᴄᴛ ᴛᴜᴛᴏʀɪᴀʟ ʙʏ ᴀʟᴘʜᴀ**\n" + Data.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif query == "cmda":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Keshav.CMDA,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Keshav.command_buttons),
         )
    elif query == "alphaversion":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Keshav.ALPHAVERSION,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Keshav.version_buttons),
        )
    elif query == "intro":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Keshav.INTRO,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Keshav.intro_buttons),
        )
    elif query == "generatee":
        await callback_query.message.reply_photo(alpha,
            caption="ᴄʜᴏᴏsᴇ ᴡʜɪᴄʜ ᴛʏᴘᴇ ᴏғ sᴇssɪᴏɴ ʏᴏᴜ ɴᴇᴇᴅᴇᴅ !",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ sᴇssɪᴏɴ", callback_data="pyrograme"),
                InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴ", callback_data="telethone")
            ]])
        )
    elif query == "generate":
        await callback_query.message.reply_photo(alpha,
            caption="ᴄʜᴏᴏsᴇ ᴡʜɪᴄʜ ᴛʏᴘᴇ ᴏғ sᴇssɪᴏɴ ʏᴏᴜ ɴᴇᴇᴅᴇᴅ !",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ sᴇssɪᴏɴ", callback_data="pyrogram"),
                InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴ", callback_data="telethon")
            ]])
        )
    elif query in ["pyrogram", "telethon"]:
        await callback_query.answer()
        try:
            if query == "pyrogram":
                await generate_session(bot, callback_query.message)
            else:
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))
    elif query in ["pyrograme", "telethone"]:
        await callback_query.answer()
        try:
            if query == "pyrograme":
                await generatee_session(bot, callback_query.message)
            else:
                await generatee_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))
