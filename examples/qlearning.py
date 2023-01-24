from random import choice, random
from typing import Literal, Optional

import numpy as np

from submission.ipd import IPDPlayer

################################
#   Tabular Q-learning agent   #
################################


def to_index(move: Literal["C", "D"]) -> int:
    """Maps "C" to 0 and "D" to 1.

    Args:
        move (Literal["C", "D"]): The move.

    Returns:
        int: The index of the move.
    """

    return 0 if move == "C" else 1


class TabularQLearningAgent(IPDPlayer):
    """An agent based on tabular Q-learning.

    This agent implements the epsilon-greedy strategy for exploration, which
    selects an action (cooperate or defect) uniformly at random with probability
    epsilon; otherwise, the agent greedily selects the action associated with
    the highest Q-value for that state.

    This agent only learns using the previous moves played by the agent and
    its opponent. Increasing this (e.g. to take the previous two moves into
    account) would allow to agent to learn a richer set of strategies at the
    expense of being harder to train in a sense; you probably want to cover
    the whole space of state-action pairs!

    Can you think of some other ways you could improve this model?
    """

    def __init__(self, epsilon: float = 0.0, file: Optional[str] = None) -> None:
        super().__init__()

        self._epsilon = epsilon
        self._q_table = np.load(file)["q_table"] if file else np.zeros((2, 2, 2))

    def play_move(self, opponent: IPDPlayer) -> Literal["C", "D"]:
        """Plays a move.

        Args:
            opponent (IPDPlayer): The opponent.

        Returns:
            Literal["C", "D"]: Whether to cooperate ("C") or defect ("D").
        """

        # Cooperate initially
        if not self.moves:
            return "C"

        # Play a random move with probability epsilon
        if random() < self._epsilon:
            return choice(["C", "D"])

        # Return the action corresponding to
        # the largest Q-value for this state
        return ("C", "D")[
            self._q_table[
                to_index(self.moves[-1]), to_index(opponent.moves[-1])
            ].argmax()
        ]

    def save_q_table(self, file: str):
        """Saves the current Q-table to a file.

        Args:
            file (str): A file path.
        """

        np.savez(file, q_table=self._q_table)
