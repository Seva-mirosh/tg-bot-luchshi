from aiogram import Router,F
from aiogram.types import CallbackQuery

callback_router = Router()

#если нужна помощь
@callback_router.callback_query(F.data=="show_help")
async def send_help(callback: CallbackQuery):
    await callback.answer("ты нажал на кнопку")
    await callback.message.answer(text="если нужна помощь @mirosh_seva")
#меньше 10 тыс на балике
@callback_router.callback_query(F.data=="show_unluck")
async def send_unluck(callback: CallbackQuery):
    await  callback.answer("ты нажал на кнопку")
    await  callback.message.answer(text="слишком мало,анлаки")