import unicodedata
import sys

from collections import defaultdict

from telegram import Update
from telegram.ext.callbackcontext import CallbackContext


punctuations = ''.join(list(chr(i) for i in range(sys.maxunicode)
                            if unicodedata.category(chr(i)).startswith('P')))

SLD = "哦噢喔耶啊哇呀哎哟阿啊呃诶额欸哇呀也耶哟欤呕噢呦嘢吧罢呗啵的价家啦来唻嘞哩咧咯啰喽吗嘛嚜么麽哪呢呐否呵哈不兮般则连罗给噻哉呸了"


def strip_punctuation(s: str):
    return s.strip(punctuations)


def rstrip_sld(s: str):
    return s.rstrip(SLD)


def strip(s: str):
    return s.rstrip(punctuations + SLD).lstrip(punctuations)


last_text = defaultdict(str)
cnt = defaultdict(int)
repeated = defaultdict(bool)


def repeat(update: Update, context: CallbackContext):
    global last_text, repeated, cnt
    if update.message is None:
        return
    if len(update.message.text) > 50:
        # do not flood
        return
    t = strip(update.message.text)
    if '我' in t and '你' in t:
      t = t.replace('你', '他')
      t = t.replace('我', '你')
    elif '我' in t:
      t = t.replace('我', '你')
    length = len(t)
    chat_id = update.effective_chat.id
    if 1 <= length <= 30 and (update.message.text.endswith("！") or update.message.text.endswith("!")):
        # repeat 3 times with "!"
        repeated[chat_id] = True
        context.bot.send_message(chat_id=chat_id,
                                 text=(strip_punctuation(t) + "！") * 3)
#     elif length == 0:
#         # just repeat it
#         repeated[chat_id] = True
#         context.bot.send_message(chat_id=chat_id,
#                                  text=update.message.text)
    elif update.message.text == last_text[chat_id] and cnt[chat_id] >= 1 and not repeated[chat_id]:
        # repeat as follower
        repeated[chat_id] = True
        context.bot.send_message(chat_id=chat_id,
                                 text=t)
    if update.message.text != last_text[chat_id]:
        last_text[chat_id] = update.message.text
        cnt[chat_id] = 1
        repeated[chat_id] = False
    else:
        cnt[chat_id] += 1
