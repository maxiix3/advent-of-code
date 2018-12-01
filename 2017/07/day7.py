import re

data = open("./day7_puzzle.txt", "r").readlines()
def day7_1():
    all_nodes = []
    all_supported = []
    for line in data:
        all_nodes.append(re.match(r'\w+', line).group(0))
        if re.search(r'->', line):
            nodes = re.search(r'-> (?P<nodes>[\w, ]+)', line).group('nodes').replace(' ', '').split(',')
            for node in nodes:
                all_supported.append(node)
    return list(set(all_nodes) - set(all_supported))[0]



node_map = {}
node_values = {}
for line in data:
    p_node = re.match(r'[\w]+', line).group(0)
    node_value = re.search(r'[\d]+', line).group(0)
    node_values[p_node] = int(node_value)
    if re.search(r'->', line):
        nodes = re.search(r'-> (?P<nodes>[\w, ]+)', line).group('nodes').replace(' ', '').split(',')
        node_map[p_node] = nodes

def child_values(node):
    children = node_map[node]
    supports = []
    for child in children:
        if child in node_map.keys():
            child_support = child_values(child)
            value = sum(child_support) + node_values[child]
        else:
            value = node_values[child]
        supports.append(value)
    if len(set(supports)) != 1:
        print ('Imbalance detected on {}, due to children {}, weighing {}'.format(node, node_map[node], supports))
    return supports


if __name__ == "__main__":
    print(day7_1(), "\n")
    child_values(day7_1())
