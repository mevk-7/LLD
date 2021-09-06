from MeetingScheduler.src.main.room import Room, RoomType
from typing import List


class Scheduler:

    __slots__ = ["rooms"]

    def __init__(self, rooms: List[Room]) -> None:
        self.rooms = rooms

    def book(self, meeting_id: str, start: int, end: int, room_type: RoomType) -> bool:
        for room in self.rooms:
            if room.get_type() == room_type and room.book(meeting_id, start, end):
                print(f"Room  {room.get_id()} booked for meeting {meeting_id}")
                return True
        print(f"No room available for meeting :{meeting_id} of type {room_type}")
        return False

    def add_new_room(self, room: Room) -> None:
        self.rooms.append(room)
