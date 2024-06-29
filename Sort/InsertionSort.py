"""
插入排序
在未排序区间选择一个基准元素，将该元素与其左侧已排序区间的元素逐一比较大小
并将该元素插入到正确位置

流程：
设基准元素为 base,我们需要将目标索引到 base 之间的所有元素向右移动一位，然后将 base 赋值到目标索引
"""

def insertion_sort(nums):
    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]  # j当前位置向右移动一位
            j -= 1
        nums[j + 1] = base  # 将 base 赋值到正确的位置

if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    insertion_sort(nums)
    print("插入排序完成后 nums = ", nums)

















