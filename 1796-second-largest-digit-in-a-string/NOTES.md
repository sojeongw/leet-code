# 문제

- 주어진 string에서 숫자만 골라 두 번째로 큰 수를 출력한다.

# 제출 답안

```python
class Solution:
    def secondHighest(self, s: str) -> int:
        result = []

        for value in s:
            if value.isdecimal() and value not in result:
                result.append(value)

        if len(result) < 2:
            return -1

        result.sort()

        return int(result[-2])
```

- 32ms
- string 값을 하나씩 돌면서 숫자인지 확인한다.
    - 숫자라면 리스트에 중복된 값이 없을 경우 추가한다.
- 길이가 2 이하라면 비교할 수 없으므로 -1을 리턴한다.
- 리스트를 정렬한 뒤 뒤에서 2번째인 수를 리턴한다.

```python
class Solution:
    def secondHighest(self, s: str) -> int:
        ...

        if len(result) == 0 or len(result) == 1:
            return -1

    ...
```

- 맨 처음에 아무 생각 없이 length 체크를 이렇게 했더니 73ms, 14% 대가 나왔다...^^;
- len() 체크도 연산 속도에 꽤나 영향을 미치는 걸까...
    - 구글에서 시간 복잡도를 검색해보면 O(1)이 나오는데 그럼 왜 느리지?

# 모범 답안

```python
class Solution:
    def secondHighest(self, s: str) -> int:
        s = set(s)
        arr = []
        for num in s:
            if num.isnumeric():
                arr.append(int(num))
        if len(arr) < 2:
            return -1
        arr.sort(reverse=True)
        return arr[1]
```

- 22ms
- set 자료 구조로 중복을 없앴다.
- isnumeric() 메서드로 숫자인지 판단한다.
- 길이가 2보다 작으면 -1을 리턴한다.
- 그렇지 않으면 정렬한 뒤 두 번째 큰 수를 반환한다.

파이썬에 내장된 함수를 잘 몰라서 활용하지 못한 게 아쉽다. 맨 처음에 중복을 미리 제거하는 게 편한 것 같다. 다음에 써먹어야지.