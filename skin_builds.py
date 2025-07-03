
import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from Handlers.commands import command_router
from Handlers.callback import callback_router
from Handlers.state import state_router
from aiogram.fsm.storage.memory import MemoryStorage
from Handlers.middleware import AntiFloodMiddleware
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher()


dp.include_router(command_router)
dp.include_router(callback_router)
dp.include_router(state_router)
dp.message.middleware(AntiFloodMiddleware())
dp.callback_query.middleware(AntiFloodMiddleware())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
