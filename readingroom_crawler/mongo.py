from dataclasses import dataclass
from pprint import pprint
from time import strftime
from typing import List, Union
import pymongo
from datetime import datetime, timedelta

client = pymongo.MongoClient("mongodb", 27017)

__all__ = ["save_reading_room"]

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


def create_room_collection(room_num: Union[int, List[int]]):
    aaa = {"timeField": "timestamp", "granularity": "seconds"}
    room_nums = room_num if isinstance(room_num, list) else [room_num]
    for num in room_nums:
        _name = f"room_{num}"
        if _name not in _database.list_collection_names():
            _database.create_collection(name=_name)
    return

def save_reading_room(room_num: int, using: List[int], not_using: List[int]):
    curr = datetime.utcnow().replace(microsecond=0)
    
    roomCollection[room_num].update_one(
        filter={
            "_id" : curr.replace(hour=0, minute=0, second=0)  - timedelta(days=1)
        },
        update={
            "$push": {
                f"{curr.hour}":{
                        "min_sec" : f"{curr.minute}:{curr.second}",
                        "use" : using,
                        "not_use" : not_using
                    }
            },
            "$set": {
                "recent" : {
                    "use": using,
                    "not_use" : not_using
                }
            }
        },
        upsert=True
    )


def drop_collections():
    _database.drop_collection(ROOM_1)
    _database.drop_collection(ROOM_2)
    _database.drop_collection(ROOM_3)

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