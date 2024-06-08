# from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton,ReplyKeyboardMarkup
#
# school = [
#     [types.KeyboardButton(text="PDP SCHOOL"), types.KeyboardButton(text="PDP ACADEMY")],
#     [types.KeyboardButton(text="PDP UNIVERSITY")],
#
# ]
#
# wenKey = types.ReplyKeyboardMarkup(keyboard=school, resize_keyboard=True)
#
# catalog = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='log in', callback_data='a'),
#      InlineKeyboardButton(text='register ', callback_data='b')],
# ])
# a = [
#     [types.KeyboardButton(text="location",request_location=True)]
# ]
# b = types.ReplyKeyboardMarkup(keyboard=a, resize_keyboard=True)
#

kb = [
    [KeyboardButton(text="Register")],
    [KeyboardButton(text="Ariza topshirish.")]
]

keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Choose Button")

kv=[
    [KeyboardButton(text="Login")]
]
keyword=ReplyKeyboardMarkup(keyboard=kv,resize_keyboard=True, input_field_placeholder="click login")

bttn=[
    [KeyboardButton(text="Arizani tekshirish")]
]
btn=ReplyKeyboardMarkup(keyboard=bttn,resize_keyboard=True, input_field_placeholder="enter")

print("")