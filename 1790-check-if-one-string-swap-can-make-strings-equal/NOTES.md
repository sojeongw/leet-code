# 문제

```text
Input: s1 = "bank", s2 = "kanb"
Output: true
```

- swap 한 번 하면 같은 글자가 되는지 확인한다.

# 제출 답안

```python
class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1 == s2:
            return True

        count = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1

        if count != 2:
            return False

        sortedS1 = ''.join(sorted(s1))
        sortedS2 = ''.join(sorted(s2))

        if sortedS1 == sortedS2:
            return True
```

- 같은 인덱스에 위치한 글자가 같으면 count를 센다.
- 중복된 글자가 2개 이상이면 한 번 swap으로 끝나지 않으므로 false가 된다.
- 2개라면 글자들을 연결한 뒤, 서로 같은 글자인지 확인한다.

# 모범 답안

```python
def areAlmostEqual(self, s1, s2):
    n = len(s1)
    diffs = []
    already2 = False
    for i in range(n):
        if s1[i] == s2[i]:
            continue
        if already2:
            return False
        diffs.append((s1[i], s2[i]))
        if len(diffs) == 2:
            if not (diffs[0][0] == diffs[1][1] and diffs[0][1] == diffs[1][0]):
                return False
            diffs = []
            already2 = True
    return len(diffs) == 0
```

- 4ms
- 같은 인덱스에 있는 글자가 같으면 넘어간다.
    - 이미 같은 글자가 2개인데 또 나왔다면 false를 리턴한다.
- 같은 글자가 아니라면 diffs에 넣어둔다.
    - 다른 글자가 2번 나왔다면
        - 얘네끼리 교차했을 때 같은 알파벳이어야 한다.
    - diffs를 비우고 2번이 채워졌음을 알린다.
- 즉, 최종적으로 2개를 제외한 diffs가 비워져 있어야 true를 반환한다.

속도는 빠르지만 이해하기 어려운 코드다.