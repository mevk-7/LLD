from abc import ABC, abstractmethod
from typing import Dict


class AbstractUser(ABC):

    @abstractmethod
    def get_id(self):
        pass


class User(AbstractUser):
    __slots__ = ["_name", "_id", "_expense_sheet", "_total_expense"]
    _total_id: int = 1
    _name: str
    _id: int
    _expense_sheet: Dict[int, float]
    _total_expense: float

    @classmethod
    def _get_unique_id(cls):
        id_ = cls._total_id
        cls._total_id += 1
        return id_

    def __init__(self, name: str):
        self._name = name
        self._id = User._get_unique_id()
        self._expense_sheet = dict()
        self._total_expense = 0

    @property
    def name(self):
        return self._name

    def get_id(self):
        return self._id

    def add_to_user_expense(self, user: AbstractUser, amount: float) -> None:
        if user is self:
            print(f"cannot add expense to self")
            return
        if user.get_id() in self._expense_sheet:
            self._expense_sheet[user.get_id()] += amount
        else:
            self._expense_sheet[user.get_id()] = amount

        self._total_expense += amount

    def get_expense_sheet(self):
        return self._expense_sheet

    def get_total_expense(self):
        return self._total_expense

    def __str__(self) -> str:
        return self._name
