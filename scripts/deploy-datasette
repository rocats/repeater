#!/bin/bash

datasette publish vercel remote.db \
  --project=repeater-bot-sqlite \
  --metadata metadata.json \
  --install datasette-auth-tokens \
  --install datasette-insert \
  --extra-options "--create --host 0.0.0.0 --cors" \
  --vercel-json=vercel.json

