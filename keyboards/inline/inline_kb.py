from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from practise_db import db



def get_type_product_kb(product_name):
    result = db.get_type(product_name)
    for i in result:
        if i[0] is None:
            menu = InlineKeyboardMarkup(resize_keyboard=True, row_width=3)
            menu.add(
                InlineKeyboardButton(text='-', callback_data='-'),
                InlineKeyboardButton(text='1', callback_data='1'),
                InlineKeyboardButton(text='+', callback_data='+')
            )
            menu.add(
                InlineKeyboardButton(text='📥Добавить в корзину', callback_data='korzina')
            )
    
            return menu
    menu = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    
    for i in result:
        buttons.append(
            InlineKeyboardButton(text=f'{i[0]} {i[1]} сум', callback_data=f'[{product_name}, {i[0]}, {i[1]}]')
        )
    menu.add(*buttons)
    
    return menu


def get_1_kb(count=1):
    menu = InlineKeyboardMarkup(resize_keyboard=True, row_width=3)
    menu.add(
        InlineKeyboardButton(text='-', callback_data='-'),
        InlineKeyboardButton(text=f'{count}', callback_data='count'),
        InlineKeyboardButton(text='+', callback_data='+')
    )
    menu.add(
        InlineKeyboardButton(text='📥Добавить в корзину', callback_data='korzina')
    )
    
    return menu


def get_korzina_kb(all_orders: list, ):
    print(f'{all_orders=}')
    menu = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    menu2 = []
    menu.add(
        InlineKeyboardButton(text='⬅️ Назад', callback_data='back_korzina'),
        InlineKeyboardButton(text='🚖 Оформить заказ', callback_data='order')
    )
    menu.add(
        InlineKeyboardButton(text='🗑 Очистить корзину', callback_data='clear_korzina')
    )
    all_orders = set(all_orders)
    for i in all_orders:
        if i[3] == None:
            menu.add(
                InlineKeyboardButton(text=f'❌{db.get_product_name(i[1])[0]}', callback_data=f'{db.get_product_name(i[1])[0]}')
            )
            print(f'{db.get_product_name(i[1])[0]}')
        else:
            menu.add(
                InlineKeyboardButton(text=f'❌{db.get_product_name(i[1])[0]} {i[3]}', callback_data=f'{db.get_product_name(i[1])[0]}.{i[3]}')
            )
            print(f'{db.get_product_name(i[1])[0]}.{i[3]}')
    return menu