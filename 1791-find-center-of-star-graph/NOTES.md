# 문제

```text
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
```

- star 형태의 그래프를 표현한 리스트에서 center 노드 값이 무엇인지 알아낸다.

# 제출 답안

```python
class Solution(object):
    def findCenter(self, edges):
        count = {}
        for i in range(len(edges)):
            for j in range(2):
                index = edges[i][j]
                try:
                    count[index] += 1
                except:
                    count[index] = 1

        max_value = max(count, key=count.get)
        return max_value
```

- 2중 for문을 돌면서 중복값이 있으면 해당 인덱스에 1을 더한다.
- 그럼 제일 많이 count 된 것이 center node가 된다.

# 모범 답안

```python
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """

        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]
```

- 644ms
- 맨 첫번째 관계에서 첫번쨰 노드값이 두번째 관계에도 있다면 그게 정답
- 없다면 맨 첫번째 관계의 두번째 노드값이 정답

대충격...왜 이 간단한 원리를 생각해내지 못했을까?