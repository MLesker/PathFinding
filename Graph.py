from Node import Node
import math

class Graph:
    def __init__(self, nodes_list, start):
        self.start = start
        self.nodes = dict()  # Dictionary of nodes in the graph, mapped with the visited-status
        for n in nodes_list:
            self.nodes[n] = False

    def __iter__(self):
        return self.nodes.__iter__()

    def __next__(self):
        return self.nodes.__next__()

    def is_visited(self, node):
        for n in self:
            if n == node:
                return self.nodes.get(n)

    def set_visited(self, node):
        for n in self:
            if n == node:
                self.nodes[n] = True

    def get_unvisited_notes(self):
        result = list()
        for n in self:
            if not self.nodes.get(n):
                result.append(n)
        return result

    def get_unvisited_neighbours(self, node):
        result = list()
        neighbours = node.get_neighbours()

        # Append if unvisited
        for neigh in neighbours:
            if not self.is_visited(neigh):
                result.append(neigh)

        return result

    def get_unvisited_node_with_smallest_distance_from_start(self, result_table):
        result = (None, math.inf)

        for node in self.get_unvisited_notes():
            node_distance = result_table.get_distance_from_start(node)
            if node_distance <= result[1]:
                result = (node, node_distance)

        return result[0]
