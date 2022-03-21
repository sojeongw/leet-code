class Solution(object):
    def findCenter(self, edges):
        flattened_edges = list(itertools.chain(*edges))
        result = [0 for _ in range(len(flattened_edges))]

        for i in flattened_edges:
            result[i] += 1

        return result.index(max(result))
        