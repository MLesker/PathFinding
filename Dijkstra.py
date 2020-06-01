from ResultTable import ResultTable


class Dijkstra:

    def __init__(self, graph):
        self.graph = graph
        self.resultTable = ResultTable(graph)
        self.create_result_table()

    def create_result_table(self):
        while len(self.graph.get_unvisited_notes()) != 0:
            # Visit node with smallest distance from start
            node = self.graph.get_unvisited_node_with_smallest_distance_from_start(self.resultTable)

            unvisitedNeighbours = self.graph.get_unvisited_neighbours(node)

            # Calculate distance from start for each neighbour of node
            unv_neighbours_distances = {
                neighbour: self.resultTable.get_distance_from_start(node) + node.edges[neighbour] for
                neighbour in unvisitedNeighbours}

            # Update resultTable if distance smaller than previous Distance
            for neighbour in unvisitedNeighbours:
                currentDistance = self.resultTable.get_distance_from_start(neighbour)
                newDistance = unv_neighbours_distances.get(neighbour)
                if newDistance < currentDistance:
                    self.resultTable.set_distance_from_start(neighbour, newDistance)
                    self.resultTable.set_previous_node(neighbour, node)

            self.graph.set_visited(node)

    def get_shortest_path(self, node):
        path = [node]
        distance = self.resultTable.get_distance_from_start(node)
        while path[0] != self.graph.start:
            prev = self.resultTable.get_previous_node(path[0])
            path.insert(0, prev)
        return path, distance