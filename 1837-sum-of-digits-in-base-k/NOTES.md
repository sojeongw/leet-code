# 1837. Sum of Digits in Base K

- 10진수인 n을 k진수로 바꾼 뒤 각 자릿수를 더한 값을 구한다.

## 제출 답안

```python
class Solution(object):
    def sumBase(self, n, k):
        converted = ''

        while n > 0:
            n, mod = divmod(n, k)
            converted += str(mod)

        return sum(map(int, converted))
```

- 20 ms, faster than 62.96%
- divmod() 메서드를 처음 배웠다.
    - 몫과 나머지를 한 번에 반환한다.
- k진수르 바꾸면서 스트링으로 변환해 연결한다.
    - 그래야 자리수 별로 sum을 구하는 게 쉬워진다.
- sum() 메서드로 각 자리를 int로 컨버팅 하면서 합계를 계산한다.

## 모범 답안

```python
class Solution(object):
    def sumBase(self, n, k):
        sum_digit = 0

        while n >= k:
            sum_digit = sum_digit + (n % k)
            n = int(n / k)

        return sum_digit + n
```

- 3ms
- 나눌 수 있을 때까지 계속 나머지를 sum_digit에 더한다.
- 최초의 n과 k를 나눈 몫이 이진수 계산 후 마지막 값과 같으므로 이 값과 sum_digit을 더한다.
- 이해하려는 과정에서 자꾸 결과를 ((k**n) * 결과)로 다시 10진수 계산하려고 해서 헷갈렸다.