from __future__ import annotations

from typing import List, Literal

"""

This file contains code for defining a representation of a player of the
iterated prisoner's dilemma game and for interfacing with DOXA.

For the most part, you will not need to modify this module at all. Instead,
create your own agent in `run.py` by implementing the `play_move` method.
You may add additional methods as you see fit!

The directory you submit to DOXA must contain all the files necessary to
run your agent, including any machine learning models. Please do not include
any files that are not related to your current submission.

"""


class IPDPlayer:
    """A player of the iterated prisoner's dilemma game."""

    score: int
    moves: List[Literal["C", "D"]]
    rewards: List[int]

    def __init__(self) -> None:
        self.score = 0
        self.moves = []
        self.rewards = []

    def play_move(self, opponent: IPDPlayer) -> Literal["C", "D"]:
        """Plays a move.

        Args:
            opponent (IPDPlayer): The opponent.

        Returns:
            Literal["C", "D"]: Whether to cooperate ("C") or defect ("D").
        """

        raise NotImplementedError

    def update(self, move: Literal["C", "D"], reward: int) -> None:
        """Updates the state of an IPD player.

        Args:
            move (str): The move that was played ("C" or "D").
            reward (int): The reward from playing the previous move.
        """

        self.score += reward
        self.moves.append(move)
        self.rewards.append(reward)


class DOXAGameRunner:
    """A game runner that interfaces with DOXA."""

    def __init__(self, player: IPDPlayer) -> None:
        super().__init__()

        self._player = player
        self._opponent = IPDPlayer()

    def _handle_doxa_initialisation(self):
        """Synchronises with DOXA at the start of a game."""

        assert input() == "INIT"
        print("OK")

    def _handle_update(self):
        """
        Receives from DOXA the moves played by the agent and its opponent,
        as well as the reward signal for both, and then updates the local
        copies of the gameplay state.
        """

        line = input()
        if line == "START":
            return

        move, reward, opponent_move, opponent_reward = line.split()

        assert move in ["C", "D"]
        assert opponent_move in ["C", "D"]

        self._player.update(move, int(reward))
        self._opponent.update(opponent_move, int(opponent_reward))

    def run(self):
        """Communicates with DOXA and runs the game."""

        self._handle_doxa_initialisation()

        # main game loop
        while True:
            self._handle_update()

            move = self._player.play_move(self._opponent)
            assert move in ["C", "D"]
            print(move)
