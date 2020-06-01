from Node import Node
from Graph import Graph
from Dijkstra import Dijkstra

# generate Test-Data
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")

nodeA.set_edges({
    nodeB: 6,
    nodeD: 1
})

nodeB.set_edges({
    nodeA: 6,
    nodeC: 5,
    nodeD: 2,
    nodeE: 2
})
nodeC.set_edges({
    nodeB: 5,
    nodeE: 5
})
nodeD.set_edges({
    nodeA: 1,
    nodeB: 2,
    nodeE: 1
})
nodeE.set_edges({
    nodeB: 2,
    nodeC: 5,
    nodeD: 1
})

graph = Graph([nodeA, nodeB, nodeC, nodeD, nodeE], nodeA)

destination = nodeD

pathfinder = Dijkstra(graph)
result = pathfinder.get_shortest_path(destination)

path = ""
for node in result[0]:
    if result[0].index(node) != len(result[0]) - 1:
        path += f"{node} -> "
    else:
        path += f"{node}"

print(f"Der kürzeste Weg nach {destination} ist {result[1]} lang und lautet: {path}")