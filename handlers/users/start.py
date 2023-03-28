from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import get_start_link

import asyncpg
from loader import dp, db
from keyboards.default.default_button import buttons


async def create_link(id: int) -> str:
    return await get_start_link(id)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)

    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    link = await create_link(user.get('telegram_id'))
    await message.answer(f"Xush kelibsiz {user.get('full_name').title()}! \n\nSizni taklif havolangiz: {link}", reply_markup=buttons)

    args = message.get_args()
    if args:
        suggesed_user = await db.select_full_name_by_id(int(args))
        await db.set_invited_user_count(user.get('telegram_id'))
        await message.answer(f"{suggesed_user} tomonidan taklif qilingansiz. {user.get('full_name').title()}!", reply_markup=buttons)
