from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from loader import dp
from keyboards.default.default_kb import start_kb, menu_kb
from practise_db import db
from states.states import Class_states





@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer(f"Выберите одно из следующих", reply_markup=start_kb)
    db.add_user(message.from_user.id, message.from_user.username, message.from_user.language_code, message.date)


@dp.message_handler(text=['🍴 Меню'])
async def menu(message: Message, state: FSMContext):
    await message.answer(f'Отправьте 📍 геолокацию или выберите адрес доставки', reply_markup=menu_kb)
    await Class_states.location.set()