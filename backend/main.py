from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from fastapi import Query
from mongo import get_reading_room

app = FastAPI(title="광운대 열람실 API", description="설명 ~ ", version="0.0.1")
app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.get("/readingroom")
async def get_room_info(room: Union[int, None]):
# async def get_room_info(room: Union[set[str], None] = Query(default=[])):
    print(f'{room=}')
    return get_reading_room(room)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        # host="127.0.0.1",
        host="0.0.0.0",
        port=8002,
    )
