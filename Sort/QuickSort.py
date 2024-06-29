"""
快速排序是一种基于分治策略的排序算法
快速排序的核心操作是“哨兵划分”
其目标是：选择数组中的某个元素作为“基准数”将所有小于基准数的元素移到其左侧，而大于基准数的元素移到其右侧
哨兵划分完成后，原数组被划分成三部分：左子数组、基准数、右子数组
且满足“左子数组任意元素 <= 基准数 <= 右子数组任意元素”
哨兵划分的实质是将一个较长数组的排序问题简化为两个较短数组的排序问题。
"""


def partition(nums, left, right):
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1
        while i < j and nums[i] <= nums[left]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i], nums[left] = nums[left], nums[i]
    return i  # 返回基准数的索引

def quick_sort(nums, left, right):
    # 当子数组的长度为1时，递归终止
    if left >= right:
        return
    
    # 哨兵划分
    pivot = partition(nums, left, right)
    
    # 递归左子数组，右子数组
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)


if __name__ == "__main__":
    nums = [2, 4, 1, 0, 3, 5]
    quick_sort(nums, 0, len(nums) - 1)
    print("快速排序完成后 nums = ", nums)



