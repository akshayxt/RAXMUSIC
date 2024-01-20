from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Rax(Client):
    def __init__(self):
        LOGGER(__name__).info(f"𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐁𝐨𝐭...")
        super().__init__(
            name="RAXMUSIC",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} ʙ̳ᴏ̳ᴛ̳ ̳s̳ᴛ̳ᴀ̳ʀ̳ᴛ̳ᴇ̳ᴅ̳:</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "𝐁𝐨𝐭 𝐡𝐚𝐬 𝐟𝐚𝐢𝐥𝐞𝐝 𝐭𝐨 𝐚𝐜𝐜𝐞𝐬𝐬 𝐭𝐡𝐞 𝐥𝐨𝐠 𝐠𝐫𝐨𝐮𝐩/𝐜𝐡𝐚𝐧𝐧𝐞𝐥. 𝐌𝐚𝐤𝐞 𝐬𝐮𝐫𝐞 𝐭𝐡𝐚𝐭 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐚𝐝𝐝𝐞𝐝 𝐲𝐨𝐮𝐫 𝐛𝐨𝐭 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐥𝐨𝐠 𝐠𝐫𝐨𝐮𝐩/𝐜𝐡𝐚𝐧𝐧𝐞𝐥."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"𝗕𝗼𝘁 𝗵𝗮𝘀 𝗳𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗮𝗰𝗰𝗲𝘀𝘀 𝘁𝗵𝗲 𝗹𝗼𝗴 𝗴𝗿𝗼𝘂𝗽/𝗰𝗵𝗮𝗻𝗻𝗲𝗹.\n  Reason : {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "𝙋𝙡𝙚𝙖𝙨𝙚 𝙥𝙧𝙤𝙢𝙤𝙩𝙚 𝙮𝙤𝙪𝙧 𝙗𝙤𝙩 𝙖𝙨 𝙖𝙣 𝙖𝙙𝙢𝙞𝙣 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙡𝙤𝙜 𝙜𝙧𝙤𝙪𝙥/𝙘𝙝𝙖𝙣𝙣𝙚𝙡."
            )
            exit()
        LOGGER(__name__).info(f"𝙈𝙪𝙨𝙞𝙘 𝘽𝙤𝙩 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝙖𝙨 {self.name}")

    async def stop(self):
        await super().stop()
