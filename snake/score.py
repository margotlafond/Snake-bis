class Score:

    MAX_LENGTH = 8

    def __init__(self, score: int, name: str) -> None:
        self._score = score
        self.name = name #uses the property defined below

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, n: str) -> None:
        """Set the name."""
        self._name = n[:self.MAX_LENGTH]

    @property
    def score(self)-> int:
        return self._score

    def __lt__(self, other: object) -> bool:
        return isinstance(other, Score) and self._score < other._score
