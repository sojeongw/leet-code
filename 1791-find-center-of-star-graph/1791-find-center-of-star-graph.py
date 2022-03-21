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
