# 1817. Finding the Users Active Minutes

- UAM이 찍힌 유저 수를 구한다.

## 제출 답안

```python
from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dic = defaultdict(set)

        for log in logs:
            dic[log[0]].add(log[1])

        result = [0 for i in range(k)]

        for value in dic.values():
            result[len(value) - 1] += 1

        return result
```

- 1825 ms, faster than 14.33%
- ID를 키, time을 value로 갖는 딕셔너리를 만든다.
    - 이때 time은 set으로 저장해 중복이 없게 한다.
- UAM이 찍혔던 개수만큼 해당 인덱스의 값을 늘린다.

## 모범 답안

```python
from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        userToMinutes = defaultdict(set)

        for user, minute in logs:
            userToMinutes[user].add(minute)

        answer = [0] * k

        for minutes in userToMinutes.values():
            answer[len(minutes) - 1] += 1

        return answer
```

- 944ms
- 사실상 로직은 비슷해 보이는데, 문법적으로 좀 더 간단하게 작성한 것 같다.
    - 이게 이만큼의 시간을 줄일 수 있는 요소인가..?