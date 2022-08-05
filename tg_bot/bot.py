from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

lucido=Client(
    "Auto Approved Bot",
    bot_token = environ["BOT_TOKEN"],
    api_id = int(environ["API_ID"]),
    api_hash = environ["API_HASH"]
)

CHAT_ID = [int(lucido) for lucido in environ.get("CHAT_ID", None).split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()
lucido.on_chat_join_request(filters.group & filters.chat(CHAT_ID) if CHAT_ID else filters.group)
async def autoapprove(client: lucido, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} approved") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))
    #   print("Welcome....")

print("yuss iam alive")
lucido.run()
