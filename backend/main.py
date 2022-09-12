from fastapi import FastAPI
# from router.room import roomRouter
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from fastapi import Query

app = FastAPI(title='광운대 열람실 API', description="설명 ~ ", version="0.0.1")
app.add_middleware(CORSMiddleware, allow_origins=["*"])    

@app.get('/readingroom')
async def get_room_info(room: Union[set[str], None] = Query(default=[])):
    print(f"{room=}")
    return 123

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        # host="127.0.0.1",
        host="0.0.0.0",
        port=8080
    )