"""
快速排序在某些输入下的时间效率可能会降低
举一个极端的例子：
假设输入数组是完全倒序的，由于我们选择最左端元素作为基准数，那么在哨兵划分完成后，基准数被交换至数组最右端
导致左子数组长度为 n - 1 、右子数组长度为 0 。

为了避免这种情况发生，我们可以优化哨兵划分中的基准数的选取策略
可以在数组中随机选取三个候选元素（通常为数组的首、尾、中点元素）
并将这三个候选元素的中位数作为基准数

"""


# 选取三个候选元素的中位数, 并返回其索引
def median_three(nums, left, mid, right):
    l, m, r = nums[left], nums[mid], nums[right]
    if l <= m <= r or r <= m <= l:
        return mid
    elif m <= l <= r or r <= l <= m:
        return left
    else:
        return right


# 哨兵划分
def partition(nums, left, right):
    mid_index = median_three(nums, left, (left + right) // 2, right)
    nums[left], nums[mid_index] = nums[mid_index], nums[left]

    # 以nums[left]为基准数
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1
        while i < j and nums[i] <= nums[left]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i], nums[left] = nums[left], nums[i]

    return i


def quick_sort(nums, left, right):
    if left >= right:
        return
    
    pivot = partition(nums, left, right)
    
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)


# 尾递归优化
def quick_sort_tail_recursion(nums, left, right):
    # 子数组长度为1时终止
    while left < right:
        pivot = partition(nums, left, right)

        if pivot - left < right - pivot:
            quick_sort_tail_recursion(nums, left, pivot - 1)
            left = pivot + 1
        else:
            quick_sort_tail_recursion(nums, pivot + 1, right)
            right = pivot - 1

if __name__ == "__main__":
    nums = [2, 4, 1, 0, 3, 5]
    # quick_sort(nums, 0, len(nums) - 1)
    quick_sort_tail_recursion(nums, 0, len(nums) - 1)
    print("经过快速排序后的 nums = ", nums)












