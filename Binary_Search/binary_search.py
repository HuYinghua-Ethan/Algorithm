"""二分查找法是一种基于分治策略的高效搜索算法
利用数据的有序性，每轮缩小一半搜索范围，直到找到目标或搜索区间为止
"""

"""
Question:
给定一个长度为 的数组 nums ，元素按从小到大的顺序排列且不重复。
请查找并返回元素 target 在该数组中的索引。若数组不包含该元素，则返回 -1。
"""

def binary_search(arr, target):
    i, j = 0, len(arr) - 1

    while i <= j:
        mid = (i + j) // 2  # 计算中值索引
        if arr[mid] < target:  # 中值比目标值小，目标值在右区间
            i = mid + 1
        elif arr[mid] > target:  # 中值比目标值大，目标值在左区间
            j = mid - 1
        else:  # 找到目标值
            return mid
    return -1

if __name__ == "__main__":
    target = 6
    nums = [1, 3, 6, 8, 12, 15, 23, 26, 31, 35]

    # 二分查找（双闭区间）
    index = binary_search(nums, target)
    if index != -1:
        print(f"元素{target}在数组中的索引为{index}")




            



