from typing import List 

# Find indices of two numbers that add up to target
def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Create dictionary to store values with indices
    ind_dict = {}

    # Iterate through list
    for i, num in enumerate(nums):
        # Check if difference is in dictionary
        if target - num in ind_dict:
            # Return indices
            return [ind_dict[target - num], i]
        # Add value to dictionary
        ind_dict[num] = i
    return