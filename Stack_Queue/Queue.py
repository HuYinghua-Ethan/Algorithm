"""
队列是一种遵循先入先出规则的线性数据结构
队列模拟了排队现象，即新来的人不断加入队列尾部，而位于队列头部的人逐个离开

我们将队列头部称为“队首”，尾部称为“队尾”，将把元素加入队尾的操作称为“入队”，删除队首元素的操作称为“出队”

"""

from collections import deque

if __name__ == "__main__":
    # 初始化队列
    que = deque()

    # 元素入队
    que.append(1)
    que.append(3)
    que.append(2)
    que.append(5)
    que.append(4)

    # 访问队首元素
    front = que[0]
    print(f"队首元素为：{front}")

    # 元素出队
    pop = que.popleft()
    print(f"出队元素为：{pop}")
    print(f"出队后 que = {que}")

    # 获取队列的长度
    size = len(que)
    print(f"队列长度 size = {size}")

    # 判断队列是否为空
    is_empty = len(que) == 0
    print(f"队列是否为空  = {is_empty}")



    






