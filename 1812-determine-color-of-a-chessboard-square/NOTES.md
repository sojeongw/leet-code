# 1812. Determine Color of a Chessboard Square

- 주어진 체스판 위치가 블랙이면 false, 화이트면 true

# 제출 답안

```python
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        chessboard = [
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
        ]

        letter, number = coordinates[0], int(coordinates[1])
        return bool(chessboard[number - 1][ord(letter) - 97])
```

- 39 ms, faster than 64.97%
- 체스 판을 그대로 그린다.
- letter는 아스키 값으로, 숫자는 -1한 인덱스로 위치를 계산해 반환한다.

```python
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter, number = ord(coordinates[0]) - 96, int(coordinates[1])
        return (letter + number) % 2 != 0
```

- 41 ms, faster than 61.83%
- (x, y) 좌표값을 구해 x + y를 했을 때 홀수면 흰색이 나온다.

```python
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        number = coordinates[1]

        if int(number) % 2 == 0:
            if coordinates[0] in "aceg":
                return True
        else:
            if coordinates[0] in "bdfh":
                return True

        return False
```

- 16ms
- 직접 알파벳을 대조해 푼다.
- 제출 답안에서는 문자열을 int로 변환하는데 여기서 시간이 걸린것 같다.
    - 10진법에서 str과 int 간의 캐스팅은 O(N^2)이 걸린다고 한다.
    - 코드가 짧고 if 문이 없다고 더 빠른 게 아니구나.
    - 때로는 단순하고 직관적으로 푸는 게 더 좋은듯.