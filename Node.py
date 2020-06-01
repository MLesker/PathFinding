import math


class Node:
    def __init__(self, name, edges=None):
        self.name = name
        self.edges = edges

    def __str__(self):
        return self.name

    def set_edges(self, edges):
        self.edges = edges

    def get_neighbours(self):
        result = list()
        for n in self.edges:
            result.append(n)
        return result

    def get_closest_neighbour(self):
        """
        Returns the neighbour with the least distance to this Node.
        If multiple neighbours have the same distance, it will return the first one it finds
        """
        result = (None, math.inf)
        for neighbour in self.edges:
            if self.edges[neighbour] < result[1]:
                result = (neighbour, self.edges[neighbour])

        return result
