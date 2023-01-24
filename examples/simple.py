from random import choice
from typing import Literal

from submission.ipd import IPDPlayer

################################
#   Simple rule-based agents   #
################################


class AllC(IPDPlayer):
    """An agent that always cooperates."""

    def play_move(self, opponent: IPDPlayer) -> Literal["C", "D"]:
        return "C"


class AllD(IPDPlayer):
    """An agent that alwys defects."""

    def play_move(self, opponent: IPDPlayer) -> Literal["C", "D"]:
        return "D"


class TitForTat(IPDPlayer):
    "An initially cooperative agent that matches the opponent's previous move."

    def play_move(self, opponent: IPDPlayer) -> Literal["C", "D"]:
        if not opponent.moves:
            return "C"

        return opponent.moves[-1]


class Random(IPDPlayer):
    """An agent that cooperates or defects uniformly at random."""

    def play_move(self, opponent: IPDPlayer) -> Literal["C", "D"]:
        return choice(["C", "D"])
