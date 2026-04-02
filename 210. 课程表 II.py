from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
        
        # 1) 建图：记录 pre 学完后，可以继续学哪些课
        graph = defaultdict(list)
        
        # 2) 入度数组：记录每门课还有几个前置条件没完成
        indegree = [0] * numCourses
        
        
        # 3) 遍历所有依赖关系
        for course, pre in prerequisites:
            
            # pre -> course
            # 表示学完 pre 后，course 被解锁
            graph[pre].append(course)
            
            # course 多了一个前置依赖
            indegree[course] += 1
        
        
        # 4) 创建队列：放当前可以直接学的课程
        queue = deque()
        
        # 5) 把所有入度为 0 的课先放进去
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        
        # 6) 存最终学习顺序
        order = []
        
        
        # 7) BFS 开始
        while queue:
            
            # 8) 取出当前可以学的一门课
            cur = queue.popleft()
            
            # 9) 放进答案
            order.append(cur)
            
            
            # 10) 看 cur 学完后会影响哪些后续课程
            for nxt in graph[cur]:
                
                # nxt 少一个未完成前置条件
                indegree[nxt] -= 1
                
                # 11) 如果 nxt 已经没有前置依赖
                if indegree[nxt] == 0:
                    
                    # 说明现在可以学
                    queue.append(nxt)
        
        
        # 12) 如果有些课程没进答案，说明图里有环
        if len(order) != numCourses:
            return []
        
        
        # 13) 返回一个合法顺序
        return order
