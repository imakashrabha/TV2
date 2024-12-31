import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7869629794:AAHETg2PO2jruM9rxkXZbvh-AwyoM-DIgOI")
APP_ID = int(os.environ.get("APP_ID", "27705761"))
API_HASH = os.environ.get("API_HASH", "822cb334ca4527a134aae97f9fe44fd6")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002397556354"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6987158459"))
PORT = os.environ.get("PORT", "8081")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://akashrabha2005:781120@cluster0.pv6yd2f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "codeflix_bots")

#Shortner (token system) 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "inshorturl.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "2f6906acdb3b908fdf074f37a47a633a0771343a")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/HowTooOpenLink/7") 

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002201654960"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}, 𝖳𝗁𝖺𝗇𝗄𝗌 𝖿𝗈𝗋 𝗎𝗌𝗂𝗇𝗀 𝗆𝖾. 𝖫𝗈𝗏𝖾 𝖬𝗈𝗏𝗂𝖾𝗌 & 𝖲𝖾𝗋𝗂𝖾𝗌? 𝖨'𝗆 𝗆𝖺𝖽𝖾 𝗍𝗈 𝗁𝖾𝗅𝗉 𝗐𝖺𝗍𝖼𝗁 𝗐𝗁𝖺𝗍 𝗒𝗈𝗎'𝗋𝖾 𝗅𝗈𝗈𝗄𝗂𝗇𝗀 𝖿𝗈𝗋.\n𝖢𝗁𝖾𝖼𝗄 𝗈𝗎𝗍 𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅𝗌 𝖻𝖾𝗅𝗈𝗐 𝖿𝗈𝗋 𝗆𝗈𝗋𝖾!👇.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6987158459").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b><a href='https://t.me/+yft5ysRDW4BiOTc9'>𝖢𝖮𝖬𝖬𝖴𝖭𝖨𝖳𝖸 💀</a></b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>𝖸𝗈𝗎'𝗋𝖾 𝗇𝗈𝗍 𝖺𝖽𝗆𝗂𝗇</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(6987158459)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
