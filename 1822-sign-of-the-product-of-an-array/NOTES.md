# 1822. Sign of the Product of an Array

- 모든 값을 곱해서 양수면 1, 0이면 0, 음수면 -1을 반환한다.

## 제출 답안

```python
def array_sign(nums):
    if 0 in nums:
        return 0

    count = 0
    for n in nums:
        if n < 0:
            count += 1

    if count % 2 == 1:
        return -1
    else:
        return 1


result = array_sign([-1, 1, -1, 1, -1])
print(result)
```

- 65 ms, faster than 77.83%
- 0이 있으면 무조건 0이니까 얼리 리턴한다.
- 원소를 돌면서 음수가 홀수개면 음수니까 -1을 반환한다.

## 모범 답안

```python
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for x in nums:
            if x == 0: return 0
            if x < 0: ans *= -1
        return ans 
```

- 44ms
- nums를 순회하면서 0이면 0, 음수면 -1을 계속 곱한다.
- 그럼 그 값이 바로 결과가 된다.
- 천잰데?