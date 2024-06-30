
"""
数组(array)是一种线性数据结构，其将相同类型的元素存储在连续的内存空间中。
我们将元素在数组中的位置称为该元素的索引(index)
"""


""""数组元素被存储在连续的内存空间中,这意味着计算数组元素的内存地址非常容易。"""
"""给定数组内存地址(首元素内存地址)和某个元素的索引,从而直接访问该元素,索引本质上是内存地址的偏移量"""

import random

# 访问数组
def random_access(nums):
    random_index = random.randint(0, len(nums) - 1)
    random_num = nums[random_index]
    return random_num


# 插入元素
def insert(nums, value, index):
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    nums[index] = value


# 删除元素
def delete_element(nums, index):
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]


# 遍历数组
def traverse(nums):
    count = 0
    # 通过索引遍历数组
    for i in range(len(nums)):
        count += nums[i]
    # 直接遍历数组元素
    for num in nums:
        count += num
    # 同时遍历数据索引和元素
    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
    for i, num in enumerate(nums):
        count += nums[i]
        count += num    


# 查找元素
def find(nums, target):
    """在数组中查找指定元素"""
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


def extend(nums, enlarge):
    """扩展数组长度"""
    # 初始化一个扩展长度后的数组
    res = [0] * (len(nums) + enlarge)
    # 将原数组中的所有元素复制到新数组
    for i in range(len(nums)):
        res[i] = nums[i]
    # 返回扩展后的新数组
    return res


if __name__ == "__main__":
    
    # 数组的初始化
    arr = [0] * 5
    nums = [1, 3, 2, 5, 4]


