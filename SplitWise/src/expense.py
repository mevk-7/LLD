from SplitWise.src.split import SplitStrategy, EqualSplit, PercentSplit, ExactSplit
from SplitWise.src.user import User
from typing import List, Dict


class Expense:

    __slots__ = ["_id", "_description", "_split_strategy", "_distribution", "_defaulters",
                 "_exact_amount", "_creditor", "_defaulter_distribution"]

    _total_id: int = 1
    _id: int
    _description: str
    _split_strategy: SplitStrategy
    _defaulter_distribution: Dict[User, float]
    _defaulters: List[User]
    _creditor: User
    _exact_amount: float

    @classmethod
    def _get_unique_id(cls):
        id_ = cls._total_id
        cls._total_id += 1
        return id_

    def __init__(self,
                 creditor: User,
                 description: str,
                 split_strategy: SplitStrategy,
                 defaulters: List[User],
                 exact_amount: float
                 ) -> None:

        self._defaulters = defaulters
        self._split_strategy = split_strategy
        self._description = description
        self._exact_amount = exact_amount
        self._creditor = creditor
        self._id = Expense._get_unique_id()

    @property
    def description(self):
        return self._description

    def process_expense(self) -> None:
        self._defaulter_distribution = self._split_strategy.distribute(self._defaulters, self._exact_amount)
        for defaulter in self._defaulter_distribution:
            self._creditor.add_to_user_expense(defaulter, self._defaulter_distribution[defaulter])
            defaulter.add_to_user_expense(self._creditor, -self._defaulter_distribution[defaulter])

    @property
    def exact_amount(self) -> float:
        return self._exact_amount

    @exact_amount.setter
    def exact_amount(self, amount: float) -> None:
        if amount < 0.0:
            print(f"Invalid amount: {amount}")
            return
        self._exact_amount = amount

    @property
    def split_strategy(self) -> SplitStrategy:
        return self._split_strategy

    @split_strategy.setter
    def split_strategy(self, split_strategy: SplitStrategy) -> None:
        self._split_strategy = split_strategy

    def print_expense(self):
        print(f"{self._creditor.name} lend amount {self._exact_amount}")
        for user in self._defaulter_distribution:
            print(user.name, "ows = ", self._defaulter_distribution[user])






