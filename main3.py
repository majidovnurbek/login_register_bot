import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, user

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import Token
from button import *

Channel_id = -1002114845403


class Form(StatesGroup):
    name = State()
    username = State()
    password = State()
    finish = State()


DataUser = {
    'username': '',
    "password": "",
}

dp = Dispatcher()
TOKEN = Token


class Login(StatesGroup):
    username = State()
    password = State()
    finish = State()


class User_p(StatesGroup):
    username = State()
    passwordlar = State()
    child = State()
    sinf = State()  # noqa
    finish = State()


class Pupil(StatesGroup):
    name = State()
    child = State()
    username = State()
    passwords = State()
    sinf = State()  # noqa
    finish = State()


pupil_group = {
    "username": "",
    "password": "",
    "child": "",
    "sinf": ""  # noqa
}


# class User(StatesGroup):
#     username = State()
#     password = State()
#     child = State()
#     sinf = State()  # noqa
#     finish = State()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Assalomu alekum! {message.from_user.full_name}", reply_markup=keyboard)

    @dp.message()
    async def reg(message: Message, state: FSMContext):
        if message.text == "Register":
            await state.set_state(Form.name)
            await message.answer("Enter name")
        elif message.text == "Login":
            await state.set_state(Login.username)
            await message.answer("enter username:")
        elif message.text == "Ariza topshirish.":
            await state.set_state(Pupil.name)
            await message.answer("enter your name")
        elif message.text == "Arizani tekshirish":
            await state.set_state(User_p.username)
            await message.answer("enter your username")


@dp.message(Form.name)
async def usernames(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.username)
    await message.answer("Enter username")


@dp.message(Form.username)
async def passwords(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.set_state(Form.password)
    await message.answer("Enter password")


@dp.message(Form.password)
async def finish(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(password=message.text)
    await state.set_state(Form.finish)
    data = await state.get_data()
    await state.clear()
    await message.answer(
        "You have successfully",
    )
    name = data.get("name", "Unknown")
    username = data.get("username", "Unknown")
    password = data.get("password", "Unknown")

    matn = f"🧑‍💻 Name: {name}\n⚡️ Username: {username}\n🔐 Password: {password}"
    await message.answer(text=matn, reply_markup=keyword)
    await bot.send_message(chat_id=Channel_id, text=matn)
    DataUser["username"] = username
    DataUser["password"] = password


###########################################Login####################################################################################################################

@dp.message(Login.username)
async def login(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.set_state(Login.password)
    await message.answer("enter password:")


@dp.message(Login.password)
async def finish(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    await state.set_state(Login.finish)
    userdata = await state.get_data()
    await state.clear()
    username = userdata.get("username", "Unknown")
    password = userdata.get("password", "Unknown")
    if username == DataUser["username"] and password == DataUser["password"]:
        await message.answer("You have successfully logged✅")
    else:
        await message.answer("Invalid username or password‼️")


###############################################pupil###########################################################################################################
@dp.message(Pupil.name)
async def pupils(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Pupil.child)
    await message.answer("enter your child's full name.")


@dp.message(Pupil.child)
async def pupil_names(message: Message, state: FSMContext):
    await state.update_data(child=message.text)
    await state.set_state(Pupil.username)
    await message.answer("enter your username")


@dp.message(Pupil.username)
async def pupil_usernames(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.set_state(Pupil.passwords)
    await message.answer("enter your password")


@dp.message(Pupil.passwords)
async def pupil_passwords(message: Message, state: FSMContext):
    await state.update_data(passwords=message.text)
    await state.set_state(Pupil.sinf)
    await message.answer("enter child's class")


@dp.message(Pupil.sinf)
async def pupil_finishs(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(sinf=message.text)
    await state.set_state(Pupil.finish)
    datas = await state.get_data()
    await state.clear()
    await message.answer("arizangiz qabul qilindi")

    pupil_name = datas.get("name", "Unknown")
    pupil_child = datas.get("child", "Unknown")
    pupil_username = datas.get("username", "Unknown")
    pupil_password = datas.get("passwords", "Unknown")
    pupil_sinf = datas.get("sinf", "Unknown")  # noqa

    school = f" your name: {pupil_name}\nyour child's name: {pupil_child}\nyour username: {pupil_username}\nyour password: {pupil_password}\nyour child's sinf: {pupil_sinf}"
    await bot.send_message(chat_id=Channel_id, text=school)
    await message.answer(f"{school}", reply_markup=btn)
    ###################################################ariza tekshish###################################################################################
    pupil_group["username"] = pupil_username
    pupil_group["password"] = pupil_password
    pupil_group["child"] = pupil_child
    pupil_group["sinf"] = pupil_sinf


@dp.message(User_p.username)
async def User(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.set_state(User_p.passwordlar)
    await message.answer("enter password:")


@dp.message(User_p.passwordlar)
async def Password(message: Message, state: FSMContext):
    await state.update_data(passwordlar=message.text)
    await state.set_state(User_p.child)
    await message.answer("enter your child's full name")


@dp.message(User_p.child)
async def child(message: Message, state: FSMContext):
    await state.update_data(child=message.text)
    await state.set_state(User_p.sinf)
    await message.answer("enter your child's class")


@dp.message(User_p.sinf)
async def Sinf(message: Message, state: FSMContext):
    await state.update_data(sinf=message.text)
    await state.set_state(User_p.finish)
    pupil_data = await state.get_data()
    await state.clear()
    username = pupil_data.get("username", "Unknown")
    password = pupil_data.get("passwordlar", "Unknown")
    child = pupil_data.get("child", "Unknown")
    sinf = pupil_data.get("sinf", "Unknown")
    print(username, password, child, sinf)

    if username == pupil_group["username"] and password == pupil_group["password"] and child == pupil_group[
        "child"] and sinf == pupil_group["sinf"]:
        await message.answer("sizning farsandingiz haqiqatan PDP SCHOOLda o'qiydi✅")
    else:
        await message.answer("bunaqa o'quvchi mavjud emas‼️")


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

import phonenumbers
from phonenumbers import geocoder
phone_number = phonenumbers.parse("+998939255504")
print(geocoder.description_for_number(phone_number,"eng"))
print()