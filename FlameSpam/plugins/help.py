from FlameXSpam import Flame, Flame2, Flame3, Flame4, Flame5, Flame6, Flame7, Flame8, Flame9, Flame10, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from FlameSpam import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/9acc785291052c8f8998d.jpg"

Flame_Help = "__Click On Below Buttons for help__"


@Flame.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Flame2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Flame3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Flame4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Flame5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Flame6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Flame7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Flame8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Flame9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Flame10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Flame_Help,
                                  buttons=[
           [
            Button.inline("• Spam •", data="spam"),
            Button.inline("• Raid •", data="raid"),
           ],
           [
            Button.inline("• Extra •", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/flameSpam")
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**

**Userbot**: Userbot Cmds
command:
i) {hl}ping 
ii) {hl}alive
iii) {hl}restart
iv) {hl}addsudo <reply to user> : Owner Cmd

**Echo**: To Active Echo On Any User
command:
i) {hl}addecho <reply to user>
ii) {hl}rmecho <reply to user>

**Leave**: To Leave Group/channel
command:
i) {hl}leave <group/chat id>
ii) {hl}leave : Type in the Group bot will auto leave that group

**Packspam**: Sticker Pack Spam
i) {hl}packspam (replying to any sticker)

**© @Flame**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**raid:** Activates raid on any individual user for given range.
command:
i) {hl}raid <count> <username
ii) {hl}raid <count> <reply to user>

**Delayraid**: Activates raid on any individual user for given range.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>

**replyraid:** Activates Reply Raid on the user!!
command:
i) {hl}replyraid <replying to user>
ii) {hl}dreplyraid <username>

**dreplyraid:** Deactivates reply raid on the user!!
command:
i) {hl}dreplyraid <replying to user>
ii) {hl}dreplyraid <username>


**© @Flame**
"""

spam_msg = f"""
**Help Spam Cmds**

**spam**: Spams a message for given counter(<= 100).
command:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>

**bigspam**: Spams a message for given counter.
command:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>

**delayspam**: Delay spam a text for given counter after given time.
command:
i) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay> <count> <replying any message>

**pornspam**: Pornography Spam.
command:
i) {hl}pornspam <count>

**hang**: Spams hanging message for given counter.
command:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @Flame**
"""                     
           
           
@Flame.on(events.CallbackQuery(pattern=r"help_back"))
@Flame2.on(events.CallbackQuery(pattern=r"help_back"))
@Flame3.on(events.CallbackQuery(pattern=r"help_back"))
@Flame4.on(events.CallbackQuery(pattern=r"help_back"))
@Flame5.on(events.CallbackQuery(pattern=r"help_back"))
@Flame6.on(events.CallbackQuery(pattern=r"help_back"))
@Flame7.on(events.CallbackQuery(pattern=r"help_back"))
@Flame8.on(events.CallbackQuery(pattern=r"help_back"))
@Flame9.on(events.CallbackQuery(pattern=r"help_back"))
@Flame10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            Flame_Help,
            buttons=[
                [
            Button.inline("Spam", data="spam"),
            Button.inline("Raid", data="raid"),
           ],
           [
            Button.inline("Extra cmds", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/flamespam")
           ],
           ],
        )           
   else:
        Alert = (
                "Noob !! Make Your Own ғʟᴀᴍᴇ Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@Flame.on(events.CallbackQuery(pattern=r"spam"))
@Flame2.on(events.CallbackQuery(pattern=r"spam"))
@Flame3.on(events.CallbackQuery(pattern=r"spam"))
@Flame4.on(events.CallbackQuery(pattern=r"spam"))
@Flame5.on(events.CallbackQuery(pattern=r"spam"))
@Flame6.on(events.CallbackQuery(pattern=r"spam"))
@Flame7.on(events.CallbackQuery(pattern=r"spam"))
@Flame8.on(events.CallbackQuery(pattern=r"spam"))
@Flame9.on(events.CallbackQuery(pattern=r"spam"))
@Flame10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "Noob !! Make Your Own ғʟᴀᴍᴇ Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@Flame.on(events.CallbackQuery(pattern=r"raid"))
@Flame2.on(events.CallbackQuery(pattern=r"raid"))
@Flame3.on(events.CallbackQuery(pattern=r"raid"))
@Flame4.on(events.CallbackQuery(pattern=r"raid"))
@Flame5.on(events.CallbackQuery(pattern=r"raid"))
@Flame6.on(events.CallbackQuery(pattern=r"raid"))
@Flame7.on(events.CallbackQuery(pattern=r"raid"))
@Flame8.on(events.CallbackQuery(pattern=r"raid"))
@Flame9.on(events.CallbackQuery(pattern=r"raid"))
@Flame10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "Noob !! Make Your Own ғʟᴀᴍᴇ Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@Flame.on(events.CallbackQuery(pattern=r"extra"))
@Flame2.on(events.CallbackQuery(pattern=r"extra"))
@Flame3.on(events.CallbackQuery(pattern=r"extra"))
@Flame4.on(events.CallbackQuery(pattern=r"extra"))
@Flame5.on(events.CallbackQuery(pattern=r"extra"))
@Flame6.on(events.CallbackQuery(pattern=r"extra"))
@Flame7.on(events.CallbackQuery(pattern=r"extra"))
@Flame8.on(events.CallbackQuery(pattern=r"extra"))
@Flame9.on(events.CallbackQuery(pattern=r"extra"))
@Flame10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "Noob !! Make Your Own ғʟᴀᴍᴇ Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)

