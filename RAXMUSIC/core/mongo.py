from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("𝙋𝙡𝙯 𝙒𝙖𝙞𝙩 𝙬𝙚 𝙖𝙧𝙚 𝘾𝙤𝙣𝙣𝙚𝙘𝙩𝙞𝙣𝙜 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙈𝙤𝙣𝙜𝙤 𝘿𝙖𝙩𝙖𝙗𝙖𝙨𝙚...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("𝙃𝙚𝙮𝙖 𝙈𝙤𝙣𝙜𝙤 𝘿𝙖𝙩𝙖𝙗𝙖𝙨𝙚 𝘾𝙤𝙣𝙣𝙚𝙘𝙩𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮.")
except:
    LOGGER(__name__).error("𝙊𝙥𝙥𝙨! 𝙁𝙖𝙞𝙡𝙚𝙙 𝙩𝙤 𝙘𝙤𝙣𝙣𝙚𝙘𝙩 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙈𝙤𝙣𝙜𝙤 𝘿𝙖𝙩𝙖𝙗𝙖𝙨𝙚.")
    exit()
