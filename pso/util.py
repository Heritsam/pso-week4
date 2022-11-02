import math
import random
import numpy as np
import matplotlib.pyplot as plt


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def random_coordinate(n=10, r=0.4):
        return [Coordinate(np.random.uniform(-r, r), np.random.uniform(-r, r)) for _ in range(n)]

    def get_distance(self, city):
        return math.hypot(self.x - city.x, self.y - city.y)

    @staticmethod
    def get_total_distance(coordinates):
        total_distance = 0

        for a, b in zip(coordinates[:-1], coordinates[1:]):
            total_distance += a.get_distance(b)
        
        return total_distance

    def __repr__(self):
        return f"({self.x}, {self.y})"


def generate_cities(size):
    return [Coordinate(x=int(random.random() * 1000), y=int(random.random() * 1000)) for _ in range(size)]


def path_cost(route):
    return sum([city.get_distance(route[index - 1]) for index, city in enumerate(route)])


def visualize_tsp(title, cities):
    fig = plt.figure()
    fig.suptitle(title)
    x_list, y_list = [], []
    for city in cities:
        x_list.append(city.x)
        y_list.append(city.y)
    x_list.append(cities[0].x)
    y_list.append(cities[0].y)

    plt.plot(x_list, y_list, 'ro')
    plt.plot(x_list, y_list, 'g')
    plt.show(block=True)