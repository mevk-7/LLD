from enum import  Enum, auto
from typing import List, Tuple
from MeetingScheduler.src.main.meeting import Meeting


class RoomType(Enum):
    __slots__ = []
    SMALL = auto()
    LARGE = auto()


class Room:

    __slots__ = ["_type", "_id", "_calender"]
    _type: RoomType
    _id: str
    calender: List[Tuple[str, int, int]]

    def __init__(self, id_, type_):
        self._type = type_
        self._id = id_
        self._calender = []

    def book(self, meeting_id,  start_time, end_time):
        for meeting in self._calender:
            if meeting.start_time <= start_time <= meeting.end_time:
                return False
            if meeting.start_time <= end_time <= meeting.end_time:
                return False

        meeting = Meeting(meeting_id, start_time, end_time, self)
        self._calender.append(meeting)
        return True

    def get_meeting_history(self):
        print(f"Meeting happened in room: {self._id} so far ->")
        for meeting in self._calender:
            print(f"\t{meeting}")

    @property
    def type(self) -> RoomType:
        return self._type

    @property
    def id(self) -> str:
        return self._id






