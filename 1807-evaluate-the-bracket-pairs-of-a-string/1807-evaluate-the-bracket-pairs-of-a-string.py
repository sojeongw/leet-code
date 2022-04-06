class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        regex = re.compile("([a-z]+)\)") 
        words = re.split(regex, s)

        d = {x[0]:x[1] for x in knowledge}
       
        for i, word in enumerate(words):
            if word.endswith("("):
                words[i] = words[i][:-1]
                words[i+1] = d.get(words[i+1], '?')
                
        return ''.join(words)