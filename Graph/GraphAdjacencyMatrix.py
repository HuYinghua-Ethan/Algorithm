""""
图的基础操作可分为对“边”的操作和对"顶点"的操作。







"""



class GraphAdjMat:
    def __init__(self, vertices, edges):
        """"构造方法"""
        # 顶点列表，元素代表"顶点值"，索引代表"顶点索引"
        self.vertices:list[int] = []
        # 邻接矩阵，行索引对应顶点索引
        self.adj_mat:list[list[int]] = []
        for val in vertices:
            self.add_vertex(val)
        # 添加边
        for e in edges:
            self.add_edge(e[0], e[1])

        def size(self):
            """获取顶点数量"""
            return len(self.vertices)
        
        def add_vertex(self, val):
            """添加顶点"""
            n = self.size()
            # 向顶点列表中添加新顶点的值
            self.vertices.append(val)
            # 在邻接矩阵中添加一行
            new_row = [0] * n
            self.adj_mat.append(new_row)
            # 在邻接矩阵中添加一列
            for row in self.adj_mat:  # 将每一行遍历出来，在每一行最后添加0
                row.append(0)

        def remove_vertex(self, index):
            """删除顶点"""
            if index >= self.size():
                raise IndexError()
            # 在顶点列表中移除索引 index 的顶点
            self.vertices.pop(index)
            # 在邻接矩阵中删除索引 index 的行
            self.adj_mat.pop(index)
            # 在邻接矩阵中删除索引 index 的列
            for row in self.adj_mat:
                row.pop(index)

        def add_edge(self, i, j):
            """添加边"""
            # 索引越界与相等处理
            if i < 0 or j < 0 or i >= self.size() or j >= self.size():
                return IndexError()
            self.adj_mat[i][j] = 1
            self.adj_mat[j][i] = 1

        def remove_edge(self, i, j):
            """删除边"""
            # 索引越界与相等处理
            if i < 0 or j < 0 or i >= self.size() or j >= self.size():
                raise IndexError()
            self.adj_mat[i][j] = 0
            self.adj_mat[j][i] = 0



"""Driver Code"""
if __name__ == "__main__":
    # 初始化无向图
    vertices = [1, 3, 2, 5, 4]
    edges = [[0, 1], [0, 3], [1, 2], [2, 3], [2, 4], [3, 4]]
    graph = GraphAdjMat(vertices, edges)

    # 添加边
    # 顶点 1, 2 的索引分别为 0, 2
    graph.add_edge(0, 2)

    # 删除边
    # 顶点 1, 3 的索引分别为 0, 1
    graph.remove_edge(0, 1)

    # 添加顶点
    graph.add_vertex(6)

    # 删除顶点
    # 顶点 3 的索引为 1
    graph.remove_vertex(1)


