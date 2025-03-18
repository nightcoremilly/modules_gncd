#meta developer @as1r1x_knayzev

from datetime import timedelta
import logging

from telethon import functions
from telethon.tl.types import Message
from telethon.tl.custom import Message
from .. import utils, loader

@loader.tds
class Sup(loader.Module):
    """Управление ботом в локальном доступе, т.к бот не может вступать в другие чаты."""

    strings = {
        "name": "Sup-Blood",
    }

    def __init__(self):
        self.name = self.strings["name"]
        self.blood_bot = "@bloody_support_bot"
        self.blood_id = 7972872820
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
    async def факт(self, message: Message) -> None:
        """Говорит рандомные факт в мире."""
        response = await self.message_q(
            "факт", self.blood_bot, mark_read=True, delete=True
        )
        await utils.answer(message, response.text)


    @loader.command()
    async def инфо(self, message: Message) -> None:
        """Показывает информацию о боте."""
        response = await self.message_q(
            "инфо", self.blood_bot, mark_read=True, delete=True
        )
        await utils.answer(message, response.text)


    @loader.command()
    async def стата(self, message: Message) -> None:
        """Показывает статистику бота."""
        response = await self.message_q(
            "стата", self.blood_bot, mark_read=True, delete=True
        )
        await utils.answer(message, response.text)


    @loader.command()
    async def ид(self, message: Message) -> None:
        """Покажет айди пользователя, бота и ваш айди. (Чтобы узнать чужой айди, вам нужно чтобы бот был взаимодействен с ботом!)"""
        response = await self.message_q(
            "ид", self.blood_bot, mark_read=True, delete=True
        )
        await utils.answer(message, response.text)


    @loader.command()
    async def чат инфо(self, message: Message) -> None:
        """Показывает информацию о чате."""
        response = await self.message_q(
            "чат инфо", self.blood_bot, mark_read=True, delete=True
        )
        await utils.answer(message, response.text)
