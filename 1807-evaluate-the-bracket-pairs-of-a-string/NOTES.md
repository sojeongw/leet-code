# 1807. Evaluate the Bracket Pairs of a String

- 괄호 안에 있는 문자를 knowldege에 있는 단어로 치환한다.

# 제출 답안

```python
import re


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_map = dict(knowledge)
        bracket_strings = re.findall(r'\(([^)]+)\)', s)

        for bracket_string in bracket_strings:
            keys = list(knowledge_map.keys())
            if bracket_string in keys:
                value = knowledge_map.get(bracket_string)
                s = re.sub(r'\(([' + bracket_string + r')]+)\)', value, s, 1)
            else:
                s = re.sub(r'\(([' + bracket_string + r')]+)\)', "?", s, 1)
```

- O(n^2)
- knowldege를 해시 테이블로 변경해 키를 넣으면 값을 바로 찾을 수 있게 한다.
- 입력 값에서 괄호 안에 있는 값들만 빼낸다.
- 돌면서 괄호 안의 값이 knowledge에 있는지 확인한다.
    - 있으면 knowledge의 value로 치환한다.
    - 없으면 ?로 치환한다.
- 하나씩 순환하면서 확인하다 보니 샘플 데이터가 많을 땐 타임 아웃이 나서 통과하지 못했다.

# 모범 답안

```python
import re


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # only match ')' 
        # regex removes the matching patterns from the string while split
        # so need a clue to check in O(1) time if the word is the one to replace
        # otherwise all words will look the same and every word will need a check
        regex = re.compile("([a-z]+)\)")
        words = re.split(regex, s)

        # 키 : 값 형태로 변환
        d = {x[0]: x[1] for x in knowledge}

        # 인덱스와 원소를 동시에 접근하면서 루프를 돌리는 함수
        for i, word in enumerate(words):
            if word.endswith("("):
                # '(' 괄호는 '' 빈 값으로 대체한다.
                words[i] = words[i][:-1]
                # '('의 다음 인덱스는 변환 대상이다.
                # 키가 d에 존재하면 그 값으로, 아니면 ?로 대체한다.
                words[i + 1] = d.get(words[i + 1], '?')
        return ''.join(words)
```

- `)`를 기준으로 단어를 잘라낸다.
- knowledge를 키 : 값 쌍으로 변환한다.
- enumerate()로 자른 단어를 순회한다.
    - '('가 나오면 ''로 대체한다.
    - 바로 다음 인덱스는 단어이므로 그 값이 key가 되는지 확인하고 값을 대체한다.
        - 없을 경우 '?'로 대체한다.
- 파이썬 문법과 정규 표현식에 익숙하지 않아 제대로 풀지 못한 문제였다.