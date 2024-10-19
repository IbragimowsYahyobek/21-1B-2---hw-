import asyncio, random
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandStart

from config import token

bot = Bot(token=token)
dp = Dispatcher()
lucky_number = random.choice([1, 2, 3])

@dp.message(CommandStart())
async def start(message:types.Message):
    await message.answer('Угадайте число от 1 до 3')

@dp.message()
async def random_num(message:types.Message):
    user_number = int(message.text)
    if lucky_number == user_number:
        await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg', caption='Ты выиграл!')
    elif lucky_number != user_number:
        await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg', caption='Ты не выиграл!')
    else:
        await message.answer('Ошибка')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")