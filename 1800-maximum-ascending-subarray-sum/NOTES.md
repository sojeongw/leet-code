# 문제

- sub array의 합이 제일 큰 것을 구한다.
    - sub array는 서로 인접한 숫자이며 오름차순이어야 한다.

# 제출 답안

```python
def maxAscendingSum(nums: List[int]) -> int:
    max_value = nums[0]
    sum_value = nums[0]

    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            sum_value += nums[i]
            if max_value < sum_value:
                max_value = sum_value
        else:
            sum_value = nums[i]

    return max_value


result = maxAscendingSum([100, 10, 1])
print(result)
```

- 28 ms, faster than 98.87%
- 일단 리스트 맨 첫번째 값이 무조건 max와 sum이 된다.
- 앞보다 뒤가 크면 sum에 합친다.
    - 만약 sum이 max보다 크면 max를 갱신한다.
- 앞보다 뒤가 작으면 sum을 다시 시작 숫자로 초기화한다.

# 모범 답안

```python
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = currSum = last = 0
        for i in nums:
            if i <= last:
                currSum = 0
            last = i
            currSum += i
            maxSum = max(maxSum, currSum)
        return maxSum
```

- 24ms
- 크게 차이는 안 나지만 변수 할당이 신기해서 참고차 가져왔다.
- 현재 값이 마지막으로 계산한 값보다 작으면 sum을 다시 0으로 초기화한 뒤 새롭게 구한다.
- max() 함수를 이용해 더 큰 값을 구한다.