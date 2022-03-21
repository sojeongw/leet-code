class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1 == s2:
            return True
        
        count = 0
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        
        if count != 2:
            return False
        
        sortedS1 = ''.join(sorted(s1))
        sortedS2 = ''.join(sorted(s2))
        
        if sortedS1 == sortedS2:
            return True