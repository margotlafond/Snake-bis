import typing

from .score import Score


class Scores:
    def __init__(self, max_scores: int, scores: list[Score]) -> None:
        self._max_scores = max_scores
        scores.sort(reverse = True)
        self._scores = scores[:self._max_scores]

    @classmethod
    def default(cls, max_scores: int) -> "Scores":
        return cls(max_scores, [Score(name="Joe", score=100), Score(name="Jack", score=80), Score(name="Averell", score=60), Score(name="William", score=40)])

    def __iter__(self) -> typing.Iterator[Score]:
        return iter(self._scores)