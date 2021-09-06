from MeetingScheduler.src.main.scheduler import Scheduler
from MeetingScheduler.src.main.room import (
    Room,
    RoomType
)

if __name__ == '__main__':
    room1 = Room("Batman", RoomType.LARGE)
    room2 = Room("Aquaman", RoomType.SMALL)
    room3 = Room("SuperMan", RoomType.LARGE)
    scheduler = Scheduler([room1, room2])
    scheduler.add_new_room(room3)

    scheduler.book("Justice League Meeting", 1, 5, RoomType.LARGE)
    scheduler.book("Marvel Meeting", 2, 7, RoomType.LARGE)
    scheduler.book("Marvel Meeting 2", 2, 5, RoomType.SMALL)
    scheduler.book("Batman secrete meeting", 6, 9, RoomType.LARGE)
