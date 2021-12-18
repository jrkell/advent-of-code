import os

class Node():
    def __init__(self, name: str) -> None:
        self.name = name
        self.linked_nodes = []
        self.isSmall = name.lower() == name
        self.isBig = not self.isSmall
        self.isStart = name == 'start'
        self.isEnd = name == 'end'

def linkNodes(nodes: list[Node], str_a: str, str_b: str) -> None:
    node_a = findNode(nodes, str_a)
    node_b = findNode(nodes, str_b)
    node_a.linked_nodes.append(node_b)
    node_b.linked_nodes.append(node_a)

def findNode(nodes: list[Node], find: str) -> Node:
    for node in nodes:
        if node.name == find:
            return node
    return None

# recursively go through and find paths
def solve(nodes: list[Node], current_node: Node, current_path: list[Node]):
    global completed_paths
    current_path = copyList(current_path) # get deep copy
    current_path.append(current_node)
    if current_node.isEnd:
        completed_paths.append(current_path)
    else:
        for node in current_node.linked_nodes:
            if node.isBig or node not in current_path:
                solve(nodes, node, current_path)

def copyList(nodes: list[Node]):
    return [node for node in nodes]

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read().splitlines()

lines = openInput()

# create nodes
completed_paths = []
nodes = []
used_strings = []
for line in lines:
    split_line = line.split('-')
    for node_name in split_line:
        if node_name not in used_strings:
            nodes.append(Node(node_name))
            used_strings.append(node_name)

# create links between nodes
for line in lines:
    split_line = line.split('-')
    linkNodes(nodes, split_line[0], split_line[1])

# get paths
solve(nodes, findNode(nodes, 'start'), [])
print(f'{len(completed_paths)=}')
