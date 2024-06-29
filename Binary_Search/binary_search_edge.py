"""查找左边界"""
"""
Question:
给定一个长度为 n 的有序数组 nums ，其中可能包含重复元素。
请返回数组中最左一个元素 target 的索引。若数组中不包含该元素，则返回 -1 。
"""

def binary_search_insertion(nums, target):
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] < target:
            i = mid + 1
        elif nums[mid] > target:
            j = mid - 1
        else:
            j = mid -1
    return i

""" 查找右边界 """
"""
代码实现思路： 将查找最右一个 target 转化为查找最左一个 target + 1
查找完成后，指针i指向最左一个 target + 1(如果存在),而j指向最右一个 target，因此返回j即可
"""

def binary_search_left_edge(nums, target):
    i = binary_search_insertion(nums, target)
    # 未找到 target
    if i == len(nums) or nums[i] != target:  
        return -1
    return i


def binary_search_right_edge(nums, target):
    i = binary_search_insertion(nums, target + 1)
    # j 指向最右一个 target,i 指向首个大于 target 的元素
    j = i - 1
    if j == -1 or nums[j] != target:  
        return -1
    return j
    

if __name__ == "__main__":
    nums = [1, 3, 6, 6, 6, 6, 6, 10, 12, 15]
    target = 6
    left_index = binary_search_left_edge(nums, target)
    right_index = binary_search_right_edge(nums, target)
    
    print(f"最左边一个元素{target}的索引为{left_index}")
    print(f"最右边一个元素{target}的索引为{right_index}")




