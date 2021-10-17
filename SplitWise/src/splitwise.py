from SplitWise.src.user import User
from SplitWise.src.expense import Expense
from SplitWise.src.split import SplitStrategy
from typing import Dict, List


class SplitWise:
    __slots__ = ["_user_expense_map", "_user_id_map"]
    _user_expense_map: Dict[int, List[Expense]]
    _user_id_map: Dict[int, User]

    def __init__(self):
        self._user_expense_map = {}
        self._user_id_map = {}

    def register_user(self, user: User) -> None:
        if user.get_id() in self._user_id_map:
            print(f"user : {user} already register")
            return
        self._user_id_map[user.get_id()] = user

    def _verify_users(self, users) -> bool:
        for user in users:
            if user.get_id() not in self._user_id_map:
                print(f"User : {user} is not registered to split wise.Please register first")
                return False
        return True

    def add_expense(self, description: str,
                    creditor: User,
                    defaulters: List[User],
                    exact_amount: float,
                    split: SplitStrategy
                    ) -> None:

        if not self._verify_users([creditor]) or not self._verify_users(defaulters):
            return

        expense = Expense(creditor, description, split, defaulters, exact_amount)
        expense.process_expense()
        if creditor not in self._user_expense_map:
            self._user_expense_map[creditor.get_id()] = []
        self._user_expense_map[creditor.get_id()].append(expense)

    def print_expense_user(self, user: User) -> None:
        if not self._verify_users([user]):
            return
        expense_sheet = user.get_expense_sheet()
        for uid in expense_sheet:
            amount = expense_sheet[uid]
            if amount < 0 :
                print(f"{user} ows : {amount} to {self._user_id_map[uid]}")
            else:
                print(f"{user} lend : {amount} to {self._user_id_map[uid]}")

    def print_all_expenses(self) -> None:
        for user in self._user_id_map.values():
            amount = user.get_total_expense()
            print(f"{user} total balance {amount}")