import os
import logging
import yaml

from telethon import TelegramClient
from telethon.sessions import StringSession


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)

CONFIG = yaml.load(open('config.yml', 'r'), Loader=yaml.SafeLoader)
API_ID = int(os.getenv('API_ID', CONFIG['23337074']))
API_HASH = os.getenv('API_HASH', CONFIG['2e0ea05d6d6bfd6708fa51f54f36baf7'])
DUMP_ID = os.getenv('DUMP_ID', CONFIG['DUMP_ID'])
STRING_SESSION = os.getenv('STRING_SESSION', CONFIG['1BJWap1sBu0bj45Z6VmvsvxCco7pzm1rObd5eKmycMuMzQIuaLkLiTncN1aFTCHoY5EPHqnol1qOE7Z8TYVi87y35NWZOq-948UNj6IGY3XuqLUQ1qAJ3DVbBvkf8kZEy3_YNxbodGSbNId65AAT2G0m98Sw-hchVj6u9ZbWxX8ta1G-oZx8cpc3aRSmKZilfOeh8nKYoOTk9dZLtCNwjPfOiPCiO1_qw_mCjoyfgM7i_Pkxa8lQFVCAIJ44VE3iPSidxRItM9HxU3zsNMDcJH7q2EShsiVFvnVj0ZfPRzgxTnPtuOKO5rPdsciwje8BcKgnWRyxfU3obF2K9NmioddNeA4fSqIY='])

Ubot = TelegramClient(StringSession(STRING_SESSION),
                      API_ID,
                      API_HASH,
                      auto_reconnect=False,
                      lang_code='en')
