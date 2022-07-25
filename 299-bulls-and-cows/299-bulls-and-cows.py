class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        m = Counter(secret)  
        x = 0
        y = 0
        for i, letter in enumerate(secret):
            u = guess[i]
            if letter == u:
                x += 1
                if m[letter] > 0:
                    m[letter] -= 1
                else:
                    y -= 1
            elif u in m:
                if m[u] > 0:
                    m[u] -= 1
                    y += 1

        return str(x) + "A" + str(y) + "B"