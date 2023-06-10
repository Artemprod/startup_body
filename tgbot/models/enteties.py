from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class User:
    id: int | None
    name: str | None
    registration_date: datetime | None
    product_info: dict | None  # Можно использовать класс, если структура информации о продукте известна
    difficulty: str | None
    questions: List[int] | None
    answers: List[str] | None
    state: int | None


@dataclass
class Question:
    id: int
    question: str


@dataclass
class Answer:
    id: int
    question_id: int
    user_id: int
    answer: Optional[str]
    date: datetime


@dataclass
class Bot:
    name: str | None
    token: str | None
    url: str | None


@dataclass
class Users:
    users: list[User]

    def append_user(self, user: User)-> None:
        self.users.append(user)
