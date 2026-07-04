class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # This will store { value: index }
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement is already in our dictionary
            if complement in seen:
                # Return the index of the complement and the current index
                return [seen[complement], index]
            
            # If not found, store the current number and its index
            seen[num] = index