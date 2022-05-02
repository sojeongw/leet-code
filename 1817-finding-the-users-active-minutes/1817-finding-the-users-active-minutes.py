class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
            dic = defaultdict(set)
            for log in logs:
                dic[log[0]].add(log[1])

            result = [0 for i in range(k)]
            for value in dic.values():
                result[len(value) - 1] += 1

            return result