from typing import Union
from fastapi import APIRouter,Query


roomRouter = APIRouter(prefix='/readingroom')

@roomRouter.get('/readingroom')
async def get_room_info(room: Union[set[str], None] = Query(default=[])):
    print(f"{room=}")
    return 123