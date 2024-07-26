"""
Top-k Question
给定一个长度为 n 的无序数组nums，请返回数组中最大的k个元素

方法一：遍历选择
k轮遍历，分别在每轮中提取第1、2、...、k大的元素
此方法只适用于 k << n 的情况，因为当k与n比较接近时，其时间复杂度趋向于O(n^2)
当k = n时，我们可以得到完整的有序序列，此时等价于“选择排序”算法。


方法二：排序
我们可以先对数组nums进行排序，再返回最右边的k个元素，时间复杂度为O(nlogn)。
显然，该方法“超额”完成任务了，因为我们只需找出最大的k个元素即可，而不需要排序其他元素。


方法三：堆
基于堆更加高效地解决Top-k问题
1.初始化一个小顶堆，其堆顶元素最小
2.先将数组的前k个元素放入堆中
3.从第k+1个元素开始，若当前元素大于堆顶元素，则将堆顶元素出堆，并将当前元素入堆
4.遍历完成后，堆中保存的就是最大的k个元素


"""

import heapq

def top_k_heap(nums, k):
    heap = []
    for i in range(k):
        heapq.heappush(heap, nums[i])
    for i in range(k,len(nums)):
        if nums[i] > nums[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
    return heap


"""Driver Code"""
if __name__ == "__main__":
    nums = [1, 3, 2, 5, 6, 4, 8, 12, 20, 16]
    k = 4

    res = top_k_heap(nums, k)
    print(f"最大的{k}个元素是 {res}")



