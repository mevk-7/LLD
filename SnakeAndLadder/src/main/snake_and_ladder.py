from dataclasses import dataclass


@dataclass
class Snake:
    __slots__ = ['_start', '_end']
    _start: int
    _end: int

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end


@dataclass
class Ladder:
    __slots__ = ['_start', '_end']
    _start: int
    _end: int

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end
