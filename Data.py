from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """

ʜᴇʏ {}!! ɴɪᴄᴇ ᴛᴏ sᴇᴇ ʏᴀ ʜᴇʀᴇ ! ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {} !\n\nᴇɴᴅ ᴠᴇʀsɪᴏɴ - ᴇɴᴅ ᴠ𝟺 ᴜʟᴛɪᴍᴀᴛᴇ ©\n\nʟᴀsᴛ ᴜᴘᴅᴀᴛᴇᴅ - 𝟷𝟻/𝟶𝟻/𝟸𝟶𝟸𝟸\n\nRegards✨💫 ~ @THE_END_NETWORK

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Click here to Generate", callback_data="intro")],
        [InlineKeyboardButton(text="✨Back🕊", callback_data="home")],
        [InlineKeyboardButton(text="✨Commands💫 ", callback_data="cmda")],
        [InlineKeyboardButton(text="✨Alpha Version💫", callback_data="alphaversion")]
    ]

    generate_button = [
        [InlineKeyboardButton("Click here to Generate", callback_data="intro")]
    ]

    support_button = [
        [InlineKeyboardButton("✨Group💜", url="https://t.me/BTS_CHAT_ZONE")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Click here to Generate", callback_data="intro")],
        [
            InlineKeyboardButton("✨Tutorial🛠", callback_data="help"),
            InlineKeyboardButton("✨Contact❄️", callback_data="about")
        ],
        [
            InlineKeyboardButton("✨Owner❤️", url="https://t.me/Timeisnotwaiting"),
            InlineKeyboardButton("✨Network💜", url="https://t.me/THE_END_NETWORK")
        ],
        [
            InlineKeyboardButton("✨Commands💫", callback_data="cmda"),
            InlineKeyboardButton("✨Alpha version💫", callback_data="alphaversion")
        ],  
    ]

    # Help Message
    HELP = """

» ᴄʟɪᴄᴋ ᴏɴ ɢᴇɴᴇʀᴀᴛᴇ ʙᴜᴛᴛᴏɴ ; ᴛʜᴇɴ ʏᴏᴜ'ʟʟ ɢᴇᴛ ᴛᴏ sᴇᴇ ᴛᴡᴏ ʙᴜᴛᴛᴏɴs\n\n» 𝟷.ᴘʏʀᴏɢʀᴀᴍ - ғᴏʀ ᴍᴜsɪᴄ ʙᴏᴛs\n\n» 𝟸.ᴛᴇʟᴇᴛʜᴏɴ - ғᴏʀ ᴀʟʟ ʙᴏᴛs ᴇxᴄᴇᴘᴛ ᴍᴜsɪᴄ ᴏɴᴇ !\n\n» ᴄʜᴏᴏsᴇ ᴡʜᴀᴛ ʏᴀ ᴡᴀɴᴛ !\n\n» sᴜʙᴍɪᴛ ᴀᴘɪ ɪᴅ , ᴀᴘɪ ʜᴀsʜ , ɴᴜᴍʙᴇʀ , ᴄᴏᴅᴇ !\n\n» sᴛʀɪɴɢ ᴡɪʟʟ ʙᴇ sᴇɴᴛ ᴛᴏ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs ! ✨💫

____

ᴛʜx ғᴏʀ ᴜsɪɴɢ ᴏᴜʀ ʙᴏᴛ ! ✨💫

"""

    # About Message
    ABOUT = """
** ᴀʟᴘʜᴀ sᴛʀɪɴɢ ʙᴏᴛ © **

ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ᴡɪᴛʜ ᴘʀɪᴠᴀᴄʏ ! ©\n\n[𝐃𝐄𝐯𝐄𝐬𝐇](t.me/xDevesh) | [𝐀𝐋𝐏𝐇𝐀](t.me/Timeisnotwaiting)\n\nʟᴀɴɢᴜᴀɢᴇ ᴜsᴇᴅ : ᴘʏᴛʜᴏɴ\n\nᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇʀs [ʜᴇʀᴇ](t.me/BTS_CHAT_ZONE)

"""

