from typing import Generator, List, Literal, Tuple

import numpy as np

from submission.ipd import IPDPlayer

Action = Literal["C", "D"]

PAYOFF_MATRIX = {
    ("C", "C"): (3, 3),
    ("C", "D"): (0, 5),
    ("D", "C"): (5, 0),
    ("D", "D"): (1, 1),
}


class IPDGame:
    """An iterated prisoner's dilemma game."""

    moves1: List[Action]
    moves2: List[Action]

    rewards1: List[int]
    rewards2: List[int]

    def __init__(self) -> None:
        self.score1 = 0
        self.score2 = 0

        self.moves1 = []
        self.moves2 = []

        self.rewards1 = []
        self.rewards2 = []

        self.total_moves = np.clip(np.random.geometric(0.00346), 1, 400)

    def play_move(self, move1: Action, move2: Action) -> Tuple[int, int]:
        """Plays a single iteration of the IPD.

        Args:
            move1 (Action): Cooperate ("C") or defect ("D").
            move2 (Action): Cooperate ("C") or defect ("D").

        Returns:
            Tuple[int, int]: The resulting rewards.
        """

        self.moves1.append(move1)
        self.moves2.append(move2)

        reward1, reward2 = PAYOFF_MATRIX[(move1, move2)]
        self.rewards1.append(reward1)
        self.rewards2.append(reward2)

        self.score1 += reward1
        self.score2 += reward2

        return reward1, reward2


def play_ipd(
    player1: IPDPlayer, player2: IPDPlayer
) -> Generator[Tuple[int, Tuple[Action, Action], Tuple[int, int]], None, None]:
    """A useful generator for playing an IPD game between two players.

    Yields:
        Tuple[
            int, Tuple[Action, Action], Tuple[int, int]
        ]: The current index, the pair of moves just played and the resulting rewards.
    """

    game = IPDGame()
    for i in range(game.total_moves):
        # Get moves from the players
        move1 = player1.play_move(player2)
        move2 = player2.play_move(player1)

        # Perform the actions
        reward1, reward2 = game.play_move(move1, move2)

        # Pass on the reward signal to the players
        player1.update(move1, reward1)
        player2.update(move2, reward2)

        yield i + 1, (move1, move2), (reward1, reward2)
