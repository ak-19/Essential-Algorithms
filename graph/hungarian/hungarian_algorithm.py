from math import inf

class HungarianAlgorithm:
    def hungarian_algorithm(self, cost_matrix):
        """
        Solves the assignment problem using the Hungarian algorithm.

        Parameters
        ----------
        cost_matrix : List[List[int]]
            A 2D list representing the cost matrix where cost_matrix[i][j] is the cost
            of assigning the i-th worker to the j-th task.

        Returns
        -------
        Tuple[List[int], int]
            Returns a tuple where the first element is a list of assignments for each worker
            such that each worker is assigned to exactly one task and each task is assigned
            to exactly one worker, minimizing the total cost. The second element is the
            minimum cost of these assignments.
        """
        self.A = cost_matrix
        matrix = [self.A[r][:] for r in range(len(self.A))]

        R = len(matrix)
        C = len(matrix[0])

        row_min = [0] * (R + 1)    
        col_min = [0] * (C + 1)
        task_worker = [0] * (C + 1)
        way = [0] * (C + 1)
        
        for worker in range(1, R+1):
            task_worker[0] = worker
            minv = [inf] * (C + 1)
            used = [False] * (C + 1)
            curr_task = 0
            curr_worker = worker
            delta = 0
            while True:
                used[curr_task] = True
                curr_worker = task_worker[curr_task]
                delta = inf
                min_task = 0
                for task in range(1, C+1):
                    if not used[task]:
                        cur = matrix[curr_worker-1][task-1] - row_min[curr_worker] - col_min[task]
                        if cur < minv[task]:
                            minv[task] = cur
                            way[task] = curr_task
                        if minv[task] < delta:
                            delta = minv[task]
                            min_task = task
                for task in range(0, C+1):
                    if used[task]:
                        row_min[task_worker[task]] += delta
                        col_min[task] -= delta
                    else:
                        minv[task] -= delta
                curr_task = min_task
                if task_worker[curr_task] == 0:
                    break

            while True:
                min_task = way[curr_task]
                task_worker[curr_task] = task_worker[min_task]
                curr_task = min_task
                if curr_task == 0: break
        
        res = [0] * R
        for task in range(1, C + 1):
            if task_worker[task] != 0: res[task_worker[task] - 1] = task - 1
        return res, sum(self.A[i][res[i]] for i in range(R))