# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "21834860")
API_HASH = os.getenv("API_HASH", "e4acef545ba34ee3fa5c511b38644647")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8074423386:AAEmjfvRB8REY9NTeZskZYzI-rvjW0pWWH8")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://divyanshshukla5375_db_user:1kZ2dsVTktdMljpr@cluster0.lo5qk5v.mongodb.net/?appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("8056097370", "").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "savefromrestricted")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1003236631193")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1003236631193")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "f30ff344ba2607502a84e51e8afdc437") # for session encryption
IV_KEY = os.getenv("IV_KEY", "376cd9947c46") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "10"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "5000000"))
JOIN_LINK = os.getenv("JOIN_LINK", "https://t.me/savefromrestricted") # this link for start command message
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/savefromrestricted")





