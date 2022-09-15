import pymongo
from dataclasses import dataclass
from datetime import datetime, timedelta

client = pymongo.MongoClient("mongodb", 27017)

# db
READING_ROOM_DB = "kwu_readingroom"
_database = client[READING_ROOM_DB]

# collection
ROOM_1 = "room_1"
ROOM_2 = "room_2"
ROOM_3 = "room_3"


@dataclass
class RoomCollection:
    room_1 = _database[ROOM_1]
    room_2 = _database[ROOM_2]
    room_3 = _database[ROOM_3]

    def __getitem__(self, key):
        if key == 1:
            return self.room_1
        if key == 2:
            return self.room_2
        if key == 3:
            return self.room_3


roomCollection = RoomCollection()

def get_reading_room(room_num:int):
    '''
    최근의 열람실 정보를 주는 API이므로, 가장 최근의 정보만을 반환함
    '''
    curr = datetime.utcnow().replace(microsecond=0)
    result  =roomCollection[room_num].find_one(
        filter={
            "_id" : curr.replace(hour=0, minute=0, second=0),
        },
        projection={
            "_id" : 0,
            "use" : "$recent.use",
            "not_use" : "$recent.not_use"
        }
    )
    if result:
        return result
    # 23:59 ~ 00:00 시에 데이터가 없을 수도 있음(5초 간격으로 저장하다보니)
    # 이런 경우 그 전날 것으로 반환
    return roomCollection[room_num].find_one(
        filter={
            "_id" : curr.replace(hour=0, minute=0, second=0) - timedelta(days=1),
        },
        projection={
            "_id" : 0,
            "use" : "$recent.use",
            "not_use" : "$recent.not_use"
        }
    )