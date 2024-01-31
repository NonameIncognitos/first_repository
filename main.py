import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message, ContentType, ChatMemberUpdated
from aiogram.filters import CommandStart, Command, ChatMemberUpdatedFilter, KICKED

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_kick_command(event: ChatMemberUpdated):
    print(f'user {event.from_user.id} is kicked bot')

@dp.message(Command(commands=['start']))
async def process_start_command(event: ChatMemberUpdated):
    print(f'user {event.from_user.id} retry')

if __name__ == "__main__":
    dp.run_polling(bot)