#meta developer @as1r1x_knayzev

# -*- coding: utf-8 -*-

"""
Управление ботом в локальном доступе через Hikka, т.к бот не может вступать в другие чаты.
"""

from datetime import timedelta
import logging

from telethon import functions
from telethon.tl.types import Message
from telethon.tl.custom import Message
from hikka import utils, loader
from telethon.utils import get_display_name

@loader.tds
class SupBloodModule(loader.Module):
    """Управление ботом в локальном доступе."""

    strings = {
        "name": "SupBlood",
        "bot_not_found": "⚠️ Бот не найден. Убедитесь, что ID бота указан правильно.",
        "error_sending_message": "❌ Ошибка при отправке сообщения боту: {}",
        "no_response_from_bot": "⚠️ Бот не ответил на запрос.",
        "command_failed": "❌ Команда не выполнена. Подробности в логах.",
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
        me = await client.get_me()
        if me:
            self.myid = me.id
        else:
            logging.error("Не удалось получить информацию о себе.")


    async def message_q(
        self,
        text: str,
        entity: Union[int, str], 
        mark_read: bool = False,
        delete: bool = False,
    ) -> Union[Message, None]:
        """Отправляет сообщение и возвращает ответ."""
        try:
            async with self.client.conversation(entity) as conv:
                msg = await conv.send_message(text)
                response = await conv.get_response()

                if mark_read:
                    await conv.mark_read()

                if delete:
                    await msg.delete()
                    await response.delete()

                return response
        except Exception as e:
            logging.exception(f"Ошибка при взаимодействии с ботом {entity}: {e}")
            return None  


    async def _send_command_to_bot(self, message: Message, command: str):
        """Отправляет команду боту и обрабатывает результат."""
        try:
            response = await self.message_q(command, self.blood_bot, mark_read=True, delete=True)

            if response:
                await utils.answer(message, response.text)
            else:
                await utils.answer(message, self.strings["no_response_from_bot"])
                logging.warning(f"Бот {self.blood_bot} не ответил на команду {command}")

        except Exception as e:
            logging.exception(f"Ошибка при выполнении команды {command}: {e}")
            await utils.answer(message, self.strings["command_failed"])

    @loader.command()
    async def факт(self, message: Message) -> None:
        """Говорит рандомные факт в мире."""
        await self._send_command_to_bot(message, "факт")

    @loader.command()
    async def инфо(self, message: Message) -> None:
        """Показывает информацию о боте."""
        await self._send_command_to_bot(message, "инфо")

    @loader.command()
    async def стата(self, message: Message) -> None:
        """Показывает статистику бота."""
        await self._send_command_to_bot(message, "стата")

    @loader.command()
    async def ид(self, message: Message) -> None:
        """Покажет айди пользователя, бота и ваш айди. (Чтобы узнать чужой айди, вам нужно чтобы пользователь и вы были взаимодействены с ботом!)"""
        await self._send_command_to_bot(message, "ид")

    @loader.command()
    async def чатинфо(self, message: Message) -> None:
        """Показывает информацию о чате."""
        await self._send_command_to_bot(message, "чат инфо")
