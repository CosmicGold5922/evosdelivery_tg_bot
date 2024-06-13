from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from pprint import pprint

from loader import dp, bot
from practise_db import db
from .user import get_category_image
from states.states import Class_states
from keyboards.inline.inline_kb import get_1_kb





@dp.callback_query_handler(text='korzina', state=Class_states.product)
async def add_to_cart(call: CallbackQuery, state=FSMContext):
    data = await state.get_data()
    if data.get('product') == data.get('product_name'):
        db.add_order(call.from_user.id, data.get('product'), data.get('price_product'), data.get('type_product'), data.get('count'), call.message.date, data.get('sub_location'))
    else:
        await state.update_data(
            {'type_product': None}
        )
        await state.update_data(
            {'price_product': db.get_product_price(data.get('product'))[0]}
        )
        data = await state.get_data()
        print(db.get_product_price(data.get('product'))[0])
        db.add_order(call.from_user.id, data.get('product'), data.get('price_product'), data.get('type_product'), data.get('count'), call.message.date, data.get('sub_location'))
    await state.update_data(
        {'korzina': True}
    )
    await Class_states.selection1.set()
    message = await call.message.edit_reply_markup()
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    message.text = data.get('category')
    await get_category_image(message, state)
    data.pop('type_product')
    data.pop('price_product')
    await state.update_data(data)


@dp.callback_query_handler(state=Class_states.product)
async def mahsulot_callback_query_handler(call: CallbackQuery, state: FSMContext):
    info = call.data.split(',')
    await state.update_data(
        {
            'product_name': info[0].strip('['),
            'type_product': info[1].strip(),
            'price_product': info[2].strip(']')
        }
    )
    await call.message.edit_reply_markup(get_1_kb())