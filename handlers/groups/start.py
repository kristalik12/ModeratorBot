from loader import dp
from filters import IsGroup
from aiogram import types

@dp.message_handler(IsGroup(), commands=['start', 'help'])
async def do_start(message: types.Message):
  await message.reply(f"{message.from_user.first_name} guruhda start bosdingiz!")