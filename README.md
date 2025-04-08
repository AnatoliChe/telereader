# telereader
A primitive script that allows you to read posts in Telegram to which the user has access.

It's simple python script uses telethon library to do as simple telegram client.

- create virtual python enviroment
  python3 -m venv .venv
  source .venv/bin/activate
- install telethon lib
  pip install -r requirements.txt
- get your api_id & api_hash from telegram
  To work with the Telegram API, you need to get your api_id and api_hash. This can be done by registering a new application on the Telegram Core site.
 Go to the site and log in to your Telegram account.
 Click "Create new application".
 Fill in the necessary fields (for example, the name of the application, a short description).
 After creating the application, you will receive your api_id and api_hash. Save them.
- edit teleread.py to change
  api_id & api_hash & group_username
- run the script python3 teleread.py
  script store session information in local file, you can change it with var session_name =
  if it's your first session or your session expires you will be asked about code from your telegram messenger

Script does as simple console telegram client, but you won't have warnings like:
"(c) coping and forwarding is not allowed in this channel."
