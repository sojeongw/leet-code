# Sample Submissions

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