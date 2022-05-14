# 1832. Check if the Sentence Is Pangram

- 알파벳 26자가 최소한 한 개씩 모두 있을 경우 True를 반환한다.

## 제출 답안

```python
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(sentence) < 26:
            return False

        removed_duplicates = set(sentence)

        if len(removed_duplicates) == 26:
            return True
        else:
            return False
```

- 23 ms, faster than 62.76%
    - 얼리 리턴을 안했을 때는 41 ms였다.
    - 얼리 리턴 유무가 이렇게까지 차이날 수 있구나.
- set으로 중복을 없앴을 때 26자가 채워지는지 체크한다.

```python
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        dic = {}

        for s in sentence:
            dic[s] = 1

        return len(dic) == 26
```

- 33 ms, faster than 26.10%
- map으로도 할 수 있을 것 같아서 해봤다.

## 모범 답안

```python
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        dic = {}
        for s in sentence:
            dic[s] = 1
        if len(dic) == 26:
            return True
        return False
```

- 7ms
- 내가 map으로 푼 것과 차이는 없어보이는데, 역시 측정 시간은 항상 상황에 따라 달라지는 걸까.