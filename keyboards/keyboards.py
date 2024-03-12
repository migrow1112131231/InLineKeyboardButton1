from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove ,KeyboardButton)
from config import Config, add_config
from handbook import handbook


config = add_config()


# кнопки и клавиатура для КНОПОК
button_play = KeyboardButton(
    text=handbook['button_play']
)
button_cancel = KeyboardButton(
    text=handbook['button_cancel']
)
keyboard_buttons = ReplyKeyboardMarkup(
    keyboard=[[button_play], [button_cancel]],
    resize_keyboard=True,
    input_field_placeholder='Use the buttons'
)



# кнопки и клавитура для /contacts
button_for_contacts_vk = InlineKeyboardButton(
    text=handbook['button_contact_vk'],
    url='https://vk.com/m_boltachev'
)
button_for_contacts_tg = InlineKeyboardButton(
    text=handbook['button_contact_tg'],
    url=f'tg://user?id={config.telegram_bot.admin}'
)
keyboard_contacts = InlineKeyboardMarkup(
    inline_keyboard=[[button_for_contacts_vk],
                     [button_for_contacts_tg]]
)


# кнопки и клавиатура для /start
inline_button_play = InlineKeyboardButton(
    text=handbook['button_play'],
    callback_data='press_button_play'
)
inline_button_cancel = InlineKeyboardButton(
    text=handbook['button_cancel'],
    callback_data='press_button_cancel'
)
keyboard_start = InlineKeyboardMarkup(
    inline_keyboard=[[inline_button_play], [inline_button_cancel]]
)


# кнопки и клавиатура для game
buttons_for_game = {f'button_{q}': InlineKeyboardButton(
    text='📦',
    callback_data=f'press_box_{q}'
) for q in range(1, 6)}
keyboard_game = InlineKeyboardMarkup(
    inline_keyboard=[[buttons_for_game[f'button_{q}']] for q in range(1, 6)]
)


button_yes = InlineKeyboardButton(
    text=handbook['button_yes'],
    callback_data='button_yes_pressed'
)
button_no = InlineKeyboardButton(
    text=handbook['button_no'],
    callback_data='button_no_pressed'
)
keyboard_restart = InlineKeyboardMarkup(
    inline_keyboard=[[button_yes], [button_no]]
)
# выбираем  что будем разрешать импортировать