import asyncio
import aiohttp
from html_job import *

ROOM_1 = "http://mobileid.kw.ac.kr/seatweb/roomview5.asp?room_no=1"
ROOM_2 = "http://mobileid.kw.ac.kr/seatweb/roomview5.asp?room_no=2"
ROOM_3 = "http://mobileid.kw.ac.kr/seatweb/roomview5.asp?room_no=3"

async def main():
    while 1:
        for x in [ROOM_1, ROOM_2, ROOM_3]:
            async with aiohttp.ClientSession() as session:
                async with session.get(x) as response:
                    html = await response.text()
                    tot_num , using, not_using = total_seat_number(html)
                    using_list, not_using_list = get_seats(html)
                await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())