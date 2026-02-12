# The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). 
# The root is the company itself, and every node in the tree represents a car distributor that receives cars from the parent node and ships them to its children nodes. 
# The leaf nodes are car dealerships that sell cars direct to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.

from typing import List, Optional

class Node:
    # Constructor to create a new node
    def __init__(self, cost: int):
        self.cost: int = cost
        self.children: List['Node'] = []
        self.parent: Optional['Node'] = None

MAX_INT = float('inf')

def get_cheapest_cost(rootNode: Node) -> int:
    if not rootNode.children:
        return rootNode.cost
    else:
        minCost = MAX_INT
        for child in rootNode.children:
            tempCost = get_cheapest_cost(child)
            if tempCost < minCost:
                minCost = tempCost
    return minCost + rootNode.cost


# debug your code below
root = Node(0)
root.children = [Node(5), Node(3), Node(6)]
root.children[0].children = [Node(4), Node(2)]
root.children[1].children = [Node(0)]
root.children[2].children = [Node(1), Node(5)]

print(get_cheapest_cost(root)) 