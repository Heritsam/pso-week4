import numpy as np

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def random_coordinate(n=10, r=0.4):
        return [Coordinate(np.random.uniform(-r, r), np.random.uniform(-r, r)) for _ in range(n)]

    def get_distance(self, other):
        """Objective function"""
        return np.sqrt(np.power(self.x - other.x, 2) + np.power(self.y - other.y, 2))

    @staticmethod
    def get_total_distance(coordinates):
        total_distance = 0

        for a, b in zip(coordinates[:-1], coordinates[1:]):
            total_distance += a.get_distance(b)
        
        return total_distance
    
    @staticmethod
    def exact_cycle(coordinates):
        return Coordinate.get_total_distance(coordinates + [coordinates[0]])