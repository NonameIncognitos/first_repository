from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = '6654614422:AAG8nK3ULsuOZlanJ33DTiOJ4E_Ggto_cEM'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def process_start_command(message:Message):
    await message.answer("Првивет\nМеня зовут RinoBot!\nНапиши что-нибудь")

@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )

@dp.message()
async def send_echo(message:Message):
    await message.reply(text=message.text)


if __name__ == "__main__":
    dp.run_polling(bot)

