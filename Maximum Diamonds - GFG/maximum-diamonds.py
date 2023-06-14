#User function Template for python3
import heapq
import math
class Solution:
    def maxDiamonds(self, A, N, K):
        # code here 
        A = [-i for i in A]
        heapq.heapify(A)
        ret = 0
        while K > 0:
            curr = heapq.heappop(A)
            heapq.heappush(A, math.ceil(curr/2))
            ret += -curr
            K-=1
        return ret


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxDiamonds(A,N,K))
# } Driver Code Ends