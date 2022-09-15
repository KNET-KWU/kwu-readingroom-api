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

