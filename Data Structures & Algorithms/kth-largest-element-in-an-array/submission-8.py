class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def quickselect(left, right):
            while left <= right:
                pivot = nums[right]
                pointer = left

                for i in range(left, right):
                    if nums[i] <= pivot:
                        nums[pointer], nums[i] = nums[i], nums[pointer]
                        pointer += 1

                nums[pointer], nums[right] = nums[right], nums[pointer]

                if pointer == target:
                    return nums[pointer]
                elif pointer < target:
                    left = pointer + 1
                else:
                    right = pointer - 1

        return quickselect(0, len(nums) - 1)