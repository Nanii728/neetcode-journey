class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result= False
        k=set()
        for i in nums:
            if i in k:
                result=True
                break
            else:
                k.add(i)
        return result


        