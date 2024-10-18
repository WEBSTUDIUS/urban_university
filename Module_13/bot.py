from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

apiToken = '7505009653:AAHVLZL2tm60KPjdjhfh6jB8dZJlSd6qjYhCLJsgI'

# Создание экземпляра бота и диспетчера
bot = Bot(token=apiToken)
dp = Dispatcher(storage=MemoryStorage())


@dp.message()
async def messages(message):
    if message.text == '/start':
        print('Hello. I am a health helper bot')
        await message.answer('Hello. I am a health helper bot')
    elif message.text == '/help':
        await message.answer('Type /start to start conversation.')
    else:
        print('Type /start to start conversation')
        await message.answer('I cant recognize your command. Try /help.')

async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
