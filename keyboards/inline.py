

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



# inline_keyboard_button --обьект
#inline_keyboard_markup -- конструктор


#это магазик
shop_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="cs.money",url="https://cs.money/ru/market/buy/")],
        [InlineKeyboardButton(text="lis-skins",url="https://lis-skins.com/ru/market/")],
        [InlineKeyboardButton(text="помощь", callback_data="show_help")]
    ]
)

#это ножи 1 страница
menu_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Bowie Knife (Нож Боуи)", url="https://wiki.cs.money/weapons/bowie-knife/doppler-sapphire")],
         [InlineKeyboardButton(text="M9 Bayonet (Штык-нож М9)", url="https://wiki.cs.money/weapons/m9-bayonet/gamma-doppler-emerald")],
        [InlineKeyboardButton(text="Butterfly Knife (Нож-бабочка)", url="https://wiki.cs.money/weapons/butterfly-knife/doppler-sapphire")],
        [InlineKeyboardButton(text="Bayonet (Штык-нож)", url="https://wiki.cs.money/weapons/bayonet/doppler-ruby")],

    [InlineKeyboardButton(text="👈", callback_data="prev"),
    InlineKeyboardButton(text="👉", callback_data="next")]

    ]
)
#это ножи 2 страница
second_menu_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Shadow Daggers (Тычковые ножи)",url="https://wiki.cs.money/weapons/shadow-daggers/doppler-phase-2")],
        [InlineKeyboardButton(text="Falchion Knife (Фальшион) ", url="https://wiki.cs.money/weapons/falchion-knife/doppler-black-pearl")],
        [InlineKeyboardButton(text="Gut Knife (Нож с лезвием-крюком)", url="https://wiki.cs.money/weapons/gut-knife/doppler-ruby")],
        [InlineKeyboardButton(text="Flip Knife (Складной нож)", url="https://wiki.cs.money/weapons/flip-knife/doppler-black-pearl")],


        [InlineKeyboardButton(text="👈", callback_data="prev"),
        InlineKeyboardButton(text="👉", callback_data="next")]
    ]
)




#это сеты по цене 1 страница
price_kb=InlineKeyboardMarkup(

    inline_keyboard=[
        [InlineKeyboardButton(text="меньше 10 тыс", callback_data="show_unluck")],
        [InlineKeyboardButton(text="до 10 тыс", url="https://rutube.ru/video/8843d3340769be1439cd1df9fda4a696/")],
        [InlineKeyboardButton(text="до 30 тыс", url="https://www.youtube.com/watch?v=slf9CujCyCA")],

        [InlineKeyboardButton(text="⬅️", callback_data="pred"),
        InlineKeyboardButton(text="➡️", callback_data="nexty")]
    ]
)
#это сеты по цене 2 страница
second_price_kb=InlineKeyboardMarkup(

    inline_keyboard=[
        [InlineKeyboardButton(text="до 50 тыс", url="https://www.youtube.com/watch?v=V6ZMIHm_YWI")],
        [InlineKeyboardButton(text="до 100 тыс", url="https://www.youtube.com/watch?app=desktop&v=FublvClqev8")],
        [InlineKeyboardButton(text="до 500 тыс", url="https://www.youtube.com/watch?v=CsOAU-j39wE")],

        [InlineKeyboardButton(text="⬅️", callback_data="pred"),
         InlineKeyboardButton(text="➡️", callback_data="nexty")]
    ]
)

