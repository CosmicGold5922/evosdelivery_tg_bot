import logging
from aiogram import Bot, Dispatcher
from database.db_sqlite import Database
from aiogram.contrib.fsm_storage.memory import MemoryStorage



API_TOKEN = "6706763747:AAFxBMWFQF2PizT1JqHe3NJyZOesIAH5_og"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database(path_to_db="pidr_az.sqlite3")