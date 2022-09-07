import unicodedata
import sys

from collections import defaultdict


from telegram import Update
from telegram.ext.callbackcontext import CallbackContext


punctuations = ''.join(list(chr(i) for i in range(sys.maxunicode)
                            if unicodedata.category(chr(i)).startswith('P')))
last_text = defaultdict(str)
last_sender = defaultdict(int)
cnt = defaultdict(int)
repeated = defaultdict(bool)

def strip_punctuation(s: str):
    return s.strip(punctuations)

def repeat(update: Update, context: CallbackContext):
    global last_text, repeated, cnt
    if update.message is None or update.message.text is None or update.message.from_user is None:
        return
    if len(update.message.text) > 50:
        # do not flood
        return
    t = update.message.text.strip()
    e = update.message.entities
    f = update.message.from_user.id
    if '我' in t and '你' in t:
      t = t.replace('你', '他').replace('我', '你')
    elif '我' in t:
      t = t.replace('我', '你')
    chat_id = update.effective_chat.id
    if 1 <= len(update.message.text) <= 30 and (update.message.text.endswith("！") or update.message.text.endswith("!")):
        # repeat 3 times with "!"
        repeated[chat_id] = True
        context.bot.send_message(chat_id=chat_id,
                                 text=(strip_punctuation(t) + "！") * 3)
    elif f != last_sender[chat_id] and update.message.text == last_text[chat_id] \
        and cnt[chat_id] >= 1 and not repeated[chat_id]:
        # repeat as follower
        repeated[chat_id] = True
        context.bot.send_message(chat_id=chat_id,
                                 text=t, entities=e)
    last_sender[chat_id] = f
    if update.message.text != last_text[chat_id]:
        last_text[chat_id] = update.message.text
        cnt[chat_id] = 1
        repeated[chat_id] = False
    else:
        cnt[chat_id] += 1


def clean_repeat(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    last_text[chat_id] = ""
