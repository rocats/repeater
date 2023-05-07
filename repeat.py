import unicodedata
import sys
import json

from typing import List
from collections import defaultdict
from urllib.request import urlopen
from telegram import Update
from telegram.ext.callbackcontext import CallbackContext


def load_sticker_library(url: str) -> List[str]:
    data = json.loads(urlopen(url).read().decode("utf-8"))["rows"]
    return [item[2] for item in data]


punctuations = "".join(
    list(
        chr(i)
        for i in range(sys.maxunicode)
        if unicodedata.category(chr(i)).startswith("P")
    )
)
last_text = defaultdict(str)
last_sender = defaultdict(int)
cnt = defaultdict(int)
repeated = defaultdict(bool)

sticker_lib = load_sticker_library(
    "https://repeater-bot-sqlite.vercel.app/remote/stickers.json"
)


def strip_punctuation(s: str):
    return s.strip(punctuations)


def repeat(update: Update, context: CallbackContext):
    global last_text, repeated, cnt
    chat_id = update.effective_chat.id

    print(update.message)

    # --- sticker  --- #
    if update.message.sticker is not None:
        sticker_uid = (
            update.message.sticker.file_unique_id
            if update.message.sticker != None
            else ""
        )

        # repeat target sticker
        if sticker_uid in sticker_lib:
            context.bot.send_sticker(
                chat_id=chat_id,
                sticker=update.message.sticker.file_id,
            )

    # --- message --- #
    if (
        update.message is None
        or update.message.text is None
        or update.message.from_user is None
    ):
        return
    if len(update.message.text) > 50:
        # do not flood
        return
    if update.message.sender_chat is not None:
        # ignore messages sent on behalf of a channel
        return

    t = update.message.text.strip()
    e = update.message.entities
    f = update.message.from_user.id

    # repeat target text
    if "我" in t and "你" in t:
        t = t.replace("你", "他").replace("我", "你")
    elif "我" in t:
        t = t.replace("我", "你")
    if "屌" in t or "嗯" in t or "好的" in t or "好吧" in t:
        repeated[chat_id] = True
        context.bot.send_message(chat_id=chat_id, text=t)
    # repeat 3 times with "!"
    if 1 <= len(update.message.text) <= 30 and (
        update.message.text.endswith("！") or update.message.text.endswith("!")
    ):
        repeated[chat_id] = True
        context.bot.send_message(chat_id=chat_id, text=(strip_punctuation(t) + "！") * 3)
    # repeat 3 times with "～"
    elif 1 <= len(update.message.text) <= 30 and (
        update.message.text.endswith("～") or update.message.text.endswith("~")
    ):
        repeated[chat_id] = True
        context.bot.send_message(chat_id=chat_id, text=((t + " ") * 3))
    # repeat with "..."
    elif 1 <= len(update.message.text) <= 30 and (
        update.message.text.endswith("...") or update.message.text.endswith("。。。")
    ):
        repeated[chat_id] = True
        context.bot.send_message(chat_id=chat_id, text=t)
    # repeat as follower
    elif (
        f != last_sender[chat_id]
        and update.message.text == last_text[chat_id]
        and cnt[chat_id] >= 1
        and not repeated[chat_id]
    ):
        repeated[chat_id] = True
        context.bot.send_message(chat_id=chat_id, text=t, entities=e)
    last_sender[chat_id] = f
    if update.message.text != last_text[chat_id]:
        last_text[chat_id] = update.message.text
        cnt[chat_id] = 1
        repeated[chat_id] = False
    else:
        cnt[chat_id] += 1


def clean_repeat(update: Update):
    chat_id = update.effective_chat.id
    last_text[chat_id] = ""
