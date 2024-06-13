import requests

from loader import db





emoji_mapping = {
    '0': '\u0030\u20E3',  # 0️⃣
    '1': '\u0031\u20E3',  # 1️⃣
    '2': '\u0032\u20E3',  # 2️⃣
    '3': '\u0033\u20E3',  # 3️⃣
    '4': '\u0034\u20E3',  # 4️⃣
    '5': '\u0035\u20E3',  # 5️⃣
    '6': '\u0036\u20E3',  # 6️⃣
    '7': '\u0037\u20E3',  # 7️⃣
    '8': '\u0038\u20E3',  # 8️⃣
    '9': '\u0039\u20E3',   # 9️⃣
    '10': '\u0038\u20E3',  # 1️⃣0️⃣
    '11': '\u0038\u20E3',  # 1️⃣1️⃣
    '12': '\u0038\u20E3',  # 1️⃣2️⃣
    '13': '\u0038\u20E3',  # 1️⃣3️⃣
    '14': '\u0038\u20E3',  # 1️⃣4️⃣
    '15': '\u0038\u20E3',  # 1️⃣5️⃣
    '16': '\u0038\u20E3',  # 1️⃣6️⃣
    '17': '\u0038\u20E3',  # 1️⃣7️⃣
    '18': '\u0038\u20E3',  # 1️⃣8️⃣
    '19': '\u0038\u20E3',  # 1️⃣9️⃣
    '20': '\u0038\u20E3'  # 2️⃣0️⃣
}


def get_location_name(latitude, longitude):
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        location_name = data.get('display_name', None)
        return location_name
    except requests.RequestException as e:
        print(f"Error retrieving location name: {e}")
        return None
    

def sofr_user_products(telegram_id):
    data = db.get_all_orders(telegram_id)
    text = ''
    price = db.get_all_orders_price(telegram_id)
    for user_id, product_id, product_price, type_product, quantity in data:
        type_pr = db.get_order_type_product(product_id, product_price)[0]
        print(type_pr)
        if type_pr is not None:
            text += f'{emoji_mapping.get(str(quantity))} ✖️ {db.get_product_name(product_id)[-1]} {type_pr}\n'
        elif type_pr == None:
            text += f'{emoji_mapping.get(str(quantity))} ✖️ {db.get_product_name(product_id)[-1]}\n'
            product_price = db.get_ordered_product_price2(product_id)[0]
    return text, price