import random

from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.filters import Command
from keyboards.inline import shop_kb, price_kb
from keyboards.inline import menu_kb
from keyboards.inline import second_menu_kb, second_price_kb



command_router = Router()
admin_router = Router


@command_router.message(Command("start"))
async def start_handler(message: Message):
    photo=(
        "https://static.tildacdn.com/tild3465-6637-4364-b965-383235366432/-.png")
    await message.answer_photo(photo=photo, caption="привет я твой бот, постараюсь подобрать скин для тебя\n Напиши /help чтобы начать")

@command_router.message(Command("about"))
async def about_handler(message: Message):
    photo = (
        "https://cdn.eloboost24.eu/media/737935/zF3b5J2WWoMKG7zy.webp"
        )
    await message.answer_photo(photo=photo,caption="найду скин для тебя")


@command_router.message(Command("help"))
async def help_handler(message: Message):
    help_text = (
        "/start - поехали!\n"
        "/about - о чем бот\n"
        "/shop - магазин где ты сможешь купить любой скин\n"
        "/knifes - сможешь увидеть 10 ножей \n"
        "/review - можешь оставить отзыв\n"
        "/price - сетапчик по твоей цене\n"
        "/form - форма для сета\n"
        "если ты хочешь найди себе тиммейта для игры, то обратись к этому боту @searchteam_cs2_bot"


        )
    await message.answer(text=help_text)


#отвечаем на любой хай
@command_router.message(F.text.lower().contains("привет"))
async def say_hi(message: Message):
    await message.reply(text="Привет!\nКак дела?")


#отвечаем на милый текст
@command_router.message(F.text.lower().contains("❤️"))
async def send_cute_message(message:Message):
    cute_text="Спасибо за сердечко"
    await message.answer(text=cute_text)


#отвечаем на стикер
@command_router.message(F.sticker)
async def react_to_message(message:Message):
    await message.answer(text="Классный стикер!")




#отвечаем на фото
@command_router.message(F.photo)
async def react_to_photo(message:Message):
    text_to_photo="Отличное фото!"
    await message.reply(text=text_to_photo)

#отвечаем на реплей
@command_router.message(F.reply_to_message)
async def react_to_reply(message:Message):
    await message.reply(text="я все вижу",parse_mode="HTML")

#отвечаем на пока
@command_router.message(F.text.lower().contains("пока"))
async def react_to_buy(message:Message):
    await message.reply(text="До свидания")


#отвечаем на команду shop
@command_router.message(Command("shop"))
async def shop_info(message: Message):
    photo=(
        "https://ixbt.online/gametech/covers/2023/02/16/nova-filepond-ZLl2bG.png"
    )
    await message.answer_photo(photo=photo,caption="ты вызвал команду /shop\n Тут можешь познокомиться с магазинов где можешь купить скин:",reply_markup=shop_kb)






# картинка ножа
@command_router.message(Command("karambit"))
async def send_photo(message: Message):
    photo = (
        "https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpovbSsLQJf2PLacDBA5ciJlY20kvrxIbrdklRc6ddzhuzI74nxt1i9rBsofT-ld9LDJgVsY1nX-QLtlejqg5bu7Zydm3Q1uSVzsXmOmUe3ghFKauBxxavJdWR7Gog")
    await message.answer_photo(photo=photo,caption="один из примеров скина")





@command_router.message(Command("review"))
async def send_review(message: Message):
    await message.answer_poll(
        question="как тебе мой бот",
        options=["имба","хорошо","нормально"],
        is_anonymous=False
    )


@command_router.message(Command("knifes"))
async def send_knifes(message: Message):
    text="нажав на кнопку ты сможешь рассмотреть ножи"
    await message.answer(text=text,reply_markup=menu_kb)

@command_router.callback_query(F.data.in_(["prev","next"]))
async def knifes_callback(callback:CallbackQuery):
    if callback.data =="next":
        await callback.message.edit_text("нажав на кнопку ты сможешь рассмотреть ножи",reply_markup=second_menu_kb)
    else:
        await callback.message.edit_text("нажав на кнопку ты сможешь рассмотреть ножи", reply_markup=menu_kb)
    await callback.answer()


#сет по твоей цене
@command_router.message(Command("price"))
async def send_builds(message: Message):
    text="сейчас подберем тебе сетап, выбери категорию:"

    await message.answer(text=text,reply_markup=price_kb)

@command_router.callback_query(F.data.in_(["pred","nexty"]))
async def price_callback(callback:CallbackQuery):
    if callback.data =="nexty":
        await callback.message.edit_text("сейчас подберем тебе сетап, выбери категорию:",reply_markup=second_price_kb)
    else:
        await callback.message.edit_text(" сейчас подберем тебе сетап, выбери категорию: ", reply_markup=price_kb)
    await callback.answer()




