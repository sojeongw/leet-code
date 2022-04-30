# 1816. Truncate Sentence

- 주어진 s를 앞에서부터 k개만큼의 단어로 자른다.

## 제출 답안

```python
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        array = s.split(" ")
        result = array[0]

        for i in range(1, k):
            result += " " + array[i]

        return result
```

- 28 ms, faster than 94.88%
- 공백 기준으로 문장을 분리한 뒤, k만큼 다시 단어를 조합한다.

## 모범 답안

```python
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = list(s.split())
        return ' '.join(s[:k])
```

- 16ms
- [:k] 문법을 생각해내지 못했다.