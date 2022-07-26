class Solution:
    def decodeString(self, s: str) -> str:
        
        
        reps = []
        
        blocks = []
        
        ret = ''
        more = False
        for i in s:
            if not i.isdigit() and i.isalnum():
                if blocks != []:
                    temp = blocks[-1]
                    temp += i
                    blocks[-1] = temp
                else:
                    ret += i
            elif i == '[':
                more = False
                blocks.append("s")
            elif i == ']':
                temp = int(reps.pop())
                temp = temp * blocks.pop()[1:]
                if blocks != []:
                    blocks[-1] = blocks[-1] + temp
                else:
                    ret += temp
            else:
                if more:
                    reps[-1] = reps[-1] + i
                else:
                    reps.append(i)
                    more = True

                
        return ret