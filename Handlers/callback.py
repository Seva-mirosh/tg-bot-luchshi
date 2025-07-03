from aiogram import Router,F
from aiogram.types import CallbackQuery, InputMediaPhoto

callback_router = Router()

#если нужна помощь
@callback_router.callback_query(F.data=="show_help")
async def send_help(callback: CallbackQuery):
    await callback.answer("подождите")
    await callback.message.answer(text="если нужна помощь @mirosh_seva")
#меньше 10 тыс на балике
@callback_router.callback_query(F.data=="show_unluck")
async def send_unluck(callback: CallbackQuery):
    await  callback.answer("подождите")
    await  callback.message.answer(text="слишком мало,анлаки")


@callback_router.callback_query(F.data == "knifes_1")
async def start_knifes_1(callback: CallbackQuery):
    # закрываем ожидани -- часики
    await callback.answer("подождите")
    media = InputMediaPhoto(
        media="https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpovbSsLQJfwObaZzRU7dCJlo-cnvLLMrbukWpc5cROjubR5YDwmmukoxIvNmuceN_CKkIgMAzV-lHtw-vpgZfv7pWYnHA3siIl7HfblkGygxwePexvjaCcHQjNU7sJQvdlS3pkbA",
        caption="Нож Боуи — это крупный нож с характерной формой клинка. Нож Боуи универсален и может использоваться как боевой, охотничий или рабочий инструмент."
    )
    await callback.message.edit_media(media=media)

@callback_router.callback_query(F.data == "knifes_2")
async def start_knifes_2(callback: CallbackQuery):

    await callback.answer("подождите")
    media = InputMediaPhoto(
            media="https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpovbSsLQJf3qr3czxb49KzgL-KmsjwPKvBmm5D19V5i_rEobP5gVO8v11kZTr6cdDAIVA5ZA2GqVW3x7281sftvZ_AzXZmv3Mm5H2LlxWw1RhIcKUx0uHVWO7n",
            caption="Штык-нож - это сочетание штыка и ножа, крепящееся к стрелковому оружию (обычно винтовке или автомату) для использования в рукопашном бою, а также могущее использоваться как отдельный нож. "
        )
    await callback.message.edit_media(media=media)

@callback_router.callback_query(F.data == "knifes_3")
async def start_knifes_3(callback: CallbackQuery):

    await callback.answer("подождите")
    media = InputMediaPhoto(
            media="https://assets.lis-skins.com/market_images/98974_b.png",
            caption="Нож бабочка (балисонг) – это раскладной вариант режущего оружия, имеющий две рукояти, одна из которых является опасной, а другая нет."
        )
    await callback.message.edit_media(media=media)



@callback_router.callback_query(F.data == "knifes_4")
async def start_knifes_4(callback: CallbackQuery):

    await callback.answer("подождите")
    media = InputMediaPhoto(
            media="https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpotLu8JAllx8zJfAJR7cymnImZksj5MqnTmm5Y8sB1teXI8oThxlHtrkNoMWyhItDDcFJoaFjW_Vm7yL2-18W6uc6ayHcwuCQntH-Om0SpwUYb_FLG0qs",
            caption="штык-нож — плоский клинок ножевого типа с рукоятью для удержания в руке, приспособлением для примыкания к оружию и ножнами"
        )
    await callback.message.edit_media(media=media)


@callback_router.callback_query(F.data == "knifes_5")
async def start_knifes_4(callback: CallbackQuery):

    await callback.answer("подождите")
    media = InputMediaPhoto(
            media="https://static.wikia.nocookie.net/counterstrike/images/b/b4/Shadow-daggers-stock.png/revision/latest?cb=20150918180157&path-prefix=ru",
            caption="Тычковый нож, также известный как пуш-даггер (push dagger), – это нож с характерной Т-образной рукоятью, где клинок расположен перпендикулярно к ней. Такое расположение позволяет удерживать нож в кулаке, выводя лезвие между пальцами, что обеспечивает эффективный удар в упор. "
        )
    await callback.message.edit_media(media=media)

@callback_router.callback_query(F.data == "knifes_6")
async def start_knifes_4(callback: CallbackQuery):

    await callback.answer("подождите")
    media = InputMediaPhoto(
            media="https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpovbSsLQJf1fLEcjVL49KJlY20heL2KoTcl3lT5MB4kOzFyoD8j1yg5RZrYjr6JY-cJgA5Zw2CrlPqxeu8hZK77c7NznA2uiFw4SyOmRfkiRpSLrs48wN4FN8",
            caption="Это нож с изогнутым лезвием, похожим на историческое оружие"
        )
    await callback.message.edit_media(media=media)

@callback_router.callback_query(F.data == "knifes_7")
async def start_knifes_4(callback: CallbackQuery):

    await callback.answer("подождите")
    media = InputMediaPhoto(
            media="https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpovbSsLQJf1ObcTjxP08-3hJCDnuXxDLbQhGld7cxrj-3--YXygED6_BVlZDv3IYLGJAE2aQvX_wW5xLzrhsDqvp7Pynpkv3Ui7XnUzhHmhAYMMLIU9_4nhg",
            caption="Специальный упор на корпусе для защиты руки от соскальзывания и возможность полностью убирать лезвие в ручку обеспечивают безопасность во время работы и транспортировки."
        )
    await callback.message.edit_media(media=media)



@callback_router.callback_query(F.data == "knifes_8")
async def start_knifes_4(callback: CallbackQuery):

    await callback.answer("подождите")
    media = InputMediaPhoto(
            media="https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpovbSsLQJf1f_BYQJD4eOllZCbn_7mNoTcl3lT5MB4kOzFyoD8j1yg5UBuazj3cYKQJwA5ZwnVrla_yLi5hcPp6szPwHZqvnVx5n_Vyhzjgh1SLrs4EHv5ZcQ",
            caption="Складно́й нож — разновидность ножа, клинок которого убирается в рукоять. На современных складных ножах часто стоят приспособления для открывания одной рукой, например шпенёк или отверстие."
        )
    await callback.message.edit_media(media=media)



