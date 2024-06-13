from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from practise_db import db



start_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='🍴 Меню')
        ],
        [
            KeyboardButton(text='🛍 Мои заказы')
        ],
        [
            KeyboardButton(text='✍️ Оставить отзыв'),
            KeyboardButton(text='⚙️ Настройки')
        ]
    ]
)


menu_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='🗺 Мои адреса')
        ],
        [
            KeyboardButton(text='📍 Отправить геолокацию', request_location=True),
            KeyboardButton(text='⬅️ Назад')
        ]
    ]
)


def get_all_categories_kb(korzina):
    result = db.get_all_categories()
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    if korzina:
        menu.add(
            KeyboardButton(text='📥 Корзина')
    )
    for i in result:
        buttons.append(
            KeyboardButton(text=i[0])
        )
    menu.add(*buttons)
    menu.add(
        KeyboardButton(text='⬅️ Назад')
    )
    
    return menu


def get_all_products_kb(category_name, korzina):
    result = db.get_all_products(category_name)
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    if korzina:
        menu.add(
            KeyboardButton(text='📥 Корзина')
    )
    for i in result:
        buttons.append(
            KeyboardButton(text=i[0])
        )
    menu.add(*buttons)
    menu.add(
        KeyboardButton(text='⬅️ Назад')
    )
    
    return menu


def get_all_locations_kb(telegram_id):
    result = db.get_all_locations(telegram_id)
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    
    for i in result:
        buttons.append(
            KeyboardButton(text=i[0])
        )
    menu.add(*buttons)
    menu.add(
        KeyboardButton(text='⬅️ Назад')
    )
    
    return menu


def get_product_kb():
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    menu.add(
        KeyboardButton(text='📥 Корзина'),
        KeyboardButton(text='⬅️ Назад')
    )
    return menu