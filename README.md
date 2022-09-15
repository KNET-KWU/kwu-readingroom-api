# 광운대 열람실 좌석 API

`https://api.k-net.kr`

## 사용방법

제 1열람실 :  `https://api.k-net.kr/readingroom?room=1`

제 2열람실 :  `https://api.k-net.kr/readingroom?room=2`

제 3열람실 :  `https://api.k-net.kr/readingroom?room=3`

## 반환 형태 (JSON)

```json
{
  "use" : [ 1, 2, 3, 10],
  "not_use" : [ 7, 8, 9, 121 ]
}
```

## 내 컴퓨터에서 돌리고 싶어요

```bash
# 커맨드 창 끌때 같이 끄고 싶으면
docker-compose up

# 그런거 아니면 -d (detach)
docker-compose up -d

# 코드 수정하고 반영하고 싶으면
docker-compose up -d --build
```
