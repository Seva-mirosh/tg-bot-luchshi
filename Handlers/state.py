import sqlite3


from aiogram.fsm.state import State,StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import Router


state_router = Router()


class Form(StatesGroup):
    name= State()
    skin = State()
    cash= State()
    rare = State()
    like_bots = State()




@state_router.message(Command("form"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("как тебя зовут")
    await state.set_state(Form.name)



@state_router.message(Form.name)
async def process_name(message:Message,state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text="на какое оружее хочешь скин'по английски'")
    await state.set_state(Form.skin)

@state_router.message(Form.skin)
async def process_name(message:Message,state: FSMContext):
    await state.update_data(skin=message.text)
    await message.answer(text="на какую сумму ты хочешь купить скин'от 1000 до 50000'")
    await state.set_state(Form.cash)




@state_router.message(Form.cash)
async def process_skin(message: Message, state: FSMContext):
    await state.update_data(cash=message.text)
    await state.set_state(Form.like_bots)
    data=await  state.get_data()
    add_user(
    name=data['name'],
    skin=data['skin'],
    cash=data['cash']
    )
    await state.clear()
    await message.reply(
        text="cool",
        reply_markup=ReplyKeyboardRemove())

conn= sqlite3.connect("users.db")
cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS weapons  (
    id INTEGER PRiMARY KEY AUTOINCREMENT,
    name TEXT,
    skin TEXT,
    cash INTEGER
    )
''')
conn.commit()

def add_user(name, skin,cash):
    cursor.execute('''
    INSERT INTO weapons (name,skin,cash)
    VALUES(?,?,?)
    ON CONFLICT(id) DO UPDATE SET
    name=excluded.name,
    skin=excluded.skin,
    cash=excluded.cash
    ''', (name,skin,cash))
    conn.commit()
def show_table():
    res=cursor.execute('''
    SELECT*FROM weapons
    ''')
    return res.fetchall()
print(show_table())


# def insert_photo():
#     a = cursor.execute('''
#     INSERT INTO users(skin,cash)
#     VALUES
#         ( )  ''')
#     return a.fetchall()
# print(insert_photo())


async def get_deagle(message:Message,skin,cash):
    cursor.execute('''
    SELECT * FROM weapons 
                       WHERE skin = ? AND cash = ?
    ''', (skin,cash))










