# telegram-repeater-bot

## Bootstrap

```bash
./install
```

## Usage

Run locally

```bash
# activate virtualenv
./venv/bin/activate
TELEGRAM_APITOKEN=<TOKEN> python3 repeater.py
```

Run as container

```bash
TELEGRAM_APITOKEN=<TOKEN> docker-compose up -d --force-recreate --build
```

The bot will repeat messages 3 times whose length is no greater than 10 and ends with "！"

If you want to use it in a group and receive all messages, don't forget to `/setprivacy` at BotFather.

## Database

SQLite CLI Client

```bash
pip3 install litecli
litecli remote.db
```

Preview tables

```bash
datasette remote.db
```

Publish

```bash
# install prerequisites
npm i -g vercel

# generate config
datasette publish vercel test.db \
  --project=test-sqlite \
  --generate-vercel-json > vercel.json

# deploy with config
datasette publish vercel test.db \
  --project=test-sqlite \
  --vercel-json=vercel.json
```

## References

- [python-telegram-bot](https://docs.python-telegram-bot.org/en/stable/telegram.bot.html#telegram.Bot.send_sticker)
- [litecli](https://github.com/dbcli/litecli)
- [datasette](https://github.com/simonw/datasette)
- [datasette-publish-vercel](https://github.com/simonw/datasette-publish-vercel)
