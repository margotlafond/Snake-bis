import typing
from pathlib import Path
from typing import Any

import yaml

from .score import Score


class Scores:  # noqa: D101
    def __init__(self, max_scores: int, scores: list[Score]) -> None:  # noqa: D107
        self._max_scores = max_scores
        self._scores = sorted(scores, reverse = True)[:self._max_scores]

    @classmethod
    def default(cls, max_scores: int) -> "Scores":  # noqa: D102
        return cls(max_scores, [Score(name="Joe", score=100), Score(name="Jack", score=80), Score(name="Averell", score=60), Score(name="William", score=1)])  # noqa: E501

    def __iter__(self) -> typing.Iterator[Score]:  # noqa: D105
        return iter(self._scores)

    def is_high_score(self, score: int) -> bool:  # noqa: D102
        return self._scores[-1].score < score or len(self._scores)<5

    def __add__(self, other: Any) -> None:  # noqa: D105
        if isinstance(other, Score):
            self._scores.append(other)
            self._scores.sort(reverse = True)
            self._scores = self._scores[:self._max_scores]

    def add_score(self, score:Score) -> None:  # noqa: D102
        if self.is_high_score(score.score):
            if len(self._scores) >= self._max_scores:
                self._scores.pop()
            self._scores.append(score)
            self._scores.sort(reverse = True)

    def save(self, scores_file: Path) -> None:  # noqa: D102
        x = [{"name": s.name, "score": s.score} for s in self]
        with scores_file.open("w") as fd: #fd pour file descriptor
            yaml.safe_dump(x, fd)