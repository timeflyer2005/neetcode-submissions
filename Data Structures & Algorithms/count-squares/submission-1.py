class CountSquares:

    def __init__(self):
        self.point_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.point_count[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        result = 0

        for (px, py), diagonal_count in list(self.point_count.items()):
            # The horizontal and vertical distances must be equal
            if abs(px - x) != abs(py - y):
                continue

            # The diagonal point cannot equal the query point
            if px == x:
                continue

            corner1_count = self.point_count[(px, y)]
            corner2_count = self.point_count[(x, py)]

            result += (
                diagonal_count
                * corner1_count
                * corner2_count
            )

        return result