from aiogram.dispatcher.filters.state import StatesGroup, State

class Class_states(StatesGroup):
    location = State()
    sub_location = State()
    selection1 = State()
    selection2 = State()
    product = State()
    korzina = State()