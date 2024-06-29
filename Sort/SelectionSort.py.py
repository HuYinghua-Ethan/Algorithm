""" 选择排序的工作原理：开启一个循环，每轮从未排序区间选择最小的元素，将其放到已排序区间的末尾"""

def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if nums[j] < nums[k]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]
            
if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    selection_sort(nums)
    print("选择排序后 nums = ", nums)














