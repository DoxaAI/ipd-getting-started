from typing import Literal

from ipd import DOXAGameRunner, IPDPlayer


class Agent(IPDPlayer):
    """An agent that plays the iterated prisoner's dilemma game on DOXA."""

    def play_move(self, opponent: IPDPlayer) -> Literal["C", "D"]:
        """Plays a move.

        Args:
            opponent (IPDPlayer): The opponent.

        Returns:
            Literal["C", "D"]: Whether to cooperate ("C") or defect ("D").
        """

        if not opponent.moves:
            return "C"

        return opponent.moves[-1]


if __name__ == "__main__":
    agent = Agent()

    DOXAGameRunner(agent).run()
