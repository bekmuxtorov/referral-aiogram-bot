from aiogram import types
from .start import create_link

from loader import dp, db


# Echo bot
@dp.message_handler(text='📊 Statistika', state=None)
async def bot_echo(message: types.Message):
    results = await db.select_all_invited_user_count()
    msg = 'Statistika:\n\n'
    for result in results:
        msg += f"{result['full_name']} - {result['invited_user_count']} ta\n"
    await message.answer(msg)

@dp.message_handler(text='📝 Referal', state=None)
async def bot_echo(message: types.Message):
    user = await db.select_user(telegram_id=message.from_user.id)
    link = await create_link(user.get('telegram_id'))
    await message.answer(f"Sizni taklif havolangiz: {link}")