import math


class ResultTable:
    def __init__(self, graph):
        self.table = list()
        for node in graph:
            self.add_row(node, math.inf if node != graph.start else 0, None)

    def add_row(self, node, distance_from_start, previous_node):
        self.table.append({
            "Node": node,
            "DistanceFromStart": distance_from_start,
            "PreviousNode": previous_node
        })

    def print(self):
        print("-------------------------")
        for line in self.table:
            print(str(line["Node"]) + "    " + str(line["DistanceFromStart"]) + "    " + str(line["PreviousNode"]))
        print("-------------------------")
        print("")

    def get_line(self, node):
        for line in self.table:
            if line["Node"] == node:
                return line

    def get_distance_from_start(self, node):
        return self.get_line(node)["DistanceFromStart"]

    def get_previous_node(self, node):
        return self.get_line(node)["PreviousNode"]

    def set_distance_from_start(self, node, distance):
        for line in self.table:
            if line["Node"] == node:
                line["DistanceFromStart"] = distance

    def set_previous_node(self, node, previous):
        for line in self.table:
            if line["Node"] == node:
                line["PreviousNode"] = previous

