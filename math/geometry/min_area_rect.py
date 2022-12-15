from typing import List
from math import inf, sqrt
from collections import defaultdict

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> float:
        """
        find rectangle if exists, closed by 4 points, get minimum area else return infinity
        """
        result = inf
        P = len(points)
        processed = defaultdict(list)

        for i, (x, y) in enumerate(points):
            for j in range(i + 1, P):
                xx, yy = points[j]
                cx, cy = (x+xx) / 2, (y+yy) / 2
                d = (x-xx) ** 2 + (y-yy) ** 2
                for xxx, yyy in processed[(cx, cy, d)]:
                    area = sqrt(((x-xxx)**2+(y-yyy)**2) * ((xx-xxx)**2 + (yy-yyy)**2))
                    result = min(result, area)

                processed[(cx, cy, d)].append((x, y))
        return result