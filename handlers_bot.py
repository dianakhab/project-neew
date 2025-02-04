from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: MemoryStorage):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()')

@start_router.message(Command('start_2'))
async def cmd_start_2(message: MemoryStorage):
    await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')

@start_router.message(F.text == '/start_3')
async def cmd_start_3(message: MemoryStorage):
    await message.answer('Запуск сообщения по команде /start_3 используя магический фильтр F.text!')
