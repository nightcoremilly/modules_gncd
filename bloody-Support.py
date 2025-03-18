#meta developer @as1r1x_knayzev

from datetime import timedelta
import logging

from telethon import functions
from telethon.tl.types import Message
from telethon.tl.custom import Message
from .. import utils, loader

@loader.tds
class name(loader.Module):
    """❗ Управление ботом в локальном доступе, т.к бот не может вступать в другие чаты."""

    strings = {
        "name": "bloody-Support",
        #при желании можно указывать ошибки и др компоненты. пример
        "loading_photo": "⏳ Загрузка графика...",
        "error_args": "❌ Ошибка: Неверные аргументы",
        "error_transfer": "❌ Ошибка: Требуется указать это или это",
        "error_conclusion": "❌ Ошибка: Требуется указать это\это",
    }

    def init(self):
        self.name = self.strings["name"]
        self.username_bot = "@bloody_support_bot"
        # self.название_твоего_бота = "@iris_moon_bot"
        self.iris_id = 7972872820
        self.client = None
        self.db = None
        self.myid = None

    async def client_ready(self, client, db):
        """Инициализация при запуске"""
        self.client = client
        self.db = db
        self.myid = (await client.get_me()).id

    async def message_q(
        self,
        text: str,
        user_id: int,
        mark_read: bool = False,
        delete: bool = False,
    ) -> Message:
        """Отправляет сообщение и возвращает ответ"""
        async with self.client.conversation(user_id) as conv:
            msg = await conv.send_message(text)
            response = await conv.get_response()

            if mark_read:
                await conv.mark_read()

            if delete:
                await msg.delete()
                await response.delete()

            return response

    @loader.command()
    async def info_command(self, message: Message) -> None:
        """описание команды"""
        response = await self.message_q(
            "info", self.username_bot, mark_read=True, delete=True
        )
        await utils.answer(message, response.text)
