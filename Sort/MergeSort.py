"""
归并算法是一种基于分治策略的排序算法， 包含 “划分” 和 “排序”阶段
划分阶段：通过递归不断地将数组从中点处分开，将长数组的排序问题转换为短数组的排序问题。
当子数组长度为 1 时终止划分，开始合并，持续地将左右两个较短的有序数组合并为一个较长的有序数组，直至结束。
"""

def merge(nums, left, mid, right):
    tmp = [0] * (right - left + 1)
    i, j, k = left, mid + 1, 0
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1

    # 剩余部分
    while i <= mid:
        tmp[k] = nums[i]
        i += 1
        k += 1
    
    while j <= right:
        tmp[k] = nums[j]
        j += 1
        k += 1
    for k in range(len(tmp)):
        nums[left + k] = tmp[k]



def merge_sort(nums, left, right):
    if left >= right:
        return
    
    mid = (left + right) // 2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)

    # 合并
    merge(nums, left, mid, right)


if __name__ == "__main__":
    nums = [7, 3, 2, 6, 0, 1, 5, 4]
    merge_sort(nums, 0, len(nums) - 1)
    print("归并排序完成后 nums = ", nums)
















