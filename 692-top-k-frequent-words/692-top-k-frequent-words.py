class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        x = Counter(sorted(words))        
        r = [[i, x[i]] for i in x]
        r.sort(key=lambda x: -x[1])
        
        return [i[0] for i in r[:k]]
        
        
        