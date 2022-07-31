class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        d = {}
        for task in tasks:
            if task in d:
                d[task] += 1
            else:
                d[task] = 1
        max_freq = max(d.values())
        last_row = 0
        for k, v in d.items():
            if v == max_freq:
                last_row += 1
        
        return max((max_freq - 1) * (n + 1) + last_row, len(tasks))