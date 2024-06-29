""""
冒泡排序：通过连续地比较与交换相邻元素实现排序
从数组最左端开始向右遍历，依次比较相邻元素大小，
如果“左元素”>“右元素”就交换二者，遍历完成后，最大的元素还会被移动到数组的最右端
"""

def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        flag = False
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if not flag:
            break    # 此轮冒泡未交换任何元素，直接跳出



if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    bubble_sort(nums)
    print("经过冒泡算法排序后nums = ", nums)












