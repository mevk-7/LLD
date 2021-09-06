from enum import  Enum, auto
from typing import List, Tuple
from MeetingScheduler.src.main.meeting import Meeting


class RoomType(Enum):
    __slots__ = []
    SMALL = auto()
    LARGE = auto()


class Room:

    __slots__ = ["type", "id", "_calender"]
    type: RoomType
    id: str
    calender: List[Tuple[str, int, int]]

    def __init__(self, id_, type_):
        self.type = type_
        self.id = id_
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
        print(f"Meeting happened in room: {self.id} so far ->")
        for meeting in self._calender:
            print(f"\t{meeting}")

    def get_type(self) -> RoomType:
        return self.type

    def get_id(self) -> str:
        return self.id






