import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TEST, TelegramAPIServer
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, WebAppInfo, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.web_app import safe_parse_webapp_init_data
from aiohttp.web_request import Request
from aiohttp.web_response import json_response

API_TOKEN = '5000479336:AAHA21TniMG8_7_ImWP3y6l31Qr1bPsn0EQ'

dp = Dispatcher()


async def check_data_handler(request: Request):
    bot: Bot = request.app["bot"]

    data = await request.post()  # application/x-www-form-urlencoded
    try:
        data = safe_parse_webapp_init_data(token=bot.token, init_data=data["_auth"])
    except ValueError:
        return json_response({"ok": False, "err": "Unauthorized"}, status=401)
    return json_response({"ok": True, "data": data.user.dict()})


# starting dialog calendar with year 1989 & month
@dp.message(CommandStart())
async def dialog_cal_handler_month(message: Message):
    btn = InlineKeyboardButton(
        text="Select",
        web_app=WebAppInfo(url='http://127.0.0.1:63342/aiogram3_calendar/test.html?_ijt=ukdt9c3sk1d4gcrsanmk6m465o')
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[btn]])

    # btn = KeyboardButton(
    #     text="Select",
    #     web_app=WebAppInfo(url='http://127.0.0.1:63342/aiogram3_calendar/test.html?_ijt=fk5bk9r42o74ku6k0nainbl56b')
    # )
    # kb = ReplyKeyboardMarkup(keyboard=[[btn]])
    await message.answer("Select date", reply_markup=kb)


@dp.message()
async def dialog_cal_handler_month(message: Message):
    await message.answer(f"Selected date {message.web_app_data.data}")


async def main() -> None:
    session = AiohttpSession(
        api=TelegramAPIServer(
            base="https://api.telegram.org/bot{token}/test/{method}",
            # base="https://aiogram-calendar.o-murphy.net/bot{token}/test/{method}",
            file="https://api.telegram.org/file/bot{token}/test/{path}",
        )
    )

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML, session=session)

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
