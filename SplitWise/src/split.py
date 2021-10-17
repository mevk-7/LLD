from abc import ABC, abstractmethod
from typing import List, Dict
from SplitWise.src.user import User


class SplitStrategy(ABC):

    @abstractmethod
    def distribute(self, defaulters: List[User], exact_amount: float) -> Dict[User, float]:
        pass


class EqualSplit(SplitStrategy):

    def distribute(self, defaulters: List[User], exact_amount: float) -> Dict[User, float]:
        total_user = len(defaulters)
        distribution = {defaulters[i]: (1.0 / total_user) * exact_amount for i in range(total_user)}
        return distribution


class ExactSplit(SplitStrategy):

    def __init__(self, distribution):
        self._distribution = distribution

    def distribute(self, defaulters: List[User], exact_amount: float) -> Dict[User, float]:
        if sum(self._distribution) != exact_amount:
            print(f"The sum of amount given does not matches with total amount: {exact_amount}")
            return {}
        return {user: amount for user, amount in zip(defaulters, self._distribution)}


class PercentSplit(SplitStrategy):

    def __init__(self, distribution: List[int]):
        self._distribution = distribution

    def distribute(self, defaulters: List[User], exact_amount: float) -> Dict[User, float]:
        if sum(self._distribution) != 100:
            print(f"Total percent does not equate to 100")
            return {}
        return {user: (exact_amount * percent) / 100 for user, percent in zip(defaulters, self._distribution)}




