# repeater

## Usage

```bash
TELEGRAM_APITOKEN=<TOKEN> docker-compose up -d --force-recreate --build
```

The bot will repeat messages 3 times whose length is no greater than 10 and ends with "！"

If you want to use it in a group and receive all messages, don't forget to `/setprivacy` at BotFather.

## References

- [python-telegram-bot](https://docs.python-telegram-bot.org/en/stable/telegram.bot.html#telegram.Bot.send_sticker)
