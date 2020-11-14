import unicodedata
import sys

punctuations = ''.join(list(chr(i) for i in range(sys.maxunicode)
                            if unicodedata.category(chr(i)).startswith('P')))

SLD = "哦噢喔耶啊哇呀哎哟阿啊呃诶额欸哇呀也耶哟欤呕噢呦嘢吧罢呗啵的价家啦来唻嘞哩咧咯啰喽吗嘛嚜么麽哪呢呐否呵哈不兮般则连罗给噻哉呸了"


def strip_punctuation(s: str):
    return s.strip(punctuations)


def rstrip_sld(s: str):
    return s.rstrip(SLD)


def strip(s: str):
    return s.rstrip(punctuations + SLD).lstrip(punctuations)


last_text = ""
cnt = 0
repeated = False


def repeat(update, context):
    global last_text, repeated, cnt
    if len(update.message.text) > 20:
        # do not flood
        return
    t = strip(update.message.text)
    length = len(t)
    if 1 <= length <= 10 and (update.message.text.endswith("！") or update.message.text.endswith("!")):
        # repeat 3 times with "!"
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=(strip_punctuation(update.message.text) + "！") * 3)
    elif length == 0:
        # just repeat it
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=update.message.text)
    elif update.message.text == last_text and cnt >= 1 and not repeated:
        # repeat as follower
        repeated = True
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=update.message.text)
    else:
        if update.message.text != last_text:
            last_text = update.message.text
            cnt = 1
            repeated = False
        else:
            cnt += 1
