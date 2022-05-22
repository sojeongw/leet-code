# 1827. Minimum Operations to Make the Array Increasing

- 주어진 배열을 strictly increasing 한 배열로 만들기 위한 operation 횟수를 구한다.
    - 한 번에 1씩만 더할 수 있다.

## 제출 답안

```python
def min_operations(nums):
    if len(nums) < 2:
        return 0

    result = 0
    for i in range(1, len(nums)):
        if nums[i - 1] >= nums[i]:
            increment = nums[i - 1] - nums[i] + 1
            result += increment
            nums[i] += increment

    return result
```

- Runtime: 230 ms, faster than 16.96%
- 두 번째 값부터 순차적으로 돌면서 앞에 있는 값과 비교한다.
    - 앞보다 작거나 같으면 그 차이보다 1 크게 만든다.

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        result = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                result += nums[i - 1] - nums[i] + 1
                nums[i] += nums[i - 1] - nums[i] + 1

        return result
```

- 146 ms, faster than 69.08%
- increment 변수를 따로 두던 걸 삭제만 했을 뿐인데 빨라졌다.
    - 변수에 바인딩 하는 시간 복잡도는 O(1)이라고 하는데 왜지. 의문이군...

## 모범 답안

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        prev = 0
        for num in nums:
            if num <= prev:
                prev += 1
                count += prev - num
            else:
                prev = num
        return count
```

- 112 ms
- 돌면서 이전 값만 가지고 비교하면서 계산한다.
- 배열로 다루는 것보다 가독성이 좋은 것 같다.