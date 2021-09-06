
class Meeting:
    __slots__ = ["start_time", "end_time", "room", "id"]
    id: str
    start_time: int
    end_time: int

    def __init__(self, id_, start_time, end_time, room):
        self.id = id_
        self.room = room
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Meeting :{self.id} starts on: {self.start_time} and ends on: {self.end_time}"
