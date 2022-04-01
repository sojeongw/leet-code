# 문제

- 주어진 문자열에서 숫자가 아닌 것은 공백으로 처리한다.
- 숫자의 총 개수를 반환한다.
    - 단, 0으로 시작하면 0을 제외한다.
    - 중복은 인정하지 않는다.

# 제출 답안

```python
import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(map(int, re.findall('\d+', word))))
```

- 58ms
- 25.43%
    - 뭐 땜에 이렇게 밀렸을까. 라이브러리 때문인가?
- 라이브러리와 정규표현식을 이용해 숫자만 거른다.
    - 각 숫자마다 int로 반환하면서 0이 맨 앞에 오면 제거한다.
    - set에 넣어 중복을 제거한다.

# 모범 답안

```python
import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set([
            int(digit)
            for digit in re.sub(r'[^0-9]', ' ', word).split(' ')
            if digit is not ''
        ]))
```

- 숫자가 아닌 것을 골라 공백으로 치환한 다음, 공백으로 글자를 자른다.
    - 단, 비어있지 않을 경우
- 자른 각 글자를 set에다 넣는다.
- 정규표현식에 r을 쓰면 백슬래시를 해석하지 않고 raw string으로 남겨둬 유용하다.
    - r을 쓰지 않으면 백슬래시를 표현할 때 두 번 써줘야 한다.

# 정규 표현식

## []

- 괄호 사의의 문자와 매치 시킨다.
- 문자 사이에 하이픈을 사용하면 범위를 나타낸다.
- [a-zA-Z]
    - 알파벳 모두
- [0-9]
    - 숫자
- ^
    - 반대를 의미한다.

### 자주 사용하는 문자 클래스

- \d
    - 숫자와 매치
    - [0-9]와 동일한 표현식
- \D
    - 숫자가 아닌 것과 매치
    - [^0-9]와 동일한 표현식
- \s
    - whitespace 문자와 매치
    - [ \t\n\r\f\v]와 동일한 표현식
    - 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
- \S
    - whitespace 문자가 아닌 것과 매치
    - [^ \t\n\r\f\v]와 동일한 표현식
- \w
    - 문자+숫자(alphanumeric)와 매치
    - [a-zA-Z0-9_]와 동일한 표현식
- \W
    - 문자+숫자(alphanumeric)가 아닌 문자와 매치
    - [^a-zA-Z0-9_]와 동일한 표현식

## +

- 반복을 의미한다.