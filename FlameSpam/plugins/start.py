import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Flame, Flame2, Flame3, Flame4, Flame5, Flame6, Flame7, Flame8, Flame9, Flame10, ALIVE_PIC, OWNER_ID
from FlameSpam.plugins.help import *


FLAME_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/2c23f012984fa91267146.jpg"

Flame_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/random_spamer")
        ],
        [
        Button.inline("• ᴄᴍᴅs •", data="help_back")
        ]
        ]
               
FlameX_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/flame_updates"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/random_spamer")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/S780821/FlameSpam")
        ]
        ]
        
        
#USERS 


@Flame.on(events.NewMessage(pattern="/start"))
@Flame2.on(events.NewMessage(pattern="/start"))
@Flame3.on(events.NewMessage(pattern="/start"))
@Flame4.on(events.NewMessage(pattern="/start"))
@Flame5.on(events.NewMessage(pattern="/start"))
@Flame6.on(events.NewMessage(pattern="/start"))
@Flame7.on(events.NewMessage(pattern="/start"))
@Flame7.on(events.NewMessage(pattern="/start"))
@Flame8.on(events.NewMessage(pattern="/start"))
@Flame9.on(events.NewMessage(pattern="/start"))
@Flame10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       FlameBot = await event.client.get_me()
       bot_id = FlameBot.first_name
       bot_username = FlameBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       flame = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [ FLAME ](https://t.me/FLAME_UPDATES)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(flame,
                  FLAME_IMG,
                  caption=ownermsg, 
                  buttons=Flame_Button)
       else:
            await event.client.send_file(flame,
                  FLAME_IMG,
                  caption=usermsg, 
                  buttons=Flame_Button)
                

