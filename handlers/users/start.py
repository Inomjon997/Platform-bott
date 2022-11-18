from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.MainState import StMain
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from keyboards.inline.keyb import keyb1

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if str(message.from_user.id)==ADMINS[0]:
        await message.answer('Salom hurmatli admin!\n')
    else:
        await StMain.nameEmail.set()

        await message.answer(f"Salom, {message.from_user.full_name} !"
                             f" Botga hush kelibsiz!"
                             f" Iltimos ismingizni va nomerni kiriting(masalan:Dilshod +998YYXXXXXXX):")

@dp.message_handler(state=StMain.nameEmail)
async def process_name(message: types.Message, state: FSMContext):
    global datass
    """
    Process email
    """
    async with state.proxy() as data:
        await dp.bot.send_message(ADMINS[0], f"Yangi foydalanuvchi:{message.text}")
    await state.finish()
    await message.reply("Rahmat siz muaffaqiyatli ro`yhatdan o'tdingiz! Tugmani bosing👇",reply_markup=keyb1)

# @dp.message_handler(commands='regdata')
# async def regdata_push(message: types.Message):
#     global datass
#     if str(message.from_user.id)==ADMINS[0]:
#         await message.answer(datass)
#     else:
#         await message.answer('Siz admin emassiz!')
#
# @dp.message_handler(commands='clrdata')
# async def clrdata_push(message: types.Message):
#     global datass
#     if str(message.from_user.id)==ADMINS[0]:
#         dancl.write('')
#         await message.answer(f'Malumotlar tozalandi!\n'
#                              f'Malumotlar:{datass}')
#     else:
#         await message.answer('Siz admin emassiz!')