from telethon import TelegramClient, events

api_id = api_id yoziladi my.telegram.org sitedan olinadi
api_hash = "api_hash yoziladi my.telegram.org sitedan olinadi"
bot_token = 'bot tokeni'
channel_username = 'https://t.me/kanaluseri'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    additional_text = """
------------------
Kanal: @satomoru_official
"""
    await client.edit_message(event.chat_id, event.message.id, 
                               f"{event.message.text}{additional_text}")

print("Bot ishga tushdi...")
client.run_until_disconnected()
