class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        
        s = set()
        repeat = -1
        total = 0

        n = len(grid)

        for row in grid:
            for num in row:
                if num in s:
                    repeat = num
                s.add(num)
                total += num

        N = n * n
        expected = N * (N + 1) // 2

        missing = expected - (total - repeat)

        return [repeat, missing]