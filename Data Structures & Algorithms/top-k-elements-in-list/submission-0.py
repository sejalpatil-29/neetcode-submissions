class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        f=[[] for i in range(len(nums)+1)]
        for n in nums:
            count[n]=1+count.get(n,0)
        for n,cnt in count.items():
            f[cnt].append(n)
        res=[]
        for i in range(len(f)-1,0,-1):
            for n in f[i]:
                res.append(n)
                if len(res)==k:
                    return res

