from aiogram.types import Message, InputFile
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from loader import dp, bot
from practise_db import db
from keyboards.default.default_kb import get_product_kb, get_all_categories_kb, get_all_products_kb, get_all_locations_kb, start_kb, menu_kb
from keyboards.inline.inline_kb import get_type_product_kb, get_1_kb, get_korzina_kb
from utils.utils import get_location_name, sofr_user_products
from states.states import Class_states





@dp.message_handler(text='📥 Корзина', state=Class_states.selection1)
async def show_korzina(message: Message, state: FSMContext):
    text, price = sofr_user_products(message.from_user.id)
    await message.answer(f'В корзине: \n{text}\nТовары: {price} сум\nДоставка: 12 000 сум\nИтого: {price + 12000} сум', reply_markup=get_korzina_kb(db.get_all_orders(message.from_user.id)))
    await Class_states.korzina.set()


@dp.message_handler(text='📥 Корзина', state=Class_states.selection2)
async def show_korzina(message: Message, state: FSMContext):
    text, price = sofr_user_products(message.from_user.id)
    await message.answer(f'В корзине: \n{text}\nТовары: {price} сум\nДоставка: 12 000 сум\nИтого: {price + 12000} сум', reply_markup=get_korzina_kb(db.get_all_orders(message.from_user.id)))
    await Class_states.korzina.set()


@dp.message_handler(content_types=['location'], state=Class_states.location)
async def update_location(message: Message, state: FSMContext):
    data = await state.get_data()
    db.add_location(message.from_user.id, message.location.latitude, message.location.longitude, get_location_name(message.location.latitude, message.location.longitude))
    await state.update_data(
        {
            'latitude': message.location.latitude,
            'longitude': message.location.longitude,
            'location': get_location_name(message.location.latitude, message.location.longitude)
        }
    )
    await message.answer("Выберите категорию:", reply_markup=get_all_categories_kb(data.get('korzina')))
    await Class_states.selection2.set()


@dp.message_handler(text=['🗺 Мои адреса'], state=Class_states.location)
async def menu(message: Message, state: FSMContext):
    await message.answer(f'Выберите адрес доставки', reply_markup=get_all_locations_kb(message.from_user.id))
    await Class_states.sub_location.set()


@dp.message_handler(text="⬅️ Назад", state=Class_states.location)
async def go_back(message: Message, state: FSMContext):
    await message.answer(text="Выберите одно из следующих", reply_markup=start_kb)
    await state.finish()


@dp.message_handler(text="⬅️ Назад", state=Class_states.sub_location)
async def go_back(message: Message, state: FSMContext):
    await message.answer(text="Отправьте 📍 геолокацию или выберите адрес доставки", reply_markup=menu_kb)
    await Class_states.location.set()


@dp.message_handler(text="⬅️ Назад", state=Class_states.selection2)
async def go_back(message: Message, state: FSMContext):
    await message.answer(text="Отправьте 📍 геолокацию или выберите адрес доставки", reply_markup=menu_kb)
    await Class_states.location.set()


@dp.message_handler(text="⬅️ Назад", state=Class_states.selection1)
async def go_back(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(text="Выберите категорию.", reply_markup=get_all_categories_kb(data.get('korzina')))
    await Class_states.selection2.set()


@dp.message_handler(text="⬅️ Назад", state=Class_states.product)
async def go_back(message: Message, state: FSMContext):
    data = await state.get_data()
    category = data.get('category', 'Лаваш')
    image = db.get_category_image(category)
    file = InputFile(path_or_bytesio=image[0])
    await message.answer_photo(
        photo=file,
        reply_markup=get_all_products_kb(category, data.get('korzina'))
    )
    await Class_states.selection1.set()



@dp.message_handler(state=Class_states.sub_location)
async def get_all_categories(message: Message, state: FSMContext):
    data = await state.get_data()
    text = message.text
    await state.update_data(
        {'sub_location': text}
    )
    await message.answer('Выберите категорию.', reply_markup=get_all_categories_kb(data.get('korzina')))
    await Class_states.selection2.set()

    
@dp.message_handler(state=Class_states.selection2)
async def get_category_image(message: Message, state: FSMContext):
    data = await state.get_data()
    image = db.get_category_image(message.text)
    result = get_all_products_kb(message.text, data.get('korzina'))
    file = InputFile(path_or_bytesio=image[0])
    if image is None:
        return
    if image is not None:
        await message.answer_photo(
            photo=file,
            reply_markup=result
        )
        await state.update_data(
            {'category': message.text}
        )
        await Class_states.selection1.set()


@dp.message_handler(state=Class_states.selection1)
async def get_product(message: Message, state: FSMContext):
    image = db.get_product_image(message.text)
    result = db.get_product_description(message.text)
    file = InputFile(path_or_bytesio=image[0])
    await message.answer('Выберите одно из следующих', reply_markup=get_product_kb())
    await message.answer_photo(
        photo=file,
        caption=result,
        reply_markup=get_type_product_kb(message.text)
    )
    await state.update_data(
        {   
            'product': message.text,
            'count': 1
        }
    )
    await Class_states.product.set()



@dp.callback_query_handler(text='+', state=Class_states.product)
async def buy_product(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    count = data.get('count', 1)

    count += 1
    
    await call.message.edit_reply_markup(get_1_kb(count))
    await state.update_data(
        {
            'count': count
        }
    )
    await call.answer(text=f'{count} шт.')


@dp.callback_query_handler(text='-', state=Class_states.product)
async def buy_product(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    count = data.get('count', 1)

    if count > 1:
        count -= 1
    else:
        return
    
    await call.message.edit_reply_markup(get_1_kb(count))
    await state.update_data(
        {
            'count': count
        }
    )
    await call.answer(text=f'{count} шт.')


@dp.callback_query_handler(text='back_korzina', state=Class_states.korzina)
async def go_back(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.message.answer(text="Выберите категорию.", reply_markup=get_all_categories_kb(data.get('korzina')))
    await Class_states.selection2.set()


@dp.callback_query_handler(text='clear_korzina', state=Class_states.korzina)
async def clear_korzina(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    db.delete_all_orders((call.from_user.id,))
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.message.answer(text="Выберите категорию.", reply_markup=get_all_categories_kb(data.get('korzina')))
    await state.update_data(
        {'korzina': False}
    )
    await call.message.answer('Выберите категорию.')
    await call.message.answer('Ваша корзина пусто', reply_markup=get_all_categories_kb(data.get('korzina')))
    await Class_states.selection2.set()


@dp.callback_query_handler(state=Class_states.korzina)
async def delete_order(call: CallbackQuery, state: FSMContext):
    text = call.data
    if '.' in text:
        before_dot = text.split('.')[0]
        after_dot = text.split('.')[-1]
    else:
        before_dot = text
        after_dot = None
    db.delete_ordered_product(before_dot, after_dot)
    text, price = sofr_user_products(call.from_user.id)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    data = await state.get_data()
    print(f'fff: {text} and {price}')
    if text == None or price == None:
        await call.message.answer('Ваша корзина пусто', reply_markup=get_all_categories_kb(data.get('korzina')))
        await Class_states.selection2.set()
    else:
        await call.message.answer(f'В корзине: \n{text}\nТовары: {price} сум\nДоставка: 12 000 сум\nИтого: {price + 12000} сум', reply_markup=get_korzina_kb(db.get_all_orders(call.from_user.id)))