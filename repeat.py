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


def repeat(update, context):
    if len(update.message.text) > 20:
        # do not flood
        return
    length = len(strip(update.message.text))
    if 1 <= length <= 3:
        # repeat 3 times with "!"
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=(strip_punctuation(update.message.text) + "！") * 3)
    elif length == 0:
        # just repeat it
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=update.message.text)
