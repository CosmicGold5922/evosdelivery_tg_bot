from aiogram import executor
from loader import dp

from handlers import start, user, cart



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)