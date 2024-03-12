from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram import Router, F
from keyboards import keyboards
from handbook import handbook
from logic import random_box, send_cat

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=handbook['/start'],
        reply_markup=keyboards.keyboard_buttons,
    )


@router.message(F.text == '/help')
async def process_help_command(message: Message):
    await message.answer(
        text=handbook['/help']
    )


@router.message(F.text == '/info')
async def process_info_command(message: Message):
    await message.answer(
        text=handbook['/info']
    )


@router.message(F.text == '/contacts')
async def process_contacts_command(message: Message):
    await message.answer(
        text=handbook['/contacts'],
        reply_markup=keyboards.keyboard_contacts
    )


@router.message(F.text == handbook['button_cancel'])
async def process_press_button_cancel(message: Message):
    await message.answer(
        text=handbook['press_button_cancel'],
    )


@router.message(F.text == handbook['button_play'])
async def process_press_button_play(message: Message):
    await message.answer(
        text=handbook['text_for_start_game_1'],
        reply_markup=ReplyKeyboardRemove(),
    )
    await message.answer(
        text=handbook['text_for_start_game_2'],
        reply_markup=keyboards.keyboard_game
    )


@router.callback_query(F.data.in_(['press_box_1', 'press_box_2', 'press_box_3', 'press_box_4', 'press_box_5']))
async def user_lost(callback: CallbackQuery):
    box = random_box()
    if callback.data == box:
        await callback.answer(
            text=handbook['user_won'],
            show_alert=True
        )
        await callback.message.answer(text='В этой коробке был котик!')
        await callback.message.answer_photo(send_cat())
    else:
        await callback.answer(
            text=handbook['user_lost'],
            show_alert=True
        )
    await callback.message.answer(
            text=handbook['play_again'],
            reply_markup=keyboards.keyboard_buttons
    )
    await callback.message.delete()


@router.callback_query(F.data == 'button_yes_pressed')
async def process_button_yes_pressed(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        text=handbook['text_for_start_game_2'],
        reply_markup=keyboards.keyboard_game
    )


# @router.callback_query(F.data == 'button_no_pressed')
# async def process_button_no_pressed(callback: CallbackQuery):
#     await
