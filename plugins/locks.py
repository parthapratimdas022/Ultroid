# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}lock <msgs/media/sticker/gif/games/inline/polls/invites/pin/changeinfo>`
    Lock the Used Setting in Used Group.

• `{i}unlock <msgs/media/sticker/gif/games/inline/polls/invites/pin/changeinfo>`
    UNLOCK the Used Setting in Used Group.

"""

from pyUltroid.functions.all import lucks, unlucks
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = False
        what = "messages"
    elif input_str == "media":
        media = False
        what = "media"
    elif input_str == "sticker":
        sticker = False
        what = "stickers"
    elif input_str == "gif":
        gif = False
        what = "GIFs"
    elif input_str == "game":
        gamee = False
        what = "games"
    elif input_str == "inline":
        ainline = False
        what = "inline bots"
    elif input_str == "poll":
        gpoll = False
        what = "polls"
    elif input_str == "invite":
        adduser = False
        what = "invites"
    elif input_str == "pin":
        cpin = False
        what = "pins"
    elif input_str == "info":
        changeinfo = False
        what = "chat info"
    elif input_str == "all":
        msg = False
        media = False
        sticker = False
        gif = False
        gamee = False
        ainline = False
        gpoll = False
        adduser = False
        cpin = False
        changeinfo = False
        what = "everything"
from . import *


@ultroid_cmd(pattern="lock ?(.*)", groups_only=True, admins_only=True)
async def lockho(e):
    mat = e.pattern_match.group(1)
    if not mat:
        return await eod(e, "`What to Lock  ?`")
    try:
        ml = lucks(mat)
    except BaseException:
        return await eod(e, "`Incorrect Input`")
    await ultroid_bot(EditChatDefaultBannedRightsRequest(e.chat_id, ml))
    await eor(e, f"Locked - `{mat}` ! ")


@ultroid_cmd(pattern="unlock ?(.*)", groups_only=True, admins_only=True)
async def unlckho(e):
    mat = e.pattern_match.group(1)
    if not mat:
        return await eod(e, "`What to Lock  ?`")
    try:
        ml = unlucks(mat)
    except BaseException:
        return await eod(e, "`Incorrect Input`")
    await ultroid_bot(EditChatDefaultBannedRightsRequest(e.chat_id, ml))
    await eor(e, f"Unlocked - `{mat}` ! ")
