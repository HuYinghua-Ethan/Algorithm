""" 二分查找不仅可用于搜索目标元素，还可用于解决许多变种问题，比如搜索目标元素的插入位置。 """

"""
Question:
给定一个长度为n的有序数组 nums 和一个元素 target ，数组不存在重复元素。
现将 target 插入数组 nums 中，并保持其有序性。
若数组中已存在元素 target ，则插入到其左方。
请返回插入后 target 在数组中的索引。

"""

# 不存在重复元素
def binary_search_insertion_simple(nums, target):
    i, j = 0, len(nums) - 1
    
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] < target:
            i = mid + 1
        elif nums[mid] > target:
            j = mid - 1
        else:
            return mid
    return i

# 存在重复元素
def binary_search_insertion(nums, target):
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] < target:
            i = mid + 1
        elif nums[mid] > target:
            j = mid - 1
        else:
            j = mid - 1
    return i

if __name__ == "__main__":
    nums = [1, 3, 6, 8, 12, 15, 23, 26, 31, 35]
    target = 6
    index = binary_search_insertion_simple(nums, target)
    
    print(f"元素{target}的插入点的索引为: {index}")












