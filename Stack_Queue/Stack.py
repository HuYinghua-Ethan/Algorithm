"""

栈是一种遵循先入后出逻辑的线性数据结构
可以将栈类比为桌面上的一摞盘子，如果想取出底部的盘子，则需要先将上面的盘子依次移走

把堆叠元素的顶部称为“栈顶”，底部称为“栈底”
将把元素添加到栈顶的操作叫作“入栈”，删除栈顶元素的操作叫作“出栈”

"""


if __name__ == "__main__":


    # 初始化栈
    # Python 没有内置的栈类，可以把list当作栈来使用
    stack = []

    # 元素入栈
    stack.append(1)
    stack.append(3)
    stack.append(2)
    stack.append(5)
    stack.append(4)
    print("栈 stack = ", stack)

    # 访问栈顶元素 最后添加的元素就是栈顶元素
    peek = stack[-1]
    print("栈顶元素peek = ", peek )

    # 元素出栈
    pop = stack.pop()
    print("出栈元素 pop = ", pop)
    print("出栈后 stack = ", stack)

    # 获取栈的长度
    size = len(stack)
    print("栈的长度 size =", size)

    # 判断栈是否为空
    is_empty = len(stack) == 0
    print("栈是否为空 = ", is_empty)
















